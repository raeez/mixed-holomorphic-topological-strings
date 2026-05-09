# Scalar Central-Extension Integration Spec

Date: 2026-04-30.
Scope: manuscript integration specification for Agent 265's opposite
central-extension scalar branch.
Status: report-only.  No TeX file is edited by this spec.

## Verdict

Agent 265 constructed a theorem-grade scalar repair in the CE source category.
It should be integrated as a source replacement, not as a same-branch
Costello-local closed exchange.

The branch replaces the scalar-reduced source \(\bar A\) by the opposite
central extension
\[
  L^-_N=\bar A^{\mathrm{cl}}_{-\hbar N\bar c}
  =
  \bar A\oplus\C[[\hbar]]K_{\mathrm{cl}},
  \qquad
  [(f,aK),(g,bK)]
  =
  (\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K).
\]
The central cochain \(J_{\mathrm{op}}=-k^\vee\), with
\(k^\vee(K_{\mathrm{cl}})=1\) and \(k^\vee(\bar A)=0\), satisfies
\[
  d_{\mathrm{CE}}J_{\mathrm{op}}=-\hbar N\bar c.
\]
Hence the ordinary scalar QME class \(\operatorname{Ob}_{\mathrm{sc}}
=\hbar N\bar c\) becomes exact after source replacement:
\[
  \operatorname{Ob}_{\mathrm{sc}}+d_{\mathrm{CE}}J_{\mathrm{op}}=0.
\]

This does not kill \(\hbar N[\bar c]\) in
\(H^2_{\mathrm{Lie}}(\bar A;\C)[[\hbar]]\).  It kills the pullback of that
class in \(C^\bullet_{\mathrm{Lie}}(L^-_N)\) because the source has been
changed and the new central cochain is allowed.

## Source Anchors

- `main.tex:423-492`: \(\omega=\bar c\), CE convention, and non-exactness on
  \(\bar A\).
- `main.tex:7577-7705`: scalar QME alternatives and current same-branch
  Costello-local obstruction language.
- `main.tex:8084-8215`: scalar-contact lift gate before non-scalar and
  closed-exchange obstruction complexes.
- `appendix-unreduced-bv-qme.tex:560-589`: unreduced primitive
  \(\eta(f)=-[f]_0\), \(d_{\mathrm{CE}}\eta=\omega\), and non-descent to
  \(\bar A\).
- `appendix-unreduced-bv-qme.tex:591-685`: scalar QME representative
  \(\hbar N[\bar c]\) and no internal scalar-reduced counterterm.
- `appendix-unreduced-bv-qme.tex:687-770`: unreduced central-character source
  replacement and \(\hbar N\omega+d_{\mathrm{CE}}(\hbar\chi_N)=0\).
- `appendix-unreduced-bv-qme.tex:2142-2232`: native finite-window Costello/QME
  habitat, Hom differential, and source-face term.
- `local-dictionary.tex:83-97`: BV pairing is not a Costello coefficient
  coevaluation kernel without a convergent Casimir.
- `local-dictionary.tex:829-923`: scalar-contact projection is a filtered
  chain map; in the ordinary branch the first two-input defect is
  \(\hbar N\omega(f,g)\gamma_{\mathbf 1}\).
