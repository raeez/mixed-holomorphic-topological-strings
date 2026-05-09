# Agent 278 Report: Internal Stratified Weiss TeX Audit

Status: report-only TeX audit.

Worktree: `/Users/raeez/topological-strings`.

Owned writable file:

- `reconstitution/swarm-2026-04-30-agent-278-internal-stratified-weiss-tex-audit.md`

No TeX file was edited.  No build was run.

## Verdict

Agent 273's specification has not yet been installed in the current TeX.
The manuscript has the ingredients for the reduced product-basis
prefactorization datum, but it does not name that datum as
\(\mathcal F^{\mathrm{red}}_{\Omega,\mathrm{prod}}\) or separate it from
the full stratified theorem surface.  The current obstruction vectors in
`open-obligations.tex`, `theorem-lanes.tex`, and
`claim-strength-ledger.tex` still use the older seven-component vector
with \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) inside the
internal theorem surface.

The TeX should install
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
\]
as the internal stratified vector and keep
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) as an external source
gate.

## Ground Anchors

- `main.tex:1175-1240`: constructed Hamiltonian CE/factorization
  observables and extension-by-zero products on product opens.
- `main.tex:6187-6233`: support-local principal-part brane current
  prefactorization products by extension by zero on intervals.
- `main.tex:6390-6404`: reduced principal-part current scope; no
  unreduced BV/factorization algebra or centrality homotopies.
- `main.tex:6436-6480`: unreduced lift obstruction datum.
- `appendix-factorization-current-conventions.tex:697-789`: normal
  \(\Omega\)-weighted brane-current brackets and interval extension
  compatibility.
- `appendix-unreduced-bv-qme.tex:2487-2630`: normal
  \(\Omega\)-equivariant Costello kernel habitat.
- `appendix-unreduced-bv-qme.tex:3431-3554`: \(Q_\Omega\)-centrality
  primitive criterion and the secondary \(L_{V_\Omega}H\) obstruction.

## Minimal Core Text

Use this vector wherever the full internal stratified theorem is asserted:

```tex
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
  =
  (
    \delta_{\mathrm{pref}},
    \delta_{\mathrm{assoc}},
    \delta_{\mathrm{Weiss}},
    \operatorname{ob}_{\mathrm{collar}},
    \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \operatorname{ob}_{\Omega\mathrm{-basic}},
    \operatorname{ob}_{\mathrm{tr}\mathrm{-top}}
  ).
\]
```

Use this reduced datum wherever the positive construction is recorded:

```tex
Let \(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\) be the
two-color product basis whose basics are bulk product disks
\(U\times B\subset X\setminus L\), brane intervals \(I\subset L\), and
finite disjoint unions.  Put
\[
  \mathcal F^{\mathrm{red}}_{\Omega,X}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \left(
    \Omega_c^\bullet(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \right)
  \widehat\otimes R_\Omega^{N,M},
\]
where
\(\mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
\cong\mathfrak h^\vee_{\mathrm{cont}}\), and
\[
  \mathcal F^{\mathrm{red}}_{\Omega,L}(I)
  =
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I).
\]
The products are extension by zero on compact supports followed by CE or
completed symmetric multiplication.  Hence
\(\delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0\) on this reduced
product-basis datum.  No collar module, arbitrary collared Weiss descent,
unreduced centrality homotopy, brane-defect QME curvature cancellation,
basic \(\Omega\)-primitive, or trace-state topology is constructed here.
```

Use this descent replacement for theorem-grade Weiss descent:

```tex
A collared stratified Weiss cover \(\mathcal U=\{U_i\}\) of \(V\) is a
stratified cover such that every finite subset of \(V\) lies in some
\(U_i\), and if the subset meets \(L\), the same \(U_i\) contains a
product collar of its lower-stratum part.  For a candidate
\(\mathcal F^{\mathrm{str}}_{\Omega,N}\), put
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0}\cap\cdots\cap U_{i_p}),
  \qquad
  \mathbb D=\check\delta+(-1)^p d_{\mathcal F},
\]
and
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)
  =
  \operatorname{Cone}\left(
    \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
    \to
    \operatorname{Tot}\check C^\bullet
    (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N})
  \right).
\]
```

Keep this source gate outside the internal vector:

```tex
The source-primary class
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) is not an internal
component of
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  It is an
external matched-conventions gate for importing Costello--Gwilliam, AFT,
CFG, Weiss/Ran, or Costello \(\Omega\)-background source theorems.
```

Use this trace aggregate sentence:

```tex
The component \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\) is the
aggregate trace-state topology obstruction; its expanded trace vector is
\(\operatorname{Ob}_{\mathrm{tr},\Omega}\).
```

## File-by-File Insertion Map

### `main.tex`

Primary positive insertion: after `main.tex:1240`, before
`\begin{prop}[Finite-window Bochner--Martinelli transfer...]`.

