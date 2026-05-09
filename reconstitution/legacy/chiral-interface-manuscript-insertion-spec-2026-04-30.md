# Chiral Interface Manuscript Insertion Spec

Date: 2026-04-30.
Owner: Agent 249.
Writable scope for this pass: this file and
`reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md`.

No TeX file is edited here.  This is the insertion specification for a
later manuscript patch.

## Verdict

Agent 243's tuple is admissible as a manuscript target, but only as a
reduced interface:
\[
  \mathfrak I_{\mathrm{ch}}
  =
  (\mathcal R_{\C\times\R},
   \mathcal F_{\mathrm{red}},
   V_{\mathrm{red}},
   Q_{\mathrm{BRST}},
   \mathbf 1,T,Y,
   \operatorname{wt},
   \zeta_\hbar,
   H_{\mathrm{anom}}).
\]
It is not a native replacement for
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\), and it is not a bare
external reference to Volume II.  It is a precise target produced only
after a controlled
\[
  \R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}
  \longrightarrow
  \R_t\times\C_{z_1}
\]
reduction retaining the \(z_2\)-mode or the full two-index
principal-part coefficient system.

The native object remains
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1])\bigr),
  \qquad
  \mathfrak h=\C[[z_1,z_2]]/\C\cdot1,
\]
with
\[
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\C\cdot1)
  \subset H^2_{(z_1,z_2)}(\C[[z_1,z_2]])\,dz_1dz_2 .
\]

## Insertion Map

1. `theorem-lanes.tex`, after
   `thm:lane-reduced-dirac-brst-zhu`, current line 1025, before
   `\paragraph{Cochain-level CE/PV--Koszul block.}`:
   add the statement `thm:lane-constructed-chiral-interface` below.

2. `local-dictionary.tex`, inside the "Local chiral/factorization
   taxonomy" longtable, after the Weyl/Moyal compatibility row, current
   lines 346-373, before `\end{longtable}`:
   add the dictionary row below.

3. `claim-strength-ledger.tex`, failed-surface status ledger, current
   lines 326-331:
   replace the short "\(\C\times\R\), VOA, BRST, and Zhu gates" item by
   the obstruction-vector row below.

4. `claim-strength-ledger.tex`, supremum controller classifications,
   after the "Reduced Dirac BRST curve algebra and Zhu bridge" item,
   current lines 574-592:
   add the interface classification row below.

5. `open-obligations.tex`, after the one-antifield Moyal target item,
   current lines 232-247, before "Weighted finite-window regulator
   independence":
   add the open obstruction item below.

6. `main.tex`, after the proof of
   `prop:native-darboux-theorem-package`, current line 1529, before
   `rmk:External global-obstruction firewall`:
   add only the short theorem-target remark below.  Do not promote it to a
   theorem in the body unless the obstruction vector is closed.

## Theorem-Lane Statement

