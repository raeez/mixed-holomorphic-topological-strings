# Omega Consistency Audit, 2026-04-30

Scope: audit only.  No TeX file was edited.  Owned output paths are this
file and `reconstitution/swarm-2026-04-30-agent-195-omega-consistency-audit.md`.

Trusted context read:

- `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`, and
  `~/ecosystem/AGENTS-HARNESS.md`.
- The requested attack-heal swarm protocol and its `references/protocol.md`.
- `local-dictionary.tex`,
  `tate-T1-weighted-completion.tex`,
  `appendix-unreduced-bv-qme.tex`,
  `appendix-factorization-current-conventions.tex`,
  `theorem-lanes.tex`.
- Reports 177, 179, 184, 189.  Report 192 is absent; the launch log
  records it as live at `reconstitution/swarm-live-launch-log-2026-04-30.md:1226`.

## Stable Core

The brane-preserving normal Omega datum is:

\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C_{z_1}\times\mathbb C_{z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\},
\]
\[
  N_LX=\mathbb R_s\oplus\mathbb C_{z_1}\oplus\mathbb C_{z_2},
  \qquad t\text{ fixed}.
\]

The canonical equivariant weight symbols in the local dictionary are
\(\epsilon_s,\epsilon_1,\epsilon_2\), not
\(\varepsilon_s,\varepsilon_1,\varepsilon_2\).  The latter are already
used for open trace orientation variables.  Evidence:
`local-dictionary.tex:407-417`.

The vector field and Cartan identity are stable:
\[
  V_\Omega=
  \epsilon_s s\partial_s
  +\epsilon_1z_1\partial_{z_1}
  +\epsilon_2z_2\partial_{z_2},
  \qquad
  Q_\Omega=Q+\iota_{V_\Omega},
  \qquad
  Q_\Omega^2=L_{V_\Omega}.
\]
Thus \(Q_\Omega\) is a differential only on invariant/basic objects, or
inside a curved Cartan package.  Evidence:
`local-dictionary.tex:424-443`,
`appendix-unreduced-bv-qme.tex:2157-2173`,
`claim-strength-ledger.tex:363-378`.

The stable weights are:

| Object | Weight |
|---|---|
| \(H_{a,b}=z_1^az_2^b\) | \(a\epsilon_1+b\epsilon_2\) |
| \(\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2\) | \(-a\epsilon_1-b\epsilon_2\) |
| \(c^{a,b},\theta^{a,b}\) | \(-a\epsilon_1-b\epsilon_2\) |
| \(u_{a,b},O_{a,b}\) | \(a\epsilon_1+b\epsilon_2\) |
| \(B_{p,q}(a)\) | \(p\epsilon_1+q\epsilon_2\) |
| \(\Theta_{r,s}(B)\) | \(-r\epsilon_1-s\epsilon_2\) |
| \(\hbar_\omega\) | \(\epsilon_1+\epsilon_2\) |
| Weyl \(\hbar\), when used equivariantly | \(\epsilon_1+\epsilon_2\) |

Evidence: `local-dictionary.tex:484-505`,
`local-dictionary.tex:545-563`,
`appendix-factorization-current-conventions.tex:399-422`,
`appendix-factorization-current-conventions.tex:493-531`,
`reconstitution/swarm-2026-04-30-agent-189-equivariant-ce-pv-refined-bracket-0957.md:29-67`.

The self-dual branch is separate:
\[
  \epsilon_1+\epsilon_2=0.
\]
One must not invert \(\epsilon_1+\epsilon_2\) and then specialize to zero.
Evidence: `local-dictionary.tex:445-457`,
`appendix-factorization-current-conventions.tex:455-462`,
`reconstitution/swarm-2026-04-30-agent-189-equivariant-ce-pv-refined-bracket-0957.md:157-165`.

Residue normalization and Euler localization are separate:
\[
  \nu_\Omega^{\mathrm{res}}=1,\qquad
  \nu_\Omega^{\mathrm{Eu}}
  =\sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
\]
The sign \(\sigma_s\) is still open.  Evidence:
`local-dictionary.tex:565-588`,
`tate-T1-weighted-completion.tex:481-499`,
`open-obligations.tex:663-676`.

## Conflict Matrix

