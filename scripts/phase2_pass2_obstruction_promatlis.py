#!/usr/bin/env python3
"""Phase-2 pass 2: section 6/7/8 topology repair + global-criterion move.

- prop:grav-ops core -> section 2 (new closing subsection, label sec:grav-ops)
- duplicate 6.2 intro prose deleted; Capelli paragraphs remain in section 6
- matching paragraph + strict-product remark -> head of the Ob_T block (section 7)
- tate-T4 input -> section 7 (subsections numbered)
- tate-P1 split at rmk:hadamard-vs-bmk: head stays (-> section 7, numbered),
  tail -> tate-P1b-bmk-promatlis-transfer.tex (-> section 8 before envelope block)
- thm:main-global-deligne-criterion block -> typed-boundary-open-closed.tex
Backups under .build_logs/.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "main.tex"
T4 = ROOT / "tate-T4-bv-vanishing.tex"
P1 = ROOT / "tate-P1-hadamard-mittag-leffler.tex"
P1B = ROOT / "tate-P1b-bmk-promatlis-transfer.tex"
TYPED = ROOT / "typed-boundary-open-closed.tex"
BK = ROOT / ".build_logs"

main = MAIN.read_text().splitlines(keepends=True)
typed = TYPED.read_text().splitlines(keepends=True)
p1 = P1.read_text().splitlines(keepends=True)
t4 = T4.read_text().splitlines(keepends=True)


def assert_starts(lines, n, prefix, name):
    actual = lines[n - 1].lstrip()
    assert actual.startswith(prefix), f"{name}:{n}: expected {prefix!r}, got {actual[:70]!r}"


def seg(lines, a, b):
    return lines[a - 1 : b]


# --- assertions ---
assert_starts(main, 3490, r"\section{\texorpdfstring{The derived commuting", "main")
assert_starts(main, 9190, r"\begin{thm}[Global open--closed obstruction criterion", "main")
assert_starts(main, 9404, r"\end{rmk}", "main")
assert_starts(main, 9406, r"\input{tate-T3-quillen-equivalence}", "main")
assert_starts(main, 15389, r"\input{tate-T4-bv-vanishing}", "main")
assert_starts(main, 15391, r"\subsection{Operators in the closed Hamiltonian sector}", "main")
assert_starts(main, 15428, "The open side of", "main")
assert_starts(main, 15445, r"Let $\mathfrak h=\widehat{\mathfrak h}", "main")
assert_starts(main, 15534, r"\begin{rmk}[Strict-product", "main")
assert_starts(main, 15578, "The Capelli scalar", "main")
assert_starts(main, 15617, r"\input{appendix-master-deformation-complex}", "main")
assert_starts(main, 15619, r"\subsection{Tate-coefficient cotangent lift", "main")
assert_starts(main, 15769, r"\input{appendix-matlis-principal-parts}", "main")
assert_starts(main, 15771, r"\subsection{Pro-Matlis envelope", "main")
assert_starts(main, 15926, r"\input{tate-P1-hadamard-mittag-leffler}", "main")
assert_starts(main, 15943, r"\input{typed-boundary-open-closed}", "main")
assert_starts(typed, 1073, r"Theorem~\ref{thm:main-global-deligne-criterion} states the OCA", "typed")
assert_starts(typed, 1079, r"\begin{defn}[Open--closed centrality convolution", "typed")
assert_starts(p1, 2684, r"\begin{rmk}[Hadamard parametrix versus the Bochner-Martinelli-Koppelman", "p1")

# --- blocks ---
globalcrit = seg(main, 9190, 9404)
grav_core = seg(main, 15445, 15532)
matching_par = seg(main, 15428, 15443)
strict_rmk = seg(main, 15534, 15576)

grav_block = (
    ["\\subsection{Operators in the closed Hamiltonian sector}\\label{sec:grav-ops}\n", "\n"]
    + grav_core
    + ["\n"]
)

# --- rebuild main.tex ---
out = []
out += seg(main, 1, 3489)
out += grav_block                       # section 2 closes with the operator algebra
out += seg(main, 3490, 9189)
out += [
    "The global open--closed comparison is the obstruction criterion of\n",
    "Theorem~\\ref{thm:main-global-deligne-criterion}.\n",
    "% MOVED: thm:main-global-deligne-criterion + addenda -> typed-boundary-open-closed.tex\n",
    "\n",
]
out += seg(main, 9405, 15388)
# T4 input dropped here (line 15389); blank 15390 kept; 6.2 header (15391) dissolved;
# intro duplicate 15393-15426 deleted; capelli paragraphs 15578-15615 stay.
out += ["\n"]
out += ["% MOVED: closed-sector operator algebra (prop:grav-ops) -> section 2; strict-product remark -> obstruction calculus\n", "\n"]
out += seg(main, 15578, 15616)
out += seg(main, 15617, 15618)          # input master-deformation + blank
out += ["\\input{tate-T4-bv-vanishing}\n", "\n"]
out += ["\\input{tate-P1-hadamard-mittag-leffler}\n", "\n"]
out += seg(main, 15619, 15620)          # Ob_T subsection header + following line
out += ["\n"] + matching_par + ["\n"] + strict_rmk + ["\n"]
out += seg(main, 15621, 15768)
out += seg(main, 15769, 15770)          # input matlis + blank
out += ["\\input{tate-P1b-bmk-promatlis-transfer}\n", "\n"]
out += seg(main, 15771, 15925)          # envelope block (8.6)
# old tate-P1 input at 15926 dropped
out += seg(main, 15927, len(main))

# --- typed: receive the global criterion ---
typed_out = seg(typed, 1, 1078) + globalcrit + ["\n"] + seg(typed, 1079, len(typed))

# --- tate-P1 split ---
p1_head = seg(p1, 1, 2683)
p1_tail = (
    ["\\subsection{The Bochner--Martinelli--Koppelman current transfer and the pro-Matlis retract}\\label{ssec:bmk-promatlis-transfer}\n", "\n"]
    + seg(p1, 2684, len(p1))
)
p1_head = [l.replace("\\subsection*{", "\\subsection{", 1) if l.lstrip().startswith("\\subsection*{") else l for l in p1_head]

# --- T4: number subsections ---
t4_out = [l.replace("\\subsection*{", "\\subsection{", 1) if l.lstrip().startswith("\\subsection*{") else l for l in t4]

BK.mkdir(exist_ok=True)
for src in (MAIN, TYPED, P1, T4):
    shutil.copy2(src, BK / (src.name + ".pre-phase2-pass2"))

MAIN.write_text("".join(out))
TYPED.write_text("".join(typed_out))
P1.write_text("".join(p1_head))
P1B.write_text("".join(p1_tail))
T4.write_text("".join(t4_out))
print(f"main.tex: {len(main)} -> {len(out)} lines")
print(f"typed: {len(typed)} -> {len(typed_out)} lines")
print(f"tate-P1 head: {len(p1)} -> {len(p1_head)} lines; tail file: {len(p1_tail)} lines")