```tex
\begin{stmt}[Statement: constructed chiral algebra interface target]
\label{thm:lane-constructed-chiral-interface}
  \emph{Status.} \emph{theorem-surface-with-missing-construction after
  Statement~\ref{thm:lane-controlled-cxr-reduction}, and false transfer
  before it}.  This statement is the only admissible ingress route for a
  one-dimensional chiral algebra attached to the local mixed
  holomorphic-topological model.  It does not replace the native
  \(\C^2\) holomorphic \(E_2\)-type factorization algebra.

  \emph{Native source.}  The source remains
  \[
    \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
    =
    C^\bullet_{\mathrm{CE},\mathrm{cont}}
    \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])\bigr),
    \qquad
    \mathfrak h=\C[[z_1,z_2]]/\C\cdot1,
  \]
  with
  \[
    \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\C\cdot1)
    \subset H^2_{(z_1,z_2)}(\C[[z_1,z_2]])\,dz_1dz_2 .
  \]

  \emph{Interface tuple.}  A constructed chiral algebra can enter the
  manuscript only as the component \(V_{\mathrm{red}}\) of
  \[
    \mathfrak I_{\mathrm{ch}}
    =
    (\mathcal R_{\C\times\R},
     \mathcal F_{\mathrm{red}},
     V_{\mathrm{red}},
     Q_{\mathrm{BRST}},
     \mathbf 1,T,Y,
     \operatorname{wt},
     \zeta_\hbar,
     H_{\mathrm{anom}}).
  \]
  Here \(\mathcal R_{\C\times\R}\) is the controlled reduction datum
  \[
    (\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},
    B_{z_2},\pi_!,L_{\mathrm{red}},
    \langle-,-\rangle_{\mathrm{red}},
    \{-,-\}_{\mathrm{red}},H_{\mathrm{anom}})
  \]
  of Statement~\ref{thm:lane-controlled-cxr-reduction}, with
  \[
    X=\R_t\times\R_s\times\C_{z_1}\times\C_{z_2},\qquad
    Y=\R_t\times\C_{z_1},\qquad
    \pi(t,s;z_1,z_2)=(t;z_1).
  \]
  The pushforward \(\pi_!\) includes the compact-support orientation
  line of the \(s,z_2\) fibre, or else an explicit trivialization of that
  line with its signs and degree shifts.

  \emph{Retained coefficient system.}  The reduced Hamiltonian algebra is
  not \(\C[[z_1]]/\C\).  It is
  \[
    \mathfrak h_{\mathrm{red}}
    =
    \C[[z_1]][[z_2]]/\C\cdot1,
  \]
  read as formal \(z_2\)-coefficients over \(Y\).  Its cotangent module is
  \[
    \mathcal P_{\mathrm{red}}
    =
    \operatorname{Ann}_{\mathrm{res}}(\C\cdot1)
    \subset H^2_{(z_1,z_2)}(\C[[z_1,z_2]])\,dz_1dz_2,
  \]
  with
  \[
    \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2,\qquad
    \langle\rho_{a,b},z_1^mz_2^n\rangle_{\mathrm{red}}
    =
    \delta_{a,m}\delta_{b,n}.
  \]
  The bracket and coadjoint action remain two-variable:
  \[
    \{f,g\}_{\mathrm{red}}
    =
    \partial_{z_1}f\,\partial_{z_2}g
    -
    \partial_{z_2}f\,\partial_{z_1}g
    \pmod{\C},
  \]
  \[
    z_1^pz_2^q\cdot\rho_{i,j}
    =
    -(pj-qi+p-q)\rho_{i-p+1,j-q+1},
  \]
  with negative-index targets equal to zero.  Hence setting \(z_2=0\)
  kills the Hamiltonian bracket and Moyal bivector, while keeping only
  the \(b=0\) principal-part line is not stable because
  \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).

  \emph{Reduced factorization target.}  For an interval
  \(I\subset\R_t\) and disk \(D\subset\C_{z_1}\),
  \[
    \mathcal F_{\mathrm{red}}(I\times D)
    =
    C^\bullet_{\mathrm{CE},\mathrm{cont}}
    \bigl(\Omega_c^\bullet(I)\widehat\otimes
    \Omega_c^{0,\bullet}(D)\widehat\otimes
    (\mathfrak h_{\mathrm{red}}\ltimes
    \mathcal P_{\mathrm{red}}[1])\bigr),
  \]
  up to the stated fibre orientation line.  The brane image is
  \[
    L_{\mathrm{red}}=\R_t\times\{z_1=0\},
  \]
  and finite-\(N\) evaluation keeps both matrices:
  \[
    \operatorname{ev}^{\mathrm{red}}_N(f)
    =
    \overline{\operatorname{Tr}f(X,Y)},\qquad
    X=\phi_1,\quad Y=\phi_2.
  \]

  \emph{Reduced Dirac/Zhu branch.}  The component \(V_{\mathrm{red}}\)
  must be produced by a factorization-to-vertex theorem with vacuum,
  translation, finite Laurent singular products, locality, conformal
  weights, and the BRST differential.  In the Dirac branch its generators
  are
  \[
    Z_1{}^i{}_j(z),\quad Z_2{}^i{}_j(z)\quad\mathrm{even},
    \qquad
    c^i{}_j(z),\quad b^i{}_j(z)\quad\mathrm{odd},
  \]
  with singular products
  \[
    Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
    \sim
    \frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
    \qquad
    b^i{}_j(z)c^k{}_\ell(w)
    \sim
    \frac{\delta^i_\ell\delta^k_j}{z-w}.
  \]
  The BRST current is
  \[
    j_{\mathrm{BRST}}
    =
    \operatorname{Tr}(c[Z_1,Z_2])
    +\frac12\operatorname{Tr}(b[c,c]),
    \qquad
    Q_{\mathrm{BRST}}=\operatorname{Res}j_{\mathrm{BRST}}(z)\,dz.
  \]
  Its square-zero proof is the moment-map equivariance computation
  \(Q[Z_1,Z_2]=[c,[Z_1,Z_2]]\) plus graded Jacobi, after the anomaly
  branch in \(H_{\mathrm{anom}}\) is fixed.

  The Zhu convention is part of the theorem.  With
  \[
    \operatorname{wt}(Z_1)=0,\quad
    \operatorname{wt}(Z_2)=1,\quad
    \operatorname{wt}(c)=0,\quad
    \operatorname{wt}(b)=1,
  \]
  and \(o(a)=a_{\operatorname{wt}(a)-1}\), put
  \[
    X^j{}_i=o(Z_1{}^i{}_j),\quad
    Y^j{}_i=o(Z_2{}^i{}_j),\quad
    C^j{}_i=o(c^i{}_j),\quad
    B^j{}_i=o(b^i{}_j).
  \]
  The pre-BRST Zhu algebra must be
  \[
    W_\hbar(\operatorname{Mat}_N^2)
    \otimes
    \operatorname{Cliff}_{bc}(\mathfrak{gl}_N),
  \]
  with
  \[
    [Y^j{}_i,X^\ell{}_k]=
    \hbar\,\delta^\ell_i\delta^j_k,
    \qquad
    [B^j{}_i,C^\ell{}_k]_{\mathrm{super}}=
    \delta^\ell_i\delta^j_k,
  \]
  and BRST differential
  \[
    QX=[C,X],\qquad QY=[C,Y],\qquad QC=\frac12[C,C],
  \]
  \[
    QB=YX-XY+\hbar N I+[B,C].
  \]
  The term \(\hbar N I\) is the Capelli contact shift fixed by the
  Weyl/Moyal normalization.

  \emph{Moyal/Zhu compatibility.}  The theorem must supply a continuous
  algebra map
  \[
    \zeta_\hbar\colon(\bar A_\hbar,*)\longrightarrow
    \operatorname{Zhu}(V_{\mathrm{red}})
  \]
  such that
  \[
    \zeta_\hbar(f*g)=\zeta_\hbar(f)\zeta_\hbar(g),
    \qquad
    [J_{f,(0)},\Theta_\rho]
    =
    \Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}.
  \]
  Equivalently, the Hochschild two-cocycle
  \[
    \operatorname{ob}_{\mathrm{Zhu}}(f,g)
    =
    \zeta_\hbar(f*g)-\zeta_\hbar(f)\zeta_\hbar(g)
  \]
  must vanish in the chosen completed stable target.

  \emph{Obstruction vector.}  The exact obstruction vector is
  \[
    \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
    =
    (\operatorname{Ob}_{\mathrm{red}},
     \operatorname{Ob}_{\mathrm{vert}},
     \operatorname{Ob}_{\mathrm{Zhu}},
     \operatorname{Ob}_{\mathrm{nat}}).
  \]
  The reduction part is
  \[
    \operatorname{Ob}_{\mathrm{red}}
    =
    (\operatorname{ob}_{s,\mathrm{or}},
     \operatorname{ob}_{z_2,\mathrm{fib}},
     \operatorname{ob}_{K,\infty},
     \operatorname{ob}_{\mathrm{pair}},
     \operatorname{ob}_{\mathrm{fac},2},
     \operatorname{ob}_{\mathrm{fac},3},
     \operatorname{ob}_{\mathrm{brane}},
     \operatorname{ob}_{\mathrm{anom}},
     \operatorname{ob}_{\mathrm{Moyal}}).
  \]
  The vertex part is
  \[
    \operatorname{Ob}_{\mathrm{vert}}
    =
    (\operatorname{ob}_{\mathrm{FV}},
     \operatorname{ob}_{\mathrm{Laurent}},
     \operatorname{ob}_{\mathrm{loc}},
     \operatorname{ob}_{\mathrm{wt}},
     \operatorname{ob}_{\mathrm{BRST}}).
  \]
  The Zhu part is
  \[
    \operatorname{Ob}_{\mathrm{Zhu}}
    =
    (\operatorname{ob}_{\mathrm{zero}},
     \operatorname{ob}_{\mathrm{Zhu}}^{\mathrm{mult}},
     \operatorname{ob}_{\mathrm{Capelli}},
     \operatorname{ob}_{\mathrm{HKR}}).
  \]
  The native-compatibility part is
  \[
    \operatorname{Ob}_{\mathrm{nat}}
    =
    (\operatorname{ob}_{\pi_!\mathrm{-source}},
     \operatorname{Ob}^{\infty}_{\mathrm{BM}},
     \operatorname{ob}_{\mathrm{false-native}}).
  \]

  \emph{Vol II control.}  Volume II supplies the operadic and Zhu
  grammar only after \(V_{\mathrm{red}}\) exists as a graded vertex
  algebra with conformal vector and the required finiteness hypotheses.
  It does not construct \(\pi_!\), the retained \(z_2\)-coefficient
  system, the anomaly homotopy, or the source map from the native
  \(\C^2\) factorization algebra.
\end{stmt}
```

