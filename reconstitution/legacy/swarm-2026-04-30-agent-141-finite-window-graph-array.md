# Agent 141 - Finite-Window Graph Array

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The missing datum from Agent 135 is now an actual row array, not a tuple
name.  The repaired manuscript defines
\(\mathsf A^{\mathrm{fw}}_{n,M}\) as a finite set of rows.  Each row records:

- graph type and \(\hbar\)-order;
- edge labels \(P_{\epsilon,L}^{w,M}\), \(\Delta_{\epsilon,L}^{w,M}\), or
  the boundary Weyl edge;
- vertex labels from the finite-window package;
- marker tensor and marker transport;
- incidence coefficient \((-1)^{i-1}\varepsilon_{\beta_i}\) or the CE/BV
  Koszul sign;
- coefficient window degree and scalar-contact filtration;
- row curvature value \(R^{\mathrm{row}}_{\alpha,M}\);
- scalar-gate value
  \(S_{\alpha,M}=\widehat\sigma_{\mathrm{sc},M}
    (R^{\mathrm{row}}_{\alpha,M})\);
- truncation coefficients \(t^{M,N}_{\alpha\alpha'}\).

The exact array identities are:

\[
R_{n,M}=\sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}
R^{\mathrm{row}}_{\alpha,M},
\qquad
\mathfrak s_{n,M}=
\sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}S_{\alpha,M}.
\]

The non-scalar reduced-curvature contribution is canonical only as the
scalar-zero row sum:

\[
R^{\mathrm{ns}}_{n,M}=
\sum_\alpha R^{\mathrm{row}}_{\alpha,M}
\quad\text{when}\quad
\sum_\alpha S_{\alpha,M}=0.
\]

Entrywise non-scalar projection needs an additional chain splitting of
\(\widehat\sigma_{\mathrm{sc},M}\); without that splitting it is not a
theorem-grade datum.

## First Orders

Order \(0\): on the length-one reduced current interface, the CE/PV current
theorem gives strict compatibility.  The row has
\[
R^{\mathrm{row}}_{0,M}=0,\qquad S_{0,M}=0.
\]

Order \(1\): the universal computed row is the one-cross two-Hamiltonian
scalar-contact graph with inputs \((a,z_1)\), \((b,z_2)\).  Since
\(\omega(z_1,z_2)=1\), its extracted scalar gate is:

\[
\begin{array}{c|c}
\text{branch} & S_{\alpha_{\mathrm{sc}},M}\\ \hline
\mathfrak{gl}_N\ \text{ordinary} & N\gamma_{\mathbf 1}\\
\text{even block marker }\lambda_0P_{\bar0}+\lambda_1P_{\bar1}
  & N(\lambda_0-\lambda_1)\gamma_{\mathbf 1}\\
\mathfrak{gl}(N|N)\ \text{full-equivariant} & 0.
\end{array}
\]

For the minimal full-equivariant closed array containing only the strict
current-interface rows and this scalar-contact row, the order-one residual is
zero.  Hence the compatible order-one non-scalar counterterm is
\[
C_{1,M}=0.
\]

For any larger graph package, the first non-scalar order remains undecided:
\[
R^{\mathrm{ns}}_{1,M}=
\sum_{\alpha\in
\mathsf A^{\mathrm{fw}}_{1,M}\setminus\{\alpha_{\mathrm{sc}}\}}
R^{\mathrm{row}}_{\alpha,M}.
\]

## Valid Attacks

