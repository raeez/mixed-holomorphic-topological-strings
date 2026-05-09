# Worker 6 theorem-status sweep -- 2026-04-28

Scope: whole-paper theorem-status consistency and stale-language sweep,
with edits confined to `main.tex`, `claim-strength-ledger.tex`,
`open-obligations.tex`, and reconstitution audit notes.

## Claims Attacked

| Claim attacked | Failure or proof | Local anchors | Replacement logic | Status recommendation |
|---|---|---|---|---|
| Umbrella theorem / old lettered theorem language | Failure found. The text still referred to old `Statement (a)`, `part (d)`, `part (e)`, "universal conilpotent theorem", "theorem package", and "Resolution of the unreduced..." language. | `main.tex:1155`, `main.tex:1164`, `main.tex:1203`, `main.tex:1219`, `main.tex:1251`, `main.tex:1267`, `main.tex:2491`, `main.tex:2654`, `main.tex:2695`, `main.tex:2724`. | Replaced old part labels by named lanes, made the main block a summary corollary, and changed "resolution" to residual analysis with proved partial results plus remaining obstruction. | Proved core only; summary corollary has no independent claim strength beyond the lanes and ledger. |
| Wrong interval source variables | Failure found. One rendered corollary still used `C^\infty_c(\R)` where the surrounding convention uses de Rham compact-support notation. The introduction also lacked the completed tensor in the interval current algebra. | `main.tex:527`, `main.tex:4487`. | Replaced by `\Omega^\bullet_c(I)\widehat\otimes\widehat{\mathfrak h}` and `a,b\in\Omega^0_c(\R)`. | Brane-line source remains a compactly supported de Rham current convention; degree-zero test functions are notation inside that convention. |
| Unreduced cotangent centrality | Failure found. The reduced-principal-part section still said "This unreduced lift is..." after listing missing homotopies. | `main.tex:4445`. | Changed to "The desired unreduced lift would be..." and kept it outside the classical reduced theorem. | Open / conditional on unreduced BV model, centrality homotopies, and QME obstruction. |
| Stable bulk--boundary Koszul duality | Failure found in ledger wording: the conjectural horizon was said not to prove a "theorem package". | `claim-strength-ledger.tex:110`. | Replaced by "local Hamiltonian BF/Moyal core." | Conjectural strategic horizon only. |
| Open-obligation boundary | Failure found in opening wording: "local theorem package" could read as a proved umbrella. | `open-obligations.tex:3`. | Replaced by "proved local core." | Obligations remain outside the proved core. |
| Theorem-lane process-language audit | Failure found in a release QA note, not in the rendered lane itself. | `reconstitution/release-qa-2026-04-28.md:144-149`. | Marked the earlier old-label risk closed by the current stable-cross-reference wording. | No rendered process-language risk remains in the theorem-status surface checked here. |
| `\Psi` / `\rho` module identification | No rendered defect found in the allowed TeX surface. | `abstract.tex:22-24`, `local-dictionary.tex:75-157`, `theorem-lanes.tex:66-84`, `main.tex:3681-3728`, `main.tex:4009-4101`. | No patch needed. Existing text says same indices are labels, not an `\mathfrak h`-module isomorphism; Rees/Fourier bridge remains open. | Separation proved where stated; Rees/Fourier bridge open. |
| Full quantum all-order or Costello graph overclaim | No rendered defect found in the allowed TeX surface after the old-label patch. | `main.tex:5452-5484`, `main.tex:5499-5515`, `theorem-lanes.tex:299-359`, `open-obligations.tex:57-68`. | No patch needed. The all-order statement is degree-zero Moyal/Weyl only; graph realization and one-antifield lift remain conditional/open. | Degree-zero Moyal/Weyl proved in its stated algebraic lane; descendant and graph lifts conditional/open. |
| Cross-volume transfer | No rendered defect found in the allowed TeX surface. | `abstract.tex:37-41`, `claim-strength-ledger.tex:112-116`, `open-obligations.tex:84-88`, `main.tex:5895-5913`. | No patch needed. Firewalls already say no compact Calabi--Yau, Vol III, BKM/Igusa, or sister-volume theorem follows without a separate matched-conventions proof. | Not asserted. |

## Commands Run

- `sed -n '1,260p' CLAUDE.md`
- `rg --files -g 'abstract.tex' -g 'claim-strength-ledger.tex' -g 'theorem-lanes.tex' -g 'open-obligations.tex' -g 'local-dictionary.tex' -g 'main.tex' -g 'reconstitution/*.md'`
- `rg -n -i -e "umbrella" -e "main theorem" -e "full quantum" -e "to all orders" -e "all-order" -e "regulator independence" -e "QME" -e "centrality" -e "unreduced" -e "compact Calabi" -e "Vol III" -e "BKM" -e "Igusa" ...`
- `rg -n -F -e "C^\\infty_c" -e "C^{\\infty}_c" -e "C_c^\\infty" ...`
- `rg -n -F -e "\\Psi" -e "\\rho" -e "isomorphism" -e "different bases" ...`
- `rg -n -F -e "theorem package" -e "Statement~(" -e "Statements~(" -e "part~(" ...`
- `nl -ba main.tex | sed -n ...` for each patched region.
- `git diff --check`

## Remaining Open Questions

No theorem-status wording blocker remains in this worker's writable surface.
The mathematical open problems are unchanged: unreduced cotangent
factorization-centre morphism and centrality homotopies, one-antifield
quantum lift, mixed brane-defect QME, regulator independence, Rees/Fourier
bridge, primary-source anchoring for some external imports, and any
cross-volume transfer theorem.
