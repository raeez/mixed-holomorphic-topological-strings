# Phase-4 EXEC W5-X28: Authorship Attribution Audit

**Agent.** W5-X28 = Authorship Attribution Audit, attack-heal swarm
wave 5. **Mode.** Read-only. **Authorship.** Raeez Lorgat. **Date.**
2026-04-28.

---

## §1. Charter

Verify authorship and attribution discipline against
`~/ecosystem/INVARIANTS.md` invariants:

- **commits-carry-no-LLM-attribution** — no `Co-Authored-By: Claude`,
  `Generated with [Claude Code]`, `noreply@anthropic.com`, or
  equivalent footers on any commit in the branch history.
- **every-file-into-the-repo rule** — author attribution lives in a
  tracked file (`authors.tex`); no shadow attribution in scratch.
- **Russian-school voice** — sole human author, named attribution to
  primary sources only, no LLM byline.

---

## §2. Method

1. Read `authors.tex` directly.
2. Grep `main.tex`, `abstract.tex`, `preamble.tex`, `commands.tex`,
   `mathmacros.tex`, `notation.tex`, `nomenclature.tex` for author
   attribution markers (case-insensitive: `claude`, `anthropic`,
   `openai`, `gpt`, `codex`, `llm`, `co-authored-by`, `generated with`).
3. Recursive grep across all 182 `*.md` files in `reconstitution/` for
   strict LLM-attribution markers (`Co-Authored-By`, `Generated with`,
   `Claude Code`, `claude.ai`, `anthropic.com`, `noreply@anthropic`).
4. `git log --all --pretty=format:"%H%n%B"` followed by case-insensitive
   grep for the same attribution markers in commit messages.
5. Header scan of all 21 `*.py` scripts in `scripts/` for any author /
   copyright block carrying LLM attribution.
6. Compute attribution-purity score = (clean files) / (total files
   audited).

---

## §3. Findings by lane

### §3.1 `authors.tex`

```
\author{Raeez Lorgat}
\email{root@raeez.com}
\urladdr{http://math.raeez.com}
```

Three lines. Sole author Raeez Lorgat. No LLM, agent, Claude, GPT,
Anthropic, OpenAI, or Codex byline. **CLEAN.**

### §3.2 `main.tex` preamble + `abstract.tex` + acknowledgements

`main.tex:6` inputs `authors.tex`. `main.tex:36` sets PDF metadata
`pdfauthor={Raeez Lorgat}`. `main.tex:39-41` rebinds the memoir
`\@author` macro to `Raeez Lorgat`. No second author block, no
contributor block, no affiliation block, no acknowledgements block
referencing any LLM, agent, or AI assistant. The 60+ `author={...}`
hits in `main.tex` lines 5971-6300 are all bibliography entries for
primary-source citations (Bershadsky, Cecotti, Ooguri, Vafa; Witten;
Costello; Loday; Quillen; Tsygan; Gwilliam; Williams; Kontsevich;
Schwarz; Zaboronsky; Harish-Chandra; Wallach; Levasseur; Stafford;
Procesi; Razmyslov; Matlis; Hartshorne; Kunz; Cox; Dickenstein;
Beilinson; Feigin; Mazur; Priddy; Vallette; Capelli) — Russian-school
named-attribution, no AI bylines.

`abstract.tex` is 46 lines of pure mathematical prose. No author block.
**CLEAN.**

`preamble.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`,
`nomenclature.tex` — zero matches for any attribution marker. **CLEAN.**

### §3.3 `reconstitution/*.md` (182 files, internal scratch)

Recursive grep for `Co-Authored-By|Generated with|Claude Code|claude.ai|anthropic.com|noreply@anthropic`
returns **2 file matches**, both false positives:

- `reconstitution/phase4-G6-editorial-roadmap-2026-04-28.md:331` —
  `\.claude/` discussed as a `.gitignore` candidate (Claude Code
  session config directory, not attribution).
- `reconstitution/phase4-G6-editorial-roadmap-2026-04-28.md:407` —
  the line `**No "Co-Authored-By: Claude" footers** on Wave-3
  inscription commits (per CLAUDE.md inherited rule "commits-carry-no-LLM-attribution").`
  This is an explicit *prohibition*, not an attribution.
- `reconstitution/phase4-exec-G2-M2-BCH-cocycle-2026-04-28.md:293` —
  the substring "generated with" appears in `Random inputs are
  generated with seed-deterministic ...` (computational provenance,
  not LLM attribution).

