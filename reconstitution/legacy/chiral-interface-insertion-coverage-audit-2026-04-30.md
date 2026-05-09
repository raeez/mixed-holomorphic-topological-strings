# Chiral Interface Insertion Coverage Audit

Date: 2026-04-30.
Owner: Agent 256.
Scope: compare Agent 249's insertion spec with the live TeX state after
Agent 250 and main-thread theorem/open-obligation additions.

No TeX file was edited.

## Verdict

The mathematical core of Agent 249's spec is already present in the live
TeX at five of the six requested insertion surfaces.  The only requested
block not present as its own block is the compact main-text remark after
`prop:native-darboux-theorem-package`.

Do not apply Agent 249's full spec verbatim.  It would duplicate the
existing theorem label `thm:lane-constructed-chiral-interface`, repeat
dictionary and ledger entries, and create a second copy of an open
obligation that is already present.  If TeX editing is reopened, the
right operation is selective refinement of existing entries, not a second
insertion pass.

## Coverage Matrix

| Agent 249 insertion block | Current TeX coverage | Missing precision | Duplicate-harm assessment |
|---|---|---|---|
| `theorem-lanes.tex`, after `thm:lane-reduced-dirac-brst-zhu`: add `thm:lane-constructed-chiral-interface`. | Covered at `theorem-lanes.tex:1027-1080`. The live statement gives the status, interface tuple, retained `z_2`/principal-part reduction, vertex/Zhu requirements, Capelli shift, principal-part action, and obstruction vector. It relies on the detailed controlled-reduction lane at `theorem-lanes.tex:698-884`, the reduced Dirac/BRST/Zhu lane at `theorem-lanes.tex:886-1025`, and the native taxonomy at `theorem-lanes.tex:227-379`, `381-415`. | The live statement is compressed. It does not repeat Agent 249's full native-source formula inside the same block, the explicit `F_red(I x D)` CE formula, the full obstruction subcomponent lists, or the "Vol II control" paragraph. | Harmful if inserted verbatim: duplicate theorem label and repeated formulas. Later refinement should patch the existing statement only. |
| `local-dictionary.tex`, after the Weyl/Moyal compatibility row. | Covered at `local-dictionary.tex:375-413`. The row records `I_ch`, `V_red`, retained modes/principal parts, bracket/BV/brane/factorization-to-vertex/BRST/Zhu/Moyal/anomaly requirements, the obstruction vector, and the false-transfer firewall. | No material block missing. | Harmful: it would duplicate a longtable row and blur the dictionary. |
| `claim-strength-ledger.tex`, failed-surface status ledger, replace the short `C x R`, VOA, BRST, Zhu gates item. | Covered in substance at `claim-strength-ledger.tex:326-347`. The title remains broad, but the body now contains `I_ch`, retained `z_2`/principal parts, false transfer, and `Ob_{I_ch}`. | Only the item title differs from Agent 249's proposed "Constructed chiral algebra interface" title. | Harmful as a new item. If desired, rename the existing item rather than adding another. |
| `claim-strength-ledger.tex`, supremum controller, add constructed-interface classification after the reduced Dirac BRST/Zhu row. | Covered by merge at `claim-strength-ledger.tex:590-624`. The reduced Dirac BRST/Zhu classification now states that an externally constructed chiral algebra enters only as `V_red` in `I_ch` after `R_{C x R}`, and only after the obstruction vector is killed or named. | There is no separate item headed "Constructed chiral algebra interface tuple." | A separate duplicate item would inflate the ledger. If a separate heading is wanted later, split or retitle the existing item. |
| `open-obligations.tex`, after the one-antifield Moyal target, add the obstruction-vector obligation. | Covered but relocated at `open-obligations.tex:154-183`, before the Matlis/local-cohomology item rather than after the one-antifield Moyal target at `open-obligations.tex:263-278`. The row contains `I_ch`, `Ob_{I_ch}`, and the reduction/vertex/Zhu/native components. | Exact Agent 249 subcomponent names are not all displayed; the current row uses coarser prose. The placement differs from the spec. | Harmful to add a second row after the one-antifield target. If ordering matters, move the existing row, do not duplicate it. |
| `main.tex`, after the proof of `prop:native-darboux-theorem-package`, add `rmk:constructed-chiral-interface-target`. | Missing as a distinct block. The anchor currently passes from `main.tex:1529` directly to `rmk:External global-obstruction firewall` at `main.tex:1531`. | The idea is partially covered elsewhere: `abstract.tex:207-212`, `principles.tex:272-276`, `theorem-lanes.tex:1027-1080`, and `open-obligations.tex:154-183`. No label `rmk:constructed-chiral-interface-target` exists. | Not a label collision. The exact Agent 249 remark would be redundant but not structurally fatal. A later TeX pass should use a one-sentence cross-reference to `thm:lane-constructed-chiral-interface`, not reprint the tuple. |

