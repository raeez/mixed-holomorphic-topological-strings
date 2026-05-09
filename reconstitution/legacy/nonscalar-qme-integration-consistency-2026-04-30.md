# Non-scalar QME integration consistency audit

Date: 2026-04-30.
Lane: non-scalar Costello/QME integration consistency after Agent 198.
Scope: report only.  No TeX edits.

## Verdict

The Agent 198 appendix block is internally consistent: it proves a native
finite-window habitat and row criterion, not a full all-graph QME theorem.
It also proves the closed rows
\(\alpha_{\mathrm{sc}}\) and \(\alpha_{11}\), and isolates the finite-row
\(\theta_3\) obstruction.  No compact Calabi--Yau or CoHA transfer was found.

The current manuscript surface has three integration gaps:

1. the new theorem labels are not cited outside `appendix-unreduced-bv-qme.tex`;
2. the fixed-window primitive matrix \(A^M c=-r^M\) is not propagated to the
   main obstruction problem, local dictionary, or open-obligation row;
3. the \(\theta_3\) row is inconsistently written as
   \(\zeta_{\nu_3,M}\) outside the appendix, and one frontmatter sentence
   treats a companion-face table as if it were a primitive.

## Findings and repairs

### 1. Theorem-grade criterion is under-propagated

Observed:

- `appendix-unreduced-bv-qme.tex:2142` defines
  `def:app-native-finite-window-realization-habitat`.
- `appendix-unreduced-bv-qme.tex:2234` proves
  `thm:app-constructive-nonscalar-costello-qme-realization`.
- `appendix-unreduced-bv-qme.tex:2387` proves
  `prop:app-closed-rows-and-theta-three-source-face`.
- `rg` finds references to these three labels only inside the appendix.

Repair target: `main.tex:1850`.

Replace:

```tex
The non-scalar Costello graph/QME surface has been sharpened to the
finite-window criterion
```

with:

```tex
The non-scalar Costello graph/QME surface has been sharpened to the
native finite-window criterion of
Definition~\ref{def:app-native-finite-window-realization-habitat} and
Theorem~\ref{thm:app-constructive-nonscalar-costello-qme-realization};
it is not an all-graph summability theorem.
```

Repair target: `main.tex:7645`.

Replace the opening two sentences of
`prob:quantum-p0-operation-realization` with:

```tex
The next theorem-grade object after
Theorem~\ref{thm:quantum-coefficient-surface} is the native finite-window
Costello/QME realization criterion of
Definition~\ref{def:app-native-finite-window-realization-habitat} and
Theorem~\ref{thm:app-constructive-nonscalar-costello-qme-realization}.
The full graph/counterterm Costello realization remains the vanishing
problem in the filtered local-functional complex
```

Repair target: `theorem-lanes.tex:2764`.

Replace the finite-row proof-input sentence with:

```tex
The native finite-window habitat, scalar gate, primitive matrix, and
closed/open row tests are
Definition~\ref{def:app-native-finite-window-realization-habitat},
Theorem~\ref{thm:app-constructive-nonscalar-costello-qme-realization}, and
Proposition~\ref{prop:app-closed-rows-and-theta-three-source-face}; the
earlier finite-row interfaces are supporting calculations.
```

Repair target: `claim-strength-ledger.tex:209`.

Change the status row title/status to:

```tex
Larger non-scalar finite-window Costello/QME packages &
theorem-grade criterion after habitat; full graph realization open &
```

and append to its boundary cell:

```tex
The fixed-window primitive criterion is the linear system
\(A^M c=-r^M\) of
Theorem~\ref{thm:app-constructive-nonscalar-costello-qme-realization};
all-graph summability, arbitrary \(\mathcal D'_c(I)\)-labels, and a
curved bulk-to-defect kernel are not supplied here.
```

### 2. Primitive matrix is not visible enough

Observed:

- The full primitive criterion appears in the appendix at
  `appendix-unreduced-bv-qme.tex:2302-2333`.
