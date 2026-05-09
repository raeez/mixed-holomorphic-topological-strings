# Swarm Report: Agent 182, Reduced Dirac BRST/Zhu

Date: 2026-04-30.
Owned files:

- `reconstitution/reduced-dirac-brst-zhu-thread-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-182-reduced-dirac-brst-zhu-0957.md`

No manuscript/theorem files were edited.

## Claim Attacked

Construct a reduced curve Dirac BRST/Zhu theorem surface compatible with
the local mixed
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\)
manuscript, without falsely replacing the native holomorphic
\(E_2\)/factorization algebra on \(\mathbb C^2\) by a curve vertex
algebra.

## Evidence Read

- `CLAUDE.md`, `AGENTS.md`.
- Attack-heal protocol:
  `/Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md`
  and `references/protocol.md`.
- Manuscript anchors:
  `main.tex:80-184`, `main.tex:588-635`,
  `main.tex:1078-1228`, `main.tex:1626-1797`,
  `main.tex:3434-3508`, `main.tex:5908-5975`,
  `main.tex:6383-6575`, `main.tex:6663-6716`,
  `main.tex:7350-7476`.
- Theorem/local-dictionary anchors:
  `theorem-lanes.tex:381-674`,
  `theorem-lanes.tex:1000-1136`,
  `theorem-lanes.tex:1931-2005`,
  `local-dictionary.tex:170-375`,
  `claim-strength-ledger.tex:335-350`,
  `abstract.tex:184-189`.
- Swarm/context files:
  `reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md`,
  `reconstitution/chiral-algebra-construction-thread-2026-04-30.md`,
  `reconstitution/local-theorem-obligations-2026-04-30.md`,
  `reconstitution/critique-refresh-2026-04-30-0943-ingestion.md`,
  and relevant processed critique excerpts.
- Vol II bridge anchors:
  `~/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:394-445`,
  `:620-650`, `:674-785`;
  `~/chiral-bar-cobar-vol2/chapters/connections/concordance.tex`.

## Verdict

The theorem surface is repairable, but only as a reduced
\(\mathbb C\times\mathbb R\) curve theorem.  It is false as a native
\(\mathbb C^2\) theorem.  The stable formulation requires an explicit
reduction package, retained \(z_2\)-coefficient/principal-part data,
Dirac BRST fields and OPEs, a Jacobi proof of \(Q_{\mathrm{BRST}}^2=0\),
a Zhu zero-mode calculation with the Capelli shift, and a conditional
Hochschild/HKR/CE-PV comparison chain.

## Constructed Surface

Controlled reduction datum:
\[
  \mathcal R_{\mathbb C\times\mathbb R}
  =
  (\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},
    B_{z_2},\pi_!,L_{\mathrm{red}},
    \langle-,-\rangle_{\mathrm{red}},
    \{-,-\}_{\mathrm{red}},H_{\mathrm{anom}}).
\]
The theorem must retain \(z_2\)-coefficients or principal parts; setting
\(z_2=0\) kills the Hamiltonian bracket.

Free reduced Dirac vertex algebra:
\[
  Z_1{}^i{}_j(z),\quad Z_2{}^i{}_j(z)
  \quad\text{even},\qquad
  c^i{}_j(z), b^i{}_j(z)
  \quad\text{odd}.
\]
Singular OPEs:
\[
  Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
  \sim
  \frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
  \qquad
  b^i{}_j(z)c^k{}_\ell(w)
  \sim
  \frac{\delta^i_\ell\delta^k_j}{z-w}.
\]
All other generating singular OPEs are regular.

BRST current:
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]),
  \qquad
  Q_{\mathrm{BRST}}=\operatorname{Res}j_{\mathrm{BRST}}(z)\,dz.
\]
Differential:
\[
  QZ_a=[c,Z_a],\quad Qc=\frac12[c,c],\quad
  Qb=[Z_1,Z_2]+[b,c].
\]
The reduced chiral algebra is
\[
  \mathcal A_{\partial,N}^{\mathrm{Dir\text{-}ch}}
  =
  H^\bullet(V_N^{\mathrm{Dir}},Q_{\mathrm{BRST}}).
\]

Square-zero proof:
\[
  Q[Z_1,Z_2]=[c,[Z_1,Z_2]]
\]
by moment-map equivariance.  Then
\[
  Q^2Z_a=
  \frac12[[c,c],Z_a]-[c,[c,Z_a]]=0,
  \qquad Q^2c=0,
\]
and
\[
  Q^2b=[c,\mu]+[\mu,c]+[[b,c],c]
  -\frac12[b,[c,c]]=0
\]
by graded Jacobi.

Zero-mode/Koszul recovery:
\[
  \phi_a=Z_{a,0},\qquad \psi=b_0,
\]
and after gauge-invariant Koszul reduction,
\[
  Q\phi_1=Q\phi_2=0,\qquad Q\psi=[\phi_1,\phi_2],
\]
matching `main.tex:118-144`.

