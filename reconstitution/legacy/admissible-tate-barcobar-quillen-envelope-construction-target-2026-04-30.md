# Admissible Tate Bar-Cobar / Quillen Envelope Construction Target

Date: 2026-04-30.
Scope: local mixed holomorphic-topological SFT on `R^2_top x C^2_hol`.
Writable surface: report only. No manuscript edits.

## Verdict

Stable core exists, but only as a relative acceptance theorem in an
admissible finite-window Tate envelope. The raw full formal disk with the
strict product/direct-sum cotangent pair does not satisfy the kernel or
endpoint theorem. It contributes an exact obstruction class.

The theorem must not be stated as "the full formal Hamiltonian algebra has
Koszul duality" without the envelope data. The true supremum statement is:

1. construct the admissible lower-central Tate-pronilpotent envelope and prove
   the bar-cobar / Quillen / PBW theorem there;
2. state the strict product/direct-sum full disk as an obstruction theorem;
3. keep cyclic trace, `P_0`, kernel, and Costello/QME upgrades as separate
   acceptance gates with named obstruction classes.

## Anchors Read

- `main.tex:5200-5221`: staged CE/PV, kernel, and admissible bar-cobar criterion.
- `main.tex:5223-5295`: Tate CE chains, conilpotence, completed PBW, and Koszul duality.
- `main.tex:5353-5367`: lower-central Tate-pronilpotence as the bar-cobar criterion.
- `main.tex:5411-5461`: admissible Tate Koszul-duality criterion.
- `tate-T3-quillen-equivalence.tex:48-154`: strict finite-window ML habitat and admissible model envelope.
- `tate-T3-quillen-equivalence.tex:204-266`: finite-window bracket, coadjoint, and Casimir obstruction terms.
- `tate-T3-quillen-equivalence.tex:289-366`: open-side twisting cochain datum.
- `tate-T3-quillen-equivalence.tex:368-523`: open-side Koszul obstruction complex and filtered-cobar recognition theorem.
- `tate-T3-quillen-equivalence.tex:745-875`: conilpotent Tate coalgebras and bar-cobar Quillen equivalence.
- `tate-T3-quillen-equivalence.tex:912-954`: Lie CE / bar-cobar specialization.
- `tate-T3-quillen-equivalence.tex:956-1021`: closed-side Tate formalism package.
- `tate-T3-quillen-equivalence.tex:1025-1096`: module reconstruction, conditional on a fixed admissible `P_0`-algebra envelope.
- `tate-T3-quillen-equivalence.tex:1123-1158`: Quillen equivalence separated from Casimir convergence.
- `tate-T3-quillen-equivalence.tex:1160-1195`: no universal strict product/direct-sum kernel habitat.
- `tate-T1-weighted-completion.tex:188-243`: weighted coefficient pair and Casimir convergence.
- `tate-T1-weighted-completion.tex:969-1001`: weighted RG acceptance gate.
- `tate-T1-weighted-completion.tex:1221-1288`: Roos/Milnor finite-window non-scalar counterterm criterion.
- `tate-T1-weighted-completion.tex:2785-2852`: strict unweighted endpoint obstruction.
- `tate-T1-weighted-completion.tex:2854-3017`: endpoint-admissible module and finite-window `q -> 1+` stabilization criterion.
- `theorem-lanes.tex:1204-1271`: bracket- and kernel-admissible CE/PV realizations.
- `theorem-lanes.tex:1660-1708`: abstract bracket-compatible CE/PV recognition criterion.
- `open-obligations.tex:102-117`: admissible Tate bar-cobar / Quillen envelope obligation.
- `claim-strength-ledger.tex:82-102`: Stage A4 relative envelope status.
- `claim-strength-ledger.tex:127-145`: Koszul layers 0-4.
- `claim-strength-ledger.tex:842-858`: Stage A4 theorem data.
- `local-dictionary.tex:680-735`: CE/PV generator and kernel dictionary.
- `local-dictionary.tex:1100-1114`: strict shifted cotangent algebra versus weighted regulator.
- `local-dictionary.tex:1226-1230`: admissible Tate / relative bar-cobar boundary.
- `main.tex:8980-9265`: Costello, Costello-Gwilliam, Priddy, Loday-Vallette, Hinich, Hovey, Lefevre-Hasegawa, Lurie, Quillen, Schwede-Shipley bibliography anchors.
- Vol II control: `notes/ambient_category_choice_attack_heal.md:47-64`, `:106-163`; `notes/antipatterns_catalogue.md:9919-9927`, `:9958-9965`, `:10020-10030`, `:10145-10157`.

