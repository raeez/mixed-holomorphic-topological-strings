# Agent 012 Global Firewall Report

Habitat: `GlobDesc` / cross-volume firewall.

Claim attacked: the local Hamiltonian BF/Moyal/CE-PV theorem might be read
as implying compact Calabi-Yau, global BCOV, MNOP/chiral-volume, Vol III,
Igusa/BKM, or sister-volume consequences.

Source and target: the source is the local \(d=2\) formal-stalk convention
base \(\mathfrak C_{\mathrm{loc}}^{(2)}\).  The target is now explicitly
\[
C_{\mathrm{tar}}=(X,\omega,\Omega,\mathfrak U,\{E_i,Q_i,\omega_i,I_i\},
\{\phi_{ij}\},\{\phi_{ijk}\},Per,Anom,QME,Conv,Hyp,Op),
\]
together with matched-conventions maps
\(\chi_{\mathrm{cl}},\chi_{\mathrm{op}},\chi_{\mathrm{anom}}\).

First-principles computation: for a compact connected holomorphic
symplectic surface,
\[
\operatorname{per}_X(v)=\delta(-\iota_v\omega)\in H^1(X,\mathbb C_X).
\]
The class vanishes iff the local Hamiltonian primitives glue to a global
holomorphic Hamiltonian, hence iff \(v=0\).  A nonzero translation on an
abelian surface is rejected by the period component.

Failure mode found: the appendix already had the right firewall shape, but
the target datum was not the explicit \(C_{\mathrm{tar}}\) required by the
04:11 controller; the obstruction vector omitted weighted-regulator and
modular-descent components; and the first Weiss/Ran obstruction shared
notation with the higher coherence tower.

Heal: `tate-P5-cross-volume.tex` now defines \(C_{\mathrm{tar}}\), the
global obstruction vector \(\operatorname{Ob}_{C_{\mathrm{tar}}}\), and
\(\operatorname{Ob}_{\mathrm{UKD}}(C_{\mathrm{tar}})\).  The transfer
criterion now accepts a target theorem only after
\(\operatorname{Ob}_{\mathrm{UKD}}(C_{\mathrm{tar}})=0\) with compatible
null-homotopies.  Missing required components are incomplete target data,
not zero obstructions.  The Weiss/Ran tower now separates
\(\operatorname{ob}^{(1)}_{\mathrm{WR}}\) from
\(\operatorname{ob}^{(r)}_{\mathrm{WR,coh}}\).

Claim status: conditional proof-ledger criterion.  The firewall itself is
proved as an acceptance criterion for target theorem data; no compact/global
consequence is proved until a concrete target supplies \(C_{\mathrm{tar}}\),
the obstruction complexes, and null-homotopies.

Files changed: `tate-P5-cross-volume.tex`; this report.

Checks run: control-surface grep for `GlobDesc`, `C_{\mathrm{tar}}`,
`Ob_UKD`, Vol III, Igusa/BKM, compact CY, and MNOP; targeted rereads of
`main.tex`, `open-obligations.tex`, and `claim-strength-ledger.tex`;
post-edit greps for stale `Ob_UKD(\mathfrak C_{\mathrm{tar}})` and
Weiss/Ran notation collisions; `git diff --check -- tate-P5-cross-volume.tex`;
`make pdf` completed successfully and wrote `out/main.pdf` with the existing
document-wide box, font-metric, and PDF destination warnings.

Remaining obligations: concrete compact BCOV, Vol III, Igusa/BKM, MNOP, or
sister-volume targets must still construct their own \(C_{\mathrm{tar}}\);
prove weighted-regulator continuity in the chosen topology; kill QME,
convergence, hyperdescent, modular-descent, six-relation, mixed-Dunn, and
KD Maurer-Cartan curvature classes; and provide the actual null-homotopies.
