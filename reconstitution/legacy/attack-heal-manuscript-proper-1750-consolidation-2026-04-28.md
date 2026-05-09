# Manuscript-Proper Attack-Heal Consolidation — 2026-04-28 17:50 Critique

## Verdict

The manuscript proper has a nonempty stable core, but it is not yet in
reader-safe form. The stable core is the reduced formal local algebra:

- Dirac/Koszul brane probe in the ghost-zero finite algebraic model.
- CE/PV generator dictionary for the reduced Hamiltonian cotangent Lie
  algebra, as a direct cochain calculation.
- Stable PBW trace sector and selected one-\(\psi\) primitive shadow.
- Matlis residue-current realization of the continuous cotangent module,
  after quotienting constants.
- Reduced defect-current bracket and scalar anomaly.
- Formal Weyl/Moyal coefficient algebra and raw odd star-commutator
  formula.
- Cross-volume no-transfer firewall, modulo a convention wording repair.

The paper still exposes stronger claims than this core supports. Those
claims must be repaired in `main.tex` and the included TeX fragments
before the manuscript can be treated as reconstituted.

## Agents

| ID | Agent | Scope | Result |
|---|---|---|---|
| M01 | Herschel | CE/PV/factorization | valid structural attacks |
| M02 | Averroes | Koszul/Matlis/Rees | valid structural attacks |
| M03 | Wegener | Moyal/radial | valid coefficient and hypothesis attacks |
| M04 | Ptolemy | Costello/QME/graphs | valid analytic/QME attacks |
| M05 | Avicenna | frontmatter/status | valid reader-contract attacks |
| M06 | Bernoulli | appendices/scripts/cross-volume | valid consistency attacks |

All agents were read-only/proposal-only. No manuscript file was edited by
the agents.

## Destroyed Claims

### D1. Full `Z^{P_0}_{fact}` Theorem

Status: destroyed as stated in reader-visible and theorem-lane surfaces.

Evidence anchors:

- `main.tex:2014-2019`
- `main.tex:2343-2348`
- `main.tex:2427-2435`
- `theorem-lanes.tex:115-125`

Failure:

The active text promotes reduced PV/Hamiltonian central operations to
`Z^{P_0}_{fact}`. The actual proved object is a reduced CE/PV model.
The full unreduced factorization-center theorem still needs a target
category, centrality homotopies, factorization products, and continuous
HKR/factorization-center descent.

Minimal heal:

Define a reduced notation, for example
`Z^{P_0}_{red}(A):=\mathrm{PV}_{red}(A)`, and use it for the local
Hamiltonian/PV comparison. Reserve `Z^{P_0}_{fact}` for the unreduced
problem statement.

### D2. Continuous Tate HKR / Factorization-Center Descent

Status: unsupported as a theorem.

Evidence anchors:

- `main.tex:2050-2067`
- `main.tex:2127-2137`
- `main.tex:2193-2209`

Failure:

The proof applies HKR to a completed free graded-commutative Tate algebra
without proving finite-window passage, topology, antisymmetrization,
transition compatibility, or `lim^1` control.

Minimal heal:

Either insert a continuous Tate HKR theorem with all hypotheses, or state
only the explicit reduced CE/PV cochain calculation and finite-window or
nilpotent cases where the argument is actually proved.

### D3. Full Conilpotent Koszul Duality for the Formal Hamiltonian Algebra

Status: destroyed as stated.

Evidence anchors:

- `main.tex:3323-3340`
- `main.tex:3428-3433`
- `main.tex:3481-3528`
- `tate-T2-nilpotent-truncation.tex:484-499`

Failure:

`prop:ce-koszul` applies the bar-cobar lemma to the full
\(\mathfrak h=\prod_{d\geq1}H_d\), but the lemma assumes
Tate-conilpotence. The manuscript itself says the full formal
Hamiltonian algebra with linear modes is not asserted conilpotent.

Minimal heal:

Restrict the proposition to nilpotent/admissible replacements, for
example \(\mathfrak m^3\) truncations, finite nilpotent windows, or a
weighted envelope. Keep full \(\mathfrak h\) CE/PV as a direct cochain
calculation, not as a bar-cobar Koszul theorem.

### D4. Compact-Support Factorization Current Local Constancy

