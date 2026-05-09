# Master Ledger Integration Audit: Supremum Targets

Date: 2026-04-30.
Agent: 242.
Scope: report-only audit after agents 228-241.
Ownership: this file and `reconstitution/swarm-2026-04-30-agent-242-master-ledger-integration-audit-supremum-targets.md`.

No TeX, script, bibliography, or figure file was edited.

## Protocol

Used the `~/ecosystem` attack-heal discipline and the Vol II
`chriss-ginzburg-rectify` rule: a loose conditional/external/expected theorem
surface should be upgraded to either a precise theorem target or an exact
obstruction theorem. The audit focused on:

- `claim-strength-ledger.tex`
- `open-obligations.tex`
- `local-dictionary.tex`
- `theorem-lanes.tex`
- `main.tex`

## Priority Integration Checklist

### P0-1. Ordinary scalar closed-exchange branch: Agent 241 not propagated

Anchors:

- `main.tex:7569-7624`: scalar QME theorem still says branch statements are
  "proved, or conditional in the exact sense stated".
- `main.tex:8022-8194`: closed-exchange triple is stated for the non-scalar
  branch, not the ordinary scalar-reduced branch.
- `claim-strength-ledger.tex:399-405`: same-branch closed exchange is named
  only by the leading class condition.
- `claim-strength-ledger.tex:1148-1161`: scalar class and non-scalar kernel
  obligations are recorded, but the scalar finite-window obstruction sequence
  is absent.
- `open-obligations.tex:501-585`: closed-exchange criterion is non-scalar;
  scalar-contact projection gate and scalar cokernel sequence are absent.

Attack:

The current surfaces can still be read as: once a closed-exchange term with
leading class `-\hbar N[\bar c]` is named, the scalar branch is conditionally
repaired. Agent 241 shows the sharper surface: the scalar-contact projection
gate comes first, and a same-branch repair requires finite-window scalar
cochain maps whose image contains the opposite class.

Proposed replacement wording:

```tex
In the ordinary scalar-reduced branch the first obstruction is the
scalar-contact lift class
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar N[\bar c_M]\ne0 .
\]
A same-branch closed-exchange theorem requires a finite-window scalar-contact
chain projection, a complex \(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)\), and
cochain maps \(\Xi_M^{\mathrm{sc}}\) whose scalar image contains
\(-\hbar N[\bar c_M]\). The exact obstruction sequence is
\[
  (o_{\sigma,M}^{(1),\mathrm{sc}},
   \beta_M^{\mathrm{sc}},
   \beta_{\mathrm{cl}}^{\mathrm{sc}},
   \mu_{\mathrm{cl}}^{\mathrm{sc}},
   \lambda_C^{\mathrm{sc}}).
\]
The one-dimensional algebraic cone with generator \(e_M\) is an accepted
defect-supported central-contact source replacement; it is not a
Costello-local closed-exchange theorem until the generator is replaced by a
closed bulk field, brane restriction, source-face computation, locality
rule, and compatible counterterm tower.
```

Priority reason:

This is the clearest remaining "conditional" surface after Agent 241. It
directly controls the ordinary scalar QME branch.

### P0-2. First \(\theta_3\) row: Agent 240 only partly propagated

Anchors:

- `claim-strength-ledger.tex:417-432`: already reflects Agent 240's finite
  two-`u` obstruction and failed eight-face row.
- `main.tex:8233-8346`: still gives the generic three acceptance routes, not
  the new finite two-`u` no-ancestor theorem or eight-face residual.
- `open-obligations.tex:587-630`: still lists the source ancestor, local
  counterterm, and companion-face alternatives generically.
- `theorem-lanes.tex:3215-3232`: records only the one-row obstruction and
  says larger complexes may repair it.

Attack:

The main/open/theorem-lane surfaces still leave the first source-ancestor and
companion-face routes as open unnamed alternatives. Agent 240 has already
attacked two concrete routes and produced exact finite obstructions.

Proposed replacement wording:

```tex
The present one-row complex has
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad d=0.
\]
In the tested two-\(u\), Hamiltonian-degree-\(\le3\) CE source envelope, the
left-cokernel functional
\[
  q=-\frac12e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
    +e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
```