- `tate-T1-weighted-completion.tex:1526-1741`: closed-exchange plus
  counterterm criterion and the \(\beta,\mu,\lambda\) obstruction sequence.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-240`:
  local Costello sources do not automatically supply the Hamiltonian
  current-valued target, \(\mathcal D'_c\) wavefront theorem, or bulk-to-defect
  kernel.
- `reconstitution/swarm-2026-04-30-agent-265-opposite-central-extension-scalar-branch-construction.md`:
  constructed branch and attack ledger.
- `reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md`:
  same-branch Costello-local scalar source obstruction.
- `reconstitution/swarm-2026-04-30-agent-247-costello-local-closed-exchange-cone-realization.md`:
  algebraic cone is not Costello-local.
- `reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md`:
  finite-window scalar obstruction sequence.

## Theorem Statement To Integrate

Use this theorem as a new item in Theorem
`\ref{thm:scalar-qme-alternatives}` or as a short theorem immediately after
it.  The most stable location is inside the scalar QME alternatives theorem,
between the central-character branch and the algebraic central-contact cone.

```tex
\begin{thm}[Opposite central source replacement for the scalar QME branch]
\label{thm:opposite-central-source-scalar-qme}
Let \(A=\C[z_1,z_2]\), \(\bar A=A/\C\cdot 1\), and
\[
  \bar c(f,g)=[\{f,g\}]_0,\qquad
  \{f,g\}=\partial_{z_1}f\,\partial_{z_2}g
  -\partial_{z_2}f\,\partial_{z_1}g .
\]
For \(N>0\), put
\[
  L^-_N=\bar A^{\mathrm{cl}}_{-\hbar N\bar c}
  =
  \bar A\oplus\C[[\hbar]]K_{\mathrm{cl}}
\]
with bracket
\[
  [(f,aK_{\mathrm{cl}}),(g,bK_{\mathrm{cl}})]
  =
  (\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K_{\mathrm{cl}}),
  \qquad [K_{\mathrm{cl}},-]=0 .
\]
If \(k^\vee(K_{\mathrm{cl}})=1\) and \(k^\vee(\bar A)=0\), then
\[
  d_{\mathrm{CE}}k^\vee=\hbar N\bar c,\qquad
  d_{\mathrm{CE}}(-k^\vee)=-\hbar N\bar c .
\]
Consequently the ordinary scalar QME representative
\[
  \operatorname{Ob}_{\mathrm{sc},M}
  =
  \hbar N\bar c_M
\]
is killed after replacing the scalar-reduced source by \(L^-_N\):
\[
  \operatorname{Ob}_{\mathrm{sc},M}
  +d_{\mathrm{CE}}(-k^\vee_M)=0 .
\]
The finite-window version is compatible under truncation maps preserving
\(z_1,z_2\) and sending \(K_{\mathrm{cl}}\) to \(K_{\mathrm{cl}}\).

This is a scalar source replacement.  It is the \(\hbar\)-adic pushout of the
unreduced central extension
\[
  0\to\C\cdot1\to A\to\bar A\to0
\]
along \(1\mapsto-\hbar N K_{\mathrm{cl}}\).  Pullback along
\[
  \Phi(f)=(\bar f,-\hbar N[f]_0K_{\mathrm{cl}})
\]
sends the primitive \(-k^\vee\) to \(\hbar\chi_N\), where
\(\chi_N(f)=N[f]_0\).  Thus it recovers the central-character cancellation
\[
  \hbar N\omega+d_{\mathrm{CE}}(\hbar\chi_N)=0
\]
on the unreduced source.

