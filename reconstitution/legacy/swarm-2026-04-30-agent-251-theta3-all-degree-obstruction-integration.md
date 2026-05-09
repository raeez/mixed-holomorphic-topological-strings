# Agent 251 - Theta3 All-Degree Obstruction Integration

## Scope

Owned files:

- `open-obligations.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-251-theta3-all-degree-obstruction-integration.md`

No claim-ledger, dictionary, main manuscript, script, figure, or build file
was edited.

Staged paths after integration are exactly the three owned files above,
relative to this assignment.  Other pre-existing staged paths in the
shared checkout were left untouched.

## Integrated Claim

Agent 245 strengthens the theta3 source obstruction from the
Hamiltonian-degree-\(\leq3\) pure two-\(u\) test to the full ordinary pure
two-\(u\) source envelope in every finite Hamiltonian degree.  The inserted
covector is
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
\]
with
\[
  q_{2u}d_{\mathrm{CE}}=0,\qquad
  q_{2u}(\zeta_{M,\nu_3})=1.
\]
Thus no ordinary pure two-\(u\) degree enlargement supplies a CE ancestor
for \(\zeta_{M,\nu_3}\).

## Attack-Heal Status

Valid attack: the earlier TeX wording made the obstruction look like a
degree-\(\leq3\) finite-window test.  Agent 245 supplies a stronger
left-cokernel valid in every finite Hamiltonian degree.

Heal: the text now states an exact obstruction theorem for the ordinary
pure two-\(u\) source envelope only.  It explicitly avoids a universal
no-go claim and names the admissible repair data.

Exact missing repair data now recorded:

- counterterm column \(A^M_{\theta_3,C}=-1\), scalar-zero value, and zero
  Roos class;
- marked source generator outside the ordinary pure two-\(u\) algebra,
  with boundary column of \(q_{2u}\)-value \(1\), codimension-two closure,
  Hom-valued Bianchi cancellation, scalar-zero value, and transport;
- marked companion relation \(R^{\mathrm{cand}}_{\Theta_3,M}=0\);
- lower-window transport
  \(v^{M,N}R^{\mathrm{cand}}_{\Theta_3,M}=0\), including the \(N=2\)
  relation killing \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\).

## Verification

Targeted diff checks:

```bash
git diff --check -- open-obligations.tex theorem-lanes.tex \
  reconstitution/swarm-2026-04-30-agent-251-theta3-all-degree-obstruction-integration.md
git show :open-obligations.tex | rg -n -F -e 'q_{2u}' -e 'ordinary pure two'
git show :theorem-lanes.tex | rg -n -F -e 'q_{2u}' -e 'ordinary pure two'
```

The whitespace check passed.  Search checks confirmed the new \(q_{2u}\)
formula and the all-degree pure two-\(u\) wording appear in both TeX
targets; the old degree-bounded source-obstruction phrase is absent from
both staged TeX targets.

No PDF build was run.  The task was a targeted integration in a shared
checkout with concurrent edits outside this ownership surface.
