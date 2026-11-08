# Rose – Konzept einer LLM-optimierten Programmiersprache

Stand: 08.11.2026 · Status: Konzept (M0), noch kein Code · Korpus: noch nichts importiert (keine `rose_`-Tabellen, keine Mathe-/Physik-Quellen im MCP)

> **Kurz:** Ein LLM soll bei einer neuen Aufgabe nicht neu erfinden, was längst
> gelöst ist. Rose ist eine kleine Kompositionssprache, in der das LLM **gelöste
> Bausteine referenziert** (Algorithmen aus Rosetta Code, mathematische
> Zusammenhänge, physikalische Gesetze, Regler, Zustandsautomaten) und nur
> noch den **Klebecode** schreibt. Ein MCP-Server auf dem dell (192.168.5.23)
> kennt diese Bausteine, sucht sie, prüft das Ergebnis und übersetzt es in die
> Zielsprache (Python, C, IEC 61131-3 ST, ESPHome-C++).

---

## 1. Problem

Ein LLM, das eine Codeaufgabe bekommt, schreibt heute fast alles aus dem
Gedächtnis neu: den Sieb des Eratosthenes, einen PID-Regler, die Wärmeleistung
eines Wasserstroms, eine Hysterese mit Mindestlaufzeit. Daraus folgen vier
Schwächen:

| Schwäche | Folge |
|---|---|
| Neuerfindung | Tokens und Zeit für Gelöstes, jedes Mal etwas anders |
| Erinnerte statt geprüfte Lösung | Off-by-one, falsche Einheiten, fehlendes Anti-Windup, ungeprüfte Randfälle |
| Keine Herkunft | Niemand weiß, woher eine Formel stammt und in welchem Bereich sie gilt |
| Keine Prüfbarkeit | Ein Automat mit unerreichbarem Zustand fällt erst im Betrieb auf |

Die Lösungen existieren bereits – verstreut über Rosetta Code, OEIS, Wikidata,
die Modelica-Standardbibliothek, Lean mathlib und die eigenen Projekte
(batmonitor-Tabellen, Heizungs-SPS, `rep_max_state.py`). Es fehlt eine Brücke,
über die ein LLM sie **findet, sicher einbindet und prüft**.

## 2. Ziel

1. Ein **Korpus gelöster Bausteine** mit Herkunft, Lizenz, Tests und
   Prüfstufe, durchsuchbar über einen MCP-Server.
2. Eine **Sprache (Rose)**, in der ein LLM diese Bausteine kompakt und
   eindeutig zusammensetzt.
3. Ein **Prüfer/Übersetzer**, der Typen, physikalische Einheiten, Verträge,
   Entscheidungstabellen und Automaten automatisch prüft und Code für die
   Zielplattform erzeugt.
4. Ein **Messverfahren**, das belegt, ob LLM + Rose besser ist als LLM allein
   (Abschnitt 11) – sonst wird Rose nicht weiterverfolgt.

„Alle gelösten Probleme“ ist kein erreichbarer Endzustand, sondern eine
Richtung: Der Korpus wächst über Importer (Abschnitt 6) und über Rückmeldungen
der LLMs selbst (`rose.submit`).

## 3. Leitidee: Suchen vor Schreiben

```
Aufgabe ──► zerlegen ──► je Teilproblem rose.search ──► Treffer? ─ja─► use <ref>
                                                          │
                                                          nein
                                                          ▼
                                                 selbst schreiben (fn/law/…)
                                                          │
           rose.check ◄───────── Rose-Quelltext ◄─────────┘
               │ Diagnosen (JSON) ─► LLM korrigiert ─► erneut check
               ▼
           rose.compile ─► Zielcode + rose.lock (Herkunft, Lizenzen)
               ▼
           rose.test ─► Sandbox ─► ok ─► rose.submit (neuer Baustein, Stufe „tested“)
```

Der entscheidende Punkt ist die **Token-Ökonomie**: Das LLM bekommt von einem
Baustein nur eine **Signaturkarte** (≈ 50 Tokens: Name, Absicht, Signatur,
Einheiten, Prüfstufe). Den eigentlichen Code der Implementierung sieht es nie –
der Übersetzer setzt ihn serverseitig ein. Das LLM denkt also auf der Ebene
„Sieb bis n“, nicht auf der Ebene der Schleifen.

## 4. Designprinzipien – warum „LLM-optimiert“

