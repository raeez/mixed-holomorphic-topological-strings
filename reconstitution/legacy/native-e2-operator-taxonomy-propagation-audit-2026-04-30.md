# Native E2 Operator Taxonomy Propagation Audit

Date: 2026-04-30
Agent: 318
Scope: manuscript propagation of Agent 312's native holomorphic
`E_2`/operator-algebra taxonomy.
Files changed: this report and
`reconstitution/swarm-2026-04-30-agent-318-native-e2-operator-taxonomy-propagation-audit.md`.
No manuscript TeX edited.

## Verdict

The taxonomy has propagated through the named manuscript surfaces. The
native object is consistently the holomorphic `E_2`/factorization algebra
on the formal `\C^2` disk. The brane Ext/open algebra, the Matlis
principal-part current algebra, and the controlled `\C\times\R`
curve/VOA/Zhu reduction are separated in the main theorem lanes,
obligations, ledger, and dictionary.

No fatal false-transfer sentence was found in the named files. The
remaining defects are local patch targets: an early topological-direction
OPE phrase, a generic BV/OPE phrase, a scalar Bochner--Martinelli display,
an incomplete dictionary tuple for one-dimensional restriction, a missing
local obstruction-vector cross-reference, and one missing coadjoint-action
dot.

## Evidence

- Native `\C^2` factorization: `main.tex:1111-1240`,
  `theorem-lanes.tex:227-379`, `theorem-lanes.tex:381-547`,
  `claim-strength-ledger.tex:641-681`, `local-dictionary.tex:170-215`.
- Brane Ext/open algebra: `main.tex:2865-2961`,
  `main.tex:2984-3046`, `theorem-lanes.tex:302-320`,
  `local-dictionary.tex:233-257`.
- Matlis principal parts and currents: `main.tex:6093-6110`,
  `main.tex:6238-6257`, `main.tex:6554-6770`,
  `theorem-lanes.tex:322-345`, `open-obligations.tex:256-330`,
  `claim-strength-ledger.tex:1180-1233`,
  `local-dictionary.tex:1444-1535`.
- Controlled curve/VOA/Zhu gate: `main.tex:1713-1719`,
  `theorem-lanes.tex:715-1100`, `open-obligations.tex:224-254`,
  `claim-strength-ledger.tex:683-741`, `local-dictionary.tex:290-421`.

## Attack-Heal Findings

1. Native object read as curve VOA.
   Result: blocked globally. `main.tex:1165-1172` and
   `theorem-lanes.tex:381-388` explicitly say the native object is
   two-complex-dimensional and not a curve vertex algebra. Heal remaining:
   patch `main.tex:655-671` and `main.tex:826-832`.

2. Brane Ext/open algebra confused with closed factorization algebra.
   Result: separated. `main.tex:2947-2961` and `main.tex:2984-3046`
   compute the point-brane Ext algebra and keep the full
   factorization-center morphism outside the proved local theorem.

3. Matlis principal parts confused with PBW one-psi labels.
   Result: separated. `main.tex:6328-6410`,
   `open-obligations.tex:288-330`, and
   `local-dictionary.tex:1213-1310` distinguish `\Psi_{a,b}` from
   `\rho_{a,b}` by action and polarization.

4. Principal-part current algebra overstated as unreduced BV center.
   Result: blocked. `main.tex:6554-6770` states a reduced support-local
   `P_0` prefactorization datum only; `main.tex:6803-6845` records the
   unreduced lift data as still missing.

5. `\C\times\R`, VOA, BRST, and Zhu material imported natively.
   Result: blocked. `theorem-lanes.tex:715-1100`,
   `open-obligations.tex:224-254`, and
   `claim-strength-ledger.tex:683-741` require a retained-mode reduction,
   vertex package, Zhu map, anomaly transport, and
   `\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}`.

6. Compact-CY, CoHA, Igusa/BKM, quintic, OSV/GV, MNOP transfer.
   Result: quarantined. `open-obligations.tex:9-13`,
   `claim-strength-ledger.tex:57-63`, and
   `theorem-lanes.tex:347-378` deny theorem support without a separate
   matched-conventions theorem.

## Exact TeX Patch Targets

No TeX patch was applied. The following are exact later patch targets.

1. `main.tex:655-671`

Insert after the itemized list:

```tex
The product on the closed side in this paragraph is the
topological-current avatar used for the local trace comparison.  The
native holomorphic operator algebra is the
\(\C^2\)-holomorphic factorization algebra
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) of
Definition~\ref{def:local-hamiltonian-chiral-factorization-algebra};
no one-dimensional vertex OPE or Zhu algebra is asserted here.
```

Reason: line 667 uses "operator-product expansion in the `\R`-direction".
Without the sentence above, that phrase can be read as a curve OPE.

2. `main.tex:826-832`

Replace the clause beginning at line 831 by:

```tex
together with associativity of the resulting factorization algebra; an
OPE algebra is present only after the separate one-complex-dimensional
reduction datum of Statement~\ref{thm:lane-constructed-chiral-interface}.
```

Reason: "factorisation/OPE algebra" is too compressed after the new
native `E_2` firewall.

