# Swarm 2026-04-30 Agent 336: Control Surface Visibility Audit

Report-only audit.  No manuscript TeX edited.  No build run.

## Claim Attacked

Future agents loading the repository might miss the late theorem-control
predicates after concurrent top-level edits: native `\mathbb C^2`
holomorphic `E_2`; BMK
`\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`; `\theta_3` with
`\Delta^1_{M,N}` and secondary `\varprojlim^1H^0`; radial
`\Omega^{\mathrm{rad}}`, decorated PBW Stokes, and signed row; the
non-scalar QME finite-window matrix/Roos/curved-kernel criterion; and the
Vol II `chriss-ginzburg-rectify` mandate.

## Verdict

Observed, current checkout: the predicates are visible on all three
control surfaces that a future agent is told to load:

- `CLAUDE.md`;
- `AGENTS.md`;
- `reconstitution/attack-heal-latest-2026-04-30.md`.

No typo patch was necessary in `CLAUDE.md`, `AGENTS.md`, or
`reconstitution/attack-heal-latest-2026-04-30.md`.

## Exact Grep Anchors

Top-level load mandate and Vol II mandate:

- `CLAUDE.md:120-123` requires
  `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
  before manuscript-proper writing or theorem-lane reconstitution.
- `AGENTS.md:118-121` requires the same Vol II skill before editing.
- `AGENTS.md:1-7` states inheritance from `~/ecosystem/INVARIANTS.md`,
  `~/ecosystem/AGENTS-HARNESS.md`, and factual mirroring of `CLAUDE.md`.
- `reconstitution/attack-heal-latest-2026-04-30.md:129-140` requires
  `CLAUDE.md`, `AGENTS.md`, the snapshot, the Vol II skill, and names the
  binding late predicates.

Native `\mathbb C^2` holomorphic `E_2`:

- `CLAUDE.md:58-60` names the native `\mathbb C^2` holomorphic `E_2`
  taxonomy before curve reduction.
- `AGENTS.md:105-107` makes the same predicate binding before theorem work.
- `reconstitution/attack-heal-latest-2026-04-30.md:134-135` records it in
  the load mandate.
- `reconstitution/attack-heal-latest-2026-04-30.md:189-192` gives the
  detailed native holomorphic `E_2` surface.

BMK `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`:

- `CLAUDE.md:60-63` separates the one-pair analytic pro-Matlis retract
  from strict native all-window support-local current transfer and names
  `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`.
- `AGENTS.md:107-109` states the same BMK obstruction.
- `reconstitution/attack-heal-latest-2026-04-30.md:135-136` includes the
  BMK predicate in the mandate.
- `reconstitution/attack-heal-latest-2026-04-30.md:196-204` records the
  BMK obstruction tuple.

`\theta_3`, `\Delta^1`, and secondary `\varprojlim^1H^0`:

- `CLAUDE.md:63-68` says `\theta_3` requires a CE ancestor,
  scalar-zero Costello counterterm, or complete companion-face table, with
  `\Delta^1_{M,N}` and secondary `\varprojlim^1H^0`.
- `AGENTS.md:109-112` states the same gate.
- `reconstitution/attack-heal-latest-2026-04-30.md:136-137` includes the
  theta predicate in the mandate.
- `reconstitution/attack-heal-latest-2026-04-30.md:220-225` records
  `\Delta^1_{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N` and the
  secondary primitive-compatibility class.

Radial `\Omega^{\mathrm{rad}}`, decorated PBW Stokes, and signed row:

- `CLAUDE.md:68-71` gives the radial/Weyl theorem surface as
  `\Omega^{\mathrm{rad}}_{a,b}`, decorated PBW Stokes, and signed row in
  `\ker B_{a,b}^*`.
- `AGENTS.md:112-114` makes the radial/Weyl obstruction surface binding.
- `reconstitution/attack-heal-latest-2026-04-30.md:137-139` includes it in
  the mandate.
- `reconstitution/attack-heal-latest-2026-04-30.md:241-249` records the
  detailed `\Omega^{\mathrm{rad}}_{a,b}` cokernel and signed-row failure.

Non-scalar QME finite-window matrix/Roos/curved-kernel criterion:

- `CLAUDE.md:71-74` requires scalar projection, finite row arrays,
  `A^Mc=-r^M`, transition matrices, Roos compatibility, centrality
  homotopies, and a curved bulk-to-defect kernel.
- `AGENTS.md:114-117` states the same non-scalar QME criterion.
- `reconstitution/attack-heal-latest-2026-04-30.md:139-140` includes the
  finite-window matrix, Roos, and curved-kernel criterion in the load
  mandate.
- `reconstitution/attack-heal-latest-2026-04-30.md:205-218` records the
  fixed-window matrix obstruction and non-scalar graph/QME class.
- `reconstitution/attack-heal-latest-2026-04-30.md:266-276` leaves the
  Roos compatibility, bulk-to-defect kernel, centrality, and bracket
  homotopies as active obligations.

## Commands Run

```bash
sed -n '1,220p' ./CLAUDE.md
sed -n '1,260p' ./AGENTS.md
sed -n '1,240p' reconstitution/attack-heal-latest-2026-04-30.md
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,180p' main.tex
sed -n '1,220p' mathmacros.tex
sed -n '1,220p' commands.tex
rg -n -F -e 'Late 2026-04-30 theorem-control predicates' -e 'late 2026-04-30 theorem-control predicates' -e 'Top-Level Control Load Mandate' -e 'native \(\mathbb C^2\) holomorphic' -e 'native `\mathbb C^2` holomorphic `E_2`' -e '\operatorname{Ob}^{\Pi}_{\mathrm{BM}}' -e '\theta_3' -e '\Delta^1_{M,N}' -e '\varprojlim^1H^0' -e '\Omega^{\mathrm{rad}}' -e 'decorated PBW Stokes' -e 'signed row' -e 'non-scalar QME' -e 'A^Mc=-r^M' -e 'Roos' -e 'curved bulk-to-defect' -e 'chriss-ginzburg-rectify' CLAUDE.md AGENTS.md reconstitution/attack-heal-latest-2026-04-30.md
rg -n -F -e 'chriss' -e 'ginsburg' -e 'ginzberg' -e 'ginzburg' CLAUDE.md AGENTS.md reconstitution/attack-heal-latest-2026-04-30.md
rg -n -F -e 'Ob}^{Pi}' -e 'Ob}^{\Pi}' -e 'Ob}^{\\Pi}' -e 'Ob^{Pi}' -e 'Ob^{\Pi}' -e 'operatorname{Ob}' CLAUDE.md AGENTS.md reconstitution/attack-heal-latest-2026-04-30.md
nl -ba CLAUDE.md | sed -n '40,105p'
nl -ba CLAUDE.md | sed -n '116,126p'
nl -ba AGENTS.md | sed -n '1,18p'
nl -ba AGENTS.md | sed -n '95,135p'
nl -ba reconstitution/attack-heal-latest-2026-04-30.md | sed -n '120,220p'
nl -ba reconstitution/attack-heal-latest-2026-04-30.md | sed -n '220,285p'
test -e reconstitution/swarm-2026-04-30-agent-336-control-surface-visibility-audit.md; printf '%s\n' $?
git diff --cached --check -- reconstitution/swarm-2026-04-30-agent-336-control-surface-visibility-audit.md
```

## Checks

- `git diff --cached --check -- reconstitution/swarm-2026-04-30-agent-336-control-surface-visibility-audit.md` passed after staging the touched file.

## Files Changed

- `reconstitution/swarm-2026-04-30-agent-336-control-surface-visibility-audit.md`
