# Theorem-Lanes Postintegration Audit, 2026-04-30

Agent: 202.

Scope: hostile audit of Agent 194's `theorem-lanes.tex` integration against
Agents 174--199.  No Agent 200 report exists under `reconstitution/` at the
time of this audit.  No TeX file was edited.

## Verdict

Agent 194's integration preserved the main firewalls: native holomorphic
`C^2` factorization is not replaced by a curve VOA; the `C x R` reduction
retains the `z_2` coefficient/principal-part system; the reduced
Dirac-BRST/Zhu lane is conditional; Matlis principal parts are separated
from PBW one-psi labels; Costello/QME and physical trace claims are kept as
obstruction surfaces.

The remaining defects are theorem-surface defects, not typographical
defects.  They should be repaired in TeX only by the integration owner.

## Attack-Heal Ledger

### A202-01: Normal Omega localization ring is too weak in the lanes

Claim attacked: the Omega weighted-kernel and stratified-trace lanes have
the correct coefficient habitat.

Failure mode: `theorem-lanes.tex:2611-2630` names the moving characters
`chi^H_{n,a,b}` and `chi^\vee_{n,a,b}`, but does not define the finite
character set or the localized coefficient ring.  Later,
`theorem-lanes.tex:2796-2802` sends the stratified functor to
`Ch_{C((epsilon_s,epsilon_1,epsilon_2))[[hbar]]}`, which does not state
inversion of all finite-window moving characters.  Agent 184's actual
finite-window ring is at `tate-T1-weighted-completion.tex:398-408`.
Agent 195 flags this exact mismatch at
`reconstitution/swarm-2026-04-30-agent-195-omega-consistency-audit.md:57-69`.

Status: valid repair needed.

Exact theorem-surface repair:

At `theorem-lanes.tex:2623`, insert the finite character set and ring:

```tex
Let \(\mathsf X_{N,M}\) be the finite set of nonzero formal characters
among \(\chi^H_{n,a,b}\) and \(\chi^\vee_{n,a,b}\) for the moving
summands contracted in the window.  The finite-window coefficient ring is
\[
  R_{\Omega}^{N,M}
  =
  \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
  [\chi^{-1}\mid \chi\in\mathsf X_{N,M}],
  \qquad w(\hbar_\omega)=\epsilon_1+\epsilon_2 .
\]
```

At `theorem-lanes.tex:2801`, replace the codomain by a ring depending on
the chosen finite or all-window localization:

```tex
\operatorname{Ch}_{R_{\Omega}^{N,M}[[\hbar_{\mathrm{QME}}]]}
```

or, for an all-window analytic theorem, replace it by the corresponding
q-moderate completion after the small-denominator bound has been proved.
Do not use `C((epsilon_s,epsilon_1,epsilon_2))` as a substitute for this
choice.

### A202-02: `hbar_omega`, Weyl `hbar`, and QME `hbar_N` need a branch datum

Claim attacked: the Omega lanes consistently distinguish the equivariant
line scalarizer from the Weyl/Moyal and BV/QME parameters.

Failure mode: `theorem-lanes.tex:1504-1509` introduces
`\hbar_\omega` for the scalarized Hamiltonian bracket, while
`theorem-lanes.tex:2815-2817` assigns weight
`epsilon_1+epsilon_2` to `\hbar` in the finite brane Weyl algebra, and
`theorem-lanes.tex:2852-2916` uses the physical parameter `\hbar_N` in
the trace-state and BV differential.  The lane never states whether
`\hbar_\omega` is independent, identified with the Weyl parameter, or
identified with the BV loop parameter.  Agent 195 records this as an
undecided branch at
`reconstitution/swarm-2026-04-30-agent-195-omega-consistency-audit.md:71-83`.

Status: valid repair needed.

Exact theorem-surface repair:

After `theorem-lanes.tex:1589`, add:

```tex
\emph{Parameter convention.}
The symbol \(\hbar_\omega\) is the equivariant scalarizer of the
symplectic-character line.  The Weyl/Moyal deformation parameter and the
BV/QME loop parameter are independent until a branch datum identifies
them.  A Weyl-equivariant branch is a ring map sending
\(\hbar_\omega\) to the Weyl parameter \(\hbar_{\mathrm W}\), with
\(w(\hbar_{\mathrm W})=\epsilon_1+\epsilon_2\).  The physical
large-\(N\) branch uses \(\hbar_{\mathrm W,N}=\lambda/N\).  It is not
identified with the BV loop parameter \(\hbar_{\mathrm{QME}}\) unless
that identification is included in the QME normalization datum.
```