3. `theorem-lanes.tex:474-488`

Replace the scalar Bochner--Martinelli display by the full kernel:

```tex
\[
  \eta=\zeta-z,\qquad
  r^2=|\eta_1|^2+|\eta_2|^2,\qquad
  d\bar\eta_j=d\bar\zeta_j-d\bar z_j .
\]
\[
  K_{\mathrm{BM}}(\zeta,z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{
    \overline{\eta_1}\,d\bar\eta_2
    -
    \overline{\eta_2}\,d\bar\eta_1
  }{r^4}
  \wedge d\zeta_1\wedge d\zeta_2 .
\]
```

Reason: `main.tex:1264-1285` already uses the full
`d\bar\eta_j=d\bar\zeta_j-d\bar z_j` kernel and warns that the
`d\bar z=0` component is only scalar.

4. `local-dictionary.tex:290-323`

Replace the tuple at lines 296-299 by:

```tex
\[
  \mathfrak R_L
  =
  (\iota_L,\mathcal B_\perp,\mathsf R_{L,\mathcal B_\perp},
   V_L,\mathbf 1_L,T_L,Y_L,\zeta_{L,\hbar})
\]
```

Then replace later references to `\mathsf R_L` in the same entry by
`\mathsf R_{L,\mathcal B_\perp}`.

Reason: the dictionary later requires OPE and Zhu data, and
`theorem-lanes.tex:699-702` already lists the complete tuple.

5. `main.tex:1713-1719`

Replace the remark by:

```tex
\begin{rmk}[Reduced chiral-interface target]\label{rmk:constructed-chiral-interface-target}
  A curve chiral algebra attached to this theory is the reduced target of
  Statement~\ref{thm:lane-constructed-chiral-interface}, not part of the
  native Darboux package.  It must pass through the controlled datum
  \(\mathcal R_{\C\times\R}\), keeping the \(z_2\)-coefficient or the full
  two-index principal-part system.  Admission is the vanishing, or the
  exact obstruction theorem, for
  \[
    \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
    =
    (\operatorname{Ob}_{\mathrm{red}},
     \operatorname{Ob}_{\mathrm{vert}},
     \operatorname{Ob}_{\mathrm{Zhu}},
     \operatorname{Ob}_{\mathrm{nat}}).
  \]
\end{rmk}
```

Reason: the local Darboux package should point to the same obstruction
vector used in `theorem-lanes.tex:1088-1100`,
`open-obligations.tex:243-254`, and `claim-strength-ledger.tex:732-740`.

6. `claim-strength-ledger.tex:319-331`

Replace line 326:

```tex
\(z_1^{N+2}\rho_{N+1,0}=-(N+2)\rho_{0,1}\);
```

by:

```tex
\(z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}\);
```

Reason: this is the Hamiltonian coadjoint action, not multiplication in
the principal-part module.

## Firewall Wording

Use this wording whenever the taxonomy is summarized:

```tex
The native operator algebra of the local
\(\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}\) model is the
\(\C^2\)-holomorphic Hamiltonian \(E_2\)-type factorization algebra
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\).  Its brane avatars are the
point-brane Ext/open algebra, the Weyl/Moyal degree-zero brane algebra,
and the support-local Matlis principal-part current algebra.  These
avatars are not curve vertex algebras and do not constitute the
unreduced open BV factorization center.  A curve VOA, BRST vertex
algebra, or Zhu comparison is admissible only after a controlled
\(\mathcal R_{\C\times\R}\) reduction retaining the \(z_2\)-mode or the
full two-index principal-part coefficient system, together with the
factorization-to-vertex data, anomaly transport, Moyal/Zhu
multiplicativity, and vanishing or exact naming of
\(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\).  Compact-CY, CoHA,
Igusa/BKM, quintic, OSV/GV, MNOP, Abel--Jacobi, and global BCOV claims
remain external comparison targets.
```

## Agent 312 Report Corrections

The manuscript convention is `\mathcal R_{\C\times\R}`, not Agent 312's
`\mathfrak R_{\mathbb C\times\mathbb R}`. Future TeX should preserve the
manuscript convention unless a deliberate notation change is applied
globally.

Agent 312's reports omit the plus sign in the displayed BRST current.
The TeX surface is correct at `theorem-lanes.tex:949-954`:
`j_{\mathrm{BRST}}=\operatorname{Tr}(c[Z_1,Z_2])
+\frac12\operatorname{Tr}(b[c,c])`.
Do not propagate the report typo into TeX.

## Commands Run

```bash
sed -n '1,260p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-312-native-holomorphic-e2-operator-algebra-attack-heal.md
sed -n '1,553p' reconstitution/native-holomorphic-e2-operator-algebra-attack-heal-2026-04-30.md
rg -n -F -e 'E_2' -e 'factorization algebra' -e 'vertex algebra' -e 'Zhu' -e 'Matlis' -e 'principal-part' -e 'Ext' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
nl -ba main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex | sed -n '<targeted ranges>'
git status --short -- reconstitution main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
```

No TeX build was run because manuscript TeX was not edited.