## Local-Dictionary Row

Insert after the current Weyl/Moyal compatibility row:

```tex
Constructed chiral algebra interface tuple &
The symbol
\[
  \mathfrak I_{\mathrm{ch}}
  =
  (\mathcal R_{\C\times\R},
   \mathcal F_{\mathrm{red}},
   V_{\mathrm{red}},
   Q_{\mathrm{BRST}},
   \mathbf 1,T,Y,
   \operatorname{wt},
   \zeta_\hbar,
   H_{\mathrm{anom}})
\]
denotes the controlled ingress datum for a one-dimensional chiral algebra.
It is neither an external citation nor the native object.  The native
object remains \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) on
\(\C^2\).  The component \(V_{\mathrm{red}}\) is admissible only after
the reduction \(\mathcal R_{\C\times\R}\) retains the \(z_2\)-mode or the
full two-index principal-part coefficient system, proves the pushed-forward
bracket, BV pairing, brane image, anomaly homotopy, vertex/OPE package,
and Zhu/Moyal multiplicativity.  Its obstruction vector is
\(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\) of
Statement~\ref{thm:lane-constructed-chiral-interface}.\\
\hline
```

## Claim-Ledger Rows

Replace the failed-surface status item at current lines 326-331 by:

```tex
  \item \emph{Constructed chiral algebra interface.}
  Status: construction target after controlled reduction, and false
  transfer before it.  The required datum is
  \[
    \mathfrak I_{\mathrm{ch}}
    =
    (\mathcal R_{\C\times\R},
     \mathcal F_{\mathrm{red}},
     V_{\mathrm{red}},
     Q_{\mathrm{BRST}},
     \mathbf 1,T,Y,
     \operatorname{wt},
     \zeta_\hbar,
     H_{\mathrm{anom}}),
  \]
  with \(\mathcal R_{\C\times\R}\) retaining \(z_2\)-coefficients or the
  full Matlis principal-part system.  Failure is the obstruction theorem
  for
  \[
    \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
    =
    (\operatorname{Ob}_{\mathrm{red}},
     \operatorname{Ob}_{\mathrm{vert}},
     \operatorname{Ob}_{\mathrm{Zhu}},
     \operatorname{Ob}_{\mathrm{nat}}).
  \]
```