Then replace `w(\hbar)=epsilon_1+epsilon_2` at
`theorem-lanes.tex:2817` by `w(\hbar_{\mathrm W})=epsilon_1+epsilon_2`
and keep `\hbar_N` only after the physical specialization
`\hbar_{\mathrm W,N}=\lambda/N`.

### A202-03: Agent 198's finite-window Costello/QME habitat is not wired into theorem-lanes

Claim attacked: the graph/QME branch catalogue has all construction
witnesses supplied by Agents 187--198.

Failure mode: `theorem-lanes.tex:2965-3141` classifies local graph/QME
branches, but its proof-input paragraph at `theorem-lanes.tex:3106-3136`
does not cite the new finite-window Costello habitat inserted by Agent
198:

- `appendix-unreduced-bv-qme.tex:2143`
  `def:app-native-finite-window-realization-habitat`;
- `appendix-unreduced-bv-qme.tex:2235`
  `thm:app-constructive-nonscalar-costello-qme-realization`;
- `appendix-unreduced-bv-qme.tex:2388`
  `prop:app-closed-rows-and-theta-three-source-face`.

This makes the lane weaker than the current manuscript: it states branch
statuses but omits the actual Hom-valued finite-window habitat and row
criterion now available.  Agent 198's report records the habitat and row
criterion at
`reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md:15-124`.

Status: valid repair needed.

Exact theorem-surface repair:

At `theorem-lanes.tex:2972`, add the construction witness:

```tex
The native finite-window Costello habitat is the completed local-functional
complex
\[
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M
  \right),
  \qquad d_M=Q+\{I^w_{0,M},-\}_{\hbar,M},
\]
together with the Hom-valued kernel complex
\[
  \mathbf K^\bullet_{\mathcal G,M}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}
  (C^\bullet_{\mathrm{lab}}(\mathcal G_M),
   \mathfrak Q^\bullet_{\mathcal G,M}(I)).
\]
```

At `theorem-lanes.tex:3106`, add the three Agent 198 labels to the proof
inputs before the finite-window array references.

### A202-04: Native E2 lane is correct, but Agent 199's field-level witness is missing

Claim attacked: the native holomorphic `E_2` lane exposes the strongest
constructed object.

Failure mode: `theorem-lanes.tex:407-415` states the CE/factorization
observable object, and `theorem-lanes.tex:417-448` records the semidirect
collision algebra.  It does not record the field-level Hamiltonian BF
witness from Agent 199: the fields, differential, and interaction.  This
is not a false claim, but it is a missed Supremum upgrade.  Agent 199
gives the witness at
`reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md:41-60`.

Status: optional strengthening, not a blocking defect.

Exact theorem-surface repair:

After `theorem-lanes.tex:407-415`, insert:

```tex
Equivalently this is the classical Hamiltonian BF field theory with
\[
  \alpha\in\Omega^{0,\bullet}(B)\widehat\otimes\mathfrak h[1],
  \qquad
  \beta\in\Omega^{0,\bullet}(B)\widehat\otimes\mathcal P[2],
\]
Dolbeault differential \(\bar\partial\), and cubic interaction
\[
  I_{\mathrm{Ham}}
  =
  \frac12\int_B
  \langle\beta,\{\alpha,\alpha\}\rangle_{\mathrm{res}} .
\]
The compactly supported observable dg Lie input is
\(\Omega_c^{0,\bullet}(B)\widehat\otimes
(\mathfrak h\ltimes\mathcal P[1])\).
```

### A202-05: Omega brane-current bracket anchor is absent from the theorem lanes

Claim attacked: the Omega/stratified lanes have the refined
`\hbar_\omega` brane-current bracket witness.

Failure mode: Agent 192 inserted and audited the algebraic
Omega-weighted current brackets in
`appendix-factorization-current-conventions.tex:400-455`, but
`theorem-lanes.tex:2755-2766` and `theorem-lanes.tex:2784-2963` do not
cite `thm:app-omega-weighted-current-brackets`.  The stable brane branch
at `theorem-lanes.tex:2819-2821` names
`A^{pp,w}_{partial,Omega,hbar}` without recording that its algebraic
current brackets are scalarized by `\hbar_\omega` off the self-dual
locus.