| # | Prinzip | Umsetzung in Rose |
|---|---|---|
| P1 | **Referenz statt Kopie** | `use rc:Sieve_of_Eratosthenes` statt 20 Zeilen Code; Bausteine per Hash festgenagelt (`rose.lock`) |
| P2 | **Eine kanonische Schreibweise** | `rose fmt` ist Teil der Sprache; keine Synonyme, kein optionales Semikolon. Gleicher Sinn → gleicher Text → gleicher AST-Hash (Duplikaterkennung, stabile Embeddings) |
| P3 | **Explizit statt implizit** | Typen, physikalische Einheiten, Effekte (`effect io, time`), Abtastzeit bei Reglern, Wertebereiche – alles steht im Text |
| P4 | **Absicht ist Code** | Jede `fn`/`law`/`ctrl`/`machine` hat ein `intent "…"`. Das ist der Suchschlüssel: Neuer Code wird automatisch auffindbar |
| P5 | **Lokal prüfbar** | `require`/`ensure`-Verträge, Tests im selben File, endliche Teile (Tabellen, Automaten) werden **vollständig aufgezählt** statt stichprobenartig getestet |
| P6 | **Maschinenlesbare Diagnosen** | Jede Meldung: Code, Ort, Erklärung, Korrekturvorschlag als JSON – das LLM repariert gezielt statt zu raten |
| P7 | **Keine eigene Laufzeit** | Rose übersetzt nach Python, C, IEC 61131-3 ST, ESPHome-C++. Die Plattformen bleiben, wie sie sind |
| P8 | **Blockstruktur ohne Einrückungsbedeutung** | `do … end` statt Einrückung; LLMs verlieren bei langen Antworten gern eine Einrückungsebene |
| P9 | **Wortschatz, der gut tokenisiert** | Kurze englische Schlüsselwörter (`fn`, `law`, `ctrl`, `machine`, `table`, `use`), ASCII, keine exotischen Operatoren |
| P10 | **Neuerfindungs-Detektor** | Ähnelt ein selbstgeschriebener Rumpf einem bekannten Baustein (Intent-Embedding oder AST-Ähnlichkeit), meldet `rose.check` den Hinweis `R201 known-solution` |

Rose ist damit weniger eine allgemeine Programmiersprache als eine
**Planungs- und Kompositionssprache mit Prüfer**. Für Schleifen, Strings und
Klebecode genügt ein bewusst kleiner Kern (Abschnitt 5.1).

## 5. Die Sprache

Grammatik-Entwurf: [`spec/grammar.ebnf`](../spec/grammar.ebnf). Beispiele:
[`examples/`](../examples).

### 5.1 Kern

```rose
module demo.primes

use rc:Sieve_of_Eratosthenes as sieve        # Rosetta-Code-Task
use oeis:A000040 as primes                   # Folge der Primzahlen

fn primes_below(n: Int{>= 2}) -> List[Int]
  intent "all primes smaller than n"
  ensure sorted(result) and all(result, primes.contains)
  cost   O(n log log n)
do
  return sieve(n - 1)
end

test primes_below(10) == [2, 3, 5, 7]
test primes_below(2)  == []
```

- Typen: `Int`, `Real`, `Bool`, `Text`, `List[T]`, `Map[K,V]`, `Opt[T]`,
  Tupel, Aufzählungen `{a, b, c}`.
- Verfeinerungen: `Int{>= 2}`, `Real[%]{0 .. 100}`.
- **Größen mit Einheit:** `Real[W]`, `Real[kg/s]`, `Real[K]`. Absolute
  Temperaturen (`degC`) und Temperaturdifferenzen (`K`) sind verschiedene
  Typen – `degC - degC` ergibt `K`, `degC + degC` ist ein Fehler.
- Effekte: Funktionen sind rein, außer sie deklarieren `effect io | time |
  rand | state`.
- Verträge: `require` (Vorbedingung), `ensure` (Nachbedingung, `result`),
  `cost` (dokumentierte Komplexität, wird im Benchmark geprüft).

### 5.2 Bausteinarten