with the ordered-variant correction

```tex
  +\frac13 e^*_{((H_{0,1},H_{0,2}),c_{\rho_{0,3}})}
```

should be inserted where ordered rows are used, together with
`q d_{\mathrm{CE}}=0` and `q(\nu_3)=1`. Hence no pure CE ancestor exists in
that finite envelope. The tested eight-face candidate has residual

```tex
  R^{\mathrm{cand}}_{\Theta_3,M}
  =
  2E_{\nu02}-2E_{\nu20}+3E_{\nu03}
  +2E_{\nu12}^{(1)}-E_{\nu12}^{(2)}
  +E_{\theta3}-2E_{\nu21}^{(2)}-3E_{\nu30},
```

and diagonal transport leaves

```tex
  \pi_{M,2}R^{\mathrm{cand}}_{\Theta_3,M}
  =
  2E^2_{\nu02}-2E^2_{\nu20}.
```

Acceptance now requires a new degree-zero local primitive, a larger marked
CE-source table with the listed marked Costello rows, or a new companion-face
table with zero signed residual, codimension-two closure, compatible
truncation matrices, and zero Roos class.

Priority reason:

The claim ledger is ahead of the manuscript. The exact obstruction should be
propagated to avoid spending further proof budget on already-failed finite
routes.

### P0-3. Costello first/third graph realization: Agent 229 exact tuple absent

Anchors:

- `claim-strength-ledger.tex:391-397`: says only "local anomaly/normalization
  obstruction theorem".
- `main.tex:8522-8772`: still frames the first/third graph problem as a
  conditional test plus checklist.
- `main.tex:8653-8719`: theorem title remains "Conditional first/third
  normalization test".
- `main.tex:8721-8772`: the obstruction problem lists checks but not the
  exact tuple from Agent 229.

Attack:

The current statement distinguishes algebraic Weyl/Moyal coefficients from
Costello analytic specialization, but it still lacks the exact obstruction
tuple. That leaves "external analytic problem" too loose.

Proposed replacement wording:

```tex
The first/third Costello specialization is controlled by
\[
  \mathfrak O_{\mathrm{Cost}}^{1,3}
  =
  (\mathfrak o_{\mathrm{Cas}},
   \hbar N[\bar c]\ \text{or}\ o_{\sigma,w}^{(r)},
   [\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}],
   \mathfrak O_{\theta_3},
   \mathfrak n_1,
   \mathfrak n_3).
\]
Here
\[
  \mathfrak n_1=P_{\partial,L}|_{\mathrm{Ham}^0}-\tfrac12 P
\]
and
\[
  \mathfrak n_3=
  [\operatorname{ObsProd}^{(3)}_{\mathrm{Costello}}
   -\tfrac{\hbar^3}{24}P^3]_{\mathrm{Ham}^0,\mathrm{conn},\mathrm{red}} .
\]
Vanishing of this tuple, with Costello locality and RG-compatible
counterterms, is the theorem target; a nonzero component is the obstruction
theorem.
```

Priority reason:

This keeps the proved algebraic coefficients from being mistaken for a
Costello graph theorem while also avoiding a vague "external" dismissal.

### P0-4. Physical \(\Omega\) large-\(N\) trace-state theorem: Agent 231 partial

Anchors:

- `main.tex:673-693`: line 692 still calls Layer 7 "conjectural here".
- `theorem-lanes.tex:2922-3121`: strong trace-state criterion exists, but the
  obstruction vector lacks Agent 231 components `ob_{\Omega,\mathrm{coeff}}`,
  `ob_{\mathrm{str}}`, and `ob_{\mathrm{branch}}`.
- `open-obligations.tex:890-999`: trace vector is shorter and lacks the rank
  versus finite-window separation.
- `local-dictionary.tex:647-664`: `Ob_\Omega` is too compressed for the
  physical trace-state target.
- `claim-strength-ledger.tex:470-475`: normal `\Omega` finite-window habitat is
  recorded, but not the full physical trace-state vector.

Attack:

