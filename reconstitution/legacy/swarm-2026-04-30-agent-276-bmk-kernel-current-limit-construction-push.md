# Agent 276 BMK Kernel Current-Limit Construction Push, 2026-04-30

Owned file:

- `reconstitution/swarm-2026-04-30-agent-276-bmk-kernel-current-limit-construction-push.md`

No manuscript TeX was edited. No build was run.

## Claim Attacked

Starting from the staged BMK/Koppelman source fixture, `main.tex`, and
`appendix-factorization-current-conventions.tex`, try to construct
internally:

1. the cutoff current limit `H_chi`;
2. the finite-window moment projection `p_N` and support-at-zero current
   inclusion `i_N`;
3. the collar quotient killing `E_{chi,N}`;
4. the Koppelman differential identity
   \[
     \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
       =\operatorname{id}-i_Np_N+E_{\chi,N}.
   \]

## Inputs Read

- `CLAUDE.md`.
- `/Users/raeez/ecosystem/INVARIANTS.md`, voice section.
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`, self-reflection section.
- `/Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `commands.tex`, `mathmacros.tex`, `notation.tex`, `preamble.tex`.
- `main.tex:1242-1452`.
- `appendix-factorization-current-conventions.tex:399-690`.
- `appendix-matlis-principal-parts.tex:1-244`.
- `references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md`.
- `references/primary-sources/matlis-local-cohomology-residue-anchor.md`.
- Reports 206, 211, 222, 268, and the relevant source-fixture plan
  entries.

The staged and working versions of the BMK appendix block agree on the
current finite-window theorem. `main.tex` has unrelated unstaged edits
only later in the file.

## Verdict

Status: `BLOCKED` for the full displayed finite-window differential
identity as a statement on the undeclared source/current complex.

Closed internally:

- The cutoff integral defining `H_chi` has a locally integrable current
  limit on each fixed finite configuration stratum.
- The finite moment map `p_N` is a chain map on compactly supported
  top Dolbeault degree by Stokes.
- The derivative-delta formula for `i_N` has the correct Taylor-residue
  sign once the current-pairing convention for
  `delta_0 dbar z_1 wedge dbar z_2` is fixed.
- A single-pair collar quotient can be defined so that terms supported
  on `supp d chi` vanish.

Not closed:

- The manuscript does not define `H_{chi,N}`. It defines `H_chi`,
  `p_N`, and `i_N`, then uses a finite-window homotopy operator with a
  stronger property.
- On the full compact-support Dolbeault complex, or on the full current
  complex, `id - i_N p_N` is false at finite `N`: scalar and high
  holomorphic moments survive.
- The cutoff proof omits the diagonal annulus term from
  `d vartheta_epsilon`. That term is not a collar term; it is the
  current-theoretic diagonal/Taylor term whose sign and normalization must
  produce the chosen projector.
- The collar quotient is only local unless the extension-by-zero
  factorization quotient is declared and checked.

## Construction Attempt

### Cutoff Current Limit