## Needed Category

Define `AdmTateLie_LC` as the category of data
`(g, {g_{\le M}}, F, D, E)` satisfying:

1. `g = lim_M g_{\le M}` is a complete Hausdorff bounded-below filtered dg
   Lie algebra.
2. Each `g_{\le M}` is finite-dimensional, and transition maps
   `g_{\le M} -> g_{\le N}` are surjective dg Lie quotient maps.
3. The shifted cotangent extension is in the same envelope:
   `g = h adm semidirect D[1]`, with continuous action and exact
   continuous dualization on the finite-window tower.
4. The lower-central condition holds:
   `cap_r (g^{(r)} + F^M g) = F^M g` for every `M`.
5. The strict finite-window ML habitat embeds fully faithfully and
   exact symmetric-monoidally into a locally presentable symmetric monoidal
   model envelope `TateChain_{\ge 0}^{adm}`.
6. Weak equivalences are admissible filtered quasi-isomorphisms: finite
   quotient quasi-isomorphisms plus associated-graded quasi-isomorphism.
7. The monoid, transfer, and smallness hypotheses needed for Lie,
   augmented associative, and conilpotent-coalgebra bar-cobar transfer are
   part of the envelope.

This category is not the raw category of all Tate vector spaces. It is a
chosen exact finite-window model habitat.

## Conilpotent CE Coalgebras

For `g in AdmTateLie_LC`,

```text
C_*^{CE}(g) = direct-sum_{n >= 0} S^n_hat(g[1])
C^*_{CE,cont}(g) = Hom_cont(C_*^{CE}(g), C)
                 ~= S_hat_Tate(g^vee_cont[-1]).
```

Conilpotence is CE-length conilpotence: each homogeneous CE chain has finite
symmetric length and is killed by a high enough iterated reduced coproduct.
Lower-central Tate-pronilpotence is separate. It is the inverse-limit
separatedness condition needed for completed cobar and PBW.

## Completed Cobar and PBW

The completed cobar functor is

```text
Omega^hat C = T^hat(s^{-1} \bar C)
```

completed in tensor length and finite Tate windows, with Loday-Vallette signs.
The completed enveloping algebra is

```text
U_hat(g) = T_hat(g) /
  closure < xy - (-1)^{|x||y|} yx - [x,y] >.
```

PBW completeness means:

```text
gr_PBW U_hat(g) ~= S_hat_Tate(g),
cap_p F^p_PBW U_hat(g) = 0,
U_hat(g) = lim_p U_hat(g) / F^p_PBW.
```

The Rees form is

```text
U_hbar(g) = T_hat(g)[[hbar]] /
  closure < xy - (-1)^{|x||y|} yx - hbar[x,y] >,
U_hbar(g)/(hbar) ~= S_hat(g).
```

This is a deformation-level statement only in the admissible envelope. The
PBW special fibre alone is only a shadow.

## Acceptance Theorem

The strongest true theorem target is:

**Theorem.** Let `g_adm in AdmTateLie_LC`. Suppose the admissible model
envelope contains `C_*^{CE}(g_adm)`, `U_hat(g_adm)`, completed symmetric
algebras, and the finite-window inverse systems, and satisfies transfer,
smallness, monoid, exact ML, and completed tensor compatibility. Then:

```text
Omega C_*^{CE}(g_adm) -> U_hat(g_adm)
```

is an admissible filtered quasi-isomorphism. The bar-cobar adjunction

```text
Omega : TateConilpCoAlg <-> TateAssocAlg^+ : Bar
```

is a Quillen equivalence in the admissible envelope. After exact continuous
dualization,