"Conjectural here" is weaker than the available construction target. Agent 231
supplies a theorem surface and exact obstruction vector.

Proposed replacement wording:

```tex
Layer 7 is a theorem-surface-with-missing-construction, not a conjectural
input. It requires the datum
\[
  \mathfrak T^{N_{\mathrm{win}},M}_{N_{\mathrm{rk}},\Omega}
  =
  (\omega_{N_{\mathrm{rk}},\Omega},
   \nu_{N_{\mathrm{rk}},\Omega},
   R_{\Omega}^{N_{\mathrm{win}},M},
   \mathscr T_+,
   D_{N_{\mathrm{rk}},\Omega},
   \kappa_{N_{\mathrm{rk}},\Omega},
   C_{N_{\mathrm{rk}},\Omega},
   H^{\mathrm{prod}},H^{P_0})
\]
with \(N_{\mathrm{rk}}\) separated from the coefficient window
\((N_{\mathrm{win}},M)\). The exact obstruction vector is
\[
  (\operatorname{ob}_{\Omega,\mathrm{Cartan}},
   \operatorname{ob}_{\Omega,\mathrm{contr}},
   \operatorname{ob}_{\Omega,\mathrm{coeff}},
   \operatorname{ob}_{\mathrm{str}},
   \operatorname{ob}_{\mathrm{red}},
   \operatorname{ob}_{\mathrm{branch}},
   \operatorname{ob}_{\mathrm{state}},
   \operatorname{ob}_{\mathrm{norm}},
   \operatorname{ob}^{\mathrm{sc}}_{\mathrm{QME}},
   \operatorname{ob}^{\mathrm{ns}}_{\mathrm{QME}},
   \operatorname{ob}_{\mathrm{cent}},
   \operatorname{ob}_{\mathrm{Ward}},
   \operatorname{ob}_{\mathrm{cum}},
   \operatorname{ob}_{\mathrm{asymp}},
   \operatorname{ob}_{\mathrm{src}}).
\]
```

Priority reason:

This is a prominent main-text phrasing issue and a common source of false
large-\(N\) closure.

### P1-5. Admissible Tate bar-cobar / Quillen envelope: Agent 239 partial

Anchors:

- `main.tex:5208-5221`: correctly separates cochain CE/PV and bar-cobar
  envelope criteria.
- `main.tex:5411-5461`: admissible Tate Koszul-duality criterion is present.
- `open-obligations.tex:102-116`: records the relative theorem but not the
  full obstruction vector.
- `claim-strength-ledger.tex:842-858`: records the strict ambient
  product/direct-sum obstruction.
- `local-dictionary.tex:1226-1230`: says accepted only after conilpotence,
  exact duality, PBW completeness, and convergence.

Attack:

The broad theorem is reflected, but Agent 239's exact obstruction vector and
separate cyclic/P0 gates are not yet visible in the control surfaces.

Proposed replacement wording:

```tex
For candidate data \((\mathfrak h,D,A_{\mathrm{op}},\tau,B_{\mathrm{cl}})\),
the admissible envelope theorem fails exactly when a component of
\[
  \mathcal O_{\mathrm{AdmTate}}
  =
  \mathcal O_{\mathrm{win}}
  +\mathcal O_{\mathrm{top}}
  +\mathcal O_{\mathrm{conilp}}
  +\mathcal O_{\mathrm{MC}}(\tau)
  +\mathcal O_{\mathrm{cobar}}(\tau)
  +\mathcal O_{\mathrm{PBW}}
  +\mathcal O_{P_0}
  +\mathcal O_{\mathrm{cyc}}
\]
is nonzero. The associative bar-cobar Quillen theorem does not by itself
construct the \(P_0\) comparison, the cyclic trace, the kernel, or the
Costello/QME realization.
```

Priority reason:

This prevents a raw full-formal-disk Koszul-duality overclaim while preserving
the positive relative theorem.

### P1-6. Global Weiss/Ran and cross-volume firewall: Agent 238 partial

Anchors:

- `open-obligations.tex:1099-1138`: matched-conventions vector lacks the
  unified Kodaira-duality curvature term.
