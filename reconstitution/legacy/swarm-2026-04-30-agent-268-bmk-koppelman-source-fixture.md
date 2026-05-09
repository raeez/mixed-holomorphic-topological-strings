# Agent 268 BMK / Koppelman Source Fixture Report, 2026-04-30

Owned files:

- `references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md`

No manuscript TeX, scripts, bibliography, figure, or build artifact was
edited.  No PDF build was run.

## Claim Attacked

The manuscript uses or alludes to Bochner--Martinelli and
Bochner--Martinelli--Koppelman kernels in the finite-window current
transfer lane.  The attack question was whether primary sources actually
support the needed holomorphic-kernel, Koppelman homotopy, Dolbeault
kernel identity, and residue/Euler-normalization claims, and whether any
external source accidentally imports stronger internal BV/QME,
factorization, Roos, Omega, or brane-defect claims.

## Stable Findings

1. Exact modern kernel anchor exists:
   `LaurentThiebaut11`, Chapter III, Definition 1.2, equation (1.1),
   p. 58, from the official Springer preview, verifies the standard BMK
   kernel normalization; Lemma 1.3, p. 58, verifies the kernel closedness
   and component dbar identity.

2. Exact modern homotopy anchor exists:
   `Ruppenthal08v2-11`, Section 5, Definition 5.1 and Theorem 5.2 /
   equation (10), pp. 14-15 of the arXiv v2 PDF/source, states the
   classical BMK formula for `C^1` `(0,q)`-forms on bounded `C^1`
   domains.  Crossref verifies the final journal metadata
   `Complex Variables and Elliptic Equations` 56(5) (2011), 423-437,
   DOI `10.1080/17476931003728388`; final journal theorem pagination was
   not separately inspected.

3. Historical source metadata is verified but formula anchors remain
   open:
   Koppelman 1967 forms/functions papers are verified by Crossref and
   AMS metadata, Bochner 1943 by Crossref/JSTOR metadata, and Martinelli
   1938 only by local plan plus secondary reference lists.  Original
   theorem, equation, and page anchors for these historical papers are
   still unverified.

4. The source split is strict:
   BMK/Koppelman sources support external several-complex-variables
   kernel and homotopy identities.  They do not prove the manuscript's
   finite-window current transfer, moment projection, collar quotient,
   support-at-zero residue currents, arity-two Hamiltonian/Matlis
   action, all-window obstruction vector, or native `E_2` factorization
   construction.

## Manuscript Map

- `main.tex:1242-1420`: finite-window BMK transfer.  External BMK
  sources support only the kernel/homotopy background.  Cutoff,
  distributional extension, finite-window projection, and collar quotient
  remain internal.
- `main.tex:1271-1283`: full dimension-two BMK kernel.  Supported up to
  convention translation by Laurent-Thiebaut Definition 1.2 and
  Ruppenthal Definition 5.1.
- `main.tex:1284-1299`: `dbar z` terms, cutoff, current limit.  The
  pre-cutoff component identity is externally supported; the current
  construction is internal.
- `main.tex:1310-1349`: residue currents and moments.  No new BMK source
  support; use existing Matlis/residue fixture plus internal residue
  calculation.
- `main.tex:1351-1378`: arity-two Hamiltonian/Matlis coadjoint formula.
  Internal.
- `main.tex:1380-1405`: all-window obstruction vector.  Internal and not
  closed by BMK sources.
- `main.tex:1407-1419`: two-variable principal part face and no
  curve-VOA/Zhu transfer.  BMK sources do not justify scalar-contact
  projection or all-arity transfer.
- `appendix-factorization-current-conventions.tex:399-475`: same
  source split as the main finite-window theorem.

## Non-Support Boundaries

The fixture explicitly forbids using these BMK/Koppelman sources as
support for:

- Costello graph realization.
- Brane-defect QME counterterms.
- Scalar-contact projection.
- Roos compatibility.
- Omega trace-state theorem.
- Native `E_2` factorization transfer or all-window uniform transfer.
- Finite-window moment projection/collar-removal.
- Hamiltonian/Matlis arity-two computation.
- Compact-CY, global BCOV, CoHA, BKM, OSV/GV, or Igusa consequences.

## Files Read