```text
C^*_{CE,cont}(g_adm) ~= (U_hat(g_adm))^!
```

in the homotopy category of complete augmented Tate algebras. The associated
infinity-categorical equivalence follows by Dwyer-Kan localization / Lurie
A.3.7.

If, in addition, the finite-window CE/PV transition obstructions
`o^br` and `o^coad` vanish and the variance/continuous-dualization data are
supplied, the same tower carries the completed CE/PV cochain identity

```text
c^I -> theta^I,
u_I -> O_I.
```

If a bracket-admissible `B` is supplied, this becomes a completed `P_0`
comparison on `B`. If a kernel-admissible convolution habitat is supplied,
the diagonal tensor

```text
Theta_B = sum_I H_I tensor theta^I + sum_I eta^I tensor O_I
```

is an MC kernel in that habitat.

## Cyclic Trace Compatibility Gate

For an open `A_infinity` object, add the following acceptance data:

1. `A_op` is a complete augmented filtered cyclic `A_infinity` algebra in
   the same admissible envelope.
2. The trace `tr_M : A_{op,\le M} -> C[-d]` is continuous, compatible with
   finite-window transition maps, and cyclic for each `m_k`.
3. The bar coalgebra `Bar(A_op)` is locally conilpotent windowwise.
4. Homotopy transfer preserves the cyclic pairing, not just the underlying
   `A_infinity` structure.
5. The twisting cochain
   `tau : Bar(A_op) -> B_cl`
   is continuous and satisfies
   `d_conv tau + (1/2)[tau,tau]_conv = 0`.

The cyclic obstruction target is:

```text
O_cyc =
  ( tr_M m_{k,M}
    - (-1)^{epsilon} tr_M m_{k,M} cyc )_{M,k}
  +
  lim^1_M HC^{n-1}(A_{op,\le M})
  +
  Cone(Bar_cyc(A_op) -> Bar(A_op)) .
```

This gate is separate from the associative bar-cobar Quillen equivalence.
The manuscript already proves that a full cyclic contraction killing all
one-psi descendants is impossible in the current cyclic model
(`theorem-lanes.tex:83-96`, `open-obligations.tex:667-672`). A positive open
cyclic theorem must either retain those descendants or enlarge the target.

## Obstruction Theorem

The exact obstruction theorem target is:

**Theorem.** For a candidate datum
`(h, D, A_op, tau, B_cl)` as in `tate-T3`, acceptance fails precisely when
one of the following components is nonzero:

```text
O_AdmTate =
  O_win
  + O_top
  + O_conilp
  + O_MC(tau)
  + O_cobar(tau)
  + O_PBW
  + O_P0
  + O_cyc.
```

Where:

```text
O_win =
  (o^br_{M,N}, o^coad_{M,N}, [(C_{\le M})_M])
```

with

```text
o^br_{M,N}(x,y)
  = pi_{M,N}[x,y]_M - [pi_{M,N}x, pi_{M,N}y]_N,

o^coad_{M,N}(x,lambda)
  = pi^vee_{M,N}(x ._M lambda)
    - (pi_{M,N}x) ._N (pi^vee_{M,N}lambda),

o^Cas_{M,N}
  = (pi_{M,N} tensor pi^vee_{M,N}) C_M - C_N.
```

The topology/Roos part is:

```text
O_top^n =
  lim^1_M H^{n-1}(C^*_{CE}(g_{\le M}))
  +
  lim^1_M H^{n-1}(PV_{\le M}).
```

The conilpotence/lower-central part is:

```text
O_conilp =
  C_*^{CE}(g) / union_r F^{(r)}_coaug C_*^{CE}(g)
  +
  cap_{r >= 1} g^{(r)}.
```

The MC and cobar parts are:

```text
O_MC(tau) =
  d_conv tau + (1/2)[tau,tau]_conv,

O_cobar(tau) =
  Cone(gr kappa_tau)
  + direct-sum_n lim^1_M H^{n-1}((Omega C_op)_{\le M})[-n]
  + direct-sum_n lim^1_M H^{n-1}(B_{cl,\le M})[-n].
```

