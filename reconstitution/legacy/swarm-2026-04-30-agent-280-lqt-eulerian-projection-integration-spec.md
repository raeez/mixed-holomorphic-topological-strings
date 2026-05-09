# Agent 280 Report: LQT Eulerian Projection Integration Spec

Date: 2026-04-30

Worktree: `/Users/raeez/topological-strings`, branch `master`.

Owned write surface:

- `reconstitution/swarm-2026-04-30-agent-280-lqt-eulerian-projection-integration-spec.md`
- `reconstitution/lqt-eulerian-projection-integration-spec-2026-04-30.md`

Report-only. No TeX, script, bibliography, source fixture, or PDF was edited.

## Claim Attacked

Use Agent 274's stable block-sum Hopf/Eulerian idempotent construction to
produce exact TeX integration instructions for:

- `theorem-lanes.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `main.tex`

The integration must distinguish the valid stable cumulant projection from
the false same-rank delete-multicycles projection.

## Verdict

The LQT finite-window projection is theorem-grade only in the stable
block-sum Hopf CE habitat.

For a Koszul-weight bound \(K\) and CE-length bound \(L\), set
\[
  A_{\psi,K}=A_\psi/F^{>K}A_\psi,
  \qquad
  \operatorname{wt}(x)=(1,0),\quad
  \operatorname{wt}(y)=(0,1),\quad
  \operatorname{wt}(\psi)=(1,1).
\]
Let \(\mathsf H^{\mathrm{st}}_{K,L}(A_\psi)\) be the stable invariant CE
window with product induced by block diagonal sum of matrix ranks and
coproduct induced by the CE coalgebra.  With \(J=\mathrm{id}-u\epsilon\),
define the Eulerian idempotent
\[
  P_{1\mathrm{cyc}}
  =
  \log^*(\mathrm{id})
  =
  \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}J^{*m}.
\]
The convolution uses the stable block-sum product and the stable CE
coproduct.  This is a chain idempotent; its image is the connected
single-cycle summand \(\operatorname{im}\Theta_{N,K,L}\).  In the safe
degreewise range
\[
  N\geq \max(K,L+2),
\]
the finite-window chain map is
\[
  \lambda_{\mathrm{LQT},K,L}
  =
  \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}.
\]
If the manuscript keeps one symbol \(W\) for both \(K\le W\) and \(L\le W\),
the displayed stable range must be \(N\ge W+2\), not \(N\ge W\).

The raw same-rank projection that keeps one-cycle permutation tensors and
deletes all multicycle tensors inside a single finite exterior CE complex is
false.  For homogeneous \(a,b\),
\[
  P_{\mathrm{del}}d_{\mathrm{CE}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)
  =
  \pm\Theta_1(ab-(-1)^{|a||b|}ba),
  \qquad
  d_{\mathrm{CE}}P_{\mathrm{del}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)=0.
\]
Thus \(P_{\mathrm{del}}\) is not a chain map when the graded commutator is
nonzero.  The Eulerian projection avoids this because products are formed by
block sum before the stable Hopf logarithm is applied; after transfer to a
fixed stable rank it is a cumulant linear combination, not deletion.

## Evidence Anchors

- Agent 274 construction: `reconstitution/swarm-2026-04-30-agent-274-chain-level-lqt-projection-construction-push.md:24-57`, `:58-83`, `:85-139`, `:141-170`.
- Agent 274 companion: `reconstitution/chain-level-lqt-projection-construction-push-2026-04-30.md:172-245`.
- Agent 272 scalar quotient attack: `reconstitution/swarm-2026-04-30-agent-272-lqt-scalar-koszul-quotient-audit.md:63-75`, `:97-132`.
- Agent 264 finite-window construction: `reconstitution/swarm-2026-04-30-agent-264-lqt-apsi-finite-window-construction-push.md:56-113`, `:163-200`, `:214-248`.
- LQT source boundary: `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md:32-53`, `:91-105`, `:197-212`.
- Current TeX anchors read before this report:
  - `theorem-lanes.tex:2079-2105`
  - `open-obligations.tex:143-172`
  - `claim-strength-ledger.tex:392-411`
  - `main.tex:1750-1785`
  - `main.tex:4306-4358`
  - `main.tex:4983-5059`
  - `main.tex:5069-5108`
  - `tate-T5-chain-level-primitive.tex:101-151`
  - `tate-T5-chain-level-primitive.tex:404-443`

No PDF build was run; this is a report-only integration specification.

## Integration Order

1. Update the theorem lane first.  This fixes the actual mathematical object:
   two-parameter window, block-sum Hopf complex, Eulerian idempotent, stable
   range, signs, scalar-Koszul quotient, and same-rank obstruction.
2. Update `open-obligations.tex`.  The old tuple should no longer list
   \(P_{1\mathrm{cyc}}\), stable range, signs, and Roos compatibility as open
   in the healed stable habitat.  It should retain only the scalar quotient
   condition and the larger open \(A_\infty\), \(\Psi\to\rho\), and QME
   obligations.
3. Update `claim-strength-ledger.tex`.  The ledger should say theorem-grade in
   the stable block-sum Hopf finite window, false for same-rank deletion.
4. Update `main.tex`.  The main narrative should state the finite-window chain
   object immediately after the external LQT template and should sharpen the
   connected large-\(N\) operation so that "cumulant" cannot be read as raw
   fixed-rank multicycle deletion.

## `theorem-lanes.tex`

Action: replace the current K3 LQT clause at `theorem-lanes.tex:2079-2105`
with the following block.  Keep the surrounding enumeration and labels.

```tex
    \item a finite-window Loday--Quillen--Tsygan comparison in the
      stable block-sum Hopf CE habitat.  Give
      \(A_\psi=T(x,y,\psi)\) the Koszul weights
      \[
        \operatorname{wt}(x)=(1,0),\qquad
        \operatorname{wt}(y)=(0,1),\qquad
        \operatorname{wt}(\psi)=(1,1),
      \]
      and, for a Koszul-weight bound \(K\), put
      \(A_{\psi,K}=A_\psi/F^{>K}A_\psi\), where \(F^{>K}\) is the
      two-sided dg ideal generated by words of total Koszul weight
      \(>K\).  Let \(CC_{\mathrm{red},\leq L}(A_{\psi,K})\) denote
      reduced cyclic chains whose CE length is at most \(L\), so
      \(a_0|\cdots|a_r\) has length \(r+1\).

      For homogeneous \(a_i\in A_{\psi,K}\), use the graded matrix
      bracket
      \[
        [E_{ij}a,E_{kl}b]
        =
        \delta_{jk}E_{il}ab
        -
        (-1)^{|a||b|}\delta_{li}E_{kj}ba
      \]
      and the trace-cycle map
      \[
        \Theta_{N,K,L}(a_0|\cdots|a_r)
        =
        \sum_{i_0,\ldots,i_r}
        (E_{i_0i_1}a_0)\wedge\cdots\wedge
        (E_{i_ri_0}a_r),
        \qquad r+1\leq L .
      \]
      The reduced cyclic relation is
      \[
        (a_0|\cdots|a_r)
        \sim
        (-1)^{r+|a_r|(|a_0|+\cdots+|a_{r-1}|)}
        (a_r|a_0|\cdots|a_{r-1}).
      \]

      Let \(\mathsf H^{\mathrm{st}}_{K,L}(A_\psi)\) be the stable
      invariant CE window obtained from block diagonal sum of matrix
      ranks, with product \(\mu_\oplus\), CE coproduct
      \(\Delta_{\mathrm{CE}}\), unit \(u\), and counit \(\epsilon\).
      Put \(J=\mathrm{id}-u\epsilon\), and define
      \[
        P_{1\mathrm{cyc}}
        =
        \log^*(\mathrm{id})
        =
        \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}J^{*m},
      \]
      where convolution is computed using \(\mu_\oplus\) and
      \(\Delta_{\mathrm{CE}}\).  Since unit, counit, product,
      coproduct, and the CE differential are chain maps in this stable
      Hopf complex,
      \[
        P_{1\mathrm{cyc}}^2=P_{1\mathrm{cyc}},
        \qquad
        d_{\mathrm{CE}}P_{1\mathrm{cyc}}
        =
        P_{1\mathrm{cyc}}d_{\mathrm{CE}}.
      \]
      Its image is the connected single-cycle summand
      \(\operatorname{im}\Theta_{N,K,L}\).

      In the safe degreewise range
      \[
        N\geq\max(K,L+2),
      \]
      define the finite-window map on stable invariant CE chains by
      \[
        \lambda_{\mathrm{LQT},K,L}
        =
        \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}
        \colon
        \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
        \longrightarrow
        CC_{\mathrm{red},\leq L}(A_{\psi,K})[1].
      \]
      If one bound \(W\) is used with \(K\leq W\) and \(L\leq W\),
      this statement means \(N\geq W+2\).  The quotient
      \(A_{\psi,K}\) alone is not a finite CE window, since reduced
      cyclic chain length remains unbounded.

      The CE and cyclic signs are fixed by
      \[
        d_{\mathrm{CE}}\Theta_1(\psi)=\Theta_1(xy-yx),
      \]
      hence
      \[
        \lambda_{\mathrm{LQT},K,L}d_{\mathrm{CE}}\Theta_1(\psi)
        =
        [xy-yx]
        =
        d_{CC}[\psi],
      \]
      and, for homogeneous \(a,b,c\),
      \[
        \lambda_{\mathrm{LQT},K,L}d_{\mathrm{CE}}\Theta_2(a,b)
        =
        [ab]-(-1)^{|a||b|}[ba],
      \]
      \[
        \lambda_{\mathrm{LQT},K,L}d_{\mathrm{CE}}\Theta_3(a,b,c)
        =
        [ab|c]-[a|bc]
        +
        (-1)^{|c|(|a|+|b|)}[ca|b].
      \]

      The Hamiltonian scalar quotient is a chain quotient only after
      quotienting by the two-term scalar-Koszul subcomplexes
      \[
        \Theta_1(\psi)\longmapsto\Theta_1(xy-yx),
        \qquad
        [\psi]\longmapsto[xy-yx],
      \]
      or after passing to homology.  Killing \(\Theta_1(\psi)\) alone
      is not a chain map.
