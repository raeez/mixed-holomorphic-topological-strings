# Agent 273 Report: Stratified Weiss Obstruction Integration Spec

Status: report-only integration specification.

Worktree: `/Users/raeez/topological-strings`.

Owned writable files:

- `reconstitution/swarm-2026-04-30-agent-273-stratified-weiss-obstruction-integration-spec.md`
- `reconstitution/stratified-weiss-obstruction-integration-spec-2026-04-30.md`

No TeX file is edited by this report.

## Verdict

Agent 266 closes one positive construction and identifies the exact
remaining theorem target.

The positive construction is the reduced product-basis prefactorization
datum on bulk product disks and brane intervals.  Its products are
extension by zero on compact supports followed by CE or completed
symmetric multiplication.  It proves
\[
  \delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0
\]
only for that reduced product-basis object.

The full stratified mixed HT theorem must not be downgraded.  It should
be strengthened to an internal obstruction theorem:
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N}
  \text{ with collars, Weiss descent, centrality, QME, and trace state}
  \quad\Longleftrightarrow\quad
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}=0
\]
with compatible null-homotopies.  The obstruction vector is the
construction problem, not a weak replacement for the theorem.

Use the manuscript name
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
\]
or make the existing
\(\operatorname{Ob}_{\mathrm{str},\Omega,N}\) an alias for it after the
components below are installed.  Do not import Agent 266's report-local
superscript `266` into manuscript TeX.

## Constructed Reduced Datum

The constructed object is a two-color reduced product-basis
prefactorization datum.  Its basis has:

1. bulk product disks
   \[
     U\times B\subset X\setminus L,\qquad
     U\subset\mathbb R^2_{t,s},\quad B\subset\mathbb C^2_{z_1,z_2};
   \]
2. brane intervals \(I\subset L\simeq\mathbb R_t\);
3. finite disjoint unions of such basics.

The bulk value is
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
with
\[
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot 1)
  \cong \mathfrak h^\vee_{\mathrm{cont}} .
\]

The brane interval value is
\[
  \mathcal F^{\mathrm{red}}_{\Omega,L}(I)
  =
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I)
  =
  \widehat{\mathbf S}(\Omega_c^0(I)\widehat\otimes
  \bar A_{w,\hbar_{\mathrm W}})
  \widehat\otimes
  \widehat{\mathbf S}(\mathcal D'_c(I)\widehat\otimes\mathcal P_w[1]).
\]

The product maps are exactly:

- extension by zero for
  \(\Omega_c^\bullet\), \(\Omega_c^{0,\bullet}\), \(\Omega_c^0\), and
  \(\mathcal D'_c\);
- completed CE or symmetric multiplication after extension to the target
  basic.

This construction does not include a Costello-compatible collar value.
The candidate collar module is
\[
  \mathcal M_{\Omega,N}^{\mathrm{cand}}(C(I;\epsilon,B);I)
  =
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I),
\]
but the first arrow in
\[
  \mathcal F^{\mathrm{red}}_{\Omega,X}(C)
  \xrightarrow{\pi^{\mathrm{cand}}_{L,\Omega}}
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\Omega_c^\bullet(I)\widehat\otimes(\mathfrak h\ltimes\mathcal P[1]))
  \xrightarrow{\kappa_{\mathrm{coef}}}
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I)
\]
is not constructed in the brane-defect Costello local-functional complex.
That failure is \(\operatorname{ob}_{\mathrm{collar}}\).

## Obstruction Vector

Install the internal vector as
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

Component meanings:

- \(\delta_{\mathrm{pref}}\), \(\delta_{\mathrm{assoc}}\): chain and
  associativity defects for \(\mu_{\mathrm{str}}\).  They vanish for the
  reduced product-basis datum above.
- \(\delta_{\mathrm{Weiss}}\): cone of the Cech/Weiss descent map for
  collared stratified Weiss covers, not a formal difference
  \(\mathcal F(V)-\operatorname*{holim}\mathcal F(U)\).
- \(\operatorname{ob}_{\mathrm{collar}}\): failure to construct
  \((\pi_L,j_L,h_\Omega)\) through brane-defect local functionals,
  propagators, counterterms, and the QME differential.
