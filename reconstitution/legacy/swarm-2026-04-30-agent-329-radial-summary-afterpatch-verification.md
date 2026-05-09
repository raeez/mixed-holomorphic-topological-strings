# Agent 329: radial summary afterpatch verification

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-summary-afterpatch-verification-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-329-radial-summary-afterpatch-verification.md`

No manuscript TeX or script file was edited.

## Claim attacked

After Agent 325 and the main-thread radial-summary patches, every
reader-facing radial/Weyl theorem surface must use the accepted normal form:
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)).
\]
The positive theorem is \(\Omega^{\mathrm{rad}}_{a,b}=0\), equivalently
decorated PBW Stokes
\[
  D^\square_{a,b}=C^+_{a,b}\partial_2.
\]
Failure is exactly a signed row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
The old \(\mathcal C_{a,b}\), harmonic projection, and left-cokernel
language is admissible only as the subordinate free normal-diagram model.

## Inputs read

- `main.tex`
- `theorem-lanes.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `appendix-radial-parts-moyal.tex`
- `reconstitution/radial-obstruction-surface-propagation-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-320-radial-obstruction-surface-propagation-audit.md`
- `reconstitution/radial-summary-propagation-final-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-325-radial-summary-propagation-final-audit.md`

The Agent 320 and Agent 325 non-`swarm-*` reports are not byte-identical to
their `swarm-*` mirrors. Both versions were checked. The checkout was already
heavily dirty from concurrent agents; this pass wrote only the two Agent 329
report files.

## Verification result

Status: partial afterpatch propagation. Several Agent 325 patch targets are now
healed in the current TeX. Residual stale language remains where a reader-facing
summary still ends at `\mathcal C_{a,b}`, left-cokernel, uniform homotopy, or
"radial/Weyl gate" without the \(\Omega^{\mathrm{rad}}\),
\(D^\square=C^+\partial_2\), and signed-row formulation.

Correct afterpatch surfaces:

- `main.tex:1055-1082`: frontmatter quantum-data summary now gives
  \(\Omega^{\mathrm{rad}}\), \(D^\square\), and signed-row failure before
  mentioning the older `\mathcal C_{a,b}` language.
- `main.tex:2428-2449`: early theorem narrative now states the interior
  dual-potential problem, decorated PBW Stokes, and signed-row failure.
- `main.tex:2750-2786`: local theorem package summary now contains the
  subordinate free-diagram formulation and the stronger dual-potential/Stokes
  formulation.
- `main.tex:7428-7472`, `main.tex:7648-7665`, and `main.tex:8308-8338`:
  the finite-N, Hamiltonian-sector, and all-order degree-zero surfaces now
  include \(\Omega^{\mathrm{rad}}\), \(D^\square\), and signed rows.
- `theorem-lanes.tex:2537-2562`, `theorem-lanes.tex:2677-2689`,
  `theorem-lanes.tex:2778-2790`, and `theorem-lanes.tex:3668-3702`:
  the principal lane statements and radial trace-diagram lane carry the
  accepted obstruction surface.
- `open-obligations.tex:510-529` and `open-obligations.tex:1369-1440`:
  the body text now records the dual-potential obstruction and decorated
  Stokes target.
- `claim-strength-ledger.tex:207-216`, `claim-strength-ledger.tex:301-309`,
  `claim-strength-ledger.tex:580-590`, and
  `claim-strength-ledger.tex:1010-1049`: these rows/items now carry the
  accepted obstruction surface.
- `appendix-radial-parts-moyal.tex:965-1027`: the dual-potential proposition
  names \(\Omega^{\mathrm{rad}}\), \(D^\square\), and signed-row failure.

## Remaining patch targets

1. `main.tex:7559-7586`.
   `cor:degree-zero-quantum-upgrade` still phrases the all-interior extension
   as \(\mathfrak o_{a,b}=0\), functorial lifts \(K_{a,b}\), or an equivalent
   left-cokernel vanishing theorem. Patch the corollary statement to name
   \(\Omega^{\mathrm{rad}}_{a,b}=0\), decorated PBW Stokes
   \(D^\square_{a,b}=C^+_{a,b}\partial_2\), and the signed
   \(B_{a,b}^*\)-row criterion.

2. `main.tex:8377-8386`.
   The proof of `thm:phi-hbar-all-order` still cites the free-kernel
   obstruction chain without
   `Proposition~\ref{prop:app-radial-dual-potential-obstruction}`. Add that
   proposition and the \(D^\square\) Stokes criterion to the proof-input chain.

3. `main.tex:8450-8458`.
   In `thm:quantum-coefficient-surface`, the \(T_{\mathrm{Ham},\hbar}\)
   factor is introduced using only the radial-normalization obstruction
   \(\mathfrak o_{a,b}\), homotopy, and left-cokernel language. Patch this
   factor description to the dual-potential obstruction surface.

4. `main.tex:8568-8571`.
   The proof of `thm:quantum-coefficient-surface` says item (4) is exactly the
   named radial-normalization obstruction, but does not name
   \(\Omega^{\mathrm{rad}}\), \(D^\square\), or signed rows. Patch by citing
   `prop:app-radial-dual-potential-obstruction` and the decorated Stokes gate.

5. `theorem-lanes.tex:2637-2654`.
   The proof-input list for the degree-zero lane cites the older free
   normal-diagram obstruction chain but not the dual-potential proposition.
   Add `Proposition~\ref{prop:app-radial-dual-potential-obstruction}` and the
   \(D^\square\) decorated Stokes target.

6. `theorem-lanes.tex:2725-2730`.
   The componentwise coefficient-surface hypothesis summary still says the
   degree-zero Hamiltonian trace comparison is read through a radial/Weyl gate
   whose remaining interior bidegrees require a kernel homotopy or
   left-cokernel vanishing theorem. Patch this summary to the
   \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row form.

