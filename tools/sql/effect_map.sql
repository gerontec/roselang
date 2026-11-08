-- Effect -> compound -> organism, built from the Rose corpus by tools/build_effect_map.py.
-- Rebuilt completely on every run; every row names its source and, where there is one, the reference.
CREATE TABLE IF NOT EXISTS rose_organism (
  organism_id   INT AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(255) NOT NULL,
  common_name   VARCHAR(255),
  kingdom       VARCHAR(64),
  family        VARCHAR(128),
  ncbi_taxid    INT,
  wikidata      VARCHAR(16),
  ref           VARCHAR(255) COMMENT 'Rose card of the organism (bio:taxon.* or bio:lotusorg.*)',
  UNIQUE KEY uq_organism_name (name),
  KEY idx_organism_taxid (ncbi_taxid),
  KEY idx_organism_common (common_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rose_compound (
  compound_id   INT AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(255) NOT NULL,
  wikidata      VARCHAR(16),
  inchikey      CHAR(27),
  atc           VARCHAR(255) COMMENT 'ATC codes, comma-separated, drugs only',
  ref           VARCHAR(255) NOT NULL COMMENT 'Rose card (bio:drug.* or bio:lotus.*)',
  UNIQUE KEY uq_compound_ref (ref),
  KEY idx_compound_wikidata (wikidata),
  KEY idx_compound_name (name),
  KEY idx_compound_inchikey (inchikey)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rose_effect (
  effect_id     INT AUTO_INCREMENT PRIMARY KEY,
  kind          ENUM('therapeutic_class','target','indication','action') NOT NULL,
  name          VARCHAR(255) NOT NULL COMMENT 'e.g. antimalarial (ATC P01B), TRPV1',
  code          VARCHAR(32) COMMENT 'ATC group code, UniProt accession, ...',
  chembl_target VARCHAR(32),
  UNIQUE KEY uq_effect (kind, name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rose_compound_organism (
  compound_id   INT NOT NULL,
  organism_id   INT NOT NULL,
  reference_doi VARCHAR(255),
  sourced       TINYINT(1) NOT NULL DEFAULT 1 COMMENT '0 = claim without a reference (Wikidata)',
  source        VARCHAR(32) NOT NULL COMMENT 'lotus | wikidata',
  PRIMARY KEY (compound_id, organism_id),
  KEY idx_co_organism (organism_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rose_compound_effect (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  compound_id   INT NOT NULL,
  effect_id     INT NOT NULL,
  relation      VARCHAR(32) NOT NULL COMMENT 'class | agonist | inhibitor | modulator | cytotoxic | treats',
  measure       VARCHAR(16) COMMENT 'EC50 | IC50 | Ki | potency',
  value_um_min  DOUBLE COMMENT 'micromolar',
  value_um_max  DOUBLE,
  test_system   VARCHAR(64) COMMENT 'enzyme | cells | animal | human',
  evidence      VARCHAR(32) COMMENT 'as in facts/*.tsv: handbook | single_study | several_studies | review | regulatory | screening',
  reference     VARCHAR(255) COMMENT 'DOI or source URL',
  source        VARCHAR(32) NOT NULL COMMENT 'atc | rose-facts | wikidata',
  UNIQUE KEY uq_ce (compound_id, effect_id, relation, source, reference(100)),
  KEY idx_ce_effect (effect_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE OR REPLACE VIEW rose_v_effect_compound_organism AS
SELECT e.kind AS effect_kind, e.name AS effect, e.code AS effect_code, ce.relation, ce.measure,
       ce.value_um_min, ce.value_um_max, ce.test_system, ce.evidence, ce.reference AS effect_reference,
       c.name AS compound, c.ref AS compound_ref, o.name AS organism, o.common_name, o.kingdom, o.family,
       co.reference_doi AS found_in_reference, co.sourced AS found_in_sourced
FROM rose_effect e
JOIN rose_compound_effect ce USING (effect_id)
JOIN rose_compound c USING (compound_id)
LEFT JOIN rose_compound_organism co USING (compound_id)
LEFT JOIN rose_organism o USING (organism_id);