- \(\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}}\): class of
  \[
    \kappa_\Omega(x)A
    -(-1)^{|x||A|}A\kappa_\Omega(x)
  \]
  in the total Cech non-scalar Hom complex.
- \(\operatorname{ob}^{P_0}_{\mathrm{cent}}\): class of
  \[
    \{\kappa_\Omega(x),A\}_{P_{0,\hbar_{\mathrm{QME}}}}
    -\rho_{\mathrm{mod}}(x;A).
  \]
  The centrality homotopy lives in the QME/local-functional complex.  Do
  not identify this parameter with \(\hbar_{\mathrm W}\) unless the
  branch datum explicitly does so.
- \(\operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}}\): class of
  \[
    \mathbb D K+\frac12[K,K]_{\hbar_{\mathrm{QME}}}
  \]
  after the scalar gate places the row in the non-scalar kernel.
- \(\operatorname{ob}_{\Omega\mathrm{-basic}}\): aggregate secondary
  class \([L_{V_\Omega}H]\) for centrality primitives, and the analogous
  \([L_{V_\Omega}K]\) for kernels, when the primitive was chosen before
  passing to the basic Cartan subcomplex.
- \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\): aggregate trace-state
  topology obstruction, pointing to the existing trace vector
  \((\operatorname{ob}_{\mathrm{state}},
  \operatorname{ob}_{\mathrm{norm}},
  \operatorname{ob}_{\mathrm{Ward}},
  \operatorname{ob}_{\mathrm{cum}},
  \operatorname{ob}_{\mathrm{conv}},
  \operatorname{ob}_{\mathrm{QME}},
  \operatorname{ob}_{\mathrm{src}})\).

Keep \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) outside the
internal vector.  It is a source-fixture or matched-conventions gate:
external Costello--Gwilliam, AFT, CFG, Weiss/Ran, or Costello
\(\Omega\)-background material supplies grammar and analogy only until a
matched-conventions morphism into the local mixed HT pair is constructed.

## File Integration Spec

### `local-dictionary.tex`

Primary anchor: `local-dictionary.tex:678-712`.

Strengthen the "Stratified factorization datum" row by separating:

1. the proved reduced product-basis prefactorization datum;
2. the full stratified factorization theorem surface;
3. the candidate collar module and its obstruction.

Add dictionary entries for:

- \(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\): bulk product disks
  and brane intervals, finite disjoint unions, no constructed collar
  module.
- \(\mathcal F^{\mathrm{red}}_{\Omega,\mathrm{prod}}\): the values and
  extension-by-zero products above.
- \(\delta_{\mathrm{Weiss}}(V,\mathcal U)\): cone of
  \[
    r_{V,\mathcal U}\colon
    \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
    \to
    \operatorname{Tot}\check C^\bullet
    (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N}).
  \]
- \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\): the
  nine-component vector above.
- \(\operatorname{ob}_{\Omega\mathrm{-basic}}\): secondary
  \(L_{V_\Omega}\)-class for primitives.
- \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\): trace-state topology
  aggregate.

Also update `local-dictionary.tex:695-712` so
\(\operatorname{ob}_{\Omega,\mathrm{strat}}\) expands to the internal
stratified vector, while \(\operatorname{ob}_{\Omega,N\to\infty}\) points
to \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).  Preserve the
normal-\(\Omega\) convention at `local-dictionary.tex:441-491` and the
normal contraction boundary at `local-dictionary.tex:518-541`.

### `open-obligations.tex`

Primary anchor: `open-obligations.tex:870-1085`.

Replace the current descent defect
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
  -
  \operatorname*{holim}_{U\in\mathcal U}
  \mathcal F^{\mathrm{str}}_{\Omega,N}(U)
\]
with the Cech totalization cone:
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0}\cap\cdots\cap U_{i_p}),
  \qquad
  \mathbb D=\check\delta+(-1)^p d_{\mathcal F},
\]
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

Define a collared stratified Weiss cover: every finite subset of \(V\)
lies in some cover member, and if it meets \(L\), the same member
contains a product collar of the lower-stratum part.

Before the full vector, insert the reduced product-basis construction as
positive data.  State explicitly that it kills only the product and
associativity components on the reduced product-basis object.

Update the vector at `open-obligations.tex:1067-1078` to the
nine-component internal vector.  Move the existing source-primary audit
paragraph into a separate source gate immediately after the vector.