Status: unsupported until the compact-support contraction is written.

Evidence anchors:

- `main.tex:2174-2180`
- `main.tex:2788-2801`
- `tate-T5-chain-level-primitive.tex:780-787`

Failure:

The text treats \(\Omega_c^\bullet(I)\) as if it contracts to
degree-zero point values. For an open interval, compactly supported de
Rham cohomology is top-degree before a shift/density convention is
specified.

Minimal heal:

Insert the Algorithm 7 contraction: choose a compactly supported density
\(\lambda_I\) of integral one, define \(p,i,K\), prove
\(dK+Kd=\mathrm{id}-ip\), and propagate the shift/orientation signs to
the CE current variables.

### D5. Matlis `Ann(C·1)` Wording

Status: notation leak; mathematics survives after repair.

Evidence anchors:

- `abstract.tex:15-20`
- `claim-strength-ledger.tex:48-52`
- `local-dictionary.tex:143-147`
- `theorem-lanes.tex:164-174`
- `main.tex:4212-4222`
- `appendix-matlis-principal-parts.tex:107-120`

Failure:

Front-facing text uses bare `Ann(C\cdot1)` and even "annihilator
submodule" language, while the body correctly says the object is not an
\(R\)-submodule and not the literal Matlis dual of \(R/\C\cdot1\).

Minimal heal:

Introduce `\operatorname{Ann}_{res}(\C\cdot1)` as the
\(\C\)-linear residue annihilator of constants, and replace all bare
front-facing uses. Say explicitly: Hamiltonian-invariant
\(\C\)-linear residue-current subspace, not an \(R\)-submodule.

### D6. Normalized Moyal `\hbar^2` Claim

Status: false.

Evidence anchors:

- `main.tex:5011-5038`
- `main.tex:5041-5056`
- `main.tex:5410-5417`

Failure:

The raw commutator has only odd powers of \(\hbar\), but the normalized
bracket \(\hbar^{-1}[f,g]_*\) has even powers. The \(s=1\) term is
\[
  \frac{\hbar^2}{24}P^3(f,g),
\]
which is generally nonzero. The displayed example
\([z_1^3z_2,z_1z_2^3]_*=8\hbar z_1^3z_2^3-3\hbar^3z_1z_2+\cdots\)
already gives a normalized \(-3\hbar^2z_1z_2\) term.

Minimal heal:

Replace "no \(\hbar^2\) correction" by:

\[
  \{f,g\}_\hbar
  =P(f,g)+\frac{\hbar^2}{24}P^3(f,g)
   +\frac{\hbar^4}{1920}P^5(f,g)+\cdots .
\]

Even powers vanish only in the raw commutator, not in the normalized
bracket.

### D7. Unconditional All-Order Degree-Zero Quantum Comparison

Status: hypothesis drop.

Evidence anchors:

- `main.tex:4903-4923`
- `main.tex:5459-5497`
- `theorem-lanes.tex:344-350`
- `appendix-radial-parts-moyal.tex:145-182`

Failure:

`thm:phi-hbar-all-order` is stated as a theorem, but its proof uses
`thm:finite-n-reduced-moyal`, which is conditional on the external
radial-parts input.

Minimal heal:

Either add the same external radial-parts hypothesis to
`thm:phi-hbar-all-order`, or split it into:

- unconditional formal Moyal coefficient theorem;
- conditional finite-\(N\)/stable trace realization.

### D8. Costello Graph Theorem from Reduced Wick/Moyal Diagrams

Status: destroyed as a proved Costello theorem; survives as reduced
Wick/Moyal coefficient computation.

Evidence anchors:

- `abstract.tex:34-36`
- `claim-strength-ledger.tex:103-106`
- `main.tex:5648-5655`
- `main.tex:5772-5778`
- `main.tex:5780-5803`
- `main.tex:5842-5875`

Failure:

The proof-bearing blocks compute reduced open-line Weyl/Moyal/Wick
coefficients. The manuscript itself says this is not a Costello
closed-open graph theorem and lists the missing elliptic parent,
brane-defect propagator, counterterms, anomaly, QME, and compatibility
data.

Minimal heal:

Rename front-facing claims to "first and third reduced Wick/Moyal
boundary coefficients computed." Reserve "Costello graph normalization"
for the conditional theorem/problem after the analytic specialization is
constructed.