| ID | Surface | Status | Evidence | Exact fix needed |
|---|---|---|---|---|
| C195-01 | Omega parameter glyphs | Conflict | Canonical `\epsilon` is fixed in `local-dictionary.tex:407-417`; `abstract.tex:195-208`, `appendix-unreduced-bv-qme.tex:2152-2184`, `open-obligations.tex:527`, `open-obligations.tex:559-560`, `open-obligations.tex:645`, `open-obligations.tex:672`, and report 179 use `\varepsilon` for Omega weights. | Replace Omega-weight `\varepsilon_s,\varepsilon_1,\varepsilon_2` by `\epsilon_s,\epsilon_1,\epsilon_2` in those Omega passages.  Do not change open trace orientation uses such as `local-dictionary.tex:112` and `local-dictionary.tex:572`. |
| C195-02 | Normal localization ring | Conflict | The dictionary inverts all nonzero finite normal characters, `local-dictionary.tex:445-457`; weighted kernels use the finite set \(\mathsf X_{N,M}\), `tate-T1-weighted-completion.tex:398-409`; the QME appendix uses only \((\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}\), `appendix-unreduced-bv-qme.tex:2175-2183`. | Replace the QME appendix ring by a finite-window ring \(R_\Omega^{N,M}=\mathbb C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega][\chi^{-1}\mid\chi\in\mathsf X_{N,M}]\), or a named global character localization.  Keep the Euler product as normalization data, not as the whole moving-character localization. |
| C195-03 | \(\hbar\) versus \(\hbar_\omega\) | Undecided conflict | `local-dictionary.tex:503-530` gives both \(w(\hbar)=\chi_\omega\) and \([f,g]_\Omega=\hbar_\omega\{f,g\}\), with possible Weyl/Moyal identification.  The QME appendix keeps both \(\hbar\) and \(\hbar_\omega\), `appendix-unreduced-bv-qme.tex:2175-2197`, and forms scalar contact terms \(\nu_\Omega\hbar[\{f,g\}_\Omega]_0\), `appendix-unreduced-bv-qme.tex:2292-2297`. | Add a branch convention before the QME datum: either \(\hbar_\omega\) is an independent equivariant line scalar and the scalar-contact order is \(\hbar\hbar_\omega\), or the Weyl branch sets \(\hbar_\omega=\hbar_{\mathrm{Weyl}}\) and renames the QME expansion parameter to avoid double counting.  Do not silently identify them in obstruction rows. |
| C195-04 | Self-dual specialization | Mostly consistent, one missing guard | The dictionary and current appendix forbid inverting \(\epsilon_1+\epsilon_2\) before self-dual specialization, `local-dictionary.tex:455-457`, `appendix-factorization-current-conventions.tex:455-462`.  The QME appendix says one may set \(\hbar_\omega=1\) on the self-dual locus, `appendix-unreduced-bv-qme.tex:2197-2198`, but the adjacent ring has no explicit self-dual no-inversion guard. | After fixing \(R_\Omega^{N,M}\), add: on the self-dual branch remove \(\epsilon_1+\epsilon_2\) from the inverted character set and retain its resonant summands in \(\operatorname{pr}_{\chi=0}\). |
| C195-05 | \(c,u,O,\theta\) weights | Integration gap | Agent 189 records \(w(c^{a,b})=w(\theta^{a,b})=-a\epsilon_1-b\epsilon_2\) and \(w(u_{a,b})=w(O_{a,b})=a\epsilon_1+b\epsilon_2\), report lines 29-67.  `local-dictionary.tex:534-543` records the generator rule but not these weights.  `theorem-lanes.tex:678-742` and `theorem-lanes.tex:922-950` are non-equivariant. | Add an explicit equivariant CE/PV weight row to `local-dictionary.tex` or the theorem lane.  Use coordinate notation \(c^{a,b},\theta^{a,b}\) for dual coordinates and \(u_{a,b},O_{a,b}\) for cotangent coordinates, or define the all-lower-index convention. |
| C195-06 | Equivariant CE/PV theorem lane | Integration gap | The local dictionary requires the refined \(\hbar_\omega\)-weighted convention, `local-dictionary.tex:517-543`; Agent 189 supplies \(d_{\mathrm{CE},\Omega}\), \(d_{\pi,\Omega}\), and \(\pi_\Omega\); `theorem-lanes.tex:1000-1136` only states the non-equivariant coordinate CE/PV theorem. | Add an Omega-refined theorem lane after the non-equivariant CE/PV block, or explicitly label the existing theorem lane as non-equivariant and point to the Omega report until the theorem lane is integrated. |
| C195-07 | Brane-current Omega brackets | Formula consistent, report missing | `appendix-factorization-current-conventions.tex:399-550` gives the current bracket theorem with \(\hbar_\omega\), correct \(B/\Theta\) weights, self-dual separation, and QME firewall.  The expected Agent 192 report is absent; launch log says it is live, `reconstitution/swarm-live-launch-log-2026-04-30.md:1226-1231`. | Obtain or regenerate `reconstitution/swarm-2026-04-30-agent-192-equivariant-brane-current-brackets-0957.md`.  Until then the theorem can be locally audited, but the requested report surface remains missing. |
| C195-08 | Residue/Euler normalization | Partial conflict | Dictionary separates residue from Euler, `local-dictionary.tex:565-588`; weighted kernel theorem includes \(\sigma_s\), `tate-T1-weighted-completion.tex:481-499`; QME appendix omits \(\sigma_s\), `appendix-unreduced-bv-qme.tex:2258-2265`; `open-obligations.tex:668-675` allows the Euler factor to be built into the residue orientation. | Add \(\sigma_s\) to the QME appendix normalization row.  Reserve plain residue normalization for no Euler denominator; if the Euler factor is absorbed into a residue orientation, name it Euler-rescaled residue normalization. |
| C195-09 | Coefficient field in stratified/trace targets | Notation conflict | `claim-strength-ledger.tex:401-405` and `open-obligations.tex:524-528` use \(\operatorname{Ch}_{\mathbb C((\epsilon_s,\epsilon_1,\epsilon_2))[[\hbar]]}\) or the `\varepsilon` variant; finite-window kernels use \(R_\Omega^{N,M}\) with character inversions. | Introduce a named \(K_\Omega\) or \(R_\Omega^{N,M}\) convention and use it in the stratified and trace targets.  If a fraction field is intended, say it inverts all nonzero normal characters used by the finite-window package. |
| C195-10 | QME implication firewall | Consistent | `local-dictionary.tex:377-382`, `tate-T1-weighted-completion.tex:537-589`, `appendix-unreduced-bv-qme.tex:2436-2441`, and report 179 all say Omega localization does not prove QME without propagator, counterterms, scalar gates, non-scalar \(H^1\), and \(\varprojlim^1H^0\). | No formula fix.  Preserve this firewall during integration. |
| C195-11 | Normal geometry | Consistent | All loaded theorem surfaces use normal scaling with \(t\) fixed, not a native \((t,s)\)-rotation: `local-dictionary.tex:393-405`, `abstract.tex:191-200`, `appendix-unreduced-bv-qme.tex:2144-2164`, `claim-strength-ledger.tex:357-368`. | No formula fix.  Apply C195-01 glyph cleanup where needed. |