The centrality equations at `open-obligations.tex:976-1053` already
contain the right shape.  Retain their QME-complex parameter
\(\hbar_{\mathrm{QME}}\) and add the total Cech Hom complex when the
homotopy is asserted over a cover.

The trace paragraph at `open-obligations.tex:1086-1199` should be tied
back to the aggregate component
\(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\), rather than treated as
a separate downstream note.

### `theorem-lanes.tex`

Primary anchor: `theorem-lanes.tex:3001-3168`.

Strengthen Statement
`\ref{thm:lane-stratified-trace-physical-large-n}` into a two-part lane:

1. positive constructed reduced product-basis prefactorization datum;
2. full internal stratified theorem as
   \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}=0\).

At `theorem-lanes.tex:3051-3064`, replace the current seven-component
vector with the nine-component internal vector.  Do not keep
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) inside it; put source
support in an "External source gate" sentence.

At `theorem-lanes.tex:3065-3077`, align the \(P_0\)-centrality bracket
with the QME/local-functional complex:
\[
  \{\rho(x),a\}_{P_{0,\hbar_{\mathrm{QME}}}}
\]
unless a branch datum explicitly identifies this bracket with the Weyl
parameter.  The reduced current bracket remains the
\(\hbar_{\mathrm W}\)/\(\hbar_\omega\)-weighted algebraic current
bracket.

At `theorem-lanes.tex:2787-2999`, add a cross-reference that invariant
centrality primitives are part of
\(\operatorname{ob}_{\Omega\mathrm{-basic}}\) in the stratified vector.
The existing QME vector
\(\operatorname{Ob}^{\mathrm{QME}}_{\Omega,w}\) remains the local graph
subproblem.

### `claim-strength-ledger.tex`

Primary anchors:

- `claim-strength-ledger.tex:183-190`
- `claim-strength-ledger.tex:522-527`
- `claim-strength-ledger.tex:748-772`
- `claim-strength-ledger.tex:774-796`

Add a proved row or clause:

`Reduced product-basis stratified prefactorization datum` has status
`proved reduced product-basis`.  Its evidence is `main.tex:1175-1235`,
`main.tex:6187-6404`, and
`appendix-factorization-current-conventions.tex:697-790`.  Its boundary:
no collar module, no arbitrary collared Weiss descent, no unreduced
centrality, no QME, no trace-state topology.

Update the "Full \(Z^{P_0}_{\mathrm{fact}}\)" row and the
"Stratified factorization on \((X,L)\)" controller row so the failure
vector is not just
\[
(\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
 \operatorname{ob}^{P_0}_{\mathrm{cent}},
 \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
 \delta_{\mathrm{Weiss}}).
\]
For the stratified theorem use
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  For the
factorization-center-only row, either keep the smaller vector and say it
is the center subvector, or expand it with
\(\operatorname{ob}_{\mathrm{collar}}\) and
\(\operatorname{ob}_{\Omega\mathrm{-basic}}\) when the row is used inside
the stratified theorem.

Update the "Protected stratified trace" row so its missing construction
is exactly the aggregate
\(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\), with
\(\operatorname{Ob}_{\mathrm{tr},\Omega}\) as the expanded trace vector.

### `main.tex`

Primary anchors:

- `main.tex:1175-1235`
- `main.tex:4239-4255`
- `main.tex:6390-6404`
- `main.tex:6436-6480`
- `main.tex:7411-7568`

After `Proposition~\ref{prop:local-hamiltonian-factorization-observables}`
or in the local-model discussion, add a short theorem/proposition
recording the reduced product-basis prefactorization datum.  It should
state the two values and extension-by-zero products, and it should say
that collars are not constructed by this proposition.

Replace or sharpen
`Remark~\ref{rmk:weiss-ran-descent-obstruction}` so it uses the
Cech cone definition of \(\delta_{\mathrm{Weiss}}\) and points to
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  The
existing global factorization-center language can remain as the global
or matched-conventions version, but it should not obscure the internal
stratified pair \((X,L)\).

