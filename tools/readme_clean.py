"""Turn a PyPI long description (Markdown, reStructuredText, HTML or plain text) into a short,
LLM-readable plain-text extract: what the package is for, its features, one usage example and its
section names. Badges, images, HTML, link targets and tables of contents are removed.

    extract(text, content_type) -> str (<= LIMIT characters) or "" when nothing useful is left
"""
import html
import re

LIMIT = 800
INTRO, FEATURES, EXAMPLE = 350, 250, 350
FEATURE_HEAD = re.compile(r"^(key )?(features?|highlights|overview|what (it|this) (does|is)|capabilities|why)\b", re.I)
EXAMPLE_HEAD = re.compile(r"(usage|example|quick ?start|getting started|tutorial|how to use|basic use)", re.I)
SKIP_HEAD = re.compile(r"(install|licen[cs]e|contribut|changelog|change log|history|credits|authors?|support|"
                       r"sponsor|citation|cite|table of contents|contents|toc|badges?|status|develop|testing|"
                       r"acknowledg|community|security|code of conduct|release|maintainers?|funding|donat)", re.I)
CODE_LANG = re.compile(r"^(python|py|pycon|python3|ipython|)$", re.I)
FENCE = "\x00FENCE"          # code fence placeholder: inline rules must not touch code blocks


# ---------------------------------------------------------------- markup -> plain lines
def _html(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"<(img|picture|source|svg|video|iframe)\b.*?(/>|>)", "", t, flags=re.S | re.I)
    t = re.sub(r"</?(picture|svg|video|iframe)\b[^>]*>", "", t, flags=re.I)
    t = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", lambda m: ("\n# " + m.group(2).strip() + "\n") if m.group(2).strip() else "\n", t, flags=re.S | re.I)
    t = re.sub(r"<br\s*/?>|</p>|</div>|</li>", "\n", t, flags=re.I)
    t = re.sub(r"<li[^>]*>", "\n- ", t, flags=re.I)
    t = re.sub(r"<pre[^>]*>(.*?)</pre>", lambda m: "\n```\n" + m.group(1) + "\n```\n", t, flags=re.S | re.I)
    t = re.sub(r"</?[a-zA-Z][^>]*>", "", t)
    return html.unescape(t)


