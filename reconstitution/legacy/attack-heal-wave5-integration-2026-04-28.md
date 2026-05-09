# Attack-Heal Wave 5 Integration

Date: 2026-04-28.

Main-thread integration owner: `/Users/raeez/topological-strings`.

Integrated results:

1. Radial parts remains conditional at all \(N\).  The manuscript now
   names the exact Weyl-trace image normalization as external input,
   and `scripts/check_moyal_coefficients.py` adds a direct \(N=2\)
   radial restriction harness on 36 operator/test-polynomial pairs.
2. The unreduced BV cotangent centrality/QME lift remains open.  The
   obstruction is recorded by BV degrees, the scalar contact term, and
   the opposite index shifts between polynomial one-\(\psi\) descendants
   and Matlis principal parts.
3. Weighted Tate regulator independence is proved only inside the
   admissible finite-window Mittag-Leffler sector.  The strict
   product/direct-sum unweighted graph theory remains outside the
   theorem because its coefficient Casimir is absent.
4. The quantum descendant lift is obstructed.  The displayed
   \(z_1^4\) computation and the exact sweep in
   `scripts/check_one_psi_homology.py` show that the naive
   \(\Psi_{a,b}\mapsto\rho_{a,b}\) label map does not intertwine the
   Moyal coadjoint action.
5. A Fourier--Rees bridge is now constructed, but only as a
   Fourier-twisted Weyl-module and associated-graded label comparison.
   It does not weaken the no-polynomial-descendant theorem and does not
   give a same-action \(\mathfrak h\)-module isomorphism.
6. Cross-volume consequences remain non-asserted.  The no-transfer
   lemmas and matched-conventions theorem datum/templates are kept as
   firewalls, not export theorems.

Worker reports preserved:

- `reconstitution/attack-heal-wave5-radial-2026-04-28.md`
- `reconstitution/attack-heal-wave5-unreduced-bv-2026-04-28.md`
- `reconstitution/attack-heal-wave5-tate-regulator-2026-04-28.md`
- `reconstitution/attack-heal-wave5-quantum-descendant-2026-04-28.md`
- `reconstitution/attack-heal-wave5-rees-fourier-2026-04-28.md`
- `reconstitution/attack-heal-wave5-crossrepo-2026-04-28.md`

Semantic merge rule applied: report artifacts and standalone scripts were
copied after review; proof-bearing manuscript files were patched
selectively so stale hunks did not remove stronger existing
matched-conventions language.

