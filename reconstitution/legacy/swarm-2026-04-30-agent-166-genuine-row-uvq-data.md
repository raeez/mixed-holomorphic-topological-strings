# Agent 166 - Genuine Row UVQ Data

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The missing larger-package truncation entries isolated by Agent 161 are now
defined when the finite-window package supplies the necessary row-coordinate
data.

For genuine order-two seed rows, set
\[
  \mathbf K^M_\Gamma=\varepsilon_\Gamma K^M_\Gamma.
\]
If \(\pi_{M,N}\mathbf K^M_\Gamma\) lies in the lower-window span with chosen
coordinates, then
\[
  \pi_{M,N}\mathbf K^M_\Gamma
    =
  \sum_{\Gamma'}
    u^{M,N}_{\Gamma,\Gamma'}\mathbf K^N_{\Gamma'}.
\]
The same entries transport differential rows because
\[
  \pi_{M,N}d_M=d_N\pi_{M,N}.
\]

For CE source faces, set
\[
  \mathbf E^M_{\Gamma,\nu}
    =
  -\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}
  K^M_\Gamma(\zeta_{M,\nu}).
\]
If the projected source face lies in the chosen lower source-face span, then
\[
  \pi_{M,N}\mathbf E^M_{\Gamma,\nu}
    =
  \sum_{\Gamma',\nu'}
    v^{M,N}_{\Gamma,\nu;\Gamma',\nu'}\mathbf E^N_{\Gamma',\nu'}.
\]

For nonzero added bracket rows with
\(\beta_i\notin\{\alpha_{\mathrm{sc}},\alpha_{11}\}\), set
\[
  \mathbf B^M_{\beta_1,\beta_2}
    =
  \frac12\varepsilon^M_{\beta_1,\beta_2}
  \{K^M_{\beta_1},K^M_{\beta_2}\}_{\hbar,M}.
\]
The bracket truncation entries are the coordinates
\[
  \pi_{M,N}\mathbf B^M_{\beta_1,\beta_2}
    =
  \sum_{\beta'_1,\beta'_2}
    q^{M,N}_{\beta_1,\beta_2;\beta'_1,\beta'_2}
    \mathbf B^N_{\beta'_1,\beta'_2}.
\]
If order-one rows transport by
\[
  \pi_{M,N}K^M_\beta=\sum_\eta r^{M,N}_{\beta,\eta}K^N_\eta
\]
and lower raw brackets reduce by
\[
  \frac12\{K^N_{\eta_1},K^N_{\eta_2}\}_{\hbar,N}
    =
  \sum_{\beta'_1,\beta'_2}
    \Theta^N_{\eta_1,\eta_2;\beta'_1,\beta'_2}
    \mathbf B^N_{\beta'_1,\beta'_2},
\]
then
\[
  q^{M,N}_{\beta_1,\beta_2;\beta'_1,\beta'_2}
    =
  \varepsilon^M_{\beta_1,\beta_2}
  \sum_{\eta_1,\eta_2}
    r^{M,N}_{\beta_1,\eta_1}
    r^{M,N}_{\beta_2,\eta_2}
    \Theta^N_{\eta_1,\eta_2;\beta'_1,\beta'_2}.
\]
In the ordered normalized bracket basis this specializes to
\[
  q^{M,N}_{\beta_1,\beta_2;\beta'_1,\beta'_2}
    =
  \frac{\varepsilon^M_{\beta_1,\beta_2}}
       {\varepsilon^N_{\beta'_1,\beta'_2}}\,
  r^{M,N}_{\beta_1,\beta'_1}r^{M,N}_{\beta_2,\beta'_2}.
\]