No actual LLM attribution in any of the 182 reconstitution files.
**CLEAN** (severity 0; the two pattern hits are negative-lexicon — they
mention the prohibited markers in order to prohibit them).

### §3.4 `git log --all` commit messages

`git log --all --pretty=format:"%B"` piped to `grep -ciE "co-authored-by|generated with|claude code|claude.ai|anthropic.com|noreply"`
returns **0 matches** across the full branch history (40+ commits
from `e4786f0` initial to `d3ce80c` head).

The only commit message matching the substring `claude` at all is
`82571ab CLAUDE.md + AGENTS.md: inherit ~/ecosystem/INVARIANTS.md ...`
— this references the filename `CLAUDE.md`, not authorship. **CLEAN.**

### §3.5 `scripts/*.py` (21 files)

Case-insensitive grep across all 21 Python scripts for `claude`,
`anthropic`, `openai`, `gpt`, `codex`, `llm` returns **0 matches**.
Header inspection of `check_moyal_coefficients.py` and other key
scripts shows standard module docstrings naming the proposition or
theorem the script verifies — Russian-school named-attribution, no AI
byline. **CLEAN.**

### §3.6 `CLAUDE.md` (root + worktree)

Two `CLAUDE.md` files exist in tree:
`/Users/raeez/topological-strings/CLAUDE.md` and
`/Users/raeez/topological-strings/.claude/worktrees/ts-b-w2/CLAUDE.md`.
Both carry the line `For Claude Code, Codex CLI, and any GPT-5.5 /
GPT-5-Codex-class agent ...` (line 28). This is a *harness instruction*
to the local agent runtime, not an authorship claim — `CLAUDE.md` is
the agent-instruction file specified by `~/ecosystem/INVARIANTS.md`,
not a manuscript artifact. The worktree file is under `.claude/`,
which is gitignored (verified: `.claude/` is not tracked by `git
ls-files`). **CLEAN by exemption** (CLAUDE.md is non-reader-visible
agent infrastructure).

---

## §4. Attribution-purity scorecard

| Lane                                  | Files audited | LLM attribution | Status |
|---------------------------------------|---------------|-----------------|--------|
| `authors.tex`                         | 1             | 0               | CLEAN  |
| TeX preamble + abstract + acknowledg. | 7             | 0               | CLEAN  |
| `reconstitution/*.md`                 | 182           | 0 (2 negative-lexicon hits) | CLEAN |
| `git log --all` commit messages       | ~45 commits   | 0               | CLEAN  |
| `scripts/*.py` headers                | 21            | 0               | CLEAN  |
| Reader-visible total                  | ~210 files + 45 commits | 0     | CLEAN  |

**Attribution-purity score: 100%** across all reader-visible TeX,
commit history, computational scripts, and internal scratch reports.
The zero hits are not approximate — they are exact: every attribution
marker scan returns either no matches or only negative-lexicon /
filename-of-instruction-file false positives.

---

## §5. Verdict

**CERTIFY.** The repository fully complies with the
`commits-carry-no-LLM-attribution` and `every-file-into-the-repo`
invariants from `~/ecosystem/INVARIANTS.md`. Sole author Raeez Lorgat
is correctly attributed in `authors.tex`, propagated through the memoir
`\@author` macro, sealed into PDF metadata, and reflected uniformly
across the 45-commit history and all 21 computational scripts. Russian-
school named-attribution discipline is intact: every `author={...}` in
`main.tex` is a bibliography citation to a primary source. No LLM, AI,
Claude, GPT, Anthropic, OpenAI, or Codex byline appears anywhere in
the reader-visible manuscript, the build apparatus, the script
provenance, the commit history, or the internal reconstitution scratch.

**No cleanup proposal required.** No severity-1 or severity-2 findings.

---

## §6. Recommendation

None. Authorship discipline is a closed audit lane.

**Optional follow-up.** If a future inscription pass adds an
acknowledgements section, ensure it lists only human collaborators or
cites primary-source references — never agent / LLM / harness names.
The CLAUDE.md harness-instruction file should remain agent-only and
non-reader-visible (its mentions of "Claude Code" are harness
configuration, not authorship). The `.claude/` directory is gitignored
and contains worktree session state — it should remain so.

End of Phase-4 EXEC W5-X28 audit.