Add this supremum-controller item after the reduced Dirac BRST/Zhu row:

```tex
  \item \emph{Constructed chiral algebra interface tuple.}
  Classification:
  \emph{theorem-surface-with-missing-construction} after
  \(\mathcal R_{\C\times\R}\), and \emph{false transfer} before it.
  The strongest admissible theorem identifies a proposed one-dimensional
  chiral algebra with \(V_{\mathrm{red}}\) in
  \(\mathfrak I_{\mathrm{ch}}\), not with the native
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\).  The proof must close
  the reduction, vertex, Zhu, and native-compatibility obstruction vector;
  otherwise the exact nonzero component of
  \(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\) is the obstruction
  theorem.
```

## Open-Obligations Row

Insert after the one-antifield Moyal target:

```tex
  \item \emph{Constructed chiral algebra interface obstruction vector.}
  The ingress datum for a one-dimensional chiral algebra is
  \[
    \mathfrak I_{\mathrm{ch}}
    =
    (\mathcal R_{\C\times\R},\mathcal F_{\mathrm{red}},
     V_{\mathrm{red}},Q_{\mathrm{BRST}},\mathbf 1,T,Y,
     \operatorname{wt},\zeta_\hbar,H_{\mathrm{anom}}).
  \]
  Its obstruction vector is
  \[
    \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
    =
    (\operatorname{Ob}_{\mathrm{red}},
     \operatorname{Ob}_{\mathrm{vert}},
     \operatorname{Ob}_{\mathrm{Zhu}},
     \operatorname{Ob}_{\mathrm{nat}}).
  \]
  Here \(\operatorname{Ob}_{\mathrm{red}}\) contains the \(s\)-orientation,
  \(z_2\)-fiber, \(\pi_!\), pairing, factorization, brane, anomaly, and
  Moyal components; \(\operatorname{Ob}_{\mathrm{vert}}\) contains
  factorization-to-vertex, finite Laurent, locality, weight, and BRST
  components; \(\operatorname{Ob}_{\mathrm{Zhu}}\) contains zero-mode,
  multiplicativity, Capelli, and HKR components; and
  \(\operatorname{Ob}_{\mathrm{nat}}\) prevents replacing the native
  \(\C^2\) factorization algebra by the curve object.  No curve chiral
  algebra, VOA, or Zhu bridge enters the stable core until the relevant
  components vanish or are carried as explicit theorem hypotheses.
```

