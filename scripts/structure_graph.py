#!/usr/bin/env python3
"""Reading-order label/ref graph for main.tex with \\input expansion.

Reports: section map with global positions, labels defined, references used,
and use-before-definition pairs in reading order. Read-only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_RE = re.compile(r"^\s*\\input\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|cref|Cref|autoref|pageref)\*?\{([^}]+)\}")
SEC_RE = re.compile(r"^\s*\\(section|subsection|subsubsection)\*?(?:\[[^\]]*\])?\{(.*)")


def walk(fname, seq, stack=()):  # seq: list of (file, line_no, text)
    path = ROOT / fname
    if not path.exists() and not fname.endswith(".tex"):
        path = ROOT / (fname + ".tex")
    if fname in stack:
        return
    try:
        lines = path.read_text(errors="replace").splitlines()
    except FileNotFoundError:
        return
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("%"):
            continue
        m = INPUT_RE.match(line)
        if m and m.group(1) not in ("mathmacros.tex", "authors.tex"):
            walk(m.group(1), seq, stack + (fname,))
        else:
            seq.append((path.name, i, line))


def main():
    seq = []
    walk("main.tex", seq)
    labels = {}   # key -> first definition global pos
    refs = {}     # key -> list of (global pos)
    secs = []     # (global pos, level, title, file, line)
    for g, (f, i, line) in enumerate(seq):
        sm = SEC_RE.match(line)
        if sm:
            secs.append((g, sm.group(1), sm.group(2)[:72], f, i))
        for key in LABEL_RE.findall(line):
            labels.setdefault(key, (g, f, i))
        for key in REF_RE.findall(line):
            refs.setdefault(key, []).append((g, f, i))

    mode = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if mode == "secs":
        for g, lvl, title, f, i in secs:
            indent = {"section": "", "subsection": "  ", "subsubsection": "    "}[lvl]
            print(f"{g:7d} {indent}{title}   [{f}:{i}]")
    elif mode == "ubd":
        # use-before-definition in reading order, sorted by gap
        rows = []
        for key, uses in refs.items():
            if key not in labels:
                rows.append((10**9, key, uses[0], None))
                continue
            dg, df, di = labels[key]
            first = min(uses)
            if first[0] < dg:
                rows.append((dg - first[0], key, first, (dg, df, di)))
        rows.sort(reverse=True)
        print(f"{len(rows)} use-before-def (or undefined) labels")
        for gap, key, (ug, uf, ui), d in rows[:120]:
            if d is None:
                print(f"UNDEF  {key}  first use {uf}:{ui}")
            else:
                print(f"gap{gap:7d}  {key}  use {uf}:{ui} -> def {d[1]}:{d[2]}")
    elif mode == "where":
        key = sys.argv[2]
        print("def:", labels.get(key))
        for u in refs.get(key, [])[:40]:
            print("use:", u)
    else:
        print(f"reading-order lines: {len(seq)}")
        print(f"labels: {len(labels)}  refs: {len(refs)}")
        undef = [k for k in refs if k not in labels]
        unused = [k for k in labels if k not in refs]
        print(f"undefined refs: {len(undef)}")
        for k in undef[:20]:
            print("  UNDEF:", k, "first use", refs[k][0][1:])
        print(f"unreferenced labels: {len(unused)}")


if __name__ == "__main__":
    main()