```

Action: immediately after that K3 item, before the next `\item`, insert this
fence if the surrounding prose still permits a separate paragraph inside the
same item.  If the integrator keeps the block above exactly, append this as
the last paragraph of K3.

```tex
      This \(P_{1\mathrm{cyc}}\) is not the raw same-rank projection
      which keeps one-cycle permutation tensors and deletes all
      multicycle tensors in a fixed exterior CE complex.  If
      \(P_{\mathrm{del}}\) denotes that raw operation, then already
      on two diagonal one-cycles
      \[
        P_{\mathrm{del}}d_{\mathrm{CE}}
        \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)
        =
        \pm\Theta_1(ab-(-1)^{|a||b|}ba),
        \qquad
        d_{\mathrm{CE}}P_{\mathrm{del}}
        \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)=0.
      \]
      Thus the same-rank deletion model fails whenever
      \(ab-(-1)^{|a||b|}ba\neq0\).  The stable Hopf projection is a
      cumulant projection: products are formed by block sum before the
      Hopf logarithm is applied, and transfer to a fixed stable rank
      subtracts diagonal-collision terms rather than deleting raw
      multicycles.
```

## `open-obligations.tex`

Action: replace the finite-window LQT item at `open-obligations.tex:143-172`
with this block.

```tex
  \item \emph{Finite-window dg LQT comparison.}
  The finite-window comparison is closed in the stable block-sum Hopf
  CE habitat and false as a raw same-rank cycle-deletion operation.
  The healed datum uses two finite bounds: a Koszul-weight bound \(K\)
  and a CE-length bound \(L\).  With
  \(A_{\psi,K}=A_\psi/F^{>K}A_\psi\) and
  \(N\geq\max(K,L+2)\), the trace-cycle map
  \[
    \Theta_{N,K,L}\colon
    CC_{\mathrm{red},\leq L}(A_{\psi,K})[1]
    \to
    C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,K}))^{GL_N}
  \]
  identifies reduced cyclic chains with the stable single-cycle image.
  On the stable block-sum Hopf CE window,
  \[
    P_{1\mathrm{cyc}}
    =
    \log^*(\mathrm{id})
    =
    \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}
    (\mathrm{id}-u\epsilon)^{*m}
  \]
  is the Eulerian chain idempotent, and
  \[
    \lambda_{\mathrm{LQT},K,L}
    =
    \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}.
  \]
  If one symbol \(W\) controls both \(K\leq W\) and \(L\leq W\), the
  stable range is \(N\geq W+2\).

  The healed stable obstruction tuple is
  \[
    \mathcal O^{\mathrm{st}}_{\mathrm{LQT},K,L}
    =
    (0,0,0,0,0,0)
  \]
  after the scalar-Koszul chain quotient
  \[
    \Theta_1(\psi)\mapsto\Theta_1(xy-yx),
    \qquad
    [\psi]\mapsto[xy-yx],
  \]
  or after passing to homology.  Before that two-term quotient,
  \(\mathcal O_{\mathrm{scalar}}\) is the nonzero chain defect
  \(d_{\mathrm{CE}}\Theta_1(\psi)=\Theta_1(xy-yx)\).

  The false same-rank operation remains obstructed.  If
  \(P_{\mathrm{del}}\) keeps fixed-rank one-cycle tensors and deletes
  fixed-rank multicycles, then
  \[
    P_{\mathrm{del}}d_{\mathrm{CE}}
    \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)
    =
    \pm\Theta_1(ab-(-1)^{|a||b|}ba),
    \qquad
    d_{\mathrm{CE}}P_{\mathrm{del}}
    \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)=0.
  \]
  Thus the open obligation is not to repair \(P_{\mathrm{del}}\); it is
  to keep the stable Hopf cumulant habitat separate from the fixed-rank
  deletion model.  The larger open \(A_\infty\) comparison, the
  \(\Psi\to\rho\) bridge, the BV/cyclicity package, and the Costello/QME
  realization remain outside this LQT repair.