At `main.tex:6390-6404` and `main.tex:6436-6480`, add one sentence:
the reduced principal-part current theorem supplies the brane interval
component of the reduced product-basis prefactorization datum and does
not construct
\(\operatorname{ob}_{\mathrm{collar}}\),
\(\delta_{\mathrm{Weiss}}\),
centrality homotopies,
\(\operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}}\),
\(\operatorname{ob}_{\Omega\mathrm{-basic}}\), or
\(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

At `main.tex:7411-7568`, cross-reference the same vector from the
Costello perturbative BV specialization problem.  This avoids treating
normal \(\Omega\)-localization or reduced current brackets as graph/QME
evidence.

## TeX-Ready Core Insert

Use this as the canonical theorem skeleton, not as a verbatim mandate.

```tex
\begin{defn}[Internal stratified Weiss obstruction complex]
Let
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
A collared stratified Weiss cover of a stratified open pair
\((V,V\cap L)\) is a cover \(\mathcal U=\{U_i\}\) by stratified opens
such that every finite subset of \(V\) lies in some \(U_i\), and if the
finite subset meets \(L\), the same \(U_i\) contains a product collar of
its lower-stratum part.

For a candidate stratified object \(\mathcal F^{\mathrm{str}}_{\Omega,N}\),
put
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0}\cap\cdots\cap U_{i_p}),
  \qquad
  \mathbb D=\check\delta+(-1)^p d_{\mathcal F}.
\]
The Weiss defect is
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)
  =
  \operatorname{Cone}\left(
  \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
  \longrightarrow
  \operatorname{Tot}\check C^\bullet
  (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N})
  \right).
\]
\end{defn}

\begin{thm}[Internal stratified descent obstruction theorem]
Fix the local mixed HT pair \((X,L)\), a brane algebra branch, a
normal-\(\Omega\) coefficient ring, and a finite-window Costello
local-functional habitat.  The corresponding stratified factorization
algebra with collars, stratified Weiss descent, product and
\(P_0\)-centrality homotopies, brane-defect QME curvature cancellation,
basic \(\Omega\)-primitives, and trace-state topology exists if and only
if
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
  )
\]
vanishes with compatible null-homotopies.
\end{thm}
```

## Acceptance Checks For The Integrator

Run after TeX integration:

```bash
rg -n "Ob\\^\\{266\\}|Ob\\^\\{\\mathrm\\{int\\}\\}_\\{\\mathrm\\{str\\},\\Omega,N\\}|ob_\\{\\mathrm\\{collar\\}\\}|ob_\\{\\Omega\\mathrm\\{-basic\\}\\}|ob_\\{\\mathrm\\{tr\\}\\mathrm\\{-top\\}\\}" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
rg -n "P_\\{0,\\hbar_\\{\\mathrm\\{W\\}\\}\\}" theorem-lanes.tex open-obligations.tex
rg -n "operatorname\\*\\{holim\\}|delta_\\{\\mathrm\\{Weiss\\}\\}\\(V,\\mathcal U\\)" open-obligations.tex theorem-lanes.tex main.tex
```

Expected: no `Ob^{266}` in TeX; the internal stratified vector appears in
the five target files; `P_{0,\hbar_{\mathrm W}}` remains only for
reduced Weyl/Moyal current brackets or explicit branch choices, not for
QME-centrality homotopies; the Weiss defect is represented by a Cech cone
where theorem-grade descent is asserted.

## Evidence Read

- Agent 266 reports:
  `reconstitution/swarm-2026-04-30-agent-266-internal-stratified-weiss-descent-construction-push.md`
  and
  `reconstitution/internal-stratified-weiss-descent-construction-push-2026-04-30.md`.
- Manuscript anchors:
  `main.tex:1175-1235`, `main.tex:4239-4255`,
  `main.tex:6390-6404`, `main.tex:6436-6480`,
  `main.tex:7411-7568`;
  `theorem-lanes.tex:2787-2999`, `theorem-lanes.tex:3001-3168`;
  `open-obligations.tex:870-1199`;
  `claim-strength-ledger.tex:183-190`, `claim-strength-ledger.tex:522-527`,
  `claim-strength-ledger.tex:748-796`;
  `local-dictionary.tex:441-541`, `local-dictionary.tex:678-712`,
  `local-dictionary.tex:1094-1127`, `local-dictionary.tex:1508-1518`.
- Source fixtures:
  `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`
  and
  `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`.

No build was run.  This is a report-only artifact.