Minimal insertion: add a proposition named
`Reduced product-basis stratified prefactorization datum` using the
reduced datum text above.  This is the cleanest local-model location:
`main.tex:1175-1240` proves the bulk CE/factorization value and
extension-by-zero products; the brane value is already introduced in
`main.tex:1147-1160` and proved later in `main.tex:6187-6233`.

Secondary insertion: sharpen `main.tex:4239-4255`.  The present remark is
global factorization-center language:
\[
  \operatorname{Tot}C^\bullet_{\mathrm{WR}}(\operatorname{Ran}(L);\cdots).
\]
Add the Cech cone definition above either inside the remark after
`main.tex:4248` or as a new paragraph after `main.tex:4255`.  The
sentence should say that this is the internal stratified pair
\((X,L)\) version, distinct from the global matched-conventions
factorization-center descent problem.

Scope cross-references:

- Insert before `main.tex:6404`: the reduced current theorem supplies
  the brane interval component of
  \(\mathcal F^{\mathrm{red}}_{\Omega,\mathrm{prod}}\) only.
- Insert before `main.tex:6481`: the unreduced lift obstruction is part
  of \(\operatorname{ob}_{\mathrm{collar}}\),
  \(\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}}\), and
  \(\operatorname{ob}^{P_0}_{\mathrm{cent}}\).
- Insert after `main.tex:7569` and before `main.tex:7570`: the Costello
  specialization problem controls the brane-defect QME, collar, and
  centrality entries of
  \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\); normal
  \(\Omega\)-localization and reduced current brackets do not kill that
  vector.

### `open-obligations.tex`

Primary insertion: inside the item beginning at `open-obligations.tex:876`.

Insert the positive reduced datum after `open-obligations.tex:900` and
before `open-obligations.tex:901`.  This prevents the reduced
product-basis construction from being swallowed by the stronger
unconstructed stratified object.

Replace `open-obligations.tex:973-981`.  The current descent defect is
the informal expression
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
  -
  \operatorname*{holim}_{U\in\mathcal U}
  \mathcal F^{\mathrm{str}}_{\Omega,N}(U).
\]
Replace it by the collared-cover and Cech-cone text above.

Replace the vector at `open-obligations.tex:1073-1084` by
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  Keep
`open-obligations.tex:1085-1090`, but move it to a source-gate paragraph
after the internal vector.

No parameter correction is needed in `open-obligations.tex:982-994`: the
\(P_0\)-centrality homotopy already uses
\(\{\rho(x),a\}_{P_{0,\hbar_{\mathrm{QME}}}}\).  When the centrality row
is asserted over covers, add
\(\operatorname{Tot}\check C^\bullet(\mathcal U;-)\) to the Hom complex
near `open-obligations.tex:1004-1041`.

Tie the trace block `open-obligations.tex:1092-1199` back to the internal
vector by inserting the trace aggregate sentence before
`open-obligations.tex:1188`.

### `theorem-lanes.tex`

Primary insertion: split the statement beginning at
`theorem-lanes.tex:3007`.

Insert the reduced product-basis datum after `theorem-lanes.tex:3055`
and before `theorem-lanes.tex:3057`.  Then replace
`theorem-lanes.tex:3057-3070` with the nine-component internal vector and
the source-gate sentence.

Correct the centrality parameter at `theorem-lanes.tex:3071-3084`.
The current text asks for \(P_{0,\hbar_{\mathrm W}}\)-homotopies while
the differential is \(d_{\mathrm{QME}}\).  Unless this branch explicitly
identifies the Weyl and QME parameters, replace
\[
  \{\rho(x),a\}_{P_{0,\hbar_{\mathrm W}}}
\]
by
\[
  \{\rho(x),a\}_{P_{0,\hbar_{\mathrm{QME}}}} .
\]

Add a cross-reference after `theorem-lanes.tex:3003` and before
`theorem-lanes.tex:3005`: invariant centrality primitives are the
\(\operatorname{ob}_{\Omega\mathrm{-basic}}\) entry of the stratified
vector.  The existing
\(\operatorname{Ob}^{\mathrm{QME}}_{\Omega,w}\) at
`theorem-lanes.tex:2991-3001` remains the local graph/QME subproblem.

Additional parameter conflict: `theorem-lanes.tex:2934-2939` uses
\(\hbar_{\mathrm W}\) in the QME curvature bracket
\(\{C_{<n,\Omega,M},C_{<n,\Omega,M}\}_{\hbar_{\mathrm W},M,\Omega}\).
The appendix model uses \(\hbar_{\mathrm{QME}}\) for the corresponding
local-functional bracket at
`appendix-unreduced-bv-qme.tex:3461-3467`.  Either change the theorem-lane
bracket to \(\hbar_{\mathrm{QME}}\) or state the branch identification.

Leave the physical vector at `theorem-lanes.tex:3169-3190` as the
expanded physical trace-state vector.  It should be referenced by
\(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\), not folded into the
internal nine-component vector componentwise.

### `claim-strength-ledger.tex`