```

## `claim-strength-ledger.tex`

Action: replace the LQT paragraph at `claim-strength-ledger.tex:392-411`
with this block.

```tex
  The LQT component is theorem-grade on the two-parameter stable
  finite-window habitat.  For the Koszul-weight quotient
  \(A_{\psi,K}=A_\psi/F^{>K}A_\psi\), CE-length bound \(L\), and
  safe range \(N\geq\max(K,L+2)\), the stable block-sum Hopf CE
  complex carries the Eulerian idempotent
  \[
    P_{1\mathrm{cyc}}
    =
    \log^*(\mathrm{id})
    =
    \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}
    (\mathrm{id}-u\epsilon)^{*m},
  \]
  whose image is the single-cycle summand
  \(\operatorname{im}\Theta_{N,K,L}\).  The finite-window chain map is
  \[
    \lambda_{\mathrm{LQT},K,L}
    =
    \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}.
  \]
  In a one-parameter notation \(K,L\leq W\), this means
  \(N\geq W+2\).

  The healed stable obstruction tuple
  \[
    \mathcal O^{\mathrm{st}}_{\mathrm{LQT},K,L}
    =
    (\mathcal O_{\mathrm{win}},
     \mathcal O_{\mathrm{Prim}},
     \mathcal O_{\mathrm{stab}},
     \mathcal O_{\mathrm{scalar}},
     \mathcal O_{\mathrm{CC}},
     \mathcal O_{\mathrm{Roos}})
  \]
  vanishes after the two-term scalar-Koszul quotient
  \(\Theta_1(\psi)\mapsto\Theta_1(xy-yx)\),
  \([\psi]\mapsto[xy-yx]\), or after homology.  Before this quotient,
  \(\mathcal O_{\mathrm{scalar}}\) is the exact chain defect
  \(d_{\mathrm{CE}}\Theta_1(\psi)=\Theta_1(xy-yx)\).
  The fixed-rank delete-multicycles projection is false, since
  \(P_{\mathrm{del}}d_{\mathrm{CE}}
  (\Theta_1(a)\wedge\Theta_1(b))\) contains
  \(\pm\Theta_1(ab-(-1)^{|a||b|}ba)\) whereas
  \(d_{\mathrm{CE}}P_{\mathrm{del}}
  (\Theta_1(a)\wedge\Theta_1(b))=0\).