Status: valid repair needed for the Omega theorem surface.

Exact theorem-surface repair:

At `theorem-lanes.tex:2821`, add:

```tex
On the algebraic current subtarget, the Omega-weighted brackets are those
of Theorem~\ref{thm:app-omega-weighted-current-brackets}; off the
self-dual locus they are either \(L_\omega^{-1}\)-valued or scalarized by
\(\hbar_\omega\).  These current brackets are algebraic current data and
do not supply Costello graph kernels for arbitrary distributional labels.
```

At `theorem-lanes.tex:2755-2766` or `3106-3136`, cite
`Theorem~\ref{thm:app-omega-weighted-current-brackets}` wherever the
Omega weighted current target is used.

### A202-06: Controlled CxR, reduced BRST/Zhu, and Matlis lanes pass the hostile checks

Claim attacked: Agent 194 may have overpromoted reduced curve or Matlis
claims.

Result: no blocking overclaim found.

Evidence:

- `theorem-lanes.tex:676-862` keeps the `C x R` reduction conditional on
  the retained `z_2` coefficient/principal-part system, two-variable
  Hamiltonian bracket, surviving second matrix, scalar anomaly, Moyal
  product, and analytic pushforward obstruction vector.  This matches
  Agents 181 and 199.
- `theorem-lanes.tex:864-1002` makes the reduced Dirac BRST/Zhu bridge
  conditional on the controlled reduction, vertex theorem, retained
  `z_2` data, anomaly convention, Capelli shift, and stable classical
  HKR/CE-PV comparison.  This matches Agent 182.
- `theorem-lanes.tex:2097-2171` correctly wires the Matlis/principal-part
  module, scalar-line exclusion, coadjoint action, continuity, residue
  rigidity, and no same-action polynomial descendant bridge.  This
  matches Agent 188.

## Files Changed

- `reconstitution/theorem-lanes-postintegration-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-202-theorem-lanes-postintegration-audit.md`

No TeX files changed.

## Verification Commands

Run before writing this ledger:

```bash
git diff --check -- theorem-lanes.tex
rg -n "label\\{([^}]*)\\}" theorem-lanes.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
rg -n -F -e 'def:app-native-finite-window-realization-habitat' \
  -e 'thm:app-constructive-nonscalar-costello-qme-realization' \
  -e 'prop:app-closed-rows-and-theta-three-source-face' theorem-lanes.tex
rg -n -F -e 'R_{\\Omega}^{N,M}' -e 'mathsf X_{N,M}' \
  -e 'C((\\epsilon_s,\\epsilon_1,\\epsilon_2))' \
  -e 'w(\\hbar)=\\epsilon_1+\\epsilon_2' theorem-lanes.tex
```

Results:

- `git diff --check -- theorem-lanes.tex`: clean.
- Duplicate-label scan in `theorem-lanes.tex`: no duplicate labels.
- Agent 198 label scan in `theorem-lanes.tex`: no hits, confirming A202-03.
- Omega localization scan found only the weaker codomain and `w(\hbar)`
  convention, confirming A202-01 and A202-02.

Post-write checks:

```bash
git diff --check -- \
  reconstitution/theorem-lanes-postintegration-audit-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-202-theorem-lanes-postintegration-audit.md \
  theorem-lanes.tex
LC_ALL=C grep -n '[^ -~]' \
  reconstitution/theorem-lanes-postintegration-audit-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-202-theorem-lanes-postintegration-audit.md
pdflatex -halt-on-error -interaction=nonstopmode -draftmode \
  -output-directory=/tmp/topological-strings-agent202-build main.tex
```

Results:

- post-write whitespace check: clean;
- ASCII scan on both owned reports: no hits;
- temporary `pdflatex` draft build in `/tmp/topological-strings-agent202-build`:
  exit code 0.  After repeated draft passes, no undefined-reference warning
  remained in the captured third pass; LaTeX still requested a rerun for
  changed labels and reported pre-existing box/font warnings.  No repository
  build artifact was written by this audit.
