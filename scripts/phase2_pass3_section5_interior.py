#!/usr/bin/env python3
"""Phase-2 pass 3: section-5 interior + section 7 assembly + tail fixes.

- new subsection header for the stranded uniqueness/rigidity block (after T3 input)
- five stratified subsubsections promoted to subsections
- graph-formalism block and non-scalar quantum tail moved from section 5 to
  section 7, placed between the P1-head input and the Ob_T assembly block
- T1/T2 starred subsections numbered (first -> subsection, rest -> subsubsection)
- Examples subsubsections promoted to subsections
- stale Appendix pointer to app:comparison-conventions corrected
Backups under .build_logs/.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "main.tex"
T1 = ROOT / "tate-T1-weighted-completion.tex"
T2 = ROOT / "tate-T2-nilpotent-truncation.tex"
BK = ROOT / ".build_logs"

main = MAIN.read_text().splitlines(keepends=True)


def assert_starts(lines, n, prefix, name="main"):
    actual = lines[n - 1].lstrip()
    assert actual.startswith(prefix), f"{name}:{n}: expected {prefix!r}, got {actual[:70]!r}"


def seg(a, b):
    return main[a - 1 : b]


assert_starts(main, 9288, r"\begin{cor}[Moment-map specialisation]")
assert_starts(main, 10910, r"\subsubsection{First-order Poisson identification}")
assert_starts(main, 12110, r"\subsubsection{Quantization and the brane trace map}")
assert_starts(main, 12791, r"\subsubsection{Graph formalism and specialization datum}")
assert_starts(main, 13373, r"\subsubsection{Formal Weyl/Moyal algebra, all orders}")
assert_starts(main, 13822, r"\begin{prob}[Non-scalar quantum \(P_0\)-operation obstruction complex]")
assert_starts(main, 14390, r"\end{prob}")
assert_starts(main, 14392, r"\begin{prop}[Open-line Weyl boundary product from midpoint kernel]")
assert_starts(main, 14533, r"\subsubsection{Third-order Costello graph class}")
assert_starts(main, 15317, r"\subsection{Tate-coefficient cotangent lift")
assert_starts(main, 15731, r"\subsubsection{The single brane:")
assert_starts(main, 15751, r"\subsubsection{Rank two:")
assert_starts(main, 15838, r"\subsubsection{The brane stack:")
assert_starts(main, 15929, r"(Appendix~\ref{app:comparison-conventions},")

# promotions in place (lines not moving)
for n in (10910, 12110, 13373, 14533, 15731, 15751, 15838):
    main[n - 1] = main[n - 1].replace("\\subsubsection{", "\\subsection{", 1)
main[15929 - 1] = main[15929 - 1].replace(
    "(Appendix~\\ref{app:comparison-conventions},", "(\\S\\ref{app:comparison-conventions},", 1
)

uniq_header = [
    "\\subsection{Uniqueness and rigidity of the trace coordinate}\\label{ssec:trace-coordinate-uniqueness}\n",
    "\n",
]

block_g = seg(12791, 13372)
block_g[0] = block_g[0].replace("\\subsubsection{", "\\subsection{", 1)
block_t = (
    ["\\subsection{Non-scalar quantum obstruction complexes and the \\texorpdfstring{$\\theta_3$}{theta3} window}\\label{ssec:nonscalar-quantum-obstructions}\n", "\n"]
    + seg(13822, 14390)
    + ["\n"]
)

out = []
out += seg(1, 9287)
out += uniq_header
out += seg(9288, 12790)
out += seg(13373, 13821)        # block G removed; Weyl/Moyal continues
out += seg(14391, 15316)        # block T removed (14391 blank kept)
out += block_g + ["\n"] + block_t
out += seg(15317, len(main))

BK.mkdir(exist_ok=True)
for src in (MAIN, T1, T2):
    shutil.copy2(src, BK / (src.name + ".pre-phase2-pass3"))

MAIN.write_text("".join(out))


def renumber(path, keep_first_as_subsection=True):
    lines = path.read_text().splitlines(keepends=True)
    first = True
    for i, l in enumerate(lines):
        if l.lstrip().startswith("\\subsection*{"):
            if first and keep_first_as_subsection:
                lines[i] = l.replace("\\subsection*{", "\\subsection{", 1)
                first = False
            else:
                lines[i] = l.replace("\\subsection*{", "\\subsubsection{", 1)
    path.write_text("".join(lines))


renumber(T1)
renumber(T2)
print(f"main.tex: {len(main)} -> {len(out)} lines; T1/T2 renumbered")