## Subcomponent Audit

Already represented:

- Native object and native-not-vertex firewall:
  `theorem-lanes.tex:227-279`, `theorem-lanes.tex:381-415`,
  `abstract.tex:52-73`.
- Controlled `C x R` reduction with retained `z_2`/principal-part
  system, two-variable bracket, coadjoint action, brane image, scalar
  anomaly, Moyal product, and anti-`z_2=0` firewall:
  `theorem-lanes.tex:698-884`.
- Reduced Dirac/BRST/Zhu package, weights, OPE generators, BRST current,
  zero modes, Capelli contact shift, and typed comparison chain:
  `theorem-lanes.tex:886-1025`.
- Constructed-interface tuple and admission obstruction vector:
  `theorem-lanes.tex:1027-1080`, `local-dictionary.tex:375-413`,
  `claim-strength-ledger.tex:326-347`, `claim-strength-ledger.tex:590-624`,
  `open-obligations.tex:154-183`.

Not written with Agent 249's full granularity:

- The exact subentry list
  `ob_{s,or}`, `ob_{z_2,fib}`, `ob_{K,infty}`,
  `ob_{pair}`, `ob_{fac,2}`, `ob_{fac,3}`, `ob_{brane}`,
  `ob_{anom}`, `ob_{Moyal}` is not written as the `Ob_red` vector.
  The live controlled-reduction lane names several of these components,
  but not the whole Agent 249 list.
- The exact `Ob_vert` list
  `ob_FV`, `ob_Laurent`, `ob_loc`, `ob_wt`, `ob_BRST` is not written as
  a displayed vector.
- The exact `Ob_Zhu` list
  `ob_zero`, `ob_Zhu^mult`, `ob_Capelli`, `ob_HKR` is not written as a
  displayed vector.
- The exact `Ob_nat` list
  `ob_{pi_!-source}`, `Ob_BM^infty`, `ob_false-native` is not written as
  a displayed vector, although `Ob_BM^infty` is already a separate native
  all-window obstruction in the theorem lanes.
- The equation
  `zeta_hbar(f*g)=zeta_hbar(f)zeta_hbar(g)` and the Hochschild cocycle
  `ob_Zhu(f,g)` from Agent 249 are not displayed in the live constructed
  interface statement.  The live text states compatibility with the
  Weyl/Moyal product, Capelli shift, and principal-part action instead.
- The "Vol II control" paragraph from Agent 249 is absent.  This is not
  a mathematical gap in the local theorem surface.  The live TeX states
  the same firewall internally: a curve/Zhu object is reduced data, not
  native `C^2` factorization data.

## Recommendation

No TeX insertion should be made by replaying Agent 249.  The only open
editorial decision is whether the main body should contain a short pointer
after `prop:native-darboux-theorem-package`.  If added later, it should be
short:

```tex
The constructed curve-chiral interface is the reduced theorem target of
Statement~\ref{thm:lane-constructed-chiral-interface}; it is not part of
the native Darboux package.
```

Any desired extra precision should be folded into the existing theorem
lane or open-obligation row by naming the missing obstruction
subcomponents there.  It should not be introduced as a second theorem,
dictionary row, ledger item, or open-obligation item.