### D9. QME Escape-Route Classification

Status: unsupported as exhaustive.

Evidence anchors:

- `principles.tex:131-154`
- `open-obligations.tex:123-151`
- `appendix-unreduced-bv-qme.tex:93-178`

Failure:

The scalar anomaly class is proved, but the text uses "must either"
language before computing the obstruction complex and its \(H^1\). The
listed mechanisms are candidate exits, not a classification.

Minimal heal:

Replace exhaustive phrasing by "known candidate mechanisms include".
Add or strengthen a problem requiring computation of the brane-defect
obstruction complex and proof that any proposed mechanisms are
exhaustive.

## Additional Valid Repairs

1. Script count: `main.tex:4981-4984` says 36 direct \(N=2\) radial
   pairs. The script and appendix support 80 pairs in each of ranks
   \(N=2\) and \(N=3\).
2. Script coverage: `scripts/check_moyal_coefficients.py` checks the
   connected cumulant projection only at leading \(P^1\) order; higher
   Moyal coefficients are checked separately as scalar monomial
   coefficients.
3. Rees/Fourier bridge: `abstract.tex:38-41` says no bridge is asserted,
   but the appendix constructs a limited label bridge. The forbidden
   object is a same-action/deformation-level module bridge.
4. Weighted regulator wording: `abstract.tex:32-34` should distinguish
   proved admissible finite-window weight independence from the
   unproved strict unweighted endpoint/equivalence.
5. Cross-volume firewall convention: `main.tex:5896-5900` and
   `tate-P5-cross-volume.tex:11-16` say \(\R\times\widehat{\C^2}_0\);
   the bulk local model elsewhere is
   \(\R^2_{\mathrm{top}}\times\widehat{\C^2}_0\) with brane line
   \(\R\times0\).
6. Figure-source hygiene: active figures are inline TikZ; the named SVG
   assets are unlabeled and unused by `main.tex`.
7. Claim-strength ledger vocabulary: `claim-strength-ledger.tex` uses
   an undeclared hybrid status, "partly constructed / open unreduced
   lift."
8. Reader-visible route codes: R0-R3/R1/R2/T4 process labels appear in
   rendered TeX surfaces and should be replaced by descriptive
   mathematical names.

## Invalid Or Non-Core Attacks

The formal Moyal convention and raw monomial coefficient formula survive:

\[
  f*g=m\exp(\hbar P/2)(f\otimes g),\qquad
  [f,g]_*=\sum_{r\ge1,\ r\ \mathrm{odd}}
    \frac{2}{2^r r!}\hbar^rP^r(f,g).
\]

The primitive one-\(\psi\) theorem also survives as a selected
one-\(\psi\) PBW/indecomposable statement. The full all-\(\psi\)
primitive homology is already stated as a problem, not as a theorem.

## First Repair Queue

1. Patch frontmatter and title/abstract claim strength:
   reduced CE/PV center, not full open factorization center.
2. Introduce `Z^{P_0}_{red}` or equivalent reduced notation and reserve
   `Z^{P_0}_{fact}` for the unreduced problem.
3. Restrict `prop:ce-koszul` to conilpotent/admissible replacements and
   add a Koszul Layers 0-7 status table in manuscript proper.
4. Insert or demote the compact-support current contraction.
5. Replace bare `Ann(C\cdot1)` by `Ann_res(C\cdot1)` and repair
   "submodule" language.
6. Correct normalized Moyal \(\hbar^2\) prose and examples.
7. Add the radial-parts hypothesis to every theorem using
   `thm:finite-n-reduced-moyal`, or split formal and trace-realization
   results.
8. Rename Costello claims to reduced Wick/Moyal coefficient claims;
   keep Costello graph realization conditional.
9. Replace QME classification phrasing by candidate-mechanism phrasing.
10. Repair script-count, script-coverage, weighted-regulator,
    cross-volume, route-code, and figure-source hygiene.

## Convergence Status

Not converged. All six agents returned and were closed. Severity 1-3
attacks remain valid inside the manuscript-proper stable-core closure.
The next attack-heal cycle should be a TeX repair wave with isolated
write scopes, followed by a referee pass against this consolidation.