Compatibility is exactly functoriality of finite-window projection:
\[
  u^{M,P}_{\Gamma,\Gamma''}
    =
  \sum_{\Gamma'}u^{M,N}_{\Gamma,\Gamma'}u^{N,P}_{\Gamma',\Gamma''},
\]
\[
  v^{M,P}_{\Gamma,\nu;\Gamma'',\nu''}
    =
  \sum_{\Gamma',\nu'}
  v^{M,N}_{\Gamma,\nu;\Gamma',\nu'}
  v^{N,P}_{\Gamma',\nu';\Gamma'',\nu''},
\]
\[
  q^{M,P}_{\beta_1,\beta_2;\theta_1,\theta_2}
    =
  \sum_{\beta'_1,\beta'_2}
  q^{M,N}_{\beta_1,\beta_2;\beta'_1,\beta'_2}
  q^{N,P}_{\beta'_1,\beta'_2;\theta_1,\theta_2}.
\]

These are formulas, not numerical graph weights.  Numerical entries require
the larger graph package data listed below.

## Valid Attacks

```yaml
- id: A1-166-01
  severity: 2
  status: healed
  lens: row-coordinate uniqueness
  target: prop:computed-finite-window-truncation-matrices
  claim: The nonzero bracket matrix q is unique whenever it exists.
  broken_step: A finite row set need not be linearly independent in the local-functional complex; a projected bracket can have several coordinate presentations.
  evidence_type: proof_gap
  evidence_ref: Definition defn:finite-window-graph-array records a finite set of rows, not a basis theorem.
  minimal_heal: Require a lower-window row basis, or a row presentation with chosen coordinates, before calling q an entry.
  residual: none for the coordinate definition; numerical entries still require row values.

- id: A1-166-02
  severity: 2
  status: healed
  lens: finite-window projection
  target: u^{M,N} and v^{M,N}
  claim: The genuine seed and source-face matrices are simply missing until larger graph weights are known.
  broken_step: Their formal definition does not require evaluating the graph integrals; they are coordinate matrices of finite-window projection, conditional on projection-closed lower row spans.
  evidence_type: proof
  evidence_ref: prop:projection-defined-uvq-truncation-data
  minimal_heal: Define u and v as coordinates of projected normalized rows.
  residual: actual numerical entries require seed weights, source faces, signs, and row bases.

- id: A1-166-03
  severity: 2
  status: healed
  lens: BV bracket compatibility
  target: q^{M,N} for nonzero added bracket rows
  claim: q is an independent black-box matrix.
  broken_step: If order-one transport r and lower bracket reduction Theta are supplied, the BV-bracket projection identity forces q by an explicit formula.
  evidence_type: proof
  evidence_ref: prop:projection-defined-uvq-truncation-data
  minimal_heal: Add q = epsilon^M sum r r Theta, with the ordered normalized specialization epsilon^M/epsilon^N times r r.
  residual: without r, Theta, and bracket signs the entries are not computable.

- id: A1-166-04
  severity: 1
  status: healed
  lens: non-scalar QME obstruction formation
  target: larger finite-window package obstruction claim
  claim: Naming u, v, and q decides the non-scalar QME obstruction.
  broken_step: The obstruction class is not formed until row values, scalar gates, projection closure, and lower-window coordinates are supplied.
  evidence_type: proof_gap
  evidence_ref: thm:actual-finite-window-nonscalar-decision-datum; def:app-nonscalar-kernel-row-complex
  minimal_heal: State the minimal data package and the H^1/Roos decision criterion.
  residual: actual H^1 and varprojlim^1 computation for any concrete larger package.
```

## Repaired Labels

- `prop:computed-finite-window-truncation-matrices` refined: `q` is now a
  coordinate family relative to a chosen lower-window basis or presentation.
- `prop:projection-defined-uvq-truncation-data` added: defines \(u\), \(v\),
  \(q\), proves compatibility, and states the minimal data package.
- `scripts/finite_window_graph_array.py` now emits
  `larger_package_uvq_projection_rules`.

## Minimal Data Package

To compute actual \(u/v/q\) entries and decide the non-scalar QME
obstruction, a larger package must supply:

1. finite seed sets \(\mathcal G^{\mathrm{gen}}_{2,M}\) with order
   assignment;
2. normalized graph weights \(\varepsilon_\Gamma K^M_\Gamma\);
3. CE-source decompositions, source transport, and
   \(\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}\);
