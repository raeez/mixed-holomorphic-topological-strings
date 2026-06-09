#!/usr/bin/env python3
"""Phase-2 pass 1: front-matter compression + section-1 reorder of main.tex.

Segment-based rebuild with content assertions. Creates a plain backup copy
at .build_logs/main.tex.pre-phase2-pass1 before writing.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "main.tex"
BACKUP = ROOT / ".build_logs" / "main.tex.pre-phase2-pass1"

lines = MAIN.read_text().splitlines(keepends=True)  # 0-indexed list


def seg(a, b):
    """1-indexed inclusive original line range."""
    return lines[a - 1 : b]


def assert_starts(n, prefix):
    actual = lines[n - 1].lstrip()
    assert actual.startswith(prefix), f"line {n}: expected {prefix!r}, got {actual[:70]!r}"


# --- content assertions on every cut boundary ---
assert_starts(49, r"\phantomsection\label{ssec:open-operator-modular-lift}")
assert_starts(83, r"\input{abstract.tex}")
assert_starts(85, r"\section*{Summary}")
assert_starts(377, r"\begin{thm}[Main theorem, introductory form]")
assert_starts(470, r"\end{thm}")
assert_starts(473, r"\phantomsection\label{tab:intro-theorem-status}")
assert_starts(668, r"\tableofcontents")
assert_starts(671, r"\input{local-dictionary}")
assert_starts(673, r"\subsection*{Conventions and notation for the local theorem}")
assert_starts(912, r"\paragraph{Compact comparison hypotheses.}")
assert_starts(930, r"\subsection*{The formal-Darboux theorem and its boundary}")
assert_starts(994, r"\subsection*{\texorpdfstring{Finite \(N\) leftovers")
assert_starts(996, r"\addcontentsline{toc}{subsection}{Finite")
assert_starts(1075, r"\section{The setup}")
assert_starts(1438, r"\subsection{Mixed holomorphic-topological strings}")
assert_starts(3210, r"\subsection{Notation for the local theorem}")
assert_starts(3279, r"\subsection{Three notions of locality}")
assert_starts(3392, r"\subsection{Unitarity}")
assert_starts(3462, "The configuration is fixed:")
assert_starts(3472, r"\section{The shifted-cotangent BF Lie algebra}")
assert_starts(8393, r"\section{CE/PV dictionary as Koszul resolution}")

# --- extracted blocks ---
theorem_block = (
    ["\\subsection{The local stalk theorem: introductory form}\\label{ssec:intro-main-theorem-statement}\n", "\n"]
    + seg(377, 470)
    + ["\n"]
)

notation_block = seg(3210, 3278)
notation_block[0] = "\\subsection*{Notation for the local theorem}\\label{ssec:intro-notation-index}\n"
notation_block.insert(1, "\\addcontentsline{toc}{subsection}{Notation for the local theorem}\n")

finiteN_block = seg(994, 1073)
finiteN_block[0] = finiteN_block[0].replace("\\subsection*{", "\\subsection{", 1)
finiteN_block = [l for l in finiteN_block if not l.lstrip().startswith("\\addcontentsline")]

localities_block = seg(3279, 3391)
unitarity_block = seg(3392, 3461)

# --- rebuild ---
out = []
out += seg(1, 48)                      # preamble .. \begin{document}
out += seg(50, 84)                     # title page + abstract (stray label dropped)
out += seg(667, 928)                   # TOC, dictionary input, conventions
out += ["\n"] + notation_block         # notation joins the conventions block
out += ["\n"]
out += seg(1074, 1437)                 # blank + section 1 head + 1.1
out += ["\n"] + localities_block       # 1.2 <- three localities (was 1.6)
out += ["\n"] + unitarity_block        # 1.3 <- unitarity (was 1.7)
out += ["\n"]
out += seg(1438, 3209)                 # mixed HT strings, local mixed model, local setup
out += ["\n"] + theorem_block          # closing subsection: the stalk theorem
out += seg(3462, 3470)                 # closing paragraph of section 1
out += seg(3471, 8392)                 # sections 2..4
out += ["\n"] + finiteN_block + ["\n"]  # finite-N leftovers closes section 4
out += seg(8393, len(lines))           # section 5 .. end

BACKUP.parent.mkdir(exist_ok=True)
shutil.copy2(MAIN, BACKUP)
MAIN.write_text("".join(out))
print(f"rewrote main.tex: {len(lines)} -> {len(out)} lines (backup at {BACKUP})")
