# Swarm Report: Agent 243, Constructed Chiral Algebra Interface Target

Date: 2026-04-30.

Owned files:

- `reconstitution/constructed-chiral-algebra-interface-integration-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-243-constructed-chiral-algebra-interface-integration-target.md`

No TeX, script, Vol II, or manuscript files were edited.

## Claim Attacked

Adversarial target: find the strongest true interface by which the
user's constructed chiral algebra can enter this local mixed HT
manuscript without becoming a vague external reference, a false
curve-VOA import, or a replacement for the native \(\mathbb C^2\)
holomorphic \(E_2\)/factorization algebra.

## Evidence Read

- `CLAUDE.md`, `AGENTS.md`.
- Ecosystem attack-heal skill and protocol:
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md` and
  `references/protocol.md`.
- Vol II rectification discipline:
  `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `main.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`,
  `preamble.tex`.
- Manuscript control files:
  `theorem-lanes.tex`, `local-dictionary.tex`,
  `claim-strength-ledger.tex`, `open-obligations.tex`.
- Chiral/reduction reports in `reconstitution/`, including the local
  chiral-algebra thread, native \(E_2\) construction, controlled
  `C x R` reduction, reduced Dirac BRST/Zhu thread, and Agent 228 target.
- Vol II controls:
  `chapters/theory/sc_chtop_heptagon.tex`,
  `chapters/connections/hochschild.tex`,
  `chapters/connections/concordance.tex`,
  and `notes/first_principles_cache.md`.

## Stable Core

The interface is the tuple
\[
  \mathfrak I_{\mathrm{ch}}
  =
  (\mathcal R_{\mathbb C\times\mathbb R},
   \mathcal F_{\mathrm{red}},
   V_{\mathrm{red}},
   Q_{\mathrm{BRST}},
   \mathbf1,T,Y,
   \operatorname{wt},
   \zeta_{\hbar},
   H_{\mathrm{anom}}).
\]

The reduction keeps
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
  \qquad
  \mathcal P_{\mathrm{red}}
  \subset
  H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2.
\]
The bracket is still
\[
  \{f,g\}_{\mathrm{red}}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g.
\]

The curve vertex algebra is admissible only after the reduction,
factorization-to-vertex package, BRST nilpotence, Zhu/zero-mode map,
Moyal multiplicativity, and anomaly transport are proved.  It is a
reduced shadow of the native \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\),
not the native object.

## Destroyed Claims

- Native curve import: false.  The native object is the \(\mathbb C^2\)
  Hamiltonian CE/factorization algebra.
- \(z_2=0\) reduction: false.  It kills the Hamiltonian bracket and the
  Moyal bivector.
- \(b=0\) principal-part residue line: false.  It is not stable since
  \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).
- Automatic Zhu bridge: false.  A graded vertex algebra with conformal
  vector, weights, zero modes, and multiplicativity is required.
- Vol II shortcut: false.  Vol II supplies operadic and Hochschild
  grammar after the reduced vertex algebra exists; it does not construct
  \(\pi_!\), anomaly transport, or the retained coefficient system.

## Healed Construction

The target report written by this agent records:

- exact reduction datum \(\mathcal R_{\mathbb C\times\mathbb R}\);
- retained \(z_2\)-coefficient and principal-part modules;
- reduced brane image \(L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\}\);
- Dirac BRST fields, OPEs, current, and square-zero proof obligation;
- Zhu weights, zero modes, Weyl relation, and Capelli shift;
- Moyal map \(\zeta_\hbar:(\bar A_\hbar,*)\to\operatorname{Zhu}(V_{\mathrm{red}})\);
- obstruction vector
  \[
    \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
    =
    (\operatorname{Ob}_{\mathrm{red}},
     \operatorname{Ob}_{\mathrm{vert}},
     \operatorname{Ob}_{\mathrm{Zhu}},
     \operatorname{Ob}_{\mathrm{nat}}).
  \]

## Proposed Insertion Points

- `theorem-lanes.tex:1025`: add the constructed chiral algebra interface
  target after the reduced Dirac BRST/Zhu statement.
- `local-dictionary.tex:346-374`: add the ingress rule after the
  Weyl/Moyal compatibility row.
- `claim-strength-ledger.tex:552-570`: add the interface classification.
- `open-obligations.tex:323-328`: replace the single gate sentence by the
  full obstruction vector.
- `main.tex:1454-1528`: insert only a theorem-target paragraph after the
  native Darboux theorem package, unless all obstruction components have
  been supplied.

## Verification

Commands run before writing included targeted `rg`, `sed`, `nl -ba`, and
`git status --short` scans over the requested repo files, existing
reconstitution reports, and relevant Vol II controls.

Post-write checks to run:

```bash
git diff --check -- reconstitution/constructed-chiral-algebra-interface-integration-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-243-constructed-chiral-algebra-interface-integration-target.md
rg -n -F -e 'mathfrak I_{\\mathrm{ch}}' -e 'Ob}_{\\mathfrak I_{\\mathrm{ch}}}' -e 'z_1\\cdot\\rho_{a,0}' -e 'YX-XY+\\hbar N I' reconstitution/constructed-chiral-algebra-interface-integration-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-243-constructed-chiral-algebra-interface-integration-target.md
git add -- reconstitution/constructed-chiral-algebra-interface-integration-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-243-constructed-chiral-algebra-interface-integration-target.md
```

No TeX build is needed for report-only Markdown artifacts.
