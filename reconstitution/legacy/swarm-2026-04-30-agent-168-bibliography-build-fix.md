# Agent 168 bibliography build fix

## Stable core

The reported hard stop is an `amsrefs` inner-key parsing error for the
Witten Chern-Simons bibliography entry.  In `amsrefs`, a `book={...}`
field inside an article-in-collection entry is resolved as an inner
bibliography object when its value contains `=`.  The inner object must
therefore be a key-value list beginning with a key such as `title`.

The invalid shape is:

```tex
book={\emph{The Floer Memorial Volume}, series={Progr. Math.}, ...}
```

Because `series=...` is present, `amsrefs` parses the whole `book`
value as an inner key-value list.  The first token is `\emph`, not a
legal key-name character, so `rkeyval` raises:

```text
Package rkeyval Error: Invalid key name character.
```

The minimal valid shape is the one currently present in `main.tex`:

```tex
book={
  title={The Floer Memorial Volume},
  series={Progr. Math.},
  volume={133},
  publisher={Birkh\"auser},
  place={Basel},
},
```

## Attack ledger

```yaml
id: A1-168-01
severity: 2
status: invalid
lens: amsrefs syntax
target: main.tex, Witten Chern-Simons bibliography entry
claim: the current worktree Witten entry still triggers rkeyval invalid-key failure
broken_step: current main.tex, staged main.tex, and HEAD main.tex all already use book={title={...}, ...}
evidence_type: command
evidence_ref: "pdflatex -output-directory=/tmp/topological-strings-agent-168 main.tex, two passes, exit 0"
files_read: [main.tex]
tools_used: [nl, rg, git show, pdflatex]
confidence: high
blast_radius: none for the current worktree
minimal_heal: no main.tex edit; preserve repaired syntax
residual: full make pdf was not run by instruction
deciding_evidence: none for this local bibliography failure
```

```yaml
id: A1-168-02
severity: 2
status: valid
lens: isolated negative reproducer
target: amsrefs book field syntax
claim: book={\emph{The Floer Memorial Volume}, series=...} is invalid amsrefs syntax
broken_step: the backslash command \emph appears where rkeyval expects an inner key name
evidence_type: failing_test
evidence_ref: "/tmp pdflatex minimal reproducer amsrefs-book-emph, exit 1, Package rkeyval Error: Invalid key name character"
files_read: [/usr/local/texlive/2025/texmf-dist/tex/latex/amsrefs/amsrefs.sty, /usr/local/texlive/2025/texmf-dist/tex/latex/amsrefs/rkeyval.sty]
tools_used: [rg, sed, pdflatex]
confidence: high
blast_radius: any nested book field mixing a formatted free-text title with later key-value fields
minimal_heal: put the volume title under title={...} inside book={...}, or use a canonical article-in-collection form
residual: none for Witten entry in the current worktree
deciding_evidence: passing isolated positive reproducer and two full /tmp manuscript pdflatex passes
```

## Fix made

No edit to `main.tex` was required in this checkout.  The worktree,
index, and `HEAD` versions already contain the minimal repaired
`book={title={The Floer Memorial Volume}, ...}` syntax for
`\bib{witten-cs}{article}`.  I did not overwrite or revert concurrent
changes.

This report was added as:

```text
reconstitution/swarm-2026-04-30-agent-168-bibliography-build-fix.md
```

## Verification

Commands run:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -jobname=amsrefs-book-emph \
  '<minimal invalid Witten entry with book={\emph{The Floer Memorial Volume}, series=...}>'
```

Result: exit 1, reproduces `Package rkeyval Error: Invalid key name character`.

```bash
pdflatex -interaction=nonstopmode -halt-on-error -jobname=amsrefs-book-nested \
  '<minimal valid Witten entry with book={title={The Floer Memorial Volume}, series=...}>'
```

Result: exit 0.

```bash
mkdir -p /tmp/topological-strings-agent-168
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=/tmp/topological-strings-agent-168 main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=/tmp/topological-strings-agent-168 main.tex
```

Result: both full manuscript passes exit 0 and write only
`/tmp/topological-strings-agent-168/main.pdf`.  The log contains no
`rkeyval` bibliography error.

## Files changed and staged state

Changed by this agent:

```text
reconstitution/swarm-2026-04-30-agent-168-bibliography-build-fix.md
```

Not changed by this agent:

```text
main.tex
out/main.pdf
```

No files were staged by this agent.

## Remaining build obligations

The full repository build target `make pdf` was not run, as instructed.
Existing unresolved references, layout warnings, and dirty worktree state
remain outside this agent's ownership.  A final integration owner should
run the sanctioned session-end build after the swarm surfaces converge.
