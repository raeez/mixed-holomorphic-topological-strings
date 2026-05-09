# Swarm Report: Agent 250, Chiral Interface Ledger/Dictionary Integration

Date: 2026-04-30.

Owned writable files:

- `local-dictionary.tex`
- `claim-strength-ledger.tex`
- `reconstitution/swarm-2026-04-30-agent-250-chiral-interface-ledger-dictionary-integration.md`

## Claim Attacked

Agent 243 constructed a chiral algebra interface target.  The attack was
whether that target could be integrated into the local dictionary and
claim ledger without turning a curve vertex algebra into the native
\(\C^2\) holomorphic factorization object.

## Valid Attacks

- Native curve import is false.  The native object remains
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) on \(\C^2\).
- A reduction that kills \(z_2\), or keeps only a one-index residue line,
  is false.  The interface must retain \(z_2\)-modes or the full
  principal-part coefficient system.
- Automatic Zhu transfer is false.  The zero-mode map, Capelli shift,
  Moyal multiplicativity, BRST nilpotence, and anomaly transport remain
  theorem data.

## Repairs Made

- Added the dictionary row for
  \[
    \mathfrak I_{\mathrm{ch}}
    =
    (\mathcal R_{\C\times\R},\mathcal F_{\mathrm{red}},
     V_{\mathrm{red}},Q_{\mathrm{BRST}},\mathbf 1,T,Y,
     \operatorname{wt},\zeta_{\hbar},H_{\mathrm{anom}}),
  \]
  with \(V_{\mathrm{red}}\) as a reduced shadow only.
- Added the exact obstruction vector
  \[
    \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
    =
    (\operatorname{Ob}_{\mathrm{red}},
     \operatorname{Ob}_{\mathrm{vert}},
     \operatorname{Ob}_{\mathrm{Zhu}},
     \operatorname{Ob}_{\mathrm{nat}})
  \]
  to the failed-surface ledger.
- Strengthened the supremum-controller classification: before the
  controlled \(\C\times\R\) reduction, the curve chiral algebra or Zhu
  bridge is false transfer; after reduction it is a
  theorem-surface-with-missing-construction, not native \(\C^2\) data.

## Verification

Targeted verification commands:

```bash
rg -n -F -e 'mathfrak I_{\mathrm{ch}}' -e 'Ob}_{\mathfrak I_{\mathrm{ch}}}' -e 'V_{\mathrm{red}}' -e 'false transfer' local-dictionary.tex claim-strength-ledger.tex
git diff --check -- local-dictionary.tex claim-strength-ledger.tex reconstitution/swarm-2026-04-30-agent-250-chiral-interface-ledger-dictionary-integration.md
git diff --name-only -- local-dictionary.tex claim-strength-ledger.tex reconstitution/swarm-2026-04-30-agent-250-chiral-interface-ledger-dictionary-integration.md
```

No TeX build was required for this ledger/dictionary-only integration.