def _markdown(t):
    t = re.sub(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)", "", t)            # linked badge
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)                          # image
    t = re.sub(r"!\[[^\]]*\]\[[^\]]*\]", "", t)
    t = re.sub(r"\[([^\]]+)\]\((?:[^()]|\([^)]*\))*\)", r"\1", t)       # [text](url) -> text
    t = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", t)                      # [text][ref]
    t = re.sub(r"^\s*\[[^\]]+\]:\s*\S+.*$", "", t, flags=re.M)          # [ref]: url
    t = re.sub(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$", "", t, flags=re.M)   # table rule
    t = re.sub(r"^(#{1,6})[ \t]*(\S.*?)[ \t]*#*[ \t]*$", lambda m: "# " + m.group(2), t, flags=re.M)
    t = re.sub(r"^#{1,6}[ \t]*$", "", t, flags=re.M)                     # empty heading (logo only)
    t = re.sub(r"^(.+)\n(=+|-+)\s*$", lambda m: "# " + m.group(1).strip(), t, flags=re.M)  # setext
    t = re.sub(r"(\*\*|__)(.+?)\1", r"\2", t)
    return t


def _rst(t):
    out, lines, i = [], t.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^\.\.\s+(code-block|code|sourcecode)::\s*(\S*)", ln)
        if m:
            i += 1
            block = []
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                if not lines[i].lstrip().startswith(":") or block:
                    block.append(lines[i])
                i += 1
            out += [FENCE + m.group(2)] + _dedent(block) + [FENCE]
            continue
        if re.match(r"^\.\.\s", ln) or re.match(r"^\.\.$", ln):        # other directives, comments, targets
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                if not lines[i].strip() and i + 1 < len(lines) and not lines[i + 1].startswith((" ", "\t")):
                    break
                i += 1
            continue
        if ln.rstrip().endswith("::") and not ln.strip().startswith(".."):  # literal block
            text = ln.rstrip()[:-2].rstrip()
            if text:
                out.append(text + ":")
            i += 1
            block = []
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                block.append(lines[i])
                i += 1
            out += [FENCE] + _dedent(block) + [FENCE]
            continue
        if i + 1 < len(lines) and ln.strip() and re.match(r"^([=\-~^*+#\"'`])\1{2,}\s*$", lines[i + 1]) \
                and len(lines[i + 1].strip()) >= len(ln.strip()) - 1:
            out.append("# " + ln.strip())
            i += 2
            continue
        if re.match(r"^([=\-~^*+#])\1{2,}\s*$", ln):                     # overline
            i += 1
            continue
        out.append(ln)
        i += 1
    t = "\n".join(out)
    t = re.sub(r"`([^`<]+?)\s*<[^>]+>`_{1,2}", r"\1", t)                # `text <url>`_
    t = re.sub(r":[a-z:]+:`~?([^`]+)`", r"\1", t)                       # :func:`x`
    t = re.sub(r"``([^`]+)``", r"`\1`", t)
    t = re.sub(r"\|[\w -]+\|_?", "", t)                                 # substitutions
    t = re.sub(r"`([^`]+)`_", r"\1", t)
    return t


def _dedent(block):
    while block and not block[-1].strip():
        block.pop()
    while block and not block[0].strip():
        block.pop(0)
    ind = min((len(b) - len(b.lstrip()) for b in block if b.strip()), default=0)
    return [b[ind:] for b in block]


def plain(text, content_type=""):
    ct = (content_type or "").lower()
    t = text.replace("\r\n", "\n").replace("\t", "    ")
    if "rst" in ct or (not ct and re.search(r"^\.\. \w+::|^={3,}\s*$", t, re.M)):
        t = _rst(t)
    t = _html(t) if re.search(r"<(p|div|img|h[1-6]|a|br|picture)\b", t, re.I) else t
    t = _markdown(t)
    t = re.sub(r"^\s*(https?://\S+|www\.\S+)\s*$", "", t, flags=re.M)   # bare link lines
    t = re.sub(r"https?://\S+", "", t)
    t = re.sub(r"[  ]+", " ", t)
    t = re.sub(r"^\s*[-*+]\s*$", "", t, flags=re.M)
    t = re.sub(r"^\s*[-*+]\s*[^\n:]{1,60}:\s*(\([^)]*\))?\s*$", "", t, flags=re.M)   # "- Website:" without its link
    t = re.sub(r"^[^\n:|]{1,40}:\s*(\|\s*[^\n:|]{1,40}:\s*)+$", "", t, flags=re.M)     # "Docs: | Source:"
    t = re.sub(r"\b([A-Za-z][\w-]*)_\b", r"\1", t)                                    # rst reference GLPK_
    t = t.replace(FENCE, "```")
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


# ---------------------------------------------------------------- plain lines -> sections -> extract
def sections(t):
    """[(heading or None, [lines])], code fences kept intact."""
    out, head, buf, fence = [], None, [], False
    for ln in t.split("\n"):
        if ln.strip().startswith("```"):
            fence = not fence
        if not fence and re.match(r"^# ", ln):
            out.append((head, buf))
            head, buf = ln[2:].strip().strip("*:").strip(), []
            continue
        buf.append(ln)
    out.append((head, buf))
    return [(h, b) for h, b in out if h or any(x.strip() for x in b)]


def _paras(lines, limit, keep_code=False):
    text, fence, out = "\n".join(lines), False, []
    for ln in text.split("\n"):
        if ln.strip().startswith("```"):
            fence = not fence
            continue
        if fence and not keep_code:
            continue
        out.append(ln.rstrip())
    s = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    s = "\n".join(x for x in s.split("\n") if not re.fullmatch(r"\s*[-*]?\s*\S{0,2}\s*", x) or not x.strip())
    if len(s) <= limit:
        return s
    cut = s[:limit]
    end = max(cut.rfind(". "), cut.rfind(".\n"), cut.rfind("\n- "), cut.rfind("\n\n"))
    return (cut[:end + 1] if end > limit // 2 else cut.rsplit(" ", 1)[0]).rstrip() + " ..."


def _code_blocks(lines):
    blocks, cur, lang, fence = [], [], "", False
    for ln in lines:
        s = ln.strip()
        if s.startswith("```"):
            if fence:
                blocks.append((lang, _dedent(cur)))
                cur = []
            else:
                lang = s[3:].strip()
            fence = not fence
            continue
        if fence:
            cur.append(ln)
    return blocks


def _good_code(lang, block):
    code = "\n".join(block)
    if not CODE_LANG.match(lang) or not code.strip():
        return False
    if re.search(r"^\s*\$?\s*(pip|conda|uv|poetry|python -m pip|git|cd|make|docker|brew|apt|sudo)\b", code, re.M) \
            and not re.search(r"\bimport\b|\(", code):
        return False
    return bool(re.search(r"\bimport\b|\w+\(|>>>", code))


def extract(text, content_type=""):
    if not text or text.strip() in ("UNKNOWN", "None"):
        return ""
    secs = sections(plain(text, content_type))
    if not secs:
        return ""
    parts = []
    intro_lines = []
    for h, b in secs[:3]:                       # opening text: before or under the first heading(s)
        if h and (SKIP_HEAD.search(h) or FEATURE_HEAD.match(h) or EXAMPLE_HEAD.search(h)):
            break
        intro_lines += b + [""]
        if len("\n".join(intro_lines)) > INTRO:
            break
    intro = _paras(intro_lines, INTRO)
    if intro:
        parts.append(intro)
    feat = next((b for h, b in secs if h and FEATURE_HEAD.match(h)), None)
    if feat:
        f = _paras(feat, FEATURES)
        if f and f not in intro:
            parts.append("Features:\n" + f)
    code = None
    for prefer in (True, False):                # example sections first, then anywhere
        for h, b in secs:
            if h and SKIP_HEAD.search(h):
                continue
            if prefer and not (h and EXAMPLE_HEAD.search(h)):
                continue
            for lang, blk in _code_blocks(b):
                if _good_code(lang, blk):
                    code = "\n".join(blk)
                    break
            if code:
                break
        if code:
            break
    if code:
        if len(code) > EXAMPLE:
            code = code[:EXAMPLE].rsplit("\n", 1)[0] + "\n..."
        parts.append("Example:\n```python\n" + code + "\n```")
    heads = [h for h, _ in secs if h and len(h) < 60 and not SKIP_HEAD.search(h)]
    if len(heads) > 1:
        parts.append("Sections: " + ", ".join(dict.fromkeys(heads[:14])))
    out = "\n\n".join(parts).strip()
    if len(out) > LIMIT:
        out = out[:LIMIT].rsplit("\n", 1)[0] + "\n..."
    return out if len(re.sub(r"\W", "", out)) >= 40 else ""