- `AGENTS.md`
- `CLAUDE.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `reconstitution/missing-primary-source-fixture-plan-2026-04-30.md`
- `main.tex`
- `appendix-factorization-current-conventions.tex`
- `appendix-matlis-principal-parts.tex`
- `references/primary-sources/matlis-local-cohomology-residue-anchor.md`
- `reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md`
- `reconstitution/swarm-2026-04-30-agent-211-bm-transfer-main-integration.md`
- `reconstitution/swarm-2026-04-30-agent-222-bm-all-window-transfer-supremum-rework.md`
- Existing source-fixture examples under `references/primary-sources/`
  for format and boundary style.

## Web / Source Checks

Verified metadata and anchors by Crossref, AMS/Springer pages, official
Springer previews, and arXiv:

- Koppelman, "The Cauchy integral for differential forms",
  DOI `10.1090/s0002-9904-1967-11744-0`.
- Koppelman, "The Cauchy integral for functions of several complex
  variables", DOI `10.1090/s0002-9904-1967-11757-9`.
- Bochner, "Analytic and Meromorphic Continuation by Means of Green's
  Formula", DOI `10.2307/1969103`.
- Range, GTM 108 book DOI `10.1007/978-1-4757-1918-5` and Chapter IV
  DOI `10.1007/978-1-4757-1918-5_4`.
- Laurent-Thiebaut Chapter III DOI `10.1007/978-0-85729-030-4_3`.
- Lieb--Michel Chapter I DOI `10.1007/978-3-322-91608-2_2`.
- Ruppenthal final article DOI `10.1080/17476931003728388` and
  arXiv:0803.0092v2.

Access limits:

- AMS Koppelman PDFs returned Cloudflare 403 HTML.
- JSTOR Bochner access returned an access-check page.
- Springer full chapter PDF requests for Laurent-Thiebaut and
  Lieb--Michel redirected to authentication HTML.  Exact anchors from
  those chapters are therefore limited to the official preview pages.
- Temporary downloaded previews and arXiv files stayed in
  `/tmp/agent268-sources` and were not imported into the repository.

## Commands Run

Key local commands:

```bash
rg -n "Bochner|Martinelli|Koppelman|BMK|K_BM|kernel" .
nl -ba main.tex | sed -n '1180,1510p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '380,490p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,230p'
sed -n '1,240p' references/primary-sources/matlis-local-cohomology-residue-anchor.md
pdftotext /tmp/agent268-sources/ruppenthal-0803.0092.pdf /tmp/agent268-sources/ruppenthal-0803.0092.txt
gzip -cd /tmp/agent268-sources/ruppenthal-0803.0092.tar > /tmp/agent268-sources/friedrichs-arxiv2.tex
rg -n "Definition 5\\.1|Theorem 5\\.2|Theorem 5\\.6|Bochner|Koppelman|BMK" /tmp/agent268-sources/friedrichs-arxiv2.tex
```

Key metadata/source commands:

```bash
curl -L -sS 'https://api.crossref.org/works/10.1090%2Fs0002-9904-1967-11744-0'
curl -L -sS 'https://api.crossref.org/works/10.1090%2FS0002-9904-1967-11757-9'
curl -L -sS 'https://api.crossref.org/works/10.2307%2F1969103'
curl -L -sS 'https://api.crossref.org/works/10.1007%2F978-1-4757-1918-5'
curl -L -sS 'https://api.crossref.org/works/10.1007%2F978-0-85729-030-4_3'
curl -L -sS 'https://api.crossref.org/works/10.1007%2F978-3-322-91608-2_2'
curl -L -sS 'https://api.crossref.org/works?query.title=Friedrichs%20extension%20lemma%20with%20boundary%20values%20and%20applications%20in%20complex%20analysis&rows=3'
curl -L --fail -sS https://arxiv.org/pdf/0803.0092 -o /tmp/agent268-sources/ruppenthal-0803.0092.pdf
curl -L --fail -sS https://arxiv.org/e-print/0803.0092 -o /tmp/agent268-sources/ruppenthal-0803.0092.tar
curl -L -sS 'https://export.arxiv.org/api/query?id_list=0803.0092'
```

## Remaining Gaps

1. Primary scan of Martinelli 1938.
2. Readable Bochner 1943 article with exact Green-formula anchor.
3. AMS Koppelman 1967 scans or PDFs with exact formula/page anchors.
4. Full Range 1986 Chapter IV and Lieb--Michel 2002 Chapter I exact
   theorem/equation anchors.
5. Henkin--Leiterer exact theorem if the manuscript chooses that modern
   reference lane.
6. Local orientation/sign check from standard BMK conventions to the
   manuscript's dimension-two `K_BM(zeta,z)`.

## Files Changed

- Added `references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md`.

The two owned files are ready to be staged and no other repo file should
be staged by this agent.
