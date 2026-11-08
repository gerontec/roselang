-- Rose corpus schema for MariaDB >= 11.7 (VECTOR + HNSW). All tables carry the prefix rose_.
-- Verified against MariaDB 11.8. Agents should read through a SELECT-only database user.

CREATE TABLE IF NOT EXISTS rose_source (
  source_id    SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name         VARCHAR(64)  NOT NULL UNIQUE,      -- rosettacode, oeis, wikidata, qudt, codata, msl, mathlib, blastdiamond, own
  url          VARCHAR(255) NOT NULL,
  license      VARCHAR(64)  NOT NULL,             -- SPDX id, e.g. GFDL-1.3-or-later, CC-BY-SA-4.0, CC0-1.0
  share_alike  BOOLEAN      NOT NULL DEFAULT FALSE,
  imported_at  DATETIME     NULL,
  note         TEXT         NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS rose_unit (
  unit_id      BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  ref          VARCHAR(190) NOT NULL UNIQUE,      -- rc:Sieve_of_Eratosthenes, oeis:A000040, law:water_heat_flow
  kind         ENUM('algo','math','law','const','model','ctrl','machine','table','bio','open') NOT NULL,  -- open = negative knowledge: no known solution, hint only, never usable via `use`
  name         VARCHAR(255) NOT NULL,
  intent       TEXT         NOT NULL,             -- embedding key
  signature    VARCHAR(1024) NULL,                -- canonical Rose type signature
  dims_in      VARCHAR(255) NULL,                 -- dimension vectors (QUDT), normalised, for SQL matching
  dims_out     VARCHAR(255) NULL,
  rose_src     MEDIUMTEXT   NULL,                 -- canonical Rose source (rose fmt)
  payload      JSON         NULL,                 -- kind-specific raw data: TeX formula, constant value, sequence terms
  ast_hash     BINARY(32)   NULL,                 -- sha256 of canonical AST, content address
  level        ENUM('imported','parsed','tested','cross_checked','proven') NOT NULL DEFAULT 'imported',
  source_id    SMALLINT UNSIGNED NOT NULL,
  source_url   VARCHAR(512) NULL,
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY idx_kind_level (kind, level),
  KEY idx_ast_hash (ast_hash),
  FULLTEXT KEY ft_unit (name, intent),
  CONSTRAINT fk_unit_source FOREIGN KEY (source_id) REFERENCES rose_source (source_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- External identifiers: rosetta task title, OEIS A-number, Wikidata Q-id, DOI, mathlib name, MSL class
CREATE TABLE IF NOT EXISTS rose_alias (
  scheme       VARCHAR(32)  NOT NULL,
  value        VARCHAR(255) NOT NULL,
  unit_id      BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (scheme, value),
  KEY idx_alias_unit (unit_id),
  CONSTRAINT fk_alias_unit FOREIGN KEY (unit_id) REFERENCES rose_unit (unit_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Concrete implementations per language (Rosetta has many per task)
CREATE TABLE IF NOT EXISTS rose_impl (
  impl_id      BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  unit_id      BIGINT UNSIGNED NOT NULL,
  lang         VARCHAR(32)  NOT NULL,             -- python, c, rust, st, esphome, rose, ...
  code         MEDIUMTEXT   NOT NULL,
  code_sha     BINARY(32)   NOT NULL,
  license      VARCHAR(64)  NOT NULL,
  source_url   VARCHAR(512) NULL,
  level        ENUM('imported','parsed','tested','cross_checked','proven') NOT NULL DEFAULT 'imported',
  runtime_ms   INT UNSIGNED NULL,
  UNIQUE KEY uq_impl (unit_id, lang, code_sha),
  FULLTEXT KEY ft_code (code),
  CONSTRAINT fk_impl_unit FOREIGN KEY (unit_id) REFERENCES rose_unit (unit_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS rose_test (
  test_id      BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  unit_id      BIGINT UNSIGNED NOT NULL,
  input        JSON NOT NULL,
  expected     JSON NOT NULL,
  tolerance    DOUBLE NULL,                       -- relative, for Real results
  origin       ENUM('source','cross','generated','manual') NOT NULL,
  CONSTRAINT fk_test_unit FOREIGN KEY (unit_id) REFERENCES rose_unit (unit_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS rose_run (
  run_id       BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  impl_id      BIGINT UNSIGNED NOT NULL,
  test_id      BIGINT UNSIGNED NULL,
  ok           BOOLEAN NOT NULL,
  output       TEXT NULL,
  ms           INT UNSIGNED NULL,
  ran_at       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY idx_run_impl (impl_id, ran_at),
  CONSTRAINT fk_run_impl FOREIGN KEY (impl_id) REFERENCES rose_impl (impl_id) ON DELETE CASCADE,
  CONSTRAINT fk_run_test FOREIGN KEY (test_id) REFERENCES rose_test (test_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS rose_dep (
  unit_id      BIGINT UNSIGNED NOT NULL,
  uses_unit_id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (unit_id, uses_unit_id),
  CONSTRAINT fk_dep_unit FOREIGN KEY (unit_id) REFERENCES rose_unit (unit_id) ON DELETE CASCADE,
  CONSTRAINT fk_dep_uses FOREIGN KEY (uses_unit_id) REFERENCES rose_unit (unit_id) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Variables of laws/models: lets SQL find "a law that yields kg/s from W and K"
CREATE TABLE IF NOT EXISTS rose_law_var (
  unit_id      BIGINT UNSIGNED NOT NULL,
  symbol       VARCHAR(32)  COLLATE utf8mb4_bin NOT NULL,   -- case-sensitive: r and R are different symbols
  quantity     VARCHAR(64)  NULL,                 -- QUDT quantity kind, e.g. MassFlowRate
  unit         VARCHAR(32)  NOT NULL,             -- SI unit, e.g. kg/s
  dim          VARCHAR(64)  NOT NULL,             -- normalised dimension vector, e.g. M1 T-1
  role         ENUM('var','param','const') NOT NULL DEFAULT 'var',
  PRIMARY KEY (unit_id, symbol),
  KEY idx_dim (dim),
  CONSTRAINT fk_lawvar_unit FOREIGN KEY (unit_id) REFERENCES rose_unit (unit_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS rose_embed_model (
  model_id     SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name         VARCHAR(64) NOT NULL UNIQUE,       -- bge-m3-FP16
  dim          SMALLINT UNSIGNED NOT NULL,
  endpoint     VARCHAR(255) NOT NULL              -- http://127.0.0.1:8084/v1
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS rose_embedding (
  unit_id      BIGINT UNSIGNED NOT NULL PRIMARY KEY,
  model_id     SMALLINT UNSIGNED NOT NULL,
  text_sha     BINARY(32) NOT NULL,               -- sha256 of embedded text, idempotent re-embedding
  v            VECTOR(1024) NOT NULL,
  VECTOR INDEX idx_v (v) M=16 DISTANCE=cosine,
  CONSTRAINT fk_emb_unit  FOREIGN KEY (unit_id)  REFERENCES rose_unit (unit_id) ON DELETE CASCADE,
  CONSTRAINT fk_emb_model FOREIGN KEY (model_id) REFERENCES rose_embed_model (model_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Staging for rose.submit: never visible to search until promoted
CREATE TABLE IF NOT EXISTS rose_submission (
  submission_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  author        VARCHAR(64) NOT NULL,
  rose_src      MEDIUMTEXT  NOT NULL,
  note          TEXT NULL,
  status        ENUM('staged','tested','promoted','rejected') NOT NULL DEFAULT 'staged',
  unit_id       BIGINT UNSIGNED NULL,
  created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_sub_unit FOREIGN KEY (unit_id) REFERENCES rose_unit (unit_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Hybrid search sketch (server side, parameters bound by the MCP server):
--   SELECT u.ref, u.signature, u.level,
--          0.6 * (1 - VEC_DISTANCE_COSINE(e.v, VEC_FromText(?)))
--        + 0.4 * MATCH(u.name, u.intent) AGAINST (? IN NATURAL LANGUAGE MODE) / ? AS score
--     FROM rose_unit u JOIN rose_embedding e USING (unit_id)
--    WHERE u.kind = ? AND u.level >= ?
--    ORDER BY score DESC LIMIT ?;