The PBW part is the separatedness and associated-graded defect:

```text
O_PBW =
  ker(gr_PBW U_hat(g) -> S_hat_Tate(g))
  + coker(gr_PBW U_hat(g) -> S_hat_Tate(g))
  + cap_p F^p_PBW U_hat(g).
```

The `P_0` part is the absence of a transferred completed `P_0` model
structure or the failure of bracket-admissibility:

```text
O_P0 =
  (failure of continuous multiplication,
   failure of continuous d_pi,
   failure of continuous Schouten contraction,
   failure of transferred P_0 model structure).
```

The cyclic part is `O_cyc` above.

For the strict product/direct-sum endpoint

```text
h_Pi = product_{d >= 1} H_d,
D_oplus = direct-sum_{d >= 1} H_d^vee,
```

the obstruction is already nonzero:

```text
(C^M_h)_M notin h_Pi tensor_hat D_oplus.
```

Equivalently, no tensor projects to all finite Casimirs
`C^M_h = sum_{d <= M} sum_i e_{d,i} tensor e^i_d`. This is the strict
endpoint no-go; weighted product coefficient modules are regulator habitats,
not the original strict continuous dual.

## Failure Modes Destroyed

1. Raw `TateVec` does not carry the theorem. The theorem lives in a stated
   admissible model envelope.
2. `U_hbar(g)/(hbar) ~= S(g)` is not deformation-level Koszul duality.
3. CE/PV generator substitution is not a kernel theorem.
4. Casimir convergence is not a hypothesis for algebraic bar-cobar
   equivalence, but it is mandatory for Costello kernels.
5. Strict product/direct-sum endpoint has no universal kernel property.
6. `P_0`-module category reconstruction is a criterion after the transferred
   `P_0` model envelope is fixed; it is not constructed by associative
   bar-cobar alone.
7. Cyclic trace compatibility is not automatic from associative bar-cobar.
8. Physical large-N, Costello/QME realization, and compact-CY/global descent
   do not follow from the admissible envelope.

## Primary Source Anchors

- Priddy 1970, `main.tex:9104-9113`: Koszul resolutions.
- Loday-Vallette 2012, `main.tex:9115-9125`: bar-cobar, operadic Koszul,
  PBW comparison, signs.
- Hinich 1997, `main.tex:9194-9204`: transfer of homotopy algebra model
  structures.
- Hovey 1999, `main.tex:9218-9228`: Quillen adjoint-functor criterion.
- Lefevre-Hasegawa 2003, `main.tex:9230-9236`: conilpotent coalgebra model
  structure.
- Lurie 2017, `main.tex:9238-9243`: higher algebra, localization and module
  category equivalence.
- Quillen 1967, `main.tex:9245-9254`: homotopical algebra.
- Schwede-Shipley 2000, `main.tex:9256-9265`: algebras and modules in
  monoidal model categories.
- Costello-Gwilliam 2017/2021, `main.tex:9010-9032`: factorization algebra
  vocabulary and local constancy/descent boundary.
- Costello 2011, `main.tex:8980-8991`: heat-kernel BV/RG package, relevant
  only after coefficient kernels are built.

## Verification Commands

```bash
git status --short
rg -n "Tate|bar-cobar|cobar|Quillen|Koszul|admissible|conilpotent|PBW|Milnor|Roos|lower-central|cyclic|CE|completion|continuous dual" main.tex theorem-lanes.tex tate-T3-quillen-equivalence.tex tate-T1-weighted-completion.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex mathmacros.tex commands.tex
nl -ba main.tex | sed -n '5200,5461p'
nl -ba tate-T3-quillen-equivalence.tex | sed -n '48,154p'
nl -ba tate-T3-quillen-equivalence.tex | sed -n '368,523p'
nl -ba tate-T3-quillen-equivalence.tex | sed -n '745,875p'
nl -ba tate-T1-weighted-completion.tex | sed -n '2785,2852p'
nl -ba theorem-lanes.tex | sed -n '1204,1271p'
nl -ba open-obligations.tex | sed -n '102,117p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md | sed -n '9911,10157p'
```