4. nonzero order-one row values \(K^M_\beta\) excluding
   \(\alpha_{\mathrm{sc}}\) and \(\alpha_{11}\);
5. bracket signs \(\varepsilon^M_{\beta_1,\beta_2}\);
6. lower-window row bases or presentations for genuine, source-face, and
   nonzero bracket rows;
7. proof that \(\pi_{M,N}\) is a chain and BV-bracket projection on these
   rows;
8. scalar-gate vanishing in the full-equivariant marked habitat, or explicit
   scalar projections otherwise.

With those data, the order-two residual is a defined element of
\(\mathcal K^1_{\mathrm{ns},M}(I)\).  A fixed-window counterterm exists
exactly when its class vanishes in
\[
  H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M}),
\]
and a compatible tower also requires the corresponding Roos class in
\[
  \varprojlim\nolimits^1 H^0(\mathcal K^\bullet_{\mathrm{ns},M}(I))
\]
to vanish.

## Script Output

Command:

```bash
python3 scripts/finite_window_graph_array.py
```

Decisive emitted keys:

```text
larger_package_uvq_projection_rules[0].family = u genuine seed projection
larger_package_uvq_projection_rules[0].projection_formula =
  pi_{M,N}G^M_Gamma=sum_{Gamma'} u^{M,N}_{Gamma,Gamma'} G^N_Gamma'

larger_package_uvq_projection_rules[1].family = v CE source-face projection
larger_package_uvq_projection_rules[1].projection_formula =
  pi_{M,N}E^M_{Gamma,nu}=sum_{Gamma',nu'}
  v^{M,N}_{Gamma,nu;Gamma',nu'} E^N_{Gamma',nu'}

larger_package_uvq_projection_rules[2].family = q nonzero added bracket projection
larger_package_uvq_projection_rules[2].matrix_entry =
  q=(epsilon^M_{beta_1,beta_2}/epsilon^N_{beta'_1,beta'_2})
  r_{beta_1,beta'_1} r_{beta_2,beta'_2}
```

The script also keeps the minimal full-equivariant order-two result:
`reduced_non_scalar_row_sum = 0` and `counterterm = C_{2,M}=0`.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
git diff --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-166-genuine-row-uvq-data.md
rg -n -F "projection-defined-uvq-truncation-data" tate-P1-hadamard-mittag-leffler.tex
rg -n -F "larger_package_uvq_projection_rules" scripts/finite_window_graph_array.py
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-166-genuine-row-uvq-data.md
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex
```

Results:

- `py_compile` passed.
- The script emitted the new \(u/v/q\) projection rules.
- `git diff --check` passed.
- Label/key scans found the new proposition and script payload key.
- trailing-whitespace grep returned no hits.
- `lacheck` reports only the pre-existing nonbreaking-space suggestions at
  lines 39, 218, and 221.
- `chktex` exits with style warnings only; the new proposition adds ordinary
  brace/spacing suggestions, but no fatal TeX syntax error was detected by
  the scoped check.
- `make pdf` was not run because the shared checkout has concurrent staged
  manuscript edits and the build writes outside this agent's owned paths.

## Files Changed/Staged

Changed:

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-166-genuine-row-uvq-data.md`

Staged after scoped verification.

After staging, the working tree showed one additional unstaged same-file
change in `tate-P1-hadamard-mittag-leffler.tex`:
`e_{\mathrm W}` to `e_{\mathrm{W}}`.  Agent 166 did not make or stage that
cosmetic edit.

## Remaining Theorem Obligations

1. Supply a concrete larger finite marked list and actual normalized graph
   weights.
2. Supply CE-source decomposition and transport, unless strict CE-cycle
   evaluation removes those rows.
3. Supply nonzero order-one row transport \(r^{M,N}\) and bracket-basis
   reduction \(\Theta^N\).
4. Prove projection closure for \(\mathcal U_M\), \(\mathcal V_M\), and
   \(\mathcal B_M\).
5. Compute the resulting \(H^1\) class and the Roos compatibility class.
