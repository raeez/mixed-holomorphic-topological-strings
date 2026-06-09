# Rectification flags — 2026-06-10 platonic restructuring

Open structural work surviving the eleven-section restructuring. Each row names the obstruction exactly; none blocks the build.

| # | flag | site | exact remaining work |
|---|---|---|---|
| 1 | local-dictionary dismemberment | `local-dictionary.tex` (2,686 lines, input before §1) | definitions to first-use sites in §§2–9; kinematic-locality theorem (dict:~1168) to §1; symbol tables to a nomenclature appendix. Blocked on: per-definition use-site map (`scripts/structure_graph.py where <label>`). |
| 2 | tate-T1 split | `tate-T1-weighted-completion.tex` (3,231 lines, §5) | envelope + kernel-admissibility theorems stay §5 (used by `thm:universal-ce-pv-koszul-criterion` at its proof); RG/QME counterterm + wavefront half (≈ lines 700–3231) → §7. Same split discipline as tate-P1. |
| 3 | BMK current block in §1.3 | main.tex §1.3 (Bochner–Martinelli proposition, ~400 lines) | → §7/§8 lane. Blocked on: compressing the stratified roadmap enumerate (§5 stratified subsection opening) whose item 7 forward-cites it. |
| 4 | §3 trace material | §3.1/§3.5 (J-derivation, boundary evaluation, B_f centrality; ADHM/Hilbert lemma) | J-material → §4 head; ADHM/Hilbert lemma → §10 as an example. Verify `lem:formal-stalk-trace` use-sites first. |
| 5 | §1.1 order | §1.1 "…in one calculation" | title promises a calculation; a Definition arrives first. Lead with the N=2 computation, then the chart definition. |
| 6 | stratified roadmap enumerate | §5 stratified subsection opening (7-item enumerate) | compress to ≤1 paragraph; it forward-announces every later theorem with labels (motivation-killing). |
| 7 | duplicate displays | A^cl_∂,N cdga, g = h ⋉ h^∨[1], J(f), generator assignment each displayed 3–8× across §§1–5 | dedupe to one display + references, chunk-by-chunk (Gate 5). |
| 8 | platonic ch. 10 | `% STRUCTURAL-STUB` before §11 | W_∞[λ]/E_∞ conditional chapter only as genuine mathematics from Prochazka / Creutzig–Kanade–Linshaw / Pope–Romans–Shen–Bakas / Yamada (site 14). Never as disclaimers (commit 3ed5e29 precedent). |
| 9 | grav-ops dedup | §2 closing subsection | its "Let h = …" recap duplicates §2.1's construction; fold into one statement during the §2 chunk sweep. |
| 10 | midpoint/third-order verification blocks | §5 (after the all-orders theorem) | agent-E verdict: appendix-grade (appendix-radial-parts-moyal), leaving 10-line statements; decide during the §5 sweep. |