- `claim-strength-ledger.tex:1166-1188`: same vector is present without
  `Ob_{\mathrm{UKD}}`.
- `local-dictionary.tex:766-777`: target-specific Vol III/Igusa/BKM
  components are only appended generically.

Attack:

The firewall is correct, but the exact obstruction theorem is sharper than
the current vector.

Proposed replacement wording:

```tex
Any global or cross-volume transfer is governed by
\[
  \operatorname{Ob}_{\mathrm{UKD}}(\mathfrak C_{\mathrm{tar}})
  =
  \left(
    \operatorname{Ob}_{\mathfrak C_{\mathrm{tar}}},
    \left[d\Theta_{\mathrm{KD}}
      +\frac12[\Theta_{\mathrm{KD}},\Theta_{\mathrm{KD}}]\right]
  \right).
\]
For Vol III, Igusa/BKM, or compact-CY claims, append the target-specific
comparison components explicitly; otherwise the target remains quarantined and
supplies no evidence for the local theorem.
```

### P1-7. Controlled \(\C\times\R\), VOA, and Zhu reduction: Agent 228 partial

Anchors:

- `theorem-lanes.tex:698-884`: controlled reduction lane exists, with a coarse
  obstruction vector at `theorem-lanes.tex:870-880`.
- `claim-strength-ledger.tex:323-328`: VOA/Zhu claims are correctly marked as
  false transfer before construction.

Attack:

The current vector does not record the sharper Agent 228 gates: binary and
ternary factorization, \(K_\infty\), and separate VOA/Zhu exits.

Proposed replacement wording:

```tex
Replace the coarse reduction obstruction by
\[
  \operatorname{Ob}_{228}
  =
  (\operatorname{ob}_{K,\infty},
   \operatorname{ob}_{\mathrm{fac},2},
   \operatorname{ob}_{\mathrm{fac},3},
   \operatorname{ob}_{\mathrm{pair}},
   \operatorname{ob}_{\mathrm{anom}},
   \operatorname{ob}_{\mathrm{VOA}},
   \operatorname{ob}_{\mathrm{Zhu}}).
\]
A curve chiral, VOA, BRST, or Zhu theorem is an exact target after this vector
vanishes, not a consequence of the controlled coefficient shadow alone.
```

### P1-8. Strict endpoint / Casimir kernel: Agent 233 and Agent 239 partial

Anchors:

- `claim-strength-ledger.tex:330-335`: names
  `\mathfrak o^{\mathrm{Cas}}`.
- `claim-strength-ledger.tex:1122-1133`: endpoint tuple present, strict
  product/direct-sum endpoint fails.
- `local-dictionary.tex:753-764`: dictionary has `\mathfrak o^{\mathrm{Cas}}`
  and `\mathfrak o_{\mathrm{BV,end}}`.
- `main.tex:5452-5460`: full formal Hamiltonian algebra requires admissible
  replacement; obstruction tuple named by reference.

Attack:

The exact quotient detecting strict endpoint failure is not in the focus
surfaces.

Proposed replacement wording:

```tex
The strict product/direct-sum endpoint obstruction is the nonzero class
\[
  \mathfrak o_{\mathrm{Cas}}
  =
  [(C_{\le M})_M]\in
  Q_{\mathrm{Cas}}
  =
  \varprojlim_M
  (H_{\le M}\widehat\otimes H_{\le M}^{\vee})/
  \operatorname{im}(\mathfrak h_\Pi\widehat\otimes D_\oplus),
\]
equivalently the finite-window diagonal has infinite support in the
direct-sum direction. Weighted or ML finite-window habitats are replacement
theorems, not the original strict endpoint.
```

### P2-9. Equivariant CE/PV refined bracket completion: Agent 236 partial

Anchors:

- `claim-strength-ledger.tex:337-342`: current failure is only
  `\operatorname{ob}_{\Omega,\mathrm{CE/PV}}`.
- `local-dictionary.tex:647-664`: global `Ob_\Omega` is compressed.

Proposed replacement wording:

```tex
Replace the single symbol by the refined vector
\[
  \operatorname{Ob}^{\mathrm{glob}}_{\Omega,\mathrm{CE/PV}}
  =
  (\operatorname{ob}_{\mathrm{Cartan}},
   \operatorname{ob}_{\mathrm{top}},
   \operatorname{ob}_{\mathrm{br}},
   \operatorname{ob}_{\mathrm{diag}},
   \operatorname{ob}_{\mathrm{res}},
   \operatorname{ob}_{\mathrm{norm}},
   \operatorname{ob}_{\mathrm{fact}},
   \operatorname{ob}_{\mathrm{Roos}},
   \operatorname{ob}_{\mathrm{QME}}).
\]
```

### P2-10. Regular-density/wavefront current branch: dictionary lag

Anchors:

- `claim-strength-ledger.tex:442-458`: regular-density/wavefront obstruction
  is reflected.
- `theorem-lanes.tex:3249-3284`: regular-density and wavefront eta branches
  are reflected.
- `local-dictionary.tex:1420-1481`: dictionary still presents
  `\mathcal D'_c(I)` and `aB` without the graph-level regular-density versus
  singular-wavefront distinction.

Proposed replacement wording:

```tex
Add dictionary rows distinguishing coefficient-current notation
\(\mathcal D'_c(I)\) from the graph-level admissible habitat
\(\mathcal D_c^{\mathrm{reg}}(I)=C_c^\infty(I)dt\). A theorem using singular
labels must also specify H\"ormander transversality, finite scaling degree,
diagonal extension, local counterterms, pushforward wavefront bounds, and the
quotient obstruction \(\eta^{\mathrm{reg}}_{n_0,M}\).
```

## Reports Not Yet Fully Reflected

- Agent 228: partially reflected. The controlled \(\C\times\R\) lane exists,
  but the exact `Ob_228` vector with VOA/Zhu gates is not propagated.
- Agent 229: partially reflected. Algebraic Weyl/Moyal coefficients and the
  Costello checklist exist; the exact
  `\mathfrak O_{\mathrm{Cost}}^{1,3}` tuple is absent.
- Agent 230: reflected for the radial all-interior target in the claim ledger,
  open obligations, and main theorem surfaces.
- Agent 231: partially reflected. The theorem lane is strong; main text still
  says "conjectural here" and shorter vectors remain in the ledger,
  obligations, and dictionary.
- Agent 232: mostly reflected by the scalar QME alternatives and non-scalar
  closed-exchange criterion; Agent 241 supersedes the scalar same-branch
  closed-exchange wording with a sharper obstruction sequence.
- Agent 233: partially reflected. Strict endpoint failure is recorded, but the
  exact `Q_{\mathrm{Cas}}` quotient should be added.
- Agent 234: reflected as the full open BV factorization-center construction
  target and obstruction vector.
- Agent 235: reflected in the claim ledger open \(A_\infty\) acceptance
  datum; main text line 692 should still be rephrased with the Agent 231/235
  theorem-target language.
- Agent 236: partially reflected. The single CE/PV symbol should become the
  refined obstruction vector.
- Agent 237: reflected in the ledger and theorem lanes; the local dictionary
  needs a precision row for graph-level regular densities versus arbitrary
  currents.
- Agent 238: partially reflected. The firewall exists, but the unified
  Kodaira-duality curvature obstruction `Ob_{\mathrm{UKD}}` is absent.
- Agent 239: partially reflected. The admissible Tate theorem exists; the
  full `O_{\mathrm{AdmTate}}` vector and separate cyclic/P0 gates should be
  added to the control surfaces.
- Agent 240: reflected in `claim-strength-ledger.tex:417-432`, not yet
  propagated to `main.tex`, `open-obligations.tex`, or `theorem-lanes.tex`.
- Agent 241: not yet reflected in the focus surfaces except for older scalar
  and non-scalar closed-exchange scaffolding. The scalar gate/cokernel/Roos
  obstruction sequence and the algebraic-cone classification should be added.

## Verification

Read current control surfaces and reports under concurrent worktree
conditions. Existing staged files by other agents were left untouched. This
audit stages only the two Agent 242 report files.