```yaml
- id: A1-141-01
  severity: 1
  status: healed
  lens: missing coefficient array
  target: tate-P1-hadamard-mittag-leffler.tex, Agent 135 array placeholder
  claim: The tuple named by Agent 135 is enough to compute the first non-scalar class.
  broken_step: It did not define row-level graph types, labels, signs, scalar gates, row curvature values, or truncation coefficients.
  evidence_type: proof_gap
  evidence_ref: defn:finite-window-graph-array
  minimal_heal: Define a valid finite row array whose sum reproduces R_{n,M} and whose truncation coefficients reproduce pi_{M,N}.
  residual: Populate the rows for any concrete Costello specialization beyond the universal scalar-contact row.

- id: A1-141-02
  severity: 1
  status: healed
  lens: non-scalar projection
  target: entrywise reduced-curvature contribution
  claim: Each graph row has a canonical non-scalar projection.
  broken_step: The manuscript supplies a scalar projection to S and a kernel, not a canonical splitting of the scalar line.
  evidence_type: proof_gap
  evidence_ref: defn:finite-window-graph-array
  minimal_heal: Define the non-scalar contribution as the scalar-zero row sum; require an extra chain splitting for entrywise projection.
  residual: A concrete package may add such a splitting, but it is additional data.

- id: A1-141-03
  severity: 1
  status: healed
  lens: first counterterm
  target: C_{n0,M}
  claim: Full-equivariant scalar-gate vanishing constructs a general first non-scalar counterterm.
  broken_step: It constructs only the scalar-gate cancellation for the computed row. Other order-one rows may remain.
  evidence_type: direct_computation
  evidence_ref: prop:first-finite-window-array-rows; scripts/finite_window_graph_array.py
  minimal_heal: Prove C_{1,M}=0 only for the minimal full-equivariant closed array; leave larger packages to the populated array.
  residual: Missing order-one rows decide whether n0=1 in a larger package.

- id: A1-141-04
  severity: 2
  status: healed
  lens: finite-window truncation
  target: pi_{M,N}
  claim: Degree truncation alone defines the array map in M.
  broken_step: Row values may split into lower-window row combinations; the coefficients are part of the theorem data.
  evidence_type: proof_gap
  evidence_ref: defn:finite-window-graph-array
  minimal_heal: Add coefficients t^{M,N}_{alpha alpha'} satisfying pi R_alpha = sum t R_alpha' and the same scalar-gate identity.
  residual: Any absent coefficient is the exact lower-window missing entry.
```

## Remaining Theorem Obligations

- Supply the finite seed set beyond the universal scalar-contact row.
- Fill every \(d_M\)-boundary, CE-source, BV-bracket, collision, and
  counterterm row with its incidence coefficient.
- Give actual \(K^M_\Gamma\) and lower counterterms \(C_{<n,M}\) for the
  chosen package.
- Provide scalar projection data, and a chain splitting only if entrywise
  non-scalar rows are required.
- Fill the truncation matrices \(t^{M,N}_{\alpha\alpha'}\).
- After those entries are present, compute
  \([R_{n_0,M}]\in H^1(\mathcal Q^\bullet_{\mathcal G,M}(I))\) and the
  Roos class \(\lambda^{\mathrm{fw}}_{n_0}\).

## Files Changed/Staged

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-141-finite-window-graph-array.md`

These paths were staged after scoped verification.

## Verification

Commands run:

```bash
python3 scripts/finite_window_graph_array.py
python3 -m py_compile scripts/finite_window_graph_array.py
git diff --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
rg -n -F "finite-window-graph-array" tate-P1-hadamard-mittag-leffler.tex
rg -n -F "first-finite-window-array-rows" tate-P1-hadamard-mittag-leffler.tex
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex
git diff --cached --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-141-finite-window-graph-array.md
git diff --cached --name-only -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-141-finite-window-graph-array.md
```

Results:

- The script computes \(\omega(z_1,z_2)=1\), \(\omega(z_2,z_1)=-1\), the
  ordinary \(\mathfrak{gl}_N\) scalar gate, the even-block scalar gate, and
  the full-equivariant zero gate with \(C_{1,M}=0\) on the minimal array.
- `py_compile` passed.
- `git diff --check` passed.
- Trailing-whitespace grep returned no hits.
- Label scans found the new definition and proposition.
- `lacheck` reports only three pre-existing nonbreaking-space suggestions at
  lines 39, 218, and 221.
- `chktex` reports nonfatal style warnings, including the pre-existing class
  and new display/table style warnings; no fatal TeX syntax error was found.
- `git diff --cached --check` passed after staging.
- `git diff --cached --name-only` listed exactly the three owned paths.
- `make pdf` was not run because the shared checkout has concurrent staged
  manuscript edits and the build writes tracked output outside this agent's
  owned paths.
