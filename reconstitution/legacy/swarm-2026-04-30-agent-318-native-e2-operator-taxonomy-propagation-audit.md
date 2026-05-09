# Swarm Report: Agent 318 Native E2 Operator Taxonomy Propagation Audit

Date: 2026-04-30
Agent: 318
Lane: propagation audit for Agent 312's native holomorphic `E_2`
operator-algebra taxonomy.
Write ownership:
`reconstitution/native-e2-operator-taxonomy-propagation-audit-2026-04-30.md`
and this report.
No manuscript TeX edited.

## Claim Attacked

The manuscript must consistently separate four objects:

1. the native holomorphic `E_2`/factorization algebra on `\C^2`;
2. the brane Ext/open algebra and Weyl/Moyal degree-zero brane algebra;
3. the Matlis principal-part coefficient/current algebra;
4. any controlled `\C\times\R` curve VOA, BRST, or Zhu reduction.

The failure mode is false transfer: reading the native `\C^2` object as
a curve vertex algebra, reading reduced principal-part currents as the
full open BV factorization center, or importing compact-CY/CoHA/BKM
language into the local theorem surface.

## Result

No fatal propagation failure was found in the named files. The taxonomy is
installed in:

- `main.tex:1111-1240` and `theorem-lanes.tex:227-547` for the native
  `\C^2` factorization algebra;
- `main.tex:2865-3046` for the point-brane Ext/open algebra;
- `main.tex:6093-6110`, `main.tex:6554-6770`, and
  `local-dictionary.tex:1444-1535` for Matlis principal parts and
  support-local currents;
- `theorem-lanes.tex:715-1100`, `open-obligations.tex:224-254`,
  `claim-strength-ledger.tex:683-741`, and
  `local-dictionary.tex:290-421` for the controlled curve/VOA/Zhu gate.

The remaining issues are patch targets, not theorem collapses.

## Exact TeX Patch Targets

1. `main.tex:655-671`: add the firewall sentence after the two-algebras
   itemize. The closed-side product there is the topological-current
   avatar; the native operator algebra is
   `\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}`; no one-dimensional vertex
   OPE or Zhu algebra is asserted.

2. `main.tex:826-832`: replace "factorisation/OPE algebra" by a gated
   phrase: the BV consistency condition gives a factorization algebra;
   an OPE algebra appears only after
   `Statement~\ref{thm:lane-constructed-chiral-interface}`.

3. `theorem-lanes.tex:474-488`: replace the scalar
   Bochner--Martinelli display using only `d\bar\zeta_j` by the full
   `K_{\mathrm{BM}}(\zeta,z)` display with
   `d\bar\eta_j=d\bar\zeta_j-d\bar z_j`, matching `main.tex:1264-1285`.

4. `local-dictionary.tex:290-323`: replace the one-dimensional
   restriction tuple by
   `(\iota_L,\mathcal B_\perp,\mathsf R_{L,\mathcal B_\perp},
   V_L,\mathbf 1_L,T_L,Y_L,\zeta_{L,\hbar})`, matching
   `theorem-lanes.tex:699-702`.

5. `main.tex:1713-1719`: expand the reduced chiral-interface remark to
   cite `\mathcal R_{\C\times\R}` and the obstruction vector
   `\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}`.

6. `claim-strength-ledger.tex:319-331`: replace
   `z_1^{N+2}\rho_{N+1,0}` by
   `z_1^{N+2}\cdot\rho_{N+1,0}`.

The full patch snippets are recorded in
`reconstitution/native-e2-operator-taxonomy-propagation-audit-2026-04-30.md`.

## Firewall Wording

Use the following wording:

```tex
The native operator algebra is the
\(\C^2\)-holomorphic Hamiltonian \(E_2\)-type factorization algebra
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\).  The point-brane Ext/open
algebra, the Weyl/Moyal brane algebra, and the support-local Matlis
principal-part current algebra are brane or defect avatars, not curve
vertex algebras and not the unreduced open BV factorization center.  A
curve VOA, BRST vertex algebra, or Zhu comparison is admissible only
after a controlled \(\mathcal R_{\C\times\R}\) reduction retaining the
\(z_2\)-mode or full two-index principal-part coefficient system and
after the factorization-to-vertex, anomaly, Moyal/Zhu, and native-return
obstructions in \(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\) have
been killed or named exactly.
```

## Report-Only Corrections To Agent 312

Agent 312's reports use `\mathfrak R_{\mathbb C\times\mathbb R}`. The
manuscript uses `\mathcal R_{\C\times\R}` throughout the named TeX files.
Propagate the manuscript notation.

Agent 312's reports display the BRST current without the plus sign before
`\frac12\operatorname{Tr}(b[c,c])`. The manuscript has the correct sign
at `theorem-lanes.tex:949-954`; do not copy the report typo.

## Tests And Commands

Read/grep audit only. No TeX build was run because no TeX was edited.

Verification commands included:

```bash
rg -n -F -e 'E_2' -e 'factorization algebra' -e 'vertex algebra' -e 'Zhu' -e 'Matlis' -e 'principal-part' -e 'Ext' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
rg -n -F -e 'operator-product expansion' -e 'factorisation/OPE algebra' -e 'z_1^{N+2}' -e '\mathfrak R_{' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex reconstitution/*312*operator-algebra*.md
git status --short -- reconstitution main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
```