Zhu weights:
\[
  \operatorname{wt}(Z_1)=0,\quad
  \operatorname{wt}(Z_2)=1,\quad
  \operatorname{wt}(c)=0,\quad
  \operatorname{wt}(b)=1.
\]
With
\[
  X^j{}_i=o(Z_1{}^i{}_j),\quad
  Y^j{}_i=o(Z_2{}^i{}_j),\quad
  C^j{}_i=o(c^i{}_j),\quad
  B^j{}_i=o(b^i{}_j),
\]
the Zhu relations are
\[
  [Y^j{}_i,X^\ell{}_k]=
  \hbar\,\delta^\ell_i\delta^j_k,\qquad
  [B^j{}_i,C^\ell{}_k]_{\mathrm{super}}=
  \delta^\ell_i\delta^j_k.
\]
The pre-BRST Zhu algebra is
\[
  W_\hbar(\operatorname{Mat}_N^2)
  \otimes
  \operatorname{Cliff}_{bc}(\mathfrak{gl}_N).
\]
The Zhu BRST differential is
\[
  QX=[C,X],\quad QY=[C,Y],\quad QC=\frac12[C,C],
\]
\[
  QB=YX-XY+\hbar N I+[B,C].
\]
Thus the degree-zero Zhu cohomology is the BRST quantum Hamiltonian
reduction with moment relation
\[
  YX-XY+\hbar N I=0,
\]
matching the normal-ordering/Capelli computation in `main.tex:6518-6538`.

Comparison chain:
\[
  \operatorname{ChirHoch}^\bullet(V_N^{\mathrm{Dir}})
  \to HH^\bullet(A(V_N^{\mathrm{Dir}}))
  \to_{\operatorname{gr}_{\hbar=0},\,N\to\infty}
  HH^\bullet(A_{\mathrm{cl,st}})
  \to_{\mathrm{HKR}}
  PV^\bullet(\widehat S(\mathfrak h_{\mathrm{red}}))
  \to
  C_{\mathrm{CE}}^\bullet(\mathfrak h_{\mathrm{red}}\ltimes P[1]).
\]
This is a chain of conditional comparison maps, not a finite-\(N\),
finite-\(\hbar\) quasi-isomorphism.

## Attack Ledger

`A182-01`: False native Zhu transfer.
Failure mode: a curve VOA/Zhu algebra cannot be the native object on
\(\mathbb C^2\).
Status: healed by making the theorem conditional on
\(\mathcal R_{\mathbb C\times\mathbb R}\) and labelling every curve
object reduced.

`A182-02`: Transverse mode erased.
Failure mode: reducing by setting \(z_2=0\) kills the Hamiltonian
bracket.
Status: healed by requiring retained \(z_2\)-coefficients or
principal-part data \(B_{z_2}\).

`A182-03`: BRST nilpotence asserted but not proved.
Failure mode: \(Q_{\mathrm{BRST}}^2=0\) could fail through the moment
map or ghost signs.
Status: healed by the explicit equivariance/Jacobi computation above.

`A182-04`: Zhu relation sign and Capelli shift.
Failure mode: omitting the transpose convention or the
\(\hbar N I\) shift contradicts the manuscript's Weyl reduction.
Status: healed by using \([Y,X]=\hbar\) in the stated index convention
and \(QB=YX-XY+\hbar N I+[B,C]\).

`A182-05`: Hochschild comparison overclaimed.
Failure mode: chiral Hochschild, Hochschild of Zhu, HKR, and CE/PV are
not automatically quasi-isomorphic.
Status: healed by stating exact hypotheses: Vol II supplies the Zhu
bridge map; HKR is associated-graded, stable, completed, and classical;
CE/PV requires the manuscript's admissible reduced Hamiltonian
completion.

## Manuscript Edits Needed

1. Insert a controlled-reduction theorem before the curve chiral/Zhu
   theorem surface.  It must define the reduction package, retained
   \(z_2\) system, brane image, bracket, pairing, and anomaly homotopy.

2. Add the reduced Dirac BRST vertex algebra definition: fields, OPEs,
   BRST current, differential, and square-zero proof.

3. Add a zero-mode comparison lemma recovering the Dirac Koszul complex
   from `main.tex:118-144`.

4. Add a Zhu theorem with weights, zero-mode convention,
   \([Y,X]=\hbar\), and BRST quantum Hamiltonian reduction with
   \(YX-XY+\hbar N I\).

5. Add a conditional Hochschild/HKR/CE-PV comparison proposition.  Do
   not assert a Vol II-style quasi-isomorphism unless the necessary
   rationality/\(C_2\)-cofiniteness or replacement hypotheses are proved
   for this reduced BRST algebra.

## Residual Open Obligations

- Actually construct
  \(\mathcal R_{\mathbb C\times\mathbb R}\) from the mixed local model.
- Verify the residue normalization of the OPE coefficient \(\hbar\).
- Prove the conformal vector and weights from the pushed-forward fields.
- Check the one-dimensional normal-ordering computation that gives
  \(\hbar N I\), or explicitly identify it with the finite-dimensional
  Weyl computation in the manuscript.
- Prove continuous HKR for the completed stable algebra used in the
  comparison chain.
- Match the reduced BRST anomaly to the manuscript's BV/QME anomaly lane.

## Verification

Verification and staging run:

- `git diff --check -- reconstitution/reduced-dirac-brst-zhu-thread-2026-04-30.md reconstitution/swarm-2026-04-30-agent-182-reduced-dirac-brst-zhu-0957.md`
- targeted `rg` for the BRST, Zhu, Capelli, and comparison-chain
  formulas in the two owned files.
- targeted attribution-marker scan in the two owned files.
- `git add` for the two owned files only.

No TeX build is needed because no TeX source was edited.