The manuscript kernel is
\[
  K_{\mathrm{BM}}(\zeta,z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{\overline{\eta_1}d\bar\eta_2
        -\overline{\eta_2}d\bar\eta_1}{r^4}
  \wedge d\zeta_1\wedge d\zeta_2,
  \qquad
  \eta=\zeta-z.
\]
Near the diagonal, `|K_BM| ~ r^{-3}` in real dimension four. Hence
\[
  \int_0^\delta r^3 r^{-3}\,dr < \infty.
\]
For smooth compactly supported `alpha`, dominated convergence gives
\[
  \lim_{\epsilon\to0}
  \int K_{\chi,\epsilon}(\zeta,z)\wedge\alpha(\zeta)
\]
as a locally integrable current in `z`. For separated supports the
displayed estimates
\[
  |\nabla^kK_{\mathrm{BM}}(\zeta,z)|
    \le C_k|\zeta-z|^{-3-k}
\]
are sufficient.

This proves existence of `H_chi`. It does not prove the differential
identity. Differentiating the cutoff kernel gives three kinds of terms:
\[
  \bar\partial(\chi(\zeta)\chi(z)\vartheta_\epsilon K_{\mathrm{BM}})
  =
  \chi\chi\,\vartheta_\epsilon\,\bar\partial K_{\mathrm{BM}}
  +\bar\partial(\chi\chi)\,\vartheta_\epsilon K_{\mathrm{BM}}
  +\chi\chi\,\bar\partial\vartheta_\epsilon\wedge K_{\mathrm{BM}}.
\]
The second term is the collar term. The third term is supported on
`\epsilon < |\zeta-z| < 2 epsilon`; it converges, if normalized
correctly, to a diagonal current. It is not supported on `supp d chi`.
Thus the proof sentence in `main.tex:1423-1427` and
`appendix-factorization-current-conventions.tex:631-640` is incomplete
unless this annular term is explicitly identified with the diagonal
part of the Koppelman formula.

Required local lemma:
\[
  \lim_{\epsilon\to0}
  \chi(\zeta)\chi(z)\bar\partial\vartheta_\epsilon(|\zeta-z|)
  \wedge K_{\mathrm{BM}}(\zeta,z)
  =
  \pm\,\chi(z)^2[\Delta]
\]
with the sign and orientation translated to the manuscript convention.
Only after that computation can one decide the sign of the `id` term in
the current identity.

### Moment Projection and Residue Currents

For top Dolbeault degree define
\[
  m_{a,b}(\alpha)
  =
  \int_B z_1^az_2^b\,\alpha^{0,2}\wedge dz_1\wedge dz_2.
\]
Then
\[
  p_N(\alpha)=
  \sum_{0<a+b\le N}m_{a,b}(\alpha)\rho_{a,b}
\]
is a chain map. If `beta` is compactly supported of degree `(0,1)`, then
\[
  m_{a,b}(\bar\partial\beta)
  =
  \pm\int_B\bar\partial
  \bigl(z_1^az_2^b\,\beta\wedge dz_1\wedge dz_2\bigr)
  =
  0
\]
because `z_1^a z_2^b` is holomorphic.

The derivative-delta inclusion
\[
  i_N(\rho_{a,b})=\Delta_{a,b}
  =
  \frac{(-1)^{a+b}}{a!\,b!}
  \partial_{z_1}^a\partial_{z_2}^b
  \delta_0\,d\bar z_1\wedge d\bar z_2
\]
has the correct algebraic sign under the convention
\[
  \partial_{z_1}^a\partial_{z_2}^b\delta_0(f)
  =
  (-1)^{a+b}
  \partial_{z_1}^a\partial_{z_2}^b f(0).
\]
Thus
\[
  \langle\Delta_{a,b},f\rangle
  =
  [z_1^az_2^b]f
  =
  \operatorname{Res}_0(\rho_{a,b}f).
\]
The Matlis appendix closes the coadjoint sign:
\[
  \operatorname{Res}_0((f\cdot\rho)g)
  =
  -\operatorname{Res}_0(\rho\{f,g\}).
\]

Remaining normalization issue: the manuscript must explicitly declare
the current-pairing convention for the form factor
`dbar z_1 wedge dbar z_2` against `dz_1 wedge dz_2`. Without that
declaration there is still a possible global scalar, usually a power of
`2i` or `(2 pi i)`, between the distributional current convention and
the residue convention. The Matlis fixture fixes the algebraic residue
normalization; it does not by itself fix this analytic current scalar.

### Finite-Window Obstruction

The finite-window identity cannot hold on the full current complex.
Take the closed top current
\[
  T=\Delta_{N+1,0}.
\]
Then `p_N(T)=0`, since all retained moments have total degree at most
`N`. If the relative-collar identity held on the full current complex,
then
\[
  T=\bar\partial H_{\mathrm{BM},N}T.
\]
Pairing with the holomorphic test function `z_1^{N+1}` gives a
contradiction:
\[
  \langle T,z_1^{N+1}\rangle=1,
  \qquad
  \langle\bar\partial H_{\mathrm{BM},N}T,z_1^{N+1}\rangle=0.
\]
The second equality is the current form of Stokes, since
`\bar\partial z_1^{N+1}=0`.

The same obstruction occurs for the scalar current `Delta_{0,0}` because
the reduced principal-part module omits `rho_{0,0}`. Therefore the
finite-window theorem must be read on a reduced finite-window quotient
or on a finite-order support-at-zero current habitat. That habitat is
not yet defined in `main.tex:1333-1348` or in
`appendix-factorization-current-conventions.tex:482-498`.

The missing object is not cosmetic. One possible definition is a
relative finite-window current complex
\[
  \mathcal C_N^\bullet(B_2,B_1)
  =
  \mathcal D'^{0,\bullet}(B_2)
  \big/
  \left(
    \mathcal D'^{0,\bullet}_{B_2\setminus B_1}(B_2)
    +
    \mathcal K_N^\bullet
  \right),
\]
where `D'_{B_2\setminus B_1}` is the collar-support subcomplex and
`\mathcal K_N^{0,2}` kills the scalar moment and all positive moments
outside `0<a+b<=N`.

But this alone does not define the homotopy: the unmodified `H_chi` need
not descend through such a quotient, since for `k in K_N^{0,2}` the
current `H_chi k` need not be zero in degree `(0,1)`. A real proof must
either enlarge the quotient by the homotopy saturation of `K_N`, or
construct a modified kernel `H_{chi,N}` whose Taylor/current subtraction
is finite-window from the start.

This is the exact current obstruction:
\[
  \operatorname{ob}_{\mathrm{curr},N}
  =
  [\Delta_{0,0}]
  \oplus
  \bigoplus_{a+b>N}\C[\Delta_{a,b}]
\]
in the holomorphic-moment dual of top compact-support Dolbeault
cohomology, together with the missing descent of `H_chi` to the quotient
where this class is killed.

### Collar Quotient

For a single nested pair `B_1 \Subset B_2`, the collar quotient can be
constructed:
\[
  \mathcal D'^{0,\bullet}(B_2)
  \longrightarrow
  \mathcal D'^{0,\bullet}(B_2)/
  \mathcal D'^{0,\bullet}_{B_2\setminus B_1}(B_2).
\]
Since `chi=1` on `B_1`, the `d chi` terms are supported in
`B_2\setminus B_1`; hence they vanish in this quotient.

This closes only the single-pair support statement. The manuscript's
factorization assertion needs more:

- extension by zero must preserve the collar subcomplex for all inclusions
  used in the prefactorization structure;
- products of representatives must not move a killed collar term back
  into the retained collision region;
- the diagonal annulus term from `d vartheta_epsilon` must be separated
  from collar terms, since it is supported on the diagonal, not on
  `supp d chi`.

Thus the collar quotient is locally constructible but not yet a proved
factorization quotient.

### Koppelman Differential Identity

The staged BMK fixture supplies external support for the uncut kernel and
the classical Koppelman homotopy formula. It does not supply the
manuscript's cutoff-current identity.

The internal identity that would close the lane should have the form
\[
  \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
  =
  M_{\chi^2}-i_Np_N+E_{\chi,N},
\]
with `M_{chi^2}` becoming `id` on the relative local region where
`chi=1`. To prove it one must specify and verify:

1. whether the differential in the kernel identity is
   `bar partial_zeta`, `bar partial_z`, or the total product
   differential, including Koszul signs;
2. the orientation and scalar in the annular limit from
   `d vartheta_epsilon`;
3. the finite Taylor/current subtraction that changes the full diagonal
   identity into the finite projector `i_Np_N`;
4. the finite-window current quotient or restricted habitat on which
   high moments and the scalar moment are genuinely zero;
5. descent of the chosen `H_{chi,N}` to that habitat.

These data are not present in the current manuscript block. Therefore
the proof is not closed as written.

## Exact Blocker

The precise obstruction is the triple
\[
  \operatorname{Ob}_{276,N}
  =
  \left(
    \operatorname{ob}_{\mathrm{diag\mbox{-}sign}},
    \operatorname{ob}_{\mathrm{curr},N},
    \operatorname{ob}_{\mathrm{collar\mbox{-}fact}}
  \right).
\]

- `ob_diag-sign`: the missing computation of the cutoff annulus current
  and its sign/scalar relative to the manuscript's
  `(2 pi i)^(-2)` BMK convention and the residue-current convention.
- `ob_curr,N`: the nonzero scalar and high-moment classes
  `Delta_{0,0}` and `Delta_{a,b}` for `a+b>N`, plus the missing descent
  of `H_chi` through the quotient killing them.
- `ob_collar-fact`: the missing proof that the collar-support quotient is
  compatible with all extension-by-zero factorization structure maps,
  not only with one nested pair of polydisks.

If these three entries are supplied, the finite-window BMK theorem can be
made theorem-grade. Without them the safe manuscript status is:

- `H_chi` exists as a cutoff current operator on fixed finite
  configuration strata;
- `p_N` and `i_N` are the correct finite-window Matlis moment maps after
  analytic current normalization is declared;
- the arity-two Hamiltonian/Matlis formula follows from the internal
  residue calculation;
- the displayed differential identity is a construction target unless it
  is explicitly restricted to a finite-window relative current quotient
  with a well-defined `H_{chi,N}`.

## Commands Run

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
awk '/^## IV\./,/^## V\./ {print}' /Users/raeez/ecosystem/INVARIANTS.md
awk '/^## VIII\./,/^## IX\./ {print}' /Users/raeez/ecosystem/AGENTS-HARNESS.md
git status --short
git diff --cached --name-only
git diff --name-only
rg -n "BMK|Bochner|Martinelli|Koppelman|current limit|cutoff|finite-window|moment projection|collar|principal part|residue|boundary" main.tex appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md
nl -ba main.tex | sed -n '1210,1475p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '360,610p'
sed -n '1,230p' reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md
sed -n '1,260p' references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md
sed -n '1,260p' references/primary-sources/matlis-local-cohomology-residue-anchor.md
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,260p'
sed -n '150,390p' reconstitution/bm-transfer-native-e2-construction-2026-04-30.md
git show :appendix-factorization-current-conventions.tex | nl -ba | sed -n '399,690p'
git show :main.tex | nl -ba | sed -n '1242,1452p'
```

## Files Changed

- Added
  `reconstitution/swarm-2026-04-30-agent-276-bmk-kernel-current-limit-construction-push.md`.

No other file was edited.