7. `open-obligations.tex:1353-1354`.
   The item heading still says "uniform homotopy gate." The body is repaired,
   but the heading is summary-level reader-facing text. Rename it to a
   dual-potential/decorated-Stokes gate.

8. `claim-strength-ledger.tex:103-109`.
   Stage A6a still describes the fourth component as a
   finite-certificate-relative radial/Weyl trace comparison with a
   uniform-homotopy gate. Patch to state the exact
   \(\Omega^{\mathrm{rad}}\), decorated PBW Stokes, and signed-row obstruction
   surface.

9. `claim-strength-ledger.tex:993-995`.
   The detailed radial/Weyl item body is repaired, but its heading and
   classification still say "uniform homotopy" and "exact uniform-homotopy
   obstruction." Rename the surface to the exact dual-potential/decorated
   Stokes obstruction.

10. `claim-strength-ledger.tex:1244-1277`.
    The "Quantum Hamiltonian and Moyal sector" item still closes the ordinary
    Weyl-trace comparison at
    \(\mathfrak o^{\mathrm{rad}}_{a,b}\in\operatorname{coker}\mathcal C_{a,b}\)
    and a uniform contracting homotopy. Patch it to cite
    `prop:app-radial-dual-potential-obstruction`, the \(B_{a,b}\)-cokernel
    class, decorated PBW Stokes, and signed-row failure.

11. `claim-strength-ledger.tex:1295-1299`.
    The componentwise quantum coefficient surface says the fourth factor is
    relative to the finite-certificate radial/Weyl gate and its
    uniform-homotopy obstruction. Patch this line to the accepted
    \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row theorem surface.

12. `appendix-radial-parts-moyal.tex:888-939`.
    The decorated Hodge obstruction theorem remains an
    \(A_{a,b}=C^+|_{\ker\partial}\)-only theorem. Add the reader-facing
    equivalence with \(\Omega^{\mathrm{rad}}_{a,b}=0\), \(B_{a,b}\), and
    signed-row failure, or explicitly point forward to
    `prop:app-radial-dual-potential-obstruction`.

13. `appendix-radial-parts-moyal.tex:965-1027`.
    This proposition has the right summary vocabulary, but still needs the
    square-cell refinement: define the square-cell complex
    \(C^\square_\bullet(a,b)\) in the appendix, state the ordinary cycle fact
    \(\operatorname{im}\partial_2=\ker\partial\) in the relevant quotient, and
    state the decorated Stokes left-cokernel criterion
    \(\lambda D^\square_{a,b}=0\Rightarrow
    \lambda(R^{\mathrm{free}}_{a,b})=0\).

14. `appendix-radial-parts-moyal.tex:1061-1110`.
    The potential-form remark still distinguishes only the bare graph Green
    operator from the decorated Hodge operator \(A_{a,b}A_{a,b}^*\). Patch it
    to distinguish the proved ordinary square-cell cycle mechanism from the
    still-missing decorated PBW Stokes identity
    \(D^\square=C^+\partial_2\).

15. `appendix-radial-parts-moyal.tex:1143-1147`.
    The edge PBW telescoping proposition ends by saying the remaining theorem
    is the left-cokernel/associated-graded necklace vanishing problem encoded
    in the Hodge statement. Patch this trailing summary to point to
    \(\Omega^{\mathrm{rad}}\), decorated Stokes, and signed-row failure.

16. `appendix-radial-parts-moyal.tex:1434-1439`.
    The proof of `thm:app-radial-finite-N` says one must construct
    all-N moment-ideal primitives, free corrections \(K_{a,b}\), or prove a
    left-cokernel obstruction. Patch to include the dual-potential and
    decorated Stokes normal form.

17. `appendix-radial-parts-moyal.tex:1698-1712`.
    The computation remark says the scripts do not construct the
    all-bidegree contracting homotopy required by the Hodge statement. Patch
    to say they also do not establish
    \(\Omega^{\mathrm{rad}}_{a,b}=0\) or the decorated PBW Stokes identity.

18. `appendix-radial-parts-moyal.tex:1820-1830`.
    The final proof item cites only the primitive obstruction and Hodge
    obstruction formulations. Patch to include
    `prop:app-radial-dual-potential-obstruction` and the
    \(D^\square\) criterion.

## Non-target old language

The following current uses of \(\mathcal C_{a,b}\) are acceptable afterpatch
uses because the same local surface already states the stronger
\(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row formulation:

- `main.tex:1079-1082`
- `main.tex:2769-2786`
- `main.tex:7446-7462`
- `main.tex:8317-8338`
- `theorem-lanes.tex:2544-2562`
- `theorem-lanes.tex:2588-2613`
- `theorem-lanes.tex:3668-3702`
- `open-obligations.tex:1369-1440`
- `claim-strength-ledger.tex:1010-1049`
- `appendix-radial-parts-moyal.tex:852-885`

These passages use the old map as the free-diagram model rather than as the
last word of the theorem surface.

## Commands run

- `git status --short`
- `wc -l main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex appendix-radial-parts-moyal.tex`
- `rg` over the requested TeX files for `\mathcal C_{a,b}`, `left-cokernel`,
  `uniform-homotopy`, `radial/Weyl gate`, `radial-normalization obstruction`,
  `\Omega^{\mathrm{rad}}`, `D^\square`, `decorated PBW Stokes`, and
  `signed row`
- `nl -ba` and `sed -n` on the requested TeX files and Agent 320/325 reports
- `cmp -s` on the Agent 320 and Agent 325 non-`swarm-*`/`swarm-*` report pairs

No build was run. This was a report-only audit.