```

Do not change the preceding status of the full open \(A_\infty\) theorem:
it remains a construction target.  The LQT component is healed; the full
admissible \(A_\infty\) comparison is not.

## `main.tex`

Action A: after the external LQT theorem at `main.tex:1764-1779`, replace the
paragraph at `main.tex:1780-1785` with this sharper boundary paragraph.

```tex
LQT supplies the stable Hopf template; the finite-window chain map used
below is an internal stable construction.  In a Koszul-weight/CE-length
window \((K,L)\), the stable block-sum CE Hopf complex carries the
Eulerian idempotent
\[
  P_{1\mathrm{cyc}}
  =
  \log^*(\mathrm{id})
  =
  \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}
  (\mathrm{id}-u\epsilon)^{*m},
\]
and, for \(N\geq\max(K,L+2)\),
\[
  \lambda_{\mathrm{LQT},K,L}
  =
  \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}.
\]
This is a cumulant projection in the stable block-sum Hopf object, not
the raw operation of deleting multicycle tensors in one fixed-rank CE
complex.  The latter fails because
\[
  P_{\mathrm{del}}d_{\mathrm{CE}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)
  =
  \pm\Theta_1(ab-(-1)^{|a||b|}ba),
  \qquad
  d_{\mathrm{CE}}P_{\mathrm{del}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)=0.
\]
No global \(HC_{*-1}\) convention is transferred into
Theorem~\ref{thm:main-local}: cyclic homology supplies the stable-trace
analogy that organises the comparison, not the proof of the Hamiltonian
sector.
```

Action B: in Definition~`\ref{defn:three-large-N-operations}` at
`main.tex:5037-5041`, replace item (2) with this block.

```tex
    \item \emph{Connected single-trace extraction}
      \(\Conn_{N\to\infty}\).  After passing to the degreewise stable
      invariant algebra, use the stable block-sum Hopf structure and
      apply the Eulerian, or cumulant, idempotent
      \(P_{1\mathrm{cyc}}=\log^*(\mathrm{id})\).  On the resulting
      symmetric algebra of stable cyclic-word generators this is the
      projection to the Hopf-primitive summand.  Products of two
      nonempty traces are decomposable and are killed by this
      projection.  This is not the same as deleting multicycle tensors
      inside one fixed-rank exterior CE complex.
