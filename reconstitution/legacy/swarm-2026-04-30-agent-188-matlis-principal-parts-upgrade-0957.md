# Agent 188 Matlis Principal-Parts Upgrade, 2026-04-30 09:57

Owned files:

- `appendix-matlis-principal-parts.tex`
- `reconstitution/swarm-2026-04-30-agent-188-matlis-principal-parts-upgrade-0957.md`

Read-only anchors:

- `CLAUDE.md`
- `AGENTS.md`
- `reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md`
- `local-dictionary.tex`
- `main.tex`
- `theorem-lanes.tex`
- `references/primary-sources/matlis-local-cohomology-residue-anchor.md`

## Stable Core

The Matlis/principal-part theorem surface is stable after the local
repairs below.

For \(R=\mathbb C[[z_1,z_2]]\), \(\mathfrak m=(z_1,z_2)\), and
\(\mathfrak h=R/\mathbb C\cdot1\),
\[
  \mathfrak h^\vee_{\mathrm{cont}}
  =
  \bigoplus_{\substack{a,b\ge0\\a+b>0}}\mathbb C\,\delta_{a,b}
  \cong
  \mathcal P
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  =
  \bigoplus_{\substack{a,b\ge0\\a+b>0}}\mathbb C\,\rho_{a,b},
\]
with
\[
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1dz_2,\qquad
  \operatorname{Res}_0(\rho_{a,b}z_1^mz_2^n)=\delta_{a,m}\delta_{b,n}.
\]

The coadjoint action is
\[
  z_1^p z_2^q\cdot\rho_{a,b}
  =
  -(pb-qa+p-q)\rho_{a-p+1,b-q+1},
\]
with negative-index targets zero.  If the target is \(\rho_{0,0}\), then
\(a=p-1\), \(b=q-1\), and \(pb-qa+p-q=0\), so the excluded scalar residue
line is not produced.

## Attacks And Repairs

### A188-1: scalar residue line

Target: `appendix-matlis-principal-parts.tex`, Matlis definition and
realization proposition.

Attack: The prior text excluded \(\rho_{0,0}\) but did not explicitly say
that it is nonzero in \(H^2_{\mathfrak m}(R)\,dz_1dz_2\), evaluates the
constant coefficient, and is removed because the dual is the dual of
\(R/\mathbb C\cdot1\).

Repair: Added the scalar-line statement and the finite-stage continuity
check.  The reduced module is now explicitly the scalar-annihilator
hyperplane, not an \(R\)-submodule and not a quotient by a stable scalar
line.

### A188-2: coadjoint action derivation

Target: `appendix-matlis-principal-parts.tex`,
Proposition `prop:app-matlis-coadjoint-action`.

Attack: The formula was correct, but the proof compressed the residue
integration-by-parts mechanism and did not explicitly verify scalar
stability.

Repair: Inserted the Lie-derivative identity
\[
  0=\operatorname{Res}\bigl(L_{X_f}(\phi g\,dz_1dz_2)\bigr)
  =\operatorname{Res}\bigl((\{f,\phi\}g+\phi\{f,g\})\,dz_1dz_2\bigr),
\]
using \(\operatorname{div}_{dz_1dz_2}X_f=0\).  This gives
\[
  \langle \{f,\rho\},g\rangle=-\langle\rho,\{f,g\}\rangle.
\]
The monomial coefficient was recomputed as
\[
  q(a+1)-p(b+1)=-(pb-qa+p-q).
\]

### A188-3: continuity/topology

Target: `appendix-matlis-principal-parts.tex`, new Lemma
`lem:app-matlis-coadjoint-continuity`.

Attack: The completed Hamiltonian algebra \(\mathbb C[[z_1,z_2]]/\mathbb C\)
could act ill-definedly on a direct-sum principal-part module unless each
principal part sees only a finite jet.

Repair: Added the finite-jet argument.  For fixed \(\rho_{a,b}\), a monomial
\(z_1^pz_2^q\) can contribute only when \(p\le a+1\), \(q\le b+1\).  For
\(a+b\le N\), the nonzero target has total index at most \(N+1\).  Hence
the action extends to the completed \(\mathfrak h\) and is continuous for
the locally finite direct-sum topology.

### A188-4: uniqueness up to scalar

Target: `appendix-matlis-principal-parts.tex`,
Theorem `thm:app-matlis-residue-rigidity`.

Attack: The earlier total-degree-zero coefficient proof was plausible but
not the strongest true theorem.  It also made nondegeneracy carry more
topological force than it should in an infinite-dimensional pairing.

Repair: Replaced it by a perfect-pairing theorem.  A perfect continuous
equivariant pairing is one whose adjoint
\(\mathcal P\to\mathfrak h^\vee_{\mathrm{cont}}\) is a topological
isomorphism.  The centralizer lemma proves that every
\(\mathfrak h\)-module endomorphism of \(\mathcal P\) is scalar:
\(\rho_{1,0}\) is cyclic; \(z_1z_2\) forces \(T\rho_{1,0}\) into
\(\bigoplus_{r\ge0}\mathbb C\rho_{r+1,r}\); \(z_2^2\rho_{1,0}=0\) kills all
\(r\ge1\) coefficients because
\[
  z_2^2\cdot\rho_{r+1,r}=(2r+4)\rho_{r+2,r-1}.
\]
Thus the residue pairing is unique up to one nonzero scalar; the
Kronecker residue normalization fixes it.

### A188-5: \(\Psi\)-no-go boundary

Target: `appendix-matlis-principal-parts.tex`,
Theorem `thm:app-matlis-polynomial-descendant-obstruction`.

Attack: The no-go theorem stated local nilpotence, but the boundary
contradiction for the actual primitive PBW labels was not visible inside
the appendix.

Repair: Added the boundary check:
\[
  z_1\cdot\widetilde\Psi_{a,b}=b\,\widetilde\Psi_{a,b-1},
  \qquad
  z_2\cdot\widetilde\Psi_{a,b}=-a\,\widetilde\Psi_{a-1,b},
\]
so \(z_1\widetilde\Psi_{a,0}=0\), while
\[
  z_1\cdot\rho_{a,0}=-\rho_{a,1}\ne0.
\]
No bidegree-preserving nonzero rescaling
\(\widetilde\Psi_{a,b}\mapsto\lambda_{a,b}\rho_{a,b}\) can be an
\(\mathfrak h\)-module map.

## Checks

- Formula check by finite script for \(0\le p,q,a,b\le6\), excluding
  scalar Hamiltonian and scalar principal part:
  `formula_failures 0`, `scalar_target_failures 0`, `cases_checked 2304`.
- Local source anchor checked:
  `references/primary-sources/matlis-local-cohomology-residue-anchor.md`
  records \(H^2_{\mathfrak m}(R)\), the Cech negative-Laurent basis, the
  scalar-annihilator \(\mathcal P\), and the Matlis/Hartshorne/Kunz source
  anchors.
- Temporary compile, without touching repository build artifacts:
  `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/ts-agent-188 main.tex`.
  Result: exit code 0, PDF written to `/tmp/ts-agent-188/main.pdf`.
  The run reports many pre-existing undefined-reference warnings from the
  concurrently edited manuscript surface.

## Residuals

- The appendix now proves the classical Matlis/coadjoint theorem surface.
  It does not construct a same-action polynomial \(\Psi\)-module bridge;
  the no-go theorem rules that out.
- The Fourier--Rees bridge remains only a Fourier-conjugated
  \(\mathcal D_\hbar\)-module label bridge.  It is not a same-action
  \(\mathfrak h\)-module identification before or after inverting
  \(\hbar\).
