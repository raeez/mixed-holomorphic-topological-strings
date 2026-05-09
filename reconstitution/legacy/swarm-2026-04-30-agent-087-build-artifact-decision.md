# Agent 087 Build Artifact Staging Decision Audit

Lane: final PDF/build artifact staging decision audit after Agent 083 clean build.

## Commands run

- `sed -n '1,240p' CLAUDE.md`
- `rg --files reconstitution`
- `git status --short -- out/main.pdf main.pdf`
- `sed -n '1,240p' Makefile`
- `test -f .gitignore && sed -n '1,240p' .gitignore || true`
- `sed -n '1,220p' out/main.log`
- `sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-083-final-overfull-layout.md`
- `sed -n '241,520p' Makefile`
- `tail -n 180 out/main.log`
- `git ls-files -s -- out/main.pdf main.pdf`
- `git check-ignore -v -- out/main.pdf main.pdf`
- `git log --oneline --decorate -n 12 -- out/main.pdf main.pdf`
- `git status --short`
- `pdfinfo out/main.pdf`
- `shasum -a 256 out/main.pdf main.pdf`
- `git hash-object out/main.pdf main.pdf`
- `git check-ignore -v --no-index -- out/main.pdf main.pdf out/foo.pdf`
- `git log --follow --name-status --oneline -n 20 -- out/main.pdf`
- `git log --follow --name-status --oneline -n 20 -- main.pdf`
- `ls -l out/main.pdf main.pdf`
- `rg --files -g '.gitattributes' -g 'README.md' -g 'readme.md' -g 'README*'`
- `rg -n "out/main\\.pdf|main\\.pdf|release pdf|Regenerate manuscript PDF|/out/|Build output|generated artifact|artifact" .gitignore Makefile README.md reconstitution -g '*.md'`
- `sed -n '1,110p' README.md`
- `sed -n '110,160p' reconstitution/phase4-exec-W5-X33-build-system-2026-04-28.md`
- `sed -n '330,350p' reconstitution/phase4-exec-W5-X33-build-system-2026-04-28.md`
- `sed -n '130,145p' reconstitution/swarm-2026-04-30-agent-077-build-layout-audit.md`
- `git diff --stat -- out/main.pdf main.pdf`
- `git diff --summary -- out/main.pdf main.pdf`
- `rg -n "^! |Emergency stop|Fatal error|Undefined control sequence|LaTeX Error|Overfull|undefined references|undefined citations|Rerun to get cross-references|Label\\(s\\) may have changed" out/main.log`
- `pdfinfo main.pdf`
- `git show --stat --oneline --summary HEAD -- out/main.pdf main.pdf`
- `git diff --cached --name-status -- out/main.pdf main.pdf`
- `git status --short --untracked-files=all -- reconstitution/swarm-2026-04-30-agent-087-build-artifact-decision.md out/main.pdf main.pdf`

## Artifact Status

`git status --short -- out/main.pdf main.pdf` reports:

```text
 M out/main.pdf
```

`main.pdf` has no working-tree delta.  `out/main.pdf` is tracked and modified
relative to HEAD.  `git ls-files -s -- out/main.pdf main.pdf` reports tracked
index entries for both PDFs:

```text
100644 a456243f5d140af1e8313fb3444ab03503b39995 0	main.pdf
100644 572d1398c53f3426c444c3f167c1eb895a174310 0	out/main.pdf
```

Current generated artifact:

- `out/main.pdf`: 255 pages, 1,502,615 bytes.
- `out/main.pdf` SHA-256:
  `4eac1059c8302b2d7ed6148cc386882e293021bf301fd23a070d1f56f1a4c90c`.
- `out/main.pdf` Git blob hash:
  `7e59a3c78325ee227d788601edd924d49a6da929`.
- `git diff --stat -- out/main.pdf main.pdf` reports
  `out/main.pdf | Bin 1478966 -> 1502615 bytes`.

Agent 083 reports `make pdf` passed with exit code 0, produced the same
255-page, 1,502,615-byte `out/main.pdf`, and cleared all overfull boxes.
The current `out/main.log` ends with:

```text
Output written on out/main.pdf (255 pages, 1502615 bytes).
```

The targeted fatal/layout scan over `out/main.log` found no hits for fatal
TeX errors, undefined controls, LaTeX errors, overfull boxes, undefined
reference/citation warnings, or rerun warnings.

For contrast, the tracked root `main.pdf` is stale relative to the present
build: 154 pages, 1,023,660 bytes, old title metadata, SHA-256
`919f884dd44d11b444c29f91bceb635af255dcf7582d37a430eea6d28bc730a0`.

## Repo Policy Inference

The repository ignores the output directory in `.gitignore`:

```text
/out/
```

With `git check-ignore -v --no-index`, this rule matches `out/main.pdf` and
other hypothetical output files.  Since `out/main.pdf` is already tracked,
the ignore rule prevents accidental admission of new build debris but does
not remove or suppress the tracked PDF.

The Makefile makes `out/main.pdf` the normal build product:

- `.DEFAULT_GOAL := pdf`
- `OUTDIR:=out`
- `TEXFLAGS := -output-directory=out -interaction=nonstopmode`
- the `pdf` target creates `out/` and builds `main.tex` through the multi-pass
  `pdflatex` cycle.

`README.md` also states: "The main PDF is written to `out/main.pdf`."

Historical evidence supports deliberate tracking, not accident:

- `git log --follow --name-status --oneline -n 20 -- out/main.pdf` shows
  repeated PDF updates through release and manuscript commits, including
  `release pdf`, `Regenerate manuscript PDF`, and recent title/manuscript
  updates.
- `reconstitution/phase4-exec-W5-X33-build-system-2026-04-28.md` explicitly
  audits `out/` as ignored while noting `tracked: out/main.pdf only
  (intentional)`, severity 0.
- The same W5-X33 audit calls `out/main.pdf` the current canonical artifact.
- Agent 077 reports that only `out/main.pdf` is tracked among generated files
  in `out/`; ignored aux/log/toc/index debris remains unstaged.

Policy inference: `/out/` is an ignored generated-output directory with one
intentional tracked exception, `out/main.pdf`, used as the canonical rendered
manuscript/release artifact.  The tracked exception should be refreshed when
the source state being released has been clean-built and accepted.

## Recommendation

`out/main.pdf` should be staged as the tracked generated artifact for this
release state, but by the integration owner after confirming no later source
edits landed after Agent 083's build.  Agent 087 did not stage it.

The reason is policy-based: this repo already tracks `out/main.pdf`
intentionally, the Makefile and README identify it as the canonical build
output, recent history repeatedly commits it, Agent 083 produced a clean
255-page build, and the modified working-tree PDF exactly matches Agent 083's
reported size/page count.

Do not stage arbitrary `out/` contents.  The policy exception is only
`out/main.pdf`.

## Residual Risk

- Multi-agent concurrency: if any source file changed after Agent 083's clean
  build, the current PDF may no longer match the final source state.  The
  integration owner should re-run or verify the final build immediately before
  staging the PDF.
- Root `main.pdf` remains tracked but stale.  This audit does not recommend
  changing it because the lane is restricted to the `out/main.pdf` decision;
  however, a release packager should decide whether to sync, remove, or
  explicitly deprecate the root artifact.
- PDF binaries include timestamps/metadata.  The current artifact is suitable
  under existing repo practice, but byte-for-byte reproducibility across later
  builds is not guaranteed unless the build environment fixes PDF metadata.
