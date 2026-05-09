# Agent 144 - Distributional Primitive for Wavefront Eta

Status: patched owned Tate theorem surface and this report.  No commits or
pushes.

## Stable Core

The Agent 139 obstruction is exact in a minimal enlarged local
distributional counterterm complex, not in the original regular-density
quotient complex.

The repaired theorem is
`thm:wt-wavefront-distributional-primitive-cone`.  For a compatible
finite-window wavefront residual, it defines
\[
  \widetilde{\mathcal Q}^{\bullet,\mathrm{WFpr}}_{w,M}(I)
    =
  \mathcal Q^\bullet_{w,M}(I)\widehat{\oplus}
  \mathbb C[[\hbar]]\cdot p^{\mathrm{WF}}_{n_0,M},
  \qquad |p^{\mathrm{WF}}_{n_0,M}|=0,
\]
with
\[
  \widetilde d_Mp^{\mathrm{WF}}_{n_0,M}
    =
  -\,\widehat{\mathfrak s}^{\mathrm{WF}}_{n_0,M},
  \qquad
  \widehat{\mathfrak s}^{\mathrm{WF}}_{n_0,M}
    =
  \mathfrak o^{\mathrm{ns,WF}}_{n_0,M}
    \in Z^1(\mathcal Q^\bullet_{w,M}(I)).
\]
Since
\[
  q_M\widehat{\mathfrak s}^{\mathrm{WF}}_{n_0,M}
    =
  \mathfrak s^{\mathrm{WF}}_{n_0,M},
\]
the exact primitive is
\[
  C^{\mathrm{sing}}_{n_0,M}=p^{\mathrm{WF}}_{n_0,M},
  \qquad
  \bar d_Mq_M(C^{\mathrm{sing}}_{n_0,M})
    =
  -\,\mathfrak s^{\mathrm{WF}}_{n_0,M}.
\]

The extension is a cone on the closed wavefront residual.  It is local:
the new generator is assigned the same support and wavefront cone as the
wavefront residual.  It is continuous for the \(\hbar\)-adic,
scalar-contact, and finite-window filtrations.  It is compatible with
finite-window truncation and admissible weight transport by
\[
  \widetilde\pi_{M,N}p^{\mathrm{WF}}_{n_0,M}
    =
  p^{\mathrm{WF}}_{n_0,N},
  \qquad
  \widetilde R^M_{w,w'}p^{\mathrm{WF}}_{n_0,M,w}
    =
  p^{\mathrm{WF}}_{n_0,M,w'}.
\]

This does not smooth a singular current.  Inside the original
\(\mathcal Q^\bullet_{w,M}(I)\), the obstruction remains exactly
\(\eta^{\mathrm{reg}}_{n_0,M}\).

## Build-Hygiene Repair

Agent 136's `/tmp` `pdflatex` failure at
`tate-T1-weighted-completion.tex:2211` came from
`\tag{\ast}` inside a `\[` display.  I replaced that display by a
numbered `equation` environment carrying the same label
`eq:wt-wavefront-singular-component`.  The fatal `Missing $ inserted`
stop is cleared.

## Repaired Labels

- `eq:wt-wavefront-singular-component`
- `thm:wt-wavefront-distributional-primitive-cone`

## Valid Attacks

```yaml
- id: A1-144-01
  severity: 1
  status: healed
  lens: original-complex exactness
  target: thm:wt-wavefront-singular-current-eta-obstruction
  claim: The wavefront graph theorem itself supplies
    C^{sing}_{n0,M} in the original \mathcal Q^\bullet_{w,M}(I).
  broken_step: Agent 139 proved only the iff condition in the quotient
    complex.  No intrinsic primitive in the original Costello counterterm
    complex is constructed.
  minimal_heal: Add a separate primitive-cone extension and keep original
    exactness equivalent to eta^{reg}_{n0,M}=0.

- id: A1-144-02
  severity: 1
  status: healed
  lens: differential-square
  target: candidate primitive differential
  claim: One may set d of a primitive equal to the nonregular quotient
    representative alone.
  broken_step: The nonregular summand is closed only after adding the
    regular summand; otherwise d^2 of the new generator may land in
    X^{reg}.
  minimal_heal: Use the closed lift
    \widehat{s}^{WF}_{n0,M}=o^{ns,WF}_{n0,M}.

- id: A1-144-03
  severity: 2
  status: healed
  lens: finite-window compatibility
  target: primitive extension tower
  claim: A formal primitive at one window automatically defines an inverse
    system.
  broken_step: Truncation compatibility requires the residual family to
    satisfy pi_{M,N} o_M=o_N.
  minimal_heal: Add that compatibility as a hypothesis and define
    \widetilde\pi_{M,N}p_M=p_N.

- id: A1-144-04
  severity: 2
  status: healed
  lens: TeX build hygiene
  target: eq:wt-wavefront-singular-component
  claim: The tagged display compiles as written.
  broken_step: \tag was placed inside a \[...\] display and caused
    `Missing $ inserted` at tate-T1-weighted-completion.tex:2211.
  minimal_heal: Replace the display by an equation environment with the
    same label.
```

## Verification

Commands run:

```bash
git diff --check -- tate-T1-weighted-completion.tex
grep -n '[[:blank:]]$' tate-T1-weighted-completion.tex
rg -n -F "\\tag{\\ast}" tate-T1-weighted-completion.tex
rg -n -F "thm:wt-wavefront-distributional-primitive-cone" tate-T1-weighted-completion.tex
rg -n -F "eq:wt-wavefront-singular-component" tate-T1-weighted-completion.tex
mkdir -p /tmp/topological-strings-agent144-build
pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/topological-strings-agent144-build main.tex
git diff --cached --check -- \
  tate-T1-weighted-completion.tex \
  reconstitution/swarm-2026-04-30-agent-144-distributional-primitive-for-wavefront-eta.md
git diff --cached --name-only -- \
  tate-T1-weighted-completion.tex \
  reconstitution/swarm-2026-04-30-agent-144-distributional-primitive-for-wavefront-eta.md
```

Results:

- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- `\tag{\ast}` scan returned no hits.
- label scans found the repaired equation and primitive-cone theorem.
- `/tmp` `pdflatex` completed successfully and wrote
  `/tmp/topological-strings-agent144-build/main.pdf`.
- The LaTeX run still has one-pass undefined-reference and destination
  warnings already present in the shared build surface; it no longer stops
  at tate-T1.
- cached diff check passed after staging.
- cached name-only listed exactly the two owned paths.

## Files Changed/Staged

- `tate-T1-weighted-completion.tex`
- `reconstitution/swarm-2026-04-30-agent-144-distributional-primitive-for-wavefront-eta.md`

## Remaining Theorem Obligations

- Realize the primitive cone by an intrinsic BV local functional if the
  manuscript later forbids formal primitive generators.
- Populate the finite-window graph array enough to decide whether the
  original \(\eta^{\mathrm{reg}}_{n_0,M}\) already vanishes without the
  cone extension.
- Extend the primitive cone to a full dg Lie counterterm habitat only if
  later QME iterations require brackets with the new primitive generator.