## Exact TeX Fix List

1. `abstract.tex:195-208`: change Omega weights from `\varepsilon_*` to
   `\epsilon_*`.
2. `appendix-unreduced-bv-qme.tex:2152-2184` and
   `appendix-unreduced-bv-qme.tex:2261`: change Omega weights from
   `\varepsilon_*` to `\epsilon_*`.
3. `appendix-unreduced-bv-qme.tex:2175-2183`: replace the product-only
   localization ring by \(R_\Omega^{N,M}\) or a named global character
   localization compatible with `tate-T1-weighted-completion.tex:398-409`.
4. `appendix-unreduced-bv-qme.tex:2184-2198` and
   `appendix-unreduced-bv-qme.tex:2292-2297`: state the
   \(\hbar/\hbar_\omega\) branch convention before any scalar-contact
   order is read.
5. `appendix-unreduced-bv-qme.tex:2258-2265`: include
   \(\sigma_s\) in the Euler convention and state that residue and
   Euler-rescaled residue are different normalizations.
6. `local-dictionary.tex:534-543`: add explicit CE/PV coordinate weights
   for \(c^{a,b},\theta^{a,b},u_{a,b},O_{a,b}\), or point to the new
   theorem lane that records them.
7. `theorem-lanes.tex:1000-1136`: add an Omega-refined CE/PV lane with
   the \(\hbar_\omega\)-scaled differential, or mark the existing lane as
   non-equivariant until Agent 194 integrates it.
8. `open-obligations.tex:527`, `open-obligations.tex:559-560`,
   `open-obligations.tex:645`, `open-obligations.tex:672`: change
   `\varepsilon_*` to `\epsilon_*` for Omega weights and replace the
   ambiguous \(\mathbb C((\epsilon_s,\epsilon_1,\epsilon_2))\) target by
   the named \(K_\Omega\) or \(R_\Omega\) convention.
9. `open-obligations.tex:668-675`: replace "built into the residue
   orientation" by "built into an Euler-rescaled residue convention" if
   that branch is intended.
10. Regenerate or add the missing Agent 192 report for
    `appendix-factorization-current-conventions.tex:399-550`.

## Remaining Open Obligations

- Construct the mixed \(T_\Omega\)-Cartan/basic coefficient model.
- Prove the normal contraction signs in the mixed de Rham/Dolbeault
  category, including \(ds\)-weight shifts.
- Prove finite-window nonresonance for any scalar specialization; prove
  \(q\)-moderate bounds for any analytic all-window claim.
- Choose the \(\hbar/\hbar_\omega\) branch and propagate it through the
  QME order filtration.
- Prove the equivariant CE/PV theorem in a bracket-admissible completion,
  not only in coordinate formulas.
- Decide residue, Euler, or Euler-rescaled residue normalization and fix
  \(\sigma_s\).
- Construct the equivariant Costello propagator, counterterms, scalar
  projection chain map, non-scalar \(H^1\) classes, and
  \(\varprojlim^1H^0\) primitive compatibility.
- Build the stratified factorization datum on \((X,L)\), then the trace
  state, Ward identities, and physical large-\(N\) topology.
