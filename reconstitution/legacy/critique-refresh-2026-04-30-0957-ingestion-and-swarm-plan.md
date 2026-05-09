# Critique Refresh Ingestion And Swarm Plan, 2026-04-30 09:57 SAST

Source:
`materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf`.

Extracted text:
`materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt`.

Identity:

- PDF creation time: 2026-04-30 09:57:34 SAST.
- Desktop modified time at ingestion: 2026-04-30 10:01:07 SAST.
- Pages: 1426.
- Raw SHA-256:
  `4d2c7af70e52c51faef63177cd1b7e2a0e54ae08d1b42228d3f78746d6640b21`.
- Text SHA-256:
  `5e56a4a3fdb694d7de8bd24dcfe18b1f519b31c2a1b89229259415054fd0ca13`.
- Extracted text size: 106083 lines, 4722716 bytes.

This supersedes the 09:43, 04:11, and earlier critique control surfaces.
All earlier swarm reports remain evidence only.

## Deep Critical Reading

The refreshed critique adds a serious new layer: the local
\(\Omega\)-background should be formulated as a brane-preserving
equivariant localization of the normal bundle
\[
  N_LX=\mathbb R_s\oplus\mathbb C_{z_1}\oplus\mathbb C_{z_2}
\]
of the Dirac brane
\[
  L=\mathbb R_t\times\{s=z_1=z_2=0\}
  \subset
  X=\mathbb R^2_{t,s}\times\mathbb C^2_{z_1,z_2}.
\]
This is not a cosmetic refinement.  It changes what the paper may
honestly claim about reduction, chiral structures, protected traces, and
large \(N\).

The critique is not authority.  It proposes a program.  The swarm must
attack every item below as a proof obligation.

### What now looks structurally right

1. The native six-real-dimensional model remains primary:
   \[
     \mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}.
   \]
   The \(\mathbb C\times\mathbb R\) curve theory is a controlled
   reduction or shadow, not the original geometry.

2. The native holomorphic algebra is a \(\mathbb C^2\) holomorphic
   \(E_2\)-type factorization algebra:
   \[
     C^\bullet_{\mathrm{CE}}
     \bigl(
       \Omega_c^{0,\bullet}(B)\widehat\otimes
       (\mathfrak h\ltimes P[1])
     \bigr).
   \]
   Curve vertex algebras and Zhu algebras only appear after a reduction
   datum has been constructed.

3. The brane line is the fixed stratum for the normal torus
   \[
     T_\Omega=
     \mathbb C^*_{\varepsilon_s}\times
     \mathbb C^*_{\varepsilon_1}\times
     \mathbb C^*_{\varepsilon_2}.
   \]
   The brane-preserving topological action is \(s\mapsto\lambda_s s\),
   \(t\mapsto t\), not a literal rotation in the \((t,s)\)-plane.

4. The local equivariant differential should be written
   \[
     Q_\Omega=Q+\iota_{V_\Omega},
     \qquad
     Q_\Omega^2=L_{V_\Omega}.
   \]
   On invariant fields \(Q_\Omega^2=0\); after inverting nonzero normal
   weights, moving normal modes become acyclic.  This must be proved in
   the actual mixed de Rham/Dolbeault coefficient category.

5. The refined Hamiltonian bracket is strict only on the self-dual
   locus \(\varepsilon_1+\varepsilon_2=0\).  Off that locus it must be
   valued in the inverse symplectic-character line or weighted by
   \[
     [f,g]_\Omega=\hbar_\omega\{f,g\},
     \qquad
     w(\hbar_\omega)=\varepsilon_1+\varepsilon_2.
   \]

6. The equivariant CE/PV map is a natural theorem surface:
   \[
     c_{a,b}\mapsto\theta_{a,b},\qquad
     u_{a,b}\mapsto O_{a,b},
   \]
   with differential coefficients multiplied by \(\hbar_\omega\) in the
   refined bracket convention.

7. The open quantum brane algebra is an equivariant quantum Hamiltonian
   reduction:
   \[
     A^q_{N,\Omega}
     =
     \operatorname{Weyl}_\hbar(\operatorname{Mat}_N^2)//_\hbar GL_N,
     \qquad
     YX-XY+\hbar N I=0,
   \]
   with \(w(X)=\varepsilon_1\), \(w(Y)=\varepsilon_2\), and
   \(w(\hbar)=\varepsilon_1+\varepsilon_2\).

8. The brane should be encoded as a lower stratum in a stratified mixed
   HT factorization algebra on \((X,L)\).  A protected observable should
   be a stratified factorization-homology trace only after the
   brane-defect QME and trace-state normalization are constructed.

### What is dangerous or false if admitted too fast

1. The \(\Omega\)-background does not prove the Costello graph/QME
   theorem.  It gives a grading/localization package and a candidate
   contraction; the equivariant propagator, counterterms, and
   brane-defect QME still need construction.