| Art | Schlüsselwort | Beispiel | Automatische Prüfung |
|---|---|---|---|
| Algorithmus | `fn` / `use rc:` | Sieb, Dijkstra, LZW | Tests, Kreuzvergleich mehrerer Implementierungen |
| Mathematik | `use math:` / `use oeis:` | Binomialkoeffizient, Gauß-Summe, Folgen | Gleichheit mit Referenz, ggf. mathlib-Beweis |
| Physikalisches Gesetz | `law` | Q̇ = ṁ·c_p·ΔT, Ohm, Wärmedurchgang | Dimensionen, Gültigkeitsbereich, Auflösung nach jeder Variablen (SymPy) |
| Konstante | `use const:` | CODATA-Werte, c_p Wasser | Einheit, Quelle, Unsicherheit |
| Streckenmodell | `model` | PT1, PT1+Totzeit, Speicher | Sprungantwort gegen Referenz |
| Regler | `ctrl` | PID mit Anti-Windup, Zweipunkt, Rampe | Abtastzeit Pflicht, Stellgrößenbegrenzung Pflicht, Simulation gegen Streckenmodell |
| Zustandsautomat | `machine` | Pumpe mit Hysterese + Mindestlaufzeit | deterministisch, vollständig, alle Zustände erreichbar, keine Verklemmung |
| Entscheidungstabelle | `table` | Entladequelle nach SOC/Netz (DMN, hit policy `unique`) | vollständig, überschneidungsfrei (vollständige Aufzählung) |
| Bioinformatik | `use bio:` | Homologiesuche, Sequenz zu Accession, Taxon mit Abstammung | Weg über die lokale DIAMOND-nr erzwungen (Abschnitt 5.7) |

### 5.3 Physikalische Gesetze – akausal

Ein `law` ist eine **Gleichung, keine Zuweisung** (wie in Modelica). Das LLM
nennt, was es sucht und was gegeben ist; der Übersetzer löst auf:

```rose
law water_heat_flow
  intent "thermal power carried by a water flow"
  var P:    Real[W]
  var mdot: Real[kg/s]
  var cp:   Real[J/(kg*K)] = const:water.cp_20degC
  var dT:   Real[K]
  eq  P = mdot * cp * dT
  valid dT in 0.5 K .. 80 K
  ref wikidata:Q... # defining formula, wird beim Import gesetzt
end

fn flow_for(p: Real[W], spread: Real[K]) -> Real[kg/s]
  intent "mass flow needed to carry power p at temperature spread"
do
  return solve water_heat_flow for mdot given P = p, dT = spread
end
```

`solve` wird zur Übersetzungszeit symbolisch aufgelöst (`mdot = P/(cp*dT)`),
inklusive Dimensionsprüfung und einer Laufzeitprüfung des Gültigkeitsbereichs.

### 5.4 Regler

```rose
ctrl buffer_temp
  intent "keep buffer tank temperature at setpoint via compressor demand"
  use    ctrl:pid.parallel.antiwindup as pid
  sample 10 s
  in     y: Real[degC]             # Messwert Puffer
  in     w: Real[degC]             # Sollwert
  out    u: Real[%]{0 .. 100}      # Verdichteranforderung
  param  kp = 8 %/K, ti = 600 s, td = 0 s
  tune   simc(model: model:fopdt(k = 0.4 K/%, tau = 1800 s, theta = 120 s))
do
  u = pid(e = w - y, kp, ti, td)
end
```

Pflichtangaben, die ein LLM sonst gern vergisst, sind **syntaktisch
erzwungen**: Abtastzeit, Stellbereich, Einheit der Verstärkung. Fehlen sie,
kommt `E410 ctrl-without-sample-time` bzw. `E411 unbounded-output`.

### 5.5 Automaten und Tabellen

Vorbild ist die Arbeitsweise des batmonitor (Entscheidungstabellen in
`bm_decisions.dmn`, Erreichbarkeitsrechnung in `rep_max_state.py`): Entscheidung
und Beträge getrennt, kleine orthogonale Tabellen, jede Regel mit
automatischer Prüfung.

```rose
machine pump_guard
  intent "circulation pump with hysteresis and minimum run time"
  in     t_buf: Real[degC]
  param  t_on = 45 degC, t_off = 50 degC, min_run = 300 s
  timer  run
  state  Off initial, On
  on Off when t_buf < t_on                      -> On  do start run
  on On  when t_buf > t_off and run >= min_run  -> Off
  out    pump: Bool = state == On
  check  deterministic, reachable, no_deadlock
end

table discharge_source
  intent "choose energy source by battery SOC and grid state"
  hit    unique
  in     soc: Real[%]{0 .. 100}, grid_ok: Bool
  out    src: {battery, grid, none}
  rule   soc >= 20 %,  true  -> battery
  rule   soc <  20 %,  true  -> grid
  rule   soc >= 10 %,  false -> battery
  rule   soc <  10 %,  false -> none
  check  complete, no_overlap
end
```

Für Realzahl-Eingänge zerlegt der Prüfer die Achsen an den Schwellwerten in
Intervalle (hier: `[0,10)`, `[10,20)`, `[20,100]`) und zählt dann vollständig auf
– genau wie `rep_max_state.py` es für die batmonitor-Zustände tut.