Add a proved row before `claim-strength-ledger.tex:183`:

```tex
Reduced product-basis stratified prefactorization datum &
proved reduced product-basis &
bulk product disks and brane intervals have extension-by-zero products;
evidence: Proposition~\ref{prop:local-hamiltonian-factorization-observables},
Theorem~\ref{thm:reduced-principal-part-boundary-current}, and
Theorem~\ref{thm:app-omega-weighted-current-brackets}; no collar module,
arbitrary collared Weiss descent, unreduced centrality, QME, basic
\(\Omega\)-primitive, or trace-state topology\\
```

Do not silently expand the four-entry center vector at
`claim-strength-ledger.tex:183-190` or `claim-strength-ledger.tex:413-423`
unless the row is being used as the full stratified theorem.  Minimal
repair: label it as the factorization-center subvector of
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).

Update `claim-strength-ledger.tex:523-528` so the missing theorem points
to
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\), not the
old unqualified \(\operatorname{Ob}_{\mathrm{str},\Omega,N}\).

Replace the seven-component vector at `claim-strength-ledger.tex:762-772`
with the nine-component internal vector.  Keep source support as a
separate source gate.

Insert after `claim-strength-ledger.tex:797`: the protected trace row is
the expansion of \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\), and
\(\operatorname{Ob}_{\mathrm{tr},\Omega}\) is the expanded trace vector.

### `local-dictionary.tex`

Primary insertion: split `local-dictionary.tex:678-693`.

Minimal repair:

1. Add a row for
   \(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\): bulk product disks,
   brane intervals, finite disjoint unions, no constructed collar module.
2. Add a row for
   \(\mathcal F^{\mathrm{red}}_{\Omega,\mathrm{prod}}\): the two values
   and extension-by-zero products.
3. Keep the existing stratified datum row as the full theorem surface,
   with collars and \(\mathcal M_{\Omega,L}\) explicitly unconstructed by
   the reduced datum.

Update `local-dictionary.tex:695-712`.  This is a top-level
seven-entry \(\Omega\)-obligation vector, not the stale stratified
seven-component vector.  Do not replace the whole vector by the internal
nine-component vector.  Instead state:

- \(\operatorname{ob}_{\Omega,\mathrm{strat}}\) expands to
  \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\);
- \(\operatorname{ob}_{\Omega,N\to\infty}\) points to
  \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\) and its expanded trace
  vector.

Add entries before `local-dictionary.tex:827` in the canonical-symbols
table for:

- \(\delta_{\mathrm{Weiss}}(V,\mathcal U)\), using the Cech cone;
- \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\), using the
  nine-component vector;
- \(\operatorname{ob}_{\Omega\mathrm{-basic}}\), using the secondary
  \(L_{V_\Omega}H\) class;
- \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\), pointing to
  \(\operatorname{Ob}_{\mathrm{tr},\Omega}\).

Preserve the normal-\(\Omega\) convention at
`local-dictionary.tex:441-491` and the normal contraction boundary at
`local-dictionary.tex:518-541`.

## Seven-Component Vector Conflicts

1. `open-obligations.tex:1075-1083` is stale.  It has seven entries and
   includes \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) inside the
   internal vector.  It lacks
   \(\operatorname{ob}_{\mathrm{collar}}\),
   \(\operatorname{ob}_{\Omega\mathrm{-basic}}\), and
   \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

2. `theorem-lanes.tex:3061-3069` is stale in the same way.  It also sits
   next to the parameter collision at `theorem-lanes.tex:3071-3084`,
   where \(P_{0,\hbar_{\mathrm W}}\) is used for a QME centrality
   homotopy.

3. `claim-strength-ledger.tex:764-772` is stale in the same way.
   `claim-strength-ledger.tex:183-190` and
   `claim-strength-ledger.tex:413-423` are four-component
   factorization-center subvectors; they should be labelled as such, not
   promoted to the full stratified vector.

4. `local-dictionary.tex:695-706` is a seven-entry top-level
   \(\Omega\)-obligation vector.  It is not the same stale vector.  Its
   conflict is expansion: \(\operatorname{ob}_{\Omega,\mathrm{strat}}\)
   currently has no visible expansion into the internal nine-component
   vector, and \(\operatorname{ob}_{\Omega,N\to\infty}\) does not yet name
   \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

No `Ob^{266}` occurrence was found in TeX; it appears only in
reconstitution reports.  No
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\) occurrence
was found in current TeX.

## Integration Order

1. `local-dictionary.tex`: install symbols and expansion discipline.
2. `main.tex`: record the positive reduced datum and internal theorem
   anchor.
3. `open-obligations.tex`: replace the descent defect and stale vector.
4. `theorem-lanes.tex`: split the lane and fix the parameter collision.
5. `claim-strength-ledger.tex`: record the proved reduced row and update
   statuses.

This order prevents the ledger from naming symbols before the dictionary
defines them and prevents the theorem lane from treating the reduced
current bracket as QME evidence.