The construction does not prove a same-branch Costello-local closed exchange.
The cochain \(-k^\vee_M\) is not closed; its CE differential is exactly the
scalar contact being killed.  A Costello-local repair of the original
scalar-reduced branch would still have to construct a closed source complex,
finite-scale propagator, bulk-to-defect graph map, source-face Hom
differential, filtered scalar-contact chain projection, local counterterms,
and compatible finite-window representatives whose scalar image is
\(-\hbar N[\bar c_M]\).
\end{thm}
```

## CE Sign Computation

The manuscript convention is
\[
  (d_{\mathrm{CE}}\lambda)(x,y)=-\lambda([x,y]).
\]
For \(x=(f,aK)\), \(y=(g,bK)\) in \(L^-_N\),
\[
  [x,y]=(\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K).
\]
Therefore
\[
\begin{aligned}
  (d_{\mathrm{CE}}k^\vee)(x,y)
    &=-k^\vee(\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K)\\
    &=\hbar N\bar c(f,g),\\
  (d_{\mathrm{CE}}(-k^\vee))(x,y)
    &=-\hbar N\bar c(f,g).
\end{aligned}
\]
On the detecting pair,
\[
  \bar c(z_1,z_2)=1,\qquad \{z_1,z_2\}_{\bar A}=0,
\]
so
\[
  (d_{\mathrm{CE}}(-k^\vee))(z_1,z_2)=-\hbar N,
  \qquad
  \operatorname{Ob}_{\mathrm{sc}}(z_1,z_2)=+\hbar N.
\]
The signs cancel.

The same pair proves non-exactness on the reduced source.  If
\(\bar c=d_{\mathrm{CE}}\xi\) on \(\bar A\), then
\[
  1=\bar c(z_1,z_2)
  =(d_{\mathrm{CE}}\xi)(z_1,z_2)
  =-\xi(\{z_1,z_2\}_{\bar A})
  =-\xi(0)=0.
\]
The contradiction is the reduced scalar obstruction.  The primitive exists
only after the central line is restored in the source.

## Proof Skeleton

1. Cite Lemma `\ref{lem:omega-cocycle}` and
   Lemma `\ref{lem:app-unreduced-scalar-primitive}` for the cocycle
   \(\bar c\), its unreduced primitive, and non-descent to \(\bar A\).
2. Define \(L^-_N\).  Jacobi follows because the central term is the CE
   cocycle \(-\hbar N\bar c\).
3. Compute \(d_{\mathrm{CE}}k^\vee\) and \(d_{\mathrm{CE}}(-k^\vee)\) with
   the manuscript sign convention.  Evaluate on \(z_1,z_2\) to fix the sign.
4. Identify the scalar QME representative from
   Theorem `\ref{thm:app-scalar-contact-qme-class}`:
   \(\operatorname{Ob}_{\mathrm{sc}}=\hbar N\bar c\) with the brane density
   factor \(\int a(t)b(t)\gamma_{\mathbf 1}(t)\,dt\).
5. Add the same brane density to \(J_{\mathrm{op}}=-k^\vee\).  The CE
   differential cancels the scalar representative exactly.
6. Relate the construction to the unreduced source by the pushout map
   \(1\mapsto-\hbar N K_{\mathrm{cl}}\).  Pullback of \(J_{\mathrm{op}}\)
   gives \(\hbar\chi_N\), matching Theorem
   `\ref{thm:app-central-character-qme-cancellation}`.
7. For finite windows \(M\), require windows to retain \(z_1,z_2\), set
   \(K_{\mathrm{cl}}\mapsto K_{\mathrm{cl}}\), and use that
   \(\bar c_M\) only detects the surviving linear pair.  Then
   \((J_{\mathrm{op},M})_M\) is compatible and there is no Roos obstruction
   inside this source-replacement inverse system.
8. Close with branch separation: the cochain \(-k^\vee\) is not a closed
   element of a Costello closed-source complex.  It is a primitive in a
   changed CE source.  The original Costello-local scalar branch remains
   governed by \(o_{\sigma,M}^{(1),\mathrm{sc}}\) and
   \(\beta_M^{\mathrm{Cost},\mathrm{sc}}\).

## Control-Surface Updates

### `main.tex`

Required update:

- In Theorem `\ref{thm:scalar-qme-alternatives}` at `main.tex:7598-7624`,
  add a separate enumerated branch for the opposite central source
  \(L^-_N=\bar A^{\mathrm{cl}}_{-\hbar N\bar c}\), with the CE sign
  computation \(d_{\mathrm{CE}}(-k^\vee)=-\hbar N\bar c\).
- Keep the existing central-character branch as the unreduced-source form of
  the same mechanism.  Add the pushout statement
  \(1\mapsto-\hbar N K_{\mathrm{cl}}\) and pullback
  \(J_{\mathrm{op}}\Phi=\hbar\chi_N\).
- Keep the algebraic central-contact cone as a separate changed source
  branch.  It adjoins a closed generator \(e_M\) with declared scalar image.
  The opposite central extension instead supplies a non-closed cochain
  \(-k^\vee_M\) whose differential is the contact term.  These are related
  shadows, not identical constructions.
- In the proof at `main.tex:7688-7704`, insert the CE sign computation and
  the finite-window compatibility check before the Costello-local exclusion.
- Preserve the current obstruction language at `main.tex:7655-7674`: the
  same-branch Costello-local repair still needs a closed source complex,
  Hom differential, scalar chain projection, and vanishing image obstruction.

Forbidden update:

- Do not rewrite the ordinary scalar-reduced \(\mathfrak{gl}_N\) branch as
  solved by Costello-local exchange.  Forgetting \(K_{\mathrm{cl}}\) returns
  the nonzero class \(\hbar N[\bar c]\) on \(\bar A\).
- Do not import \(K_{\mathrm{cl}}\) as a BV field.  No BV dual, coefficient
  Casimir, propagator, or counterterm calculus for it has been constructed.
- Do not use this branch to solve the non-scalar QME row or \(\theta_3\).

### `theorem-lanes.tex`

Required update:

- In Statement `\ref{thm:lane-u1-anomaly}` at `theorem-lanes.tex:3536-3574`,
  add one sentence after the local assertion: the opposite pushout
  \(L^-_N\) makes \(\hbar N\bar c\) CE-exact by the central cochain
  \(-k^\vee\), so it is a proved source-replacement branch for the scalar
  QME symbol.
- In Statement `\ref{thm:lane-quantum-coefficient-surface}` at
  `theorem-lanes.tex:2618-2660`, do not replace the balanced
  \(\{0_{\mathrm{sc}}\}\) factor.  The theorem's scalar factor remains the
  balanced supertrace branch.  Add, if needed, a scope sentence saying the
  opposite central source is an alternative scalar branch with changed
  source, not the componentwise balanced surface.
- Near the non-scalar/closed-exchange language at `theorem-lanes.tex:2744`
  and following, add that scalar source replacement precedes the formation of
  \(\ker\widehat\sigma_{\mathrm{sc}}\); it does not supply a class in the
  same Costello-local closed-exchange tower.

### `open-obligations.tex`

Required update:

- In the scalar anomaly obligation block at `open-obligations.tex:377-415`,
  insert the opposite central source formula after the unreduced
  central-character sentence and before the algebraic cone:
  \[
    L^-_N=\bar A\oplus\C[[\hbar]]K_{\mathrm{cl}},\qquad
    d_{\mathrm{CE}}(-k^\vee)=-\hbar N\bar c.
  \]
  Mark it closed only in the CE source-replacement branch.
- Preserve the open Costello-local obligation in the same block:
  a genuine same-branch repair still requires a closed field/source complex,
  bulk-to-defect propagator, locality/support rule, scalar-contact chain
  projection, and compatible finite-window/Roos representatives.
- In the Ward-identity block at `open-obligations.tex:1148-1151`, clarify that
  "absorbed by source replacement" includes the opposite central source only
  after the Ward source is changed from \(C^\bullet_{\mathrm{Lie}}(\bar A)\)
  to \(C^\bullet_{\mathrm{Lie}}(L^-_N)\).

### `claim-strength-ledger.tex`

Required update:

- Add a ledger row or sentence classifying "opposite scalar central source" as
  proved CE source replacement.  It proves
  \[
    \pi^*(\hbar N[\bar c])=0
    \quad\text{in}\quad
    H^2_{\mathrm{Lie}}(L^-_N;\C[[\hbar]])
  \]
  with primitive \(-k^\vee\).
- At `claim-strength-ledger.tex:1127-1150`, list this as an alternative to
  the balanced scalar factor, not as part of the componentwise balanced
  quantum coefficient surface.
- At `claim-strength-ledger.tex:1203-1228`, refine the scalar component:
  central-character and opposite central-extension branches are source
  replacements; the algebraic cone is a changed algebraic source branch; the
  Costello-local same-branch obstruction vector remains
  \[
    (o_{\sigma,M}^{(1),\mathrm{sc}},
     \beta_M^{\mathrm{Cost},\mathrm{sc}},
     \beta_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}},
     \mu_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}},
     \lambda_C^{\mathrm{Cost},\mathrm{sc}}).
  \]

## Branch Boundary

The branch is source replacement for four independent reasons.

1. The cochain that cancels the scalar obstruction is not closed:
   \[
     d_{\mathrm{CE}}(-k^\vee_M)=-\hbar N\bar c_M.
   \]
   A same-branch closed-exchange class must be represented by
   \(W_M\in Z^1(\mathcal X^{\bullet,\mathrm{Cost},\mathrm{sc}}_{w,M}(I))\).
2. The underlying CE source changes from \(\bar A\) to \(L^-_N\).  Exactness
   occurs only after pullback to \(L^-_N\).  On \(\bar A\), the class is still
   detected by \(z_1,z_2\).
3. The central line \(K_{\mathrm{cl}}\) is not a Costello BV field.  The
   manuscript has no dual \(K_{\mathrm{cl}}^\vee\), degree \(-1\) pairing,
   heat-kernel propagator, graph weights, or RG-compatible counterterms for
   it.
4. The construction supplies no current-valued bulk-to-defect theorem, no
   \(\mathcal D'_c\) wavefront/counterterm theorem, and no non-scalar
   \(\theta_3\) primitive.

Therefore the manuscript should mark:

- scalar CE source-replacement branch: proved;
- ordinary scalar-reduced same-branch Costello-local closed exchange: still
  open/obstructed by the named control classes;
- larger non-scalar Costello/QME branch: unchanged.

## Verification

Direct finite monomial check run in this work:

```text
CE cocycle failures through bidegree<6: 0
cbar(z1,z2)= 1
bar bracket {z1,z2}_bar terms: []
d(-kvee)(z1,z2) in L_-: -hbar*N
Ob_sc(z1,z2): +hbar*N
```

No PDF build was run.  This is a report-only integration specification.