### 5.6 Diagnosen

```json
{
  "code": "E201",
  "name": "unit-mismatch",
  "at": {"file": "heat.rose", "line": 14, "col": 12},
  "message": "cannot add Real[W] and Real[kW*h]",
  "fix": [{"replace": "e_day", "with": "e_day / 24 h", "why": "power from daily energy"}],
  "see": "rose.explain('E201')"
}
```

Kategorien: `E1xx` Syntax, `E2xx` Typen/Einheiten, `E3xx` Bausteine
(unbekannt, keine Implementierung für das Ziel), `E4xx` Regler, `E5xx`
Automaten/Tabellen, `R2xx` Empfehlungen (z. B. `R201 known-solution`).

### 5.7 Bio-Aufgaben: Abkürzung über die lokale DIAMOND-nr

**Regel:** Betrifft eine Aufgabe Proteinsequenzen, Homologie, Taxa oder
Accessions, nimmt Rose **immer den lokalen Weg** über die DIAMOND-Datenbank auf
dem dell. Nie NCBI-Online-BLAST (`blastp -remote`, Biopython `NCBIWWW.qblast`),
nie Entrez-`efetch` für Sequenzen, die lokal vorliegen, nie eine selbst
geschriebene Alignment-Schleife über eine Datenbank.

**Bestand** (Repo [gerontec/blastDiamond](https://github.com/gerontec/blastDiamond)):

| Teil | Was |
|---|---|
| `~/diamond/nr_full.dmnd` (NVMe) | komplette NCBI-nr als DIAMOND-DB, täglich ergänzt (`nr_daily_delta.py`, Cron 04:30) |
| `wagodb.blast_*` | Metadaten: Accessions, Länge, `createdate`, Taxa mit Abstammung (`blast_taxon`, Cron 04:55) |
| `dmnd_preselect.py` | Vorauswahl nach Taxon (mit Untertaxa), Länge, `new_days` → kleine Teil-.dmnd, Cache 2 Tage |
| `dmnd_getseq.py` | Reste einer Accession direkt über die Offset-Tabelle der .dmnd |
| `blast_job` + `blast_api_worker.py` | Warteschlange mit RAM-Planung: Grenze min(48 GB, MemAvailable − 4 GB), `--block-size` passend |
| `api.php` | `?r=acc`, `?r=taxon`, `?r=search`, `?r=job`, `?r=amylo` |

**Abbildung der Bausteine:**

| Rose-Baustein | wird übersetzt in |
|---|---|
| `bio:meta.*` – Accession, Taxon, Abstammung, Zählen, „neu seit“ | **reines SQL** auf `blast_*`, keine Suche |
| `bio:seq.get(acc, range?)` | `dmnd_getseq` |
| `bio:search.blastp` / `bio:search.blastx` | Job in `blast_job` (intern) bzw. `POST ?r=search` mit `X-Api-Key` (extern) |
| `bio:amylo` | `?r=amylo` (Tesla P4) |

**Zweistufig erzwungen** – wie im Worker und in `rep_newseq.py`:

1. **Eingrenzen** in MariaDB (Taxon samt Untertaxa, Länge, Erstellungsdatum) → Teil-.dmnd.
2. **Fein suchen** in dieser Menge mit `--dbsize` der vollen nr, damit die
   E-Werte mit einer Suche über die ganze nr vergleichbar bleiben.

`bio:search` ohne Filter ist ein Fehler (`E602`), außer es steht ausdrücklich
`scope all_nr` da. Dann gibt der Prüfer eine Schätzung von Laufzeit und RAM aus
`blast_ram_log` aus. Eine ungefilterte Suche über die ganze nr dauert für 51 aa
mehr als 7 min und belegt ~15 GB RSS, mit Vorauswahl sind es Sekunden.

**Kein zweiter Suchweg:** Der übersetzte Code ruft `diamond` nie selbst auf,
sondern reicht einen Job an die vorhandene Warteschlange. So bleibt die
RAM-Planung des 64-GB-Rechners an einer Stelle.

**Zählfragen sind keine Suche.** „Wie viele SARS-CoV-2-Sequenzen haben
Spike-Länge?“ ist ein `bio:meta.count`, also ein `SELECT` (948 665 Sequenzen,
9 s). Das deckt sich mit der Arbeitsteilung aus 8.3: Zählen macht SQL, nicht
das Modell.

**Empfindlichkeit:** Standard ist `very_sensitive`. `ultra_sensitive` nur mit
Begründung, denn gemessen lieferte es bei der Spike-Abfrage dieselben Treffer
bei etwa 3-facher Laufzeit (13 s gegen 41–46 s).

```rose
use bio:search.blastp as blastp
use bio:meta

fn new_spike_like(query: Fasta) -> List[bio.Hit]
  intent "spike-like proteins added to nr in the last 90 days"
  effect io
do
  return blastp(query, taxon = meta.taxon("Coronaviridae"), len = 1100 .. 1400,
                new_days = 90, sensitivity = very_sensitive, max_targets = all)
end

fn spike_length_count() -> Int
  intent "number of SARS-CoV-2 sequences of spike length in nr"
do
  return meta.count(taxon = meta.taxon("Severe acute respiratory syndrome coronavirus 2"),
                    len = 1200 .. 1300)
end
```

Bio-Diagnosen: `E601 remote-blast` (Online-BLAST oder `qblast` im Code →
`bio:search`), `E602 unfiltered-nr-search`, `E603 charset-join` (Join von
`utf8mb4`-Accessions auf `blast_acc.acc` (ascii) → `CONVERT(… USING ascii)`,
sonst Vollscan über 1,9 Mrd. Zeilen), `R203 local-data-available` (Download
einer Sequenz, die lokal vorliegt), `R204 masked-residues` (Sequenzen aus der
.dmnd können X-Läufe aus der makedb-Maskierung enthalten).

## 6. Der Korpus – Quellen

| Quelle | Inhalt | Lizenz | Nutzung |
|---|---|---|---|
| **Rosetta Code** (MediaWiki-API) | rund 1 300 Tasks + Entwurfs-Tasks, Lösungen in > 900 Sprachen | GFDL 1.3 (Share-alike) | Task-Beschreibung → `intent`, Implementierungen je Sprache, **Ausgaben mehrerer Sprachen als Test-Orakel** |
| TheAlgorithms (GitHub) | Algorithmen in Python, C, Go, … | MIT | permissive Alternative zu Rosetta-Implementierungen |
| **OEIS** | > 370 000 Folgen mit Formeln und Programmen | CC BY-SA 4.0 | `math`-Bausteine, Testwerte |
| **Lean mathlib** | > 200 000 bewiesene Sätze | Apache-2.0 | Aussagen als `math`-Fakten (Stufe `proven`), Umformungsregeln für Verträge |
| NIST DLMF | Spezielle Funktionen, Identitäten | Nutzungsbedingungen prüfen | nur Metadaten und Verweise |
| **Wikidata** | „defining formula“ (P2534) mit Größensymbolen (P7235), ISQ-Dimensionen (P4020) | CC0 | Grundstock der `law`-Bausteine |
| **QUDT** | Größenarten, Einheiten, Dimensionsvektoren | CC BY 4.0 | Einheitensystem des Prüfers |
| **CODATA** | Naturkonstanten mit Unsicherheit | gemeinfrei (NIST) | `const`-Bausteine |
| **Modelica Standard Library** | > 1 000 Modelle: Thermik, Elektrik, Fluid, Mechanik | BSD-3 | `law`- und `model`-Bausteine, akausale Gleichungen direkt übernehmbar |
| python-control, Fachliteratur | PID-Formen, Anti-Windup, Einstellregeln (Ziegler-Nichols, SIMC) | BSD-3 / Zitat | `ctrl`-Bibliothek, eigene Implementierung |
| SCXML (W3C), IEC 61131-3 SFC | Automatenmodelle | W3C / Norm | Import-/Exportformate für `machine` |
| **gerontec/blastDiamond** (lokal) | komplette NCBI-nr als DIAMOND-DB + Metadaten `blast_*` | NCBI-Daten gemeinfrei, Code eigen | `bio`-Bausteine, nur Abbildung auf die vorhandene Strecke (5.7) |
| **Eigene Projekte** | batmonitor-DMN, `rep_max_state.py`, CODESYS-Heizung, ESPHome-Regler | eigen | über die vorhandene `vec_`-Wissensbasis verknüpfen, nicht kopieren |

Nicht verwendet: Project-Euler-Lösungen (Veröffentlichung untersagt),
Stack Overflow (CC BY-SA mit unklarer Codeherkunft).

**Lizenzen sind Teil des Datenmodells.** Jede Implementierung trägt ihre
SPDX-Kennung. `rose.compile` schreibt ein `rose.lock` mit Herkunft und Lizenz
jedes eingesetzten Bausteins und kennt den Schalter
`--license permissive`, der Share-alike-Quellen (GFDL, CC BY-SA) ausschließt.
Rosetta-Code-Implementierungen in veröffentlichtem Code sind damit eine bewusste
Entscheidung, kein Versehen.

## 7. Prüfstufen

Jeder Baustein und jede Implementierung hat eine Stufe; die Suche liefert sie
mit, das LLM bevorzugt höhere Stufen.

| Stufe | Bedeutung |
|---|---|
| `imported` | aus der Quelle übernommen, nicht ausgeführt |
| `parsed` | lässt sich parsen/kompilieren |
| `tested` | läuft in der Sandbox, Ausgabe stimmt mit der Referenz überein |
| `cross_checked` | ≥ 2 unabhängige Implementierungen liefern dieselben Ergebnisse |
| `proven` | Vertrag formal geprüft (mathlib-Beweis, vollständige Aufzählung, CBMC) |

Fremdcode läuft **nur in der Sandbox**: `systemd-run` mit `MemoryMax`,
`bwrap`/nspawn ohne Netz, harte Zeitgrenze je Lauf (≤ 20 s).

## 8. MCP-Server `rose` auf dem dell (192.168.5.23)

Spezifikation der Werkzeuge: [`spec/mcp-tools.md`](../spec/mcp-tools.md).
Datenbankschema: [`schema/rose_schema.sql`](../schema/rose_schema.sql).

### 8.1 Einbettung in die vorhandene Infrastruktur

| Baustein | Bestand auf dem dell | Rose nutzt |
|---|---|---|
| Datenbank | MariaDB 11.8, `wagodb`, `VECTOR(1024)` + HNSW | Tabellen mit Präfix `rose_` in `wagodb` (im Backup, über den vorhandenen `mariadb`-MCP lesbar) |
| Embedding | bge-m3 FP16, llama-server :8084 (P4) | Embedding der `intent`-Texte und Task-Beschreibungen (nicht des Codes) |
| Hybride Suche | Muster aus `vec_suche.py` (FULLTEXT + Vektor) | dasselbe Muster, plus Filter auf Art, Signatur, Dimension, Stufe, Lizenz |
| MCP-Transport | `mariadb`-MCP per `ssh -T 192.168.5.23` (stdio, gemessen 13 ms/Abfrage) | gleicher Weg: `~/mcp/rose/rose-mcp.sh`, optional streamable HTTP |
| Wissensbasis | `vec_mcp_wissen` | Rose-Doku und Diagnosecodes als Quelle `rose` eintragen |

### 8.2 Werkzeuge (Überblick)

| Tool | Zweck |
|---|---|
| `rose.search` | hybride Suche nach Absicht; Filter `kind`, `target`, `min_level`, `license` |
| `rose.match_signature` | typgesteuerte Suche („`(List[Int]) -> Int`“, „liefert `Real[kg/s]` aus `Real[W]`, `Real[K]`“) |
| `rose.get` | Signaturkarte, Rose-Quelltext, Tests, Herkunft eines Bausteins |
| `rose.examples` | vorhandene Implementierungen eines Bausteins in einer Sprache (z. B. Rosetta in Rust) |
| `rose.law_solve` | Gesetz nach einer Variablen auflösen, mit Einheiten |
| `rose.check` | Rose-Quelltext prüfen → Diagnosen (JSON) |
| `rose.compile` | übersetzen in `python`, `c`, `st`, `esphome` → Code + `rose.lock` |
| `rose.test` | Tests in der Sandbox ausführen |
| `rose.submit` | neuen Baustein einreichen (Staging, ungeprüft bis `rose.test` grün) |
| `rose.explain` | Diagnosecode erklären |

### 8.3 Arbeitsteilung LLM ↔ Server

Die Messung an der `vec_`-Wissensbasis hat gezeigt: kleine Modelle schlagen
zuverlässig nach, **filtern und zählen aber falsch**. Darum gilt:

- **Filtern, Ranking, Typ- und Einheitenabgleich macht der Server in SQL.**
- Das LLM wählt aus wenigen, vorsortierten Treffern und schreibt den
  Klebecode.
- Antworten sind klein (Signaturkarten, k ≤ 10), damit auch Qwen3-4B lokal
  damit arbeiten kann.

## 9. Ablauf an einem Beispiel

Aufgabe an das LLM: *„Die Wärmepumpe soll 9 kW bei 5 K Spreizung liefern.
Berechne den nötigen Volumenstrom und schalte die Umwälzpumpe mit Hysterese
45/50 °C und 5 min Mindestlaufzeit. Ziel: ESPHome.“*

1. `rose.search("mass flow from thermal power and temperature spread", kind="law")`
   → `law:water_heat_flow` (Stufe `cross_checked`, Quelle Wikidata + MSL)
2. `rose.search("pump hysteresis minimum run time", kind="machine")`
   → `machine:hysteresis_min_runtime` (Stufe `proven`)
3. LLM schreibt 15 Zeilen Rose: `use` beider Bausteine, Parameter, Ein-/Ausgänge.
4. `rose.check` → `E201`: Leistung als `9` ohne Einheit → LLM korrigiert zu `9 kW`.
5. `rose.compile(target="esphome")` → C++-Lambda-Block + `rose.lock`.
6. `rose.test` → Automat vollständig aufgezählt, Gesetz gegen Referenzwerte geprüft.
7. Ergebnis: ≈ 15 Zeilen Rose statt ≈ 120 Zeilen freihändigem C++, jede Zeile mit
   Herkunft.

## 10. Abgrenzung / Vorbilder

| Vorbild | Übernommen | Nicht übernommen |
|---|---|---|
| Unison | inhaltsadressierter Code (Hash des AST) | eigene Laufzeit und Codebasis-Format |
| Modelica | akausale Gleichungen, Einheiten | DAE-Simulator, objektorientierte Modellhierarchie |
| Dafny / SPARK | `require`/`ensure` | vollständige Beweisführung als Pflicht |
| Hoogle | Suche nach Typsignatur | – |
| DMN / SCXML / IEC 61131 | Tabellen, Automaten, Zielformat ST | XML als Quellformat |
| ArchLang (gerontec/archlang) | „das LLM schreibt Text, der Compiler sagt präzise, was falsch ist“ | – |

## 11. Wie der Nutzen gemessen wird

Rose rechtfertigt sich nur, wenn es messbar besser ist. Drei Varianten, gleiche
Aufgaben, gleiche Modelle (Qwen3-4B lokal, DeepSeek über `ds`, Claude):

- **A** LLM allein, schreibt direkt Python/C.
- **B** LLM + MCP mit dem Korpus, schreibt aber direkt Python/C (Bausteine als
  Beispielcode).
- **B2** LLM + MCP + **Python-Modul `rose`** (bzw. Perl-Modul): derselbe Korpus, `solve`,
  Einheiten, `rose.lock` – aber als Bibliothek in normalem Python, Prüfungen zur Laufzeit
  bzw. über ein Typprüfer-Plugin. Eine Erweiterung von Python selbst (PEP) ist keine
  realistische Option.
- **C** LLM + MCP + Rose.

Aufgaben: (1) Rosetta-Tasks im **Leave-one-out** – der Task wird aus dem Index
entfernt, Teilprobleme bleiben auffindbar; (2) 30 eigene Aufgaben aus dem
Haus-Umfeld (Regler, Automaten, Energieflüsse) mit festen Prüfungen;
(3) 10 Bio-Aufgaben (Homologie, „neu seit“, Zählen nach Taxon). Dort zählt
zusätzlich, ob das LLM den lokalen Weg nimmt oder doch Online-BLAST schreibt.

Kennzahlen: pass@1, Tokens ein/aus, Anzahl check-Runden, Laufzeit,
Einheitenfehler, Fehler in Automaten/Tabellen.

**Entscheidungsregel:** Ist C nicht deutlich besser als B2 (pass@1 und
Fehlerarten), wird die Sprache eingestellt; Rose lebt dann als Python-Modul
plus MCP-Korpus weiter. Die eigentliche Frage lautet: Bringt die **statische**
Prüfung vor dem Lauf (Einheiten, vollständige Tabellen, `E305` bei offenen
Problemen) messbar mehr als dieselben Prüfungen zur Laufzeit? B allein ist bereits ein Gewinn – der Korpus ist der Kern, die
Sprache muss ihren Mehrwert beweisen.

## 12. Fahrplan

| Meilenstein | Inhalt | Abnahme |
|---|---|---|
| **M0** | dieses Konzept | Review |
| **M1** | Rosetta-Import → `rose_unit`/`rose_impl`, Embeddings der Task-Texte | Retrieval: umformulierte Task-Beschreibung → richtiger Task in den Top-3 bei ≥ 80 % |
| **M2** | MCP-Server v0: `search`, `get`, `examples`; `bio`-Bausteine als dünne Abbildung auf blastDiamond (SQL, `dmnd_getseq`, Job-Warteschlange) | Variante B des Benchmarks lauffähig; Bio-Abfrage aus 5.7 liefert dieselben Treffer wie `rep_newseq.py` |
| **M3** | Rose v0: Parser (Lark), Prüfer (Typen, Einheiten), Übersetzer → Python; `fn`, `use`, `test`, `intent` | Beispiel `primes.rose` übersetzt und grün |
| **M4** | `law` + Import Wikidata/QUDT/CODATA/MSL-Thermik, `solve` mit SymPy | 50 Gesetze nach jeder Variable auflösbar, Dimensionen geprüft |
| **M5** | `table`, `machine` mit vollständiger Aufzählung; Ziele ST und C | batmonitor-Tabellen als Rose nachgebaut, Differenztest gegen Original grün |
| **M6** | `ctrl`-Bibliothek (PID mit Anti-Windup, Zweipunkt, Rampe, PT1-Filter, SIMC) + Ziel ESPHome | Simulation gegen `model:fopdt`, Sprungantwort im Toleranzband |
| **M7** | Benchmark A/B/B2/C, Entscheidung Sprache vs. Python-Modul | Bericht mit Zahlen |
| **M8** (in vielen Monaten, nur wenn M7 positiv) | Rose bei Rosetta Code als Sprache eintragen ([Add a Language](https://rosettacode.org/wiki/Rosetta_Code:Add_a_Language)): Sprachseite, Kategorie, Syntax-Highlighting, eigene Lösungen | die eigenen Rose-Lösungen sind lauffähig, `tested`, mit offenem Compiler nachvollziehbar |

Technik: Python 3 auf dem dell, `lark` (Parser), `sympy` (Gesetze), `pint` +
QUDT (Einheiten), `mariadb`-Connector, MCP-Python-SDK. Pakete per
`pip --user`. Bezeichner, Kommentare, API-Felder und Spalten auf Englisch.

### M8 – Rose bei Rosetta Code

Der Kreis schließt sich: Rose lebt vom Rosetta-Korpus und gibt später zurück.
Voraussetzungen, bevor die Sprache eingetragen wird:

- öffentlich verfügbarer Compiler/Übersetzer (MIT), damit jeder die Lösungen
  ausführen kann;
- eine nennenswerte Zahl von Tasks mit **eigenständigen** Rose-Lösungen – nicht
  nur `use rc:<derselbe Task>`; eine Lösung, die den Task selbst referenziert,
  wäre zirkulär und für Rosetta wertlos. Für M8 bekommt der Übersetzer daher
  einen Modus `--self-contained`, der verbietet, den gelösten Task selbst zu
  importieren;
- eigene Rose-Lösungen stehen auf Rosetta unter GFDL – das ist bei der
  Veröffentlichung bewusst so zu wählen;
- Schwerpunkt der eingereichten Lösungen dort, wo Rose etwas zeigt, was andere
  Sprachen nicht zeigen: Einheiten, Gesetze, Regler, geprüfte Automaten.

## 13. Risiken und offene Fragen

- **Lizenz:** GFDL/CC BY-SA im Zielcode → `rose.lock` und `--license
  permissive` (Abschnitt 6). Korpus und Sprache getrennt lizenzieren: Sprache
  und Werkzeuge MIT, Korpus-Daten unter der jeweiligen Quelllizenz.
- **Qualität von Rosetta Code:** viele Lösungen veraltet oder unvollständig →
  Prüfstufen, Sandbox, Kreuzvergleich.
- **Embedding für Code und Formeln:** bge-m3 ist für Fließtext gut, für Code
  mittel. Deshalb wird die Absicht eingebettet, Code über FULLTEXT und
  Signatur gesucht, Formeln über Symbole und Dimensionen. Ein eigenes
  Code-Embedding-Modell ist eine Option für später, keine Startbedingung.
- **Signaturen für Rosetta-Tasks** existieren nicht; sie müssen beim Import
  erzeugt werden (LLM-Vorschlag + Prüfung gegen die Beispielausgaben). Das ist
  der aufwendigste Teil von M1/M3.
- **Umfang:** „alle“ Probleme, Gesetze, Regler ist unbegrenzt. Begrenzung
  über Meilensteine und die Entscheidungsregel in Abschnitt 11.
- **Sicherheit:** Fremdcode nur in der Sandbox; `rose.submit` landet im
  Staging und wird nicht ungeprüft befördert.
- **Lastgrenzen:** Importläufe nur mit `MemoryMax`, P4-Speicher ist mit
  bge-m3 + Qwen3-4B bereits zu ~70 % belegt.