## Main-Text Remark

Insert after `prop:native-darboux-theorem-package` only as a compact
pointer:

```tex
\begin{rmk}[Constructed chiral algebra interface target]
\label{rmk:constructed-chiral-interface-target}
  A one-dimensional chiral algebra can enter the formal-local theory only
  through the reduced interface tuple
  \[
    \mathfrak I_{\mathrm{ch}}
    =
    (\mathcal R_{\C\times\R},\mathcal F_{\mathrm{red}},
     V_{\mathrm{red}},Q_{\mathrm{BRST}},\mathbf 1,T,Y,
     \operatorname{wt},\zeta_\hbar,H_{\mathrm{anom}}).
  \]
  The tuple is a theorem target after the controlled
  \(\C\times\R\) reduction with retained \(z_2\)-coefficients or full
  principal parts.  It is not the native \(\C^2\) factorization algebra
  and not an external replacement for it.  The exact remaining condition
  is the vanishing, or explicit hypothesizing, of
  \(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\) in
  Statement~\ref{thm:lane-constructed-chiral-interface}.
\end{rmk}
```

## Attack-Heal Closure

The insertion is stable under the two fatal attacks.

First, it cannot falsely import a curve algebra as native: every use of
\(V_{\mathrm{red}}\) factors through \(\mathcal R_{\C\times\R}\) and
keeps the native source
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\).

Second, it cannot demote the chiral algebra to an external reference:
the tuple makes \(V_{\mathrm{red}}\), the BRST current, the weights, the
Zhu map, and the Moyal multiplicativity part of the local theorem target.
If a component fails, the manuscript records the named obstruction
component rather than a vague "external input" condition.