```

Action C: if the main-text proof near `main.tex:5008-5025` is expanded, add
one sentence after `Projection to indecomposables ...`:

```tex
  The projection is the stable cumulant projection; the fixed-rank
  same-rank deletion operation is not used in this proof.
```

This sentence is optional if Action A and Action B are both applied.

## Status Matrix

| Component | Integration status |
|---|---|
| Koszul window \(A_{\psi,K}\) | proved finite dg quotient |
| CE-length window \(L\) | required; \(A_{\psi,K}\) alone is not finite in cyclic length |
| Stable range | \(N\geq\max(K,L+2)\), or \(N\geq W+2\) for \(K,L\le W\) |
| \(P_{1\mathrm{cyc}}\) | Eulerian idempotent in stable block-sum Hopf CE complex |
| Same-rank deletion | false; not a chain map |
| Scalar quotient | chain-level only after two-term scalar-Koszul quotient or after homology |
| \(O_{\mathrm{Roos}}\) | zero in the healed quotient tower |
| Full \(A_\infty\), \(\Psi\to\rho\), BV/QME | still outside this LQT repair |

## Self-Check Before Manuscript Edit

- Keep \(K\) and \(L\) distinct unless the local paragraph explicitly defines
  \(K,L\le W\).
- Do not write \(N\ge W\) for the one-parameter finite-window LQT clause; use
  \(N\ge W+2\).
- Do not call \(P_{\mathrm{del}}\) a projection onto primitives.  It is not a
  chain map.
- Do not claim Loday--Quillen 1984 or Tsygan 1983 proves the dg finite-window
  \(A_\psi\) chain map.  They support the stable homological template only.
- Do not fold the LQT repair into the full open \(A_\infty\) theorem.  The
  latter remains a construction target.