- `theorem-lanes.tex:2737-2748` contains the compressed formula.
- `main.tex:7741-7747`, `local-dictionary.tex:968-980`, and
  `open-obligations.tex:375-382` name the obstruction vector but do not
  display the fixed-window matrix criterion or left-cokernel certificate.

Repair target: `main.tex:7747`.

Insert:

```tex
In the native finite-window habitat, choose degree-one row coordinates
\(\rho^M_i\) and degree-zero primitive candidates \(\eta^M_j\):
\[
  R^{\mathrm{ns}}_{n,M}=\sum_i r^M_i\rho^M_i,\qquad
  d_{\mathrm{ns},M}\eta^M_j=\sum_i A^M_{ij}\rho^M_i .
\]
The fixed-window primitive exists in the supplied span exactly when
\[
  A^M c=-r^M .
\]
Failure is certified by a covector
\[
  \ell A^M=0,\qquad \ell(r^M)\ne0 .
\]
The inverse-limit lift also requires
\[
  T^{M,N}r^M=r^N,\qquad T^{M,N}A^M=A^NP^{M,N},
\]
and vanishing of the Roos class
\[
  [P^{M,N}c_M-c_N]\in
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
```

Repair target: `local-dictionary.tex:937`.

Add to the `\(\mathcal Q^\bullet_{w,M}(I)\)` row:

```tex
In the native finite-window habitat of
Definition~\ref{def:app-native-finite-window-realization-habitat}, the
same residual kernel is denoted
\(\mathcal K^\bullet_{\mathrm{ns},M}(I)=
\ker\widehat\sigma_{\mathrm{sc},M}\).
```

Repair target: `local-dictionary.tex:968`.

Add a row:

```tex
\(A^M,r^M,\ell\) &
Fixed-window primitive matrix.  With
\[
  R^{\mathrm{ns}}_{n,M}=\sum_i r^M_i\rho^M_i,\qquad
  d_{\mathrm{ns},M}\eta^M_j=\sum_i A^M_{ij}\rho^M_i,
\]
a counterterm in the supplied finite primitive span exists exactly when
\(A^M c=-r^M\).  A covector
\(\ell A^M=0\), \(\ell(r^M)\ne0\), proves nonvanishing in that supplied
finite row subcomplex.\\
\hline
```

Repair target: `open-obligations.tex:382`.

Insert the same fixed-window matrix paragraph before the sentence
`Thus changing admissible weight...`.

### 3. \(\theta_3\) notation and companion status drift

Observed:

- Appendix and theta source reports use \(\zeta_{M,\nu_3}\).
- `abstract.tex:198`, `claim-strength-ledger.tex:501`, and
  `open-obligations.tex:494` use \(\zeta_{\nu_3,M}\).
- `abstract.tex:201-205` says the companion-face table supplies a
  differential \(d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M}\).  The appendix
  says a companion table changes the residual vector; it is not itself a
  degree-zero primitive.
- `local-dictionary.tex:998` calls it a `companion-face primitive`.

Repairs:

```tex
% abstract.tex:198, claim-strength-ledger.tex:501, open-obligations.tex:494
\zeta_{\nu_3,M}  ->  \zeta_{M,\nu_3}
```

Repair target: `abstract.tex:201-205`.

Replace with:

```tex
It is healed only by either a CE ancestor or a scalar-zero Costello local
counterterm producing a degree-zero \(C_{\theta_3,M}\) with
\[
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M}
\]
and Roos-compatible finite-window projections, or by a complete
Hom-valued companion-face table whose row sum changes the residual vector
to zero.  The companion table is not a primitive.
```

Repair target: `local-dictionary.tex:996-1001`.

Replace the witness list tail with:

