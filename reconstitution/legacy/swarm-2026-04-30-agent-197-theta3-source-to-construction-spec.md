# Agent 197 - Theta3 Source-to-Construction Specification

Status: report-only construction specification; no commits or pushes.

## Stable Core

I found no CE ancestor, no local counterterm primitive, and no complete
companion-face table in the current source surfaces.  The current data
remain:
\[
  \mathsf E_{\theta_3,M}
    =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  K^0_{\theta_3,M}=0,\qquad
  K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M}.
\]
The script verifies the same finite-row decision:

```text
theta_3_current_finite_row_subcomplex:
  primitive_exists = false
  obstruction_covector = E_theta_3 -> 1
  obstruction_value_on_residual = 1

theta_3_with_supplied_candidate_C_theta_3:
  primitive_exists = true
  primitive_coefficients = C_theta_3 -> 1
```

Thus the supplied row has a real finite-row obstruction.  It is not a proof
of non-exactness in the full local-functional complex.

## Construction Attempt

The only sign-compatible primitive has matrix entry
\[
  A^M_{\mathsf E,C}=-1,
  \qquad
  d_{\mathrm{ns},M}C_{\theta_3,M}
    =
  -\mathsf E_{\theta_3,M}
    =
  K^M_{\Theta_3}(\zeta_{M,\nu_3}).
\]
I searched the manuscript, script, processed critique, primary-source
anchors, and reconstitution reports for:

- a source ancestor \(\eta_{\theta_3,M}\) with
  \(d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3}\);
- a local counterterm
  \(C^M_{\Theta_3,\nu_3,w}(\epsilon;B^\Theta_\bullet)\) with
  \(dC=-\mathsf E_{\theta_3,M}\);
- a source-face set \(F_{\Theta_3,M}\) whose signed CE residual sum is zero.

The only positive hit is the hypothetical interface case
`theta_3_with_supplied_candidate_C_theta_3`.  It supplies the matrix test
that would pass after a primitive is given; it does not supply the
primitive.

## Exact Missing Datum

The minimal exact data structure is written in
`reconstitution/theta3-source-to-construction-spec-2026-04-30.md`.  It has
three mutually exclusive healing payloads:

1. `theta3_ce_ancestor`: source element \(\eta_{\theta_3}\), its CE
   boundary, Hom-valued Bianchi rows, scalar projection, and primitive
   transport.
2. `theta3_counterterm_primitive`: an actual degree-zero local functional,
   its \(d_{\mathrm{ns}}\)-boundary, locality proof, scalar projection, and
   transport.
3. `theta3_complete_companion_faces`: every CE source face in
   \(d_{\mathrm{CE}}\zeta_M\), all signs, row coordinates, scalar gates,
   source-face truncation matrices \(v^{M,N}\), and codimension-two closure.

These fields are necessary because the marked Costello list definition
requires every boundary output, coefficient, marker transport, counterterm
vertex, source face, and codimension-two closure entry.  The finite-window
primitive search then requires the boundary matrix \(A\), residual vector
\(r\), row transport \(T\), primitive transport \(P\), and Roos class
\([Pc_M-c_N]\).

## File Anchors

- `tate-P1-hadamard-mittag-leffler.tex:379`: finite-window graph/QME package
  data.
- `tate-P1-hadamard-mittag-leffler.tex:1816`: finite-row primitive search
  interface \(Ac=-r\).
- `tate-P1-hadamard-mittag-leffler.tex:1898`: concrete
  \(\theta_3\) row.
- `tate-P1-hadamard-mittag-leffler.tex:2026`: one-row obstruction
  certificate.
- `tate-P1-hadamard-mittag-leffler.tex:2092`: actual finite-window
  non-scalar decision datum.
- `appendix-unreduced-bv-qme.tex:1623`: marked Costello list and complete
  boundary table.
- `appendix-unreduced-bv-qme.tex:1900`: marked habitat compatibility and
  Hom-valued source face.
- `scripts/finite_window_graph_array.py:792`: executable order-three CE row.
- `scripts/finite_window_graph_array.py:889`: executable primitive-search
  cases.
- `reconstitution/swarm-2026-04-30-agent-187-finite-window-qme-rows-0957.md:33`:
  finite-row obstruction summary.
- `reconstitution/swarm-2026-04-30-agent-193-theta3-companion-primitive-search-0957.md:38`:
  prior no-primitive verdict.

## Commands Run

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sha256sum materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt
git status --short
rg -n "theta|theta_3|theta3|E_theta|companion|finite-window|finite window|CE ancestor|counterterm|primitive|residual|face|row|column|QME|Hadamard|Mittag|Moyal|obstruction|dC|d eta|eta" main.tex tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-187-finite-window-qme-rows-0957.md reconstitution/swarm-2026-04-30-agent-193-theta3-companion-primitive-search-0957.md reconstitution/finite-window-theta3-companion-primitive-search-2026-04-30.md materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt
rg -n "theta_3|Theta_3|nu_3|E_theta_3|C_theta_3|eta_theta_3|CE-source|source-face|primitive" reconstitution/swarm-2026-04-30-agent-1*.md reconstitution/finite-window-theta3-companion-primitive-search-2026-04-30.md
rg -n "counterterm|primitive|CE ancestor|source-face|companion|Bianchi|theta" references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

The refreshed critique hashes matched the supplied SHA-256 values.
`py_compile` passed.  The script output contained no present primitive
except the guarded hypothetical `theta_3_with_supplied_candidate_C_theta_3`.

## Files Changed

- `reconstitution/theta3-source-to-construction-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-197-theta3-source-to-construction-spec.md`

## Verdict

Blocked as a construction; advanced as a precise source-to-construction
specification.  The theta obstruction can be killed only after one of the
three payloads above is supplied.  The exact missing mathematical object is
not a convenience field: without it, \(Ac=-r\), \(TA=AP\), and the Roos
\(\varprojlim^1H^0\) test are undefined for the enlarged local-functional
claim.