2. A stratified factorization-homology trace is not produced by analogy
   with any external Chern-Simons model.  The exact source theorem and
   hypotheses must be audited from primary sources before the analogy
   enters the stable core.

3. The full physical large-\(N\) expansion is not implied by stable
   trace invariant theory.  It requires states, topology, cumulants,
   normalizations, convergence, and QME Ward identities.

4. The residue-normalized convention and smooth Euler-localization
   convention cannot both be used silently.  The paper must choose or
   compare them by an explicit normalization theorem.

5. The refined bracket away from
   \(\varepsilon_1+\varepsilon_2=0\) is not the old Hamiltonian Lie
   algebra over scalars.  It is a line-valued or \(\hbar_\omega\)-weighted
   Lie object.

## Platonic Reconstitution Target

The manuscript should be reorganized around the following theorem
surfaces, each of which must survive attack-heal cycles:

1. Dirac brane probe and moment-map action.
2. Hamiltonian BF closed fields, BV pairing, CME.
3. Stable trace theorem and PBW shadow.
4. Matlis principal-part cotangent theorem.
5. Coadjoint action and \(\Psi\)-no-go.
6. Inner CE/PV derived \(P_0\)-centre theorem.
7. Brane-line current factorization theorem.
8. Native holomorphic \(E_2\) / \(\mathbb C^2\) factorization theorem.
9. Moyal principal-part target and Capelli scalar shift.
10. Controlled \(\mathbb C\times\mathbb R\) reduction retaining
    \(z_2\)-coefficients.
11. Reduced Dirac BRST chiral algebra and Zhu bridge.
12. Equivariant normal \(\Omega\)-background datum.
13. Equivariant Hamiltonian/cotangent weights and CE/PV theorem.
14. Equivariant Dirac brane algebra.
15. Brane-locus \(\Omega\)-localized equations.
16. Stratified factorization algebra on \((X,L)\).
17. Stratified factorization-homology trace theorem surface.
18. Costello graph/QME and brane-defect kernel theorem surface.
19. Physical \(\Omega\)-large-\(N\) trace-state theorem surface.
20. Compact/global transfer firewall.

## 216+ Agent Topology

Launch six at a time.  The first 216 agents are twenty lanes with
roughly ten or eleven agents each; the controller may extend beyond 216
for repeated failed or undecided theorem surfaces.

1. Native geometry and BV field complex.
2. Dirac brane probe and moment-map signs.
3. Hamiltonian algebra, scalar quotient, and scalar anomaly.
4. Matlis principal parts and coadjoint action.
5. \(\Psi\)-descendant no-go and PBW shadow.
6. CE/PV derived-centre theorem.
7. Brane-line currents and compactly supported de Rham source.
8. Native holomorphic \(E_2\) / Bochner-Martinelli kernel.
9. Controlled \(\mathbb C\times\mathbb R\) reduction.
10. Reduced Dirac BRST chiral algebra.
11. Zhu/Hochschild/HKR/CE-PV bridge.
12. Moyal coefficients and Capelli/Weyl normalization.
13. Radial all-\(N\) trace homotopies.
14. Weighted Tate and kernel convergence.
15. Costello graph/QME finite-window rows and counterterms.
16. Normal \(\Omega\)-background weights and \(Q_\Omega\).
17. Equivariant CE/PV, refined bracket, and line-valued algebra.
18. Stratified factorization algebra and brane module.
19. Stratified factorization-homology trace and physical large \(N\).
20. Manuscript theorem package, abstract, introduction, and firewall.

Each agent must:

- read `CLAUDE.md`, `AGENTS.md`, the attack-heal protocol, this file,
  and its owned manuscript files;
- use `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
  before writing manuscript-proper text;
- treat the critique as an attack surface, not as authority;
- use Deep Supremum Discipline: always take the harder route; never
  downgrade a theorem as a convenience move; first construct the missing
  object, map, habitat, topology, homotopy, kernel, counterterm,
  computation, source theorem with verified hypotheses, or obstruction
  class; only then, if blocked, record the exact obstruction;
- edit only owned files in its forked workspace;
- return a report with claim attacked, verdict, proof/failure, anchors,
  exact formulas, files changed, checks, and remaining obligations.

## First Six Launch Slots

174. Frontmatter/abstract theorem package.  Owns `abstract.tex`.

175. Native geometry/Dirac-brane introduction architecture.  Owns
`main.tex` introduction and local-model theorem-package region.

176. Native holomorphic \(E_2\) and Bochner-Martinelli factorization
theorem lane.  Owns `theorem-lanes.tex`.

177. Normal \(\Omega\)-background theorem surface.  Owns
`local-dictionary.tex` and a report; proposes a future manuscript include
if a new section is needed.

178. Stratified factorization and physical trace-state obligations.
Owns `open-obligations.tex`.

179. Costello graph/QME equivariant brane-defect kernel attack.  Owns
`appendix-unreduced-bv-qme.tex`.