```tex
  K^M_{\Theta_3}(\eta_{\theta_3,M}),\qquad
  C^{\mathrm{ct}}_{\theta_3,M},\qquad
  \text{or a complete Hom-valued companion-face table.}
\]
In the first two cases the primitive has differential
\(d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M}\),
scalar-contact value zero, and vanishing Roos compatibility class.  In
the companion-face case no degree-zero \(C_{\theta_3,M}\) is supplied;
the finite row table changes the residual vector before the primitive
matrix is formed.\\
```

### 4. Closed rows are present but should be named in the status tables

Observed:

- `appendix-unreduced-bv-qme.tex:2389-2414` proves
  \(\alpha_{\mathrm{sc}}\) and \(\alpha_{11}\) closed with zero primitive.
- `abstract.tex:191-193` now reflects this.
- `claim-strength-ledger.tex:202-208` and
  `theorem-lanes.tex:3010-3028` still name \(\alpha_{\mathrm{sc}}\) but not
  \(\alpha_{11}\) in the compact branch-status surfaces.

Repair target: `claim-strength-ledger.tex:208` and `theorem-lanes.tex:3028`.

Insert:

```tex
The labelled scalar-zero row \(\alpha_{11}\) with inputs \((z_1,z_1)\)
is also closed:
\[
  R^{\mathrm{row}}_{\alpha_{11},M}=0,\qquad
  S_{\alpha_{11},M}=0,\qquad C_{\alpha_{11},M}=0,
\]
because \(\omega(z_1,z_1)=0\); retaining or suppressing this zero row
does not create a larger-package QME solution.
```

## Attacks that did not survive

- Full all-graph QME overclaim: not found.  The strongest positive claim is
  finite-window and data-dependent; theorem-lanes also says no summation over
  all graph topologies without separate summability data.
- Compact Calabi--Yau / CoHA false transfer: not found.  All matches are
  firewall or quarantine language.
- Closed-row failure: not found.  The appendix proof of
  \(\alpha_{\mathrm{sc}}\) and \(\alpha_{11}\) is consistent with the
  current abstract and row computations.

## Checks run

```bash
sed -n '1,260p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' ~/ecosystem/INVARIANTS.md
sed -n '1,260p' ~/ecosystem/AGENTS-HARNESS.md
sed -n '1,240p' .agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' ~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg -n 'finite[- ]window|primitive|QME|theta_3|alpha|all-graph|compact Calabi|CoHA' abstract.tex theorem-lanes.tex main.tex claim-strength-ledger.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex
rg -n '\\zeta_{\\nu_3,M}|\\zeta_{M,\\nu_3}' abstract.tex claim-strength-ledger.tex open-obligations.tex local-dictionary.tex theorem-lanes.tex main.tex appendix-unreduced-bv-qme.tex reconstitution/*.md
git diff --check -- abstract.tex theorem-lanes.tex main.tex claim-strength-ledger.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex
chktex -q abstract.tex theorem-lanes.tex main.tex claim-strength-ledger.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex
pdflatex -draftmode -interaction=nonstopmode -halt-on-error -output-directory=/tmp/topological-strings-agent204-tex main.tex
PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite_window_graph_array.py > /tmp/agent204-finite-window-graph-array.json
```

Results:

- `git diff --check` passed.
- `chktex` returned style warnings only: dash length, label placement,
  spacing, bracket suggestions.  No fatal TeX error.
- `pdflatex -draftmode` to `/tmp/topological-strings-agent204-tex` exited
  `0`.  It reported many undefined references on the first pass, as expected
  in the dirty single-pass checkout; no syntax stop.
- `finite_window_graph_array.py` confirms:
  `minimal_full_equivariant_order_2_zero` solved by zero primitive;
  `theta_3_current_finite_row_subcomplex` obstructed with covector
  `[['E_theta_3', '1']]`; exact supplied CE-ancestor and counterterm payloads
  solve the row, while absent or differential-free payloads remain obstructed.

## Files changed

- `reconstitution/nonscalar-qme-integration-consistency-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-204-nonscalar-qme-integration-consistency.md`

No TeX files were edited by this lane.
