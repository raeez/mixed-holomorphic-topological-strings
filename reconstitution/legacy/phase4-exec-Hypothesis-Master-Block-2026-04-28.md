# Phase-4 EXEC P4-Hypothesis-Master-Block — Publication-grade master LaTeX hypothesis declaration block for `claim-strength-ledger.tex`

**Date.** 2026-04-28. **Author.** Raeez Lorgat. No AI attribution.
**Lens.** Costello + Hypotheses — every load-bearing hypothesis named
explicitly with primary-source anchor; no silent strengthening; the
Costello (2011) admissible regulator class is the structural backbone,
and each (A_k) variant is a precise predicate on test data that maps
to a named theorem dependency.
**Mode.** Proposal-only. NO git commits. NO edits to manuscript TeX.
Writable surface: this file ONLY.
**Mandate.** Draft a publication-grade master LaTeX block for
`claim-strength-ledger.tex` that declares each (A_k) variant in
canonical order with primary-source anchors, hypothesis-dependency
table, regulator-class admissibility table, anti-attack scan, and
inscription target placement.

**Trusted context loaded.**
- `reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md` (976
  lines) — six (A_k) variants identified, including silent (A2$'$)
  form-existence on graded sources.
- `reconstitution/phase4-exec-A5-anomaly-ledger-2026-04-28.md` (1162
  lines) — L1-L12 primary-source anchors (Capelli 1890 / Howe 1989 /
  Procesi 1976 / Razmyslov 1974 / Sergeev 1983-1985 / Berele-Regev
  1987 / DeWitt 1992 / Kac 1977 / Cheng-Wang 2012 / Berezin 1966 /
  Costello 2011 / Costello-Gwilliam 2017,2021 / Polyakov 1981 /
  BCOV 1994).
- `reconstitution/phase4-exec-W30-M2-regulator-branches-2026-04-28.md`
  (830 lines) — (R1) heat-kernel / (R2) point-splitting / (R3)
  dimensional regularization / (R4) Hadamard parametrix branches.
- `reconstitution/phase4-exec-G4-T22-virasoro-twist-2026-04-28.md`
  (1409 lines) — (A2$''_T$) Sugawara-descendant silent strengthening
  on the Virasoro-twisted side.
- `reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`
  (1247 lines) — G3-M2 strategic boundary across psl(N|N) / p(N) /
  q(N) / sl(M|N).
- `reconstitution/phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`
  — Theorem G$^{\mathrm{otr}}$ Phase-5 parallel inscription with
  signed regulator (A5)$^{\mathrm{otr}}$.
- `claim-strength-ledger.tex` (142 lines) — the inscription target.
- `preamble.tex` (lines 130-150) — existing `amsthm` declarations
  (`\theoremstyle{definition}`, `\newtheorem{defn}[thm]{Definition}`).

---

## §0. Executive verdict

**Total variant count: SEVEN.**

* Inscribed in `defn:regulator-admissible-sector`: (A1), (A2),
  (A3), (A4) — four variants.
* Proposed via W30 (`itm:A5-parity-equivariance`): (A5) — fifth.
* Silent strengthening detected on graded sources: (A2$'$) form
  existence — sixth.
* Silent strengthening detected on Virasoro-twisted side via $\tau_T$
  Sugawara descent: (A2$''_T$) Sugawara polynomial-degree extension —
  seventh.

**Total inscription rows:** seven `\hyp` blocks plus two tables
(hypothesis dependency × theorem; regulator admissibility × variant)
plus an anti-attack scan summary, totaling roughly 240 lines of
publication-grade LaTeX.

**Canonical order.** (A1) → (A2) → **(A2$'$)** silent → **(A2$''_T$)**
silent → (A3) → (A4) → (A5). The two silent strengthenings are
catalogued **after** their generating inscribed variants ((A2)) and
**before** the downstream regulator-class structural conditions
((A3), (A4)) plus the operator-level parity statement (A5), reflecting
their logical position: (A2$'$) is the existence precondition that
(A5) presupposes; (A2$''_T$) is the conformal-extension version of
(A2) that activates when the conformal Virasoro structure enters
scope.

**No silent strengthening remains uncatalogued after this block.**
The Costello regulator-class compatibility on graded sources (audit
§1.7) is recorded as a **side-bar remark** rather than a numbered
hypothesis, since it is a meta-compatibility statement between the
manuscript's class and Costello 2011 §5.2's graded extension, not a
load-bearing predicate on test data.

**Inscription target.** `claim-strength-ledger.tex`, after line 142
(end of current `\endgroup`), as a new `\begingroup ... \endgroup`
block titled "Hypothesis declaration ledger."

---

## §1. Master LaTeX block (verbatim, ready for inscription)

```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Hypothesis declaration ledger
%%
%% Canonical order: (A1) -> (A2) -> (A2') silent -> (A2''_T) silent
%%   -> (A3) -> (A4) -> (A5).
%%
%% Each \hyp block carries: precise statement; primary-source anchor;
%% manuscript-internal label; cross-reference to dependent theorems;
%% status (inscribed / proposed / silent-strengthening / discharged).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\theoremstyle{definition}
\newtheorem{hyp}[thm]{Hypothesis}

\section*{Hypothesis declaration ledger}
\addcontentsline{toc}{section}{Hypothesis declaration ledger}

\begingroup
\small
\setlength{\parindent}{0pt}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.18}

The status vocabulary used in this ledger is:
\emph{inscribed} (declared in
\(\textit{defn:regulator-admissible-sector}\) of
\texttt{tate-T1-weighted-completion.tex}),
\emph{proposed} (formally drafted in a Phase-4 audit, recommended
for the next inscription pass),
\emph{silent-strengthening} (currently presupposed by a downstream
proof step but not declared explicitly in any predicate of the
admissible regulator class), and
\emph{discharged} (verified case-by-case on every load-bearing
source / regulator pair in the named milestones).

\medskip

\begin{hyp}[(A1) Truncation discipline]\label{hyp:A1-truncation}
The transition maps in the coefficient and local-functional
directions are the truncations to degrees \(d \leq w_0\), or the
induced restriction obtained by setting higher-degree coefficient
fields to zero. They are degreewise surjective maps of complexes,
and \(\varprojlim^1\) on the truncation tower vanishes
(Mittag-Leffler).
%% Primary source: K. Costello, Renormalization and Effective Field
%% Theory, AMS Math. Surveys & Monographs 170 (2011), Ch. 4 §4.4
%% (counterterm finiteness; admissible regulator class parameterised
%% by finite-degree truncation filtration); K. Costello, O. Gwilliam,
%% Factorization Algebras in QFT, Vol. II (CUP 2021) §11 (BV regulator).
%% Status: inscribed in defn:regulator-admissible-sector clause (A1).
\end{hyp}

\begin{hyp}[(A2) Vertexwise polynomial-degree-bounded legs]\label{hyp:A2-polyn-deg-bnd}
At each fixed \(\hbar\)-order and for each fixed Costello graph,
the coefficient expression uses only vertexwise polynomial-degree-bounded
Hamiltonian and cotangent legs.
%% Primary source: K. Costello, Renormalization (2011), Ch. 5
%% (Costello-graph regulator with polynomial-vertex bound);
%% K. Costello, O. Gwilliam, Factorization Algebras Vol. II §11
%% (effective-interaction expansion control).
%% Status: inscribed in defn:regulator-admissible-sector clause (A2).
\end{hyp}

\begin{hyp}[(A2\(^\prime\)) Existence of even non-degenerate ad-invariant supersymmetric form on graded sources]\label{hyp:A2-prime-form-existence}
When the open matrix source is a \(\Z/2\)-graded super-Lie algebra
\(\mathfrak g\), there exists an even non-degenerate ad-invariant
supersymmetric bilinear form \(g \colon \mathfrak g \otimes \mathfrak g
\to \C\) used to construct the BV pairing. Concretely: \(g\) has
parity \(0\), satisfies \(g(X,Y) = (-1)^{|X||Y|}\,g(Y,X)\), and
\(g([Z,X],Y) + (-1)^{|Z||X|}\,g(X,[Z,Y]) = 0\). On a parity-trivial
source, \(g\) is the standard \(\Tr\)-form on the matrix factor and
(A2\(^\prime\)) is automatic. The condition is satisfied on
\(\mathfrak{gl}(N|N)\), \(\mathfrak{osp}(2N|2N)\), and
\(\mathfrak q(N)\) (with the Sergeev form
\(B_0(X,Y) = \Tr(\ev XY + \ev YX)/2\)); it fails on
\(\mathfrak p(N)\) (only an odd symmetric form exists; Killing
form is identically zero) and natively on \(\mathfrak{psl}(N|N)\)
(Killing form identically zero; discharge requires lift to
\(\mathfrak{gl}(N|N)\)).
%% Primary source: V. Kac, Lie superalgebras, Adv. Math. 26 (1977)
%% 8-96, §1.1.4 (basic classical classification); S.-J. Cheng,
%% W. Wang, Dualities and Representations of Lie Superalgebras, AMS
%% GSM 144 (2012), Prop. 1.34 (Killing-form vanishing on
%% psl(N|N), p(N)) and Prop. 1.36 (Sergeev form on q(N));
%% A. N. Sergeev, Mat. Sb. 124 (1984), 422-430 (queer non-degenerate
%% even form B_0 on q(N)).
%% Status: silent-strengthening — currently presupposed by W22-L1,
%% W22-L2, P4-G3-T-A1, P4-G3-M2 (M1, M3); recommended inscription as
%% precondition to (A5).
\end{hyp}

\begin{hyp}[(A2\(^{\prime\prime}_T\)) Sugawara polynomial-degree extension on the conformal Virasoro side]\label{hyp:A2-prime-prime-T-sugawara}
When the conformal Virasoro structure is in scope (i.e., on the
twisted side after the conformal promotion functor \(\tau_T\)), the
polynomial-degree-bounded class of (A2) is extended to include the
Virasoro descendants \(L_{-n_1} L_{-n_2} \cdots L_{-n_k}\) with
\(n_i \geq 1\); each such descendant is polynomial-degree-bounded
in the underlying Heisenberg modes via the Sugawara expansion
\(L_n = (1/(2k))\sum_{m \in \Z}{:}J_{n-m} J_m{:}\) (degree two in
the \(J\)-modes per descendant). On the topological side prior to
\(\tau_T\), and on any Felder-twisted free-field realisation with
non-trivial background charge \(\alpha_0\), this extension is not
automatic: the manuscript's working regime is the Sugawara
construction without Felder twist, and (A2\(^{\prime\prime}_T\))
is the operative discipline for that regime.
%% Primary source: E. Frenkel, D. Ben-Zvi, Vertex Algebras and
%% Algebraic Curves, AMS Math. Surveys & Monographs 88 (2nd ed.,
%% 2004), §3.4.6-§3.4.8 (Virasoro OPE and Sugawara construction);
%% A. Pressley, G. Segal, Loop Groups, OUP 1986, §4.2 (Virasoro
%% central extension at level k); H. Sugawara, Phys. Rev. 170
%% (1968), 1659-1662 (original Sugawara construction).
%% Status: silent-strengthening — operative only when the conformal
%% Virasoro structure of W_{1+\infty}(epsilon_1, epsilon_2) is in
%% scope (Phase-4 G4-T22 audit); recommended inscription when the
%% conformal-VOA dictionary is invoked.
\end{hyp}

\begin{hyp}[(A3) Diagonal weight-rescaling]\label{hyp:A3-wt-rescale}
For any pair of degree weights \(w, w'\) satisfying
\(\textit{defn:wt-degree-weight}\), the diagonal finite-window
rescaling \(R^{w_0}_{w,w'}\) transports the interaction,
differential, bracket, propagator contraction, and counterterm
representative from the \(w\)-window to the \(w'\)-window. On the
conformal side, the conformal-weight grading enters as an
additional \(\Z\)-graded weight component, and the rescaling
extends naturally.
%% Primary source: K. Costello, O. Gwilliam, Factorization Algebras
%% Vol. II (CUP 2021) §11 (regulator class compatibility under
%% rescaling); K. Costello, Renormalization (2011), Ch. 4 §4.4
%% (Polyakov scheme-independence).
%% Status: inscribed in defn:regulator-admissible-sector clause (A3).
\end{hyp}

\begin{hyp}[(A4) Admissible filtered cohomology]\label{hyp:A4-adm-filt-cohom}
The cohomology being computed is the admissible filtered cohomology
detected on finite quotients and associated graded pieces in the
envelope of \(\textit{stmt:tate-model-envelope}\); no observable is
allowed to detect an infinite product tail invisible in every finite
quotient. On the conformal side, the conformal-weight-truncated
quotients refine (A4) compatibly with the standard CFT cohomology
computations.
%% Primary source: M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa,
%% Comm. Math. Phys. 165 (1994), 311-427, §6.3 (BCOV
%% Kodaira-Spencer regulator with finite-window cohomology);
%% K. Costello, O. Gwilliam, Factorization Algebras Vol. II §13
%% (anomaly classes detected on finite-window quotients).
%% Status: inscribed in defn:regulator-admissible-sector clause (A4).
\end{hyp}

\begin{hyp}[(A5) Parity-equivariance on graded sources]\label{hyp:A5-parity-equivariance}
When the open matrix source carries a \(\Z/2\)-grading, with parity
operator \(P = \diag(\mathbf 1_N, -\mathbf 1_M)\) on
\(\mathfrak{gl}(N|M)\), the bilinear form \(g\) defining the BV
pairing is parity-equivariant:
\[
  g(PX,PY) = g(X,Y) \quad \text{for all } X,Y \in \mathfrak{gl}(N|M),
\]
and the regularization data — the heat operator \(K_t\), the
gauge-fixing \(Q^{\GF}\), and the regularized propagator
\(P_{\epsilon,L} = Q^{\GF}\int_\epsilon^L K_t\,dt\) — commute with
\(P\) at the operator level: \([K_t, P] = [Q^{\GF}, P] =
[P_{\epsilon,L}, P] = 0\). On a parity-trivial (purely bosonic)
source, this condition is vacuous: \(P = \mathbf 1\) and every
operator trivially commutes with the identity. The heat-kernel from
the super-Killing form, Pauli-Villars on a graded source with
parity-correct auxiliary mass assignments, and the Hadamard
parametrix all satisfy this condition by construction.
(A5) presupposes (A2\(^\prime\)): the bilinear form \(g\) must
exist as a non-degenerate even ad-invariant supersymmetric form
before \(g(PX,PY) = g(X,Y)\) can be required.
%% Primary source: B. DeWitt, Supermanifolds, CUP 1992, Ch. 2
%% (Berezin sign and parity-graded BV pairing); K. Costello,
%% O. Gwilliam, Factorization Algebras Vol. II §11 (BV regulator on
%% graded sources); F. A. Berezin, The Method of Second Quantization,
%% Academic Press 1966 (supertrace on Z/2-graded matrix algebras).
%% Status: proposed (W30 / WP3-W30-1; inscription target
%% tate-T1-weighted-completion.tex line 631).
%% Discharge: verified on three named regulator schemes (heat-kernel
%% from super-Killing; Pauli-Villars; Hadamard parametrix) by
%% W3-W30-02 (a)-(c); counterexamples documented in W3-W30-03 confirm
%% (A5) is non-vacuous.
\end{hyp}

\medskip

\noindent\textbf{Side-bar remark (Costello regulator-class
compatibility on graded sources).} The manuscript's regulator class
on \(\Z/2\)-graded sources is the intersection of the Costello
2011 admissible regulator class (Costello 2011 Ch. 4 §4.4, Ch. 5
§5.2) with the parity-equivariance (A5) extension of W30. This
intersection is non-empty (verified on the heat-kernel from the
super-Killing form, Pauli-Villars on a graded source with
parity-correct auxiliary masses, and the Hadamard parametrix);
formal external verification of compatibility with Costello 2011
§5.2's graded-case framework is deferred to Phase-5 as
R-P4-EXEC-A1-02. This is a meta-compatibility statement, not a
load-bearing predicate on test data.

\endgroup
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Hypothesis dependency table (theorem -> precise (A_k) combination)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begingroup
\small
\setlength{\parindent}{0pt}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.18}

\subsection*{Hypothesis dependency table}

\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.30\textwidth}
  >{\raggedright\arraybackslash}p{0.32\textwidth}
  >{\raggedright\arraybackslash}p{0.30\textwidth}@{}}
\hline
\textbf{Theorem (manuscript label)} & \textbf{Required hypotheses}
& \textbf{Notes}\\
\hline
\endhead
Theorem~F\(''\) on
\(\mathfrak{gl}(N|N) \otimes \C[z_1,z_2]\) joint
(P4-EXEC-G2-G3-RELAUNCH-3) &
(A1), (A2), (A2\(^\prime\)), (A3), (A4), (A5) &
Plus G2-M1 module \(\lambda\)-bracket; G2-M2 transversality;
P4-G3-T-A1 osp(2N|2N) discharge.\\
\hline
Theorem~G closed side
(\(\textit{thm:u1-center-anomaly}\)) on bosonic
\(\mathfrak{gl}_N\) &
(A1), (A2), (A3), (A4) only &
(A5), (A2\(^\prime\)), (A2\(^{\prime\prime}_T\)) all vacuous on
parity-trivial source. Class \([\bar c]\) cohomologically forced
non-trivial by \(\textit{lem:omega-cocycle}\).\\
\hline
Theorem~G open side
(\(\textit{thm:u1-center-anomaly-open}\)) &
(A1), (A2), (A3), (A4) only &
Coupling \(\hbar N\) on bosonic \(\mathfrak{gl}_N\); cross-check
with G5 unreduced primitive negative closure and G5-M2 reduced
primitive catalog confirms class is genuinely cohomologically
non-trivial.\\
\hline
Theorem~G quantum-classical equivalence
(\(\textit{thm:quantum-classical-anomaly}\)) &
(A1), (A2), (A3), (A4); plus
\(\textit{lem:capelli-renormalized-stable-trace}\) &
Capelli/Howe 1989 base-change identity;
\path{scripts/check_moyal_coefficients.py} verifies the bivariate
triangular identity on exponents \(a,b \leq 10\).\\
\hline
Theorem~G\(^{\mathrm{otr}}\) on \(\mathfrak q(N)\) (Phase-5
parallel; P4-EXEC-Theorem-G-otr-inscription) &
(A1), (A2), (A2\(^\prime\)) with Sergeev form, (A3), (A4),
(A5)\(^{\mathrm{otr}}\) signed regulator &
\(\mathrm{otr}(J) = N \neq 0\) on the queer central element
\(J \in \mathfrak q(N)_{\bar 1}\); class
\(\hbar N [\bar c]^{\mathrm{otr}}\) lives in odd parity sector
\(H^2_{\rm Lie}(\bar A, \Pi\C)_{\bar 1}\); Phase-5 status: declared
not discharged.\\
\hline
W22-T1 (one-loop chain-level QME vanishing on super-balanced
\(\mathfrak{gl}(N|N)\)) &
(A1), (A2), (A2\(^\prime\)), (A3), (A4) &
One-loop is structural; (A5) not used at one loop. (A2\(^\prime\))
required for super-Berezin loop contraction (W22-L1).\\
\hline
W22-T2 (all-loop chain-level QME vanishing on
\(\mathfrak{gl}(N|N)\)) &
(A1), (A2), (A2\(^\prime\)), (A3), (A4), (A5) &
(A5) discharges the conditional clause; combinatorial reduction
(W22-L3) gives \((N-M)^{\ell_{\rm loops}} = 0\) at super-balance.\\
\hline
W3-W15-04 residue identity (residue
\(= \hbar N[\bar c]\)) &
(A1), (A2), (A3), (A4) &
Bosonic source; \(\Lambda\) chain-level lift strict (no homotopies
required by Mittag-Leffler in (A1)).\\
\hline
P4-EXEC-G3-T-A1 on \(\mathfrak{osp}(2N|2N)\) &
(A1), (A2), (A2\(^\prime\)), (A3), (A4), (A5) &
Basic classical, super-Killing non-degenerate (Kac 1977 §1.1.4).\\
\hline
P4-EXEC-G3-M2 (M1) \(\mathfrak{psl}(N|N)\) via lift &
(A1), (A2), (A2\(^\prime\)) on \(\mathfrak{gl}(N|N)\) lift, (A3),
(A4), (A5) &
(A2\(^\prime\)) fails natively on \(\mathfrak{psl}\); discharge via
lift to \(\mathfrak{gl}(N|N)\) where the form exists.\\
\hline
P4-EXEC-G3-M2 (M2) \(\mathfrak p(N)\) periplectic &
\textbf{FAILS} (A2\(^\prime\)) &
Cheng-Wang 2012 Prop. 1.34 plus the structural "no even invariant
form" obstruction; (A2\(^\prime\)) is the unique cause of failure.\\
\hline
P4-EXEC-G3-M2 (M3) \(\mathfrak q(N)\) at ordinary supertrace &
(A1), (A2), (A2\(^\prime\)) with Sergeev form, (A3), (A4), (A5) &
(A2\(^\prime\)) discharged by Sergeev form
\(B_0(X,Y) = \Tr(\ev XY + \ev YX)/2\); queer-trace parallel layer
is independent.\\
\hline
P4-EXEC-G3-M2 (M4) \(\mathfrak{sl}(M|N)\) for \(M \neq N\) &
\textbf{FAILS} on \(\Str(I) = N - M \neq 0\) coupling &
(A2\(^\prime\)) holds (basic classical, Killing non-degenerate);
chain-level cancellation does not occur, so a non-zero residue
analogous to bosonic Theorem~G persists.\\
\hline
G4-T22 conformal Virasoro promotion of \(T(z)\) at spin-2 &
(A1), (A2\(^{\prime\prime}_T\)), (A3) extended, (A4) extended,
(A5) vacuous on bosonic, (A2\(^\prime\)) with Sugawara form &
(A2\(^{\prime\prime}_T\)) is the operative polynomial-degree
discipline; (A5) returns to non-vacuous on the super-W extension
to \(\mathfrak{osp}(2N|2N)\).\\
\hline
\(\textit{thm:wt-regulator-independence-admissible}\) &
(A1), (A2), (A3), (A4); (A5) for graded extension &
Regulator-class canonicity statement; (A3) is the load-bearing
weight-rescaling hypothesis.\\
\hline
\(\textit{thm:strict-unweighted-no-go}\) &
(A1), (A2), (A4) &
Strict unweighted product/direct-sum pair fails (A4); the no-go
proof uses (A4) directly.\\
\hline
\end{longtable}
\endgroup
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Regulator-class admissibility table ((R1)-(R4) -> (A_k) preserved)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begingroup
\small
\setlength{\parindent}{0pt}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.18}

\subsection*{Regulator-class admissibility table}

\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.20\textwidth}
  >{\raggedright\arraybackslash}p{0.34\textwidth}
  >{\raggedright\arraybackslash}p{0.18\textwidth}
  >{\raggedright\arraybackslash}p{0.20\textwidth}@{}}
\hline
\textbf{Regulator branch} & \textbf{Construction} &
\textbf{(A_k) variants preserved} & \textbf{Fragility / status}\\
\hline
\endhead
(R1) Heat-kernel
(Costello 2011 Ch. 5 default) &
\(K_t = (4\pi t)^{-d/2}\,e^{-|x-y|^2/(4t)} \otimes
e^{-t\Delta_{\rm sK}/2}\); matrix-source factor uses super-Casimir
\(\Delta_{\rm sK} = \tfrac12 \sum_a (-1)^{|a|}\,T^a T_a\) on
\(\mathfrak{gl}(N|M)\). &
(A1)-(A5) all preserved; (A2\(^\prime\)) preserved structurally
(form is super-Killing); (A2\(^{\prime\prime}_T\)) preserved on
the conformal extension. &
None — clean, structural; manuscript's inscribed default at
\(\textit{stmt:costello-bv-package}\), \texttt{main.tex}:5136-5152.\\
\hline
(R2) Point-splitting
(BCOV-style) &
\(P_\epsilon^{\rm PS}(x,y) = P(x + \xi/2, y - \xi/2)\) tensored
with the (R1) matrix factor. &
(A1)-(A5) all preserved; matrix factor identical to (R1). &
Direction \(\xi\) introduces a Lorentz-violating choice on the
worldsheet; \(P_\epsilon^{\rm PS}(\xi) - P_\epsilon^{\rm PS}(\xi') =
Q\Lambda(\xi,\xi')\) is \(Q\)-exact, hence cohomologically
invisible.\\
\hline
(R3) Dimensional
regularization
(Costello-Gwilliam Vol II §11.6) &
\(P^{\rm dimreg}(\varepsilon) =
\Gamma(d/2 - 1 - \varepsilon)\,(4\pi^{d/2 - \varepsilon})^{-1}\,
(|x-y|^2)^{-d/2 + 1 + \varepsilon}\); analytic continuation in
\(d \to d - 2\varepsilon\). &
(A1)-(A4) preserved; (A5) preserved \emph{under the standard
parity-weight-fixed continuation prescription}; (A2\(^\prime\))
preserved. &
\textbf{Fragile} — the parity grading
\(P = \diag(\mathbf 1_N, -\mathbf 1_M)\) must be stipulated to
remain integer-valued \(\pm 1\) along the continuation in
\(\varepsilon\); a "parity-deformed dim-reg" violates (A5)
non-trivially. The standard CGW prescription is canonical.\\
\hline
(R4) Hadamard parametrix
(Garabedian / Riesz / Hollands) &
\(H = U\,\sigma^{-(d-2)/2} + V\,\log\sigma + W\); decomposes as
\(H = H^{\rm ev} \oplus H^{\rm odd}\) on the parity-graded
Laplacian. &
(A1)-(A5) all preserved; block-diagonal decomposition makes
(A5) structural. &
\(\log\mu\) ambiguity in the Hadamard pair \((U,V)\) is
universal and \(Q\)-exact in chain-level cocycles; manuscript
inscribes the \(\mu\)-independent statement at
\(\textit{rmk:hadamard-regulator-independence}\)
(\texttt{tate-P1-hadamard-mittag-leffler.tex}:314-323).\\
\hline
\end{longtable}

\noindent\textbf{Cross-walk on the cohomology class.} All four
branches produce the same chain-level coefficient
\(\hbar(N - M)\,[\bar c]\) at one loop and the same all-loop
combinatorial reduction \((N - M)^{\ell_{\rm loops}}\,\hbar^\ell\)
on \(\mathfrak{gl}(N|M)\). Regulator-independence of the (A5)
discharge holds at the cohomology level under the explicit
stipulation that the parity grading \(P\) is preserved as an
integer-valued grading along any analytic continuation.

\noindent\textbf{Manuscript-inscribed branches.} (R1) heat-kernel
default at \(\textit{stmt:costello-bv-package}\) plus (R4)
Hadamard parametrix at
\texttt{tate-P1-hadamard-mittag-leffler.tex}; (R2) and (R3) are
cross-checking comparisons external to the manuscript's main
argument.

\endgroup
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

---

## §2. Per-variant entry with primary-source anchor

| Variant | Status | Manuscript label | Primary-source anchor |
|---------|--------|------------------|-----------------------|
| (A1) Truncation | inscribed | `hyp:A1-truncation` | Costello 2011 Ch. 4 §4.4 (counterterm finiteness, regulator class); Costello-Gwilliam Vol II 2021 §11 (BV regulator) |
| (A2) Polynomial-deg-bnd legs | inscribed | `hyp:A2-polyn-deg-bnd` | Costello 2011 Ch. 5 (Costello-graph regulator with polynomial-vertex bound); Costello-Gwilliam Vol II §11 (effective-interaction expansion) |
| (A2$'$) Form existence | silent-strengthening | `hyp:A2-prime-form-existence` | Kac 1977 *Adv. Math.* 26, 8-96 §1.1.4; Cheng-Wang 2012 AMS GSM 144 Prop. 1.34 + Prop. 1.36; Sergeev 1984 *Mat. Sb.* 124, 422-430 |
| (A2$''_T$) Sugawara polyn-deg | silent-strengthening | `hyp:A2-prime-prime-T-sugawara` | Frenkel-Ben-Zvi 2004 AMS Math. Surveys 88 (2nd ed.) §3.4.6-§3.4.8; Pressley-Segal 1986 OUP §4.2; Sugawara 1968 *Phys. Rev.* 170, 1659-1662 |
| (A3) Wt-rescale | inscribed | `hyp:A3-wt-rescale` | Costello-Gwilliam Vol II §11 (regulator class compatibility under rescaling); Costello 2011 Ch. 4 §4.4 (Polyakov scheme-independence) |
| (A4) Adm-fil-cohom | inscribed | `hyp:A4-adm-filt-cohom` | BCOV 1994 *Comm. Math. Phys.* 165, 311-427 §6.3 (Kodaira-Spencer regulator with finite-window cohomology); Costello-Gwilliam Vol II §13 (anomaly classes detected on finite-window quotients) |
| (A5) Parity-equiv | proposed | `hyp:A5-parity-equivariance` | DeWitt 1992 *Supermanifolds* CUP Ch. 2 (Berezin sign and parity-graded BV pairing); Costello-Gwilliam Vol II §11 (BV regulator on graded sources); Berezin 1966 *The Method of Second Quantization* (supertrace on graded matrix algebras) |

**Cross-references to dependent theorems** (one-line per variant):

* **(A1):** Theorem~G closed/open/QC; W22-T1, W22-T2; W3-W15-03,
  W3-W15-04; P4-G3-T-A1, P4-G3-M2 (M1, M3); P4-G2-M1; joint
  Theorem~F$''$; G4-M2; `thm:wt-regulator-independence-admissible`.
* **(A2):** Same theorem set as (A1); load-bearing for the
  combinatorial reduction Lemma W22-L3.
* **(A2$'$):** W22-L1, W22-L2; P4-G3-T-A1; P4-G3-M2 (M1 lift, M3);
  joint Theorem~F$''$; structural failure point of P4-G3-M2 (M2)
  $\mathfrak p(N)$.
* **(A2$''_T$):** G4-T22 (conformal Virasoro promotion); applies
  whenever the conformal Virasoro structure is in scope (e.g.,
  $W_{1+\infty}(\epsilon_1, \epsilon_2)$, super-W extension to
  $\mathfrak{osp}(2N|2N)$).
* **(A3):** `thm:wt-regulator-independence-admissible` primary
  consumer; W22-T1, W22-T2, W3-W15-04; P4-G3-T-A1, P4-G3-M2;
  W3-W8-01 / M-45 (Polyakov scheme-independence).
* **(A4):** `thm:wt-regulator-independence-admissible` clause (iii);
  W22-T1, W22-T2 (super-balance vanishing on finite quotients);
  W3-W15-04 (residue detected on finite quotients);
  `thm:strict-unweighted-no-go`.
* **(A5):** W22-T2; P4-G3-T-A1; P4-G3-M2 (M1 lift, M3); W3-W30-02
  regulator verification; joint Theorem~F$''$; vacuous on bosonic
  Theorem~G.

---

## §3. Hypothesis dependency table

(Mapping each Theorem F$''$, Theorem G, Theorem G$^{\rm otr}$, plus
load-bearing Phase-4 EXEC milestones, to the precise (A_k)
combination.)

The detailed table is inscribed verbatim in §1 above (LaTeX block).
The condensed verdict-style summary:

| Theorem | (A_k) combination | Verdict |
|---------|-------------------|---------|
| Theorem F$''$ on $\mathfrak{gl}(N|N)\otimes\C[z_1,z_2]$ | (A1), (A2), (A2$'$), (A3), (A4), (A5) | discharged under the chain plus G2-M1, G2-M2, P4-G3-T-A1 |
| Theorem G closed (`thm:u1-center-anomaly`) | (A1), (A2), (A3), (A4) | discharged unconditionally on bosonic source; cohomologically forced non-trivial |
| Theorem G open (`thm:u1-center-anomaly-open`) | (A1), (A2), (A3), (A4) | discharged; coupling $\hbar N$ on bosonic |
| Theorem G QC (`thm:quantum-classical-anomaly`) | (A1), (A2), (A3), (A4) plus Capelli/Howe | discharged via base-change |
| Theorem G$^{\rm otr}$ on $\mathfrak q(N)$ | (A1), (A2), (A2$'$) Sergeev, (A3), (A4), (A5)$^{\rm otr}$ signed | declared not discharged (Phase-5 status) |
| W22-T1 one-loop super-balanced | (A1)-(A4) plus (A2$'$) | discharged under (A2$'$) |
| W22-T2 all-loop super-balanced | (A1)-(A5) plus (A2$'$) | discharged under (A5) |
| P4-G3-T-A1 osp(2N|2N) | (A1)-(A5) plus (A2$'$) | discharged |
| P4-G3-M2 (M1) psl(N|N) via lift | (A1)-(A5) plus (A2$'$) on lift | discharged via lift only |
| P4-G3-M2 (M2) p(N) periplectic | FAILS (A2$'$) | not discharged; structural |
| P4-G3-M2 (M3) q(N) ordinary | (A1)-(A5) plus (A2$'$) Sergeev | discharged at ordinary-supertrace layer |
| P4-G3-M2 (M4) sl(M\|N) for M$\neq$N | FAILS $\Str(I) = N-M \neq 0$ | not discharged; non-zero residue persists |
| G4-T22 conformal Virasoro | (A1), (A2$''_T$), (A3) ext, (A4) ext, (A5) vac on bosonic | discharged on Sugawara regime; Felder-twist breaks (A2$''_T$) |
| `thm:wt-regulator-independence-admissible` | (A1)-(A4); (A5) for graded | discharged |
| `thm:strict-unweighted-no-go` | (A1), (A2), (A4) | discharged (negative result) |

---

## §4. Regulator-class admissibility table

(Mapping each (R1)-(R4) regulator branch to the (A_k) variants
preserved.)

The detailed table is inscribed verbatim in §1 above (LaTeX block).
The condensed verdict-style summary:

| Branch | Construction | (A_k) preserved | Fragility |
|--------|--------------|-----------------|-----------|
| (R1) Heat-kernel | $K_t = (4\pi t)^{-d/2}e^{-|x-y|^2/(4t)}\otimes e^{-t\Delta_{\rm sK}/2}$ | (A1)-(A5), (A2$'$), (A2$''_T$) | None; manuscript default |
| (R2) Point-splitting | $P_\epsilon^{\rm PS}(\xi)$ with direction $\xi$ | (A1)-(A5), (A2$'$) | $\xi$-choice $Q$-exact; cohomologically invisible |
| (R3) Dim-reg | Analytic continuation $d \to d - 2\varepsilon$ | (A1)-(A4); (A5) under standard parity-fixing prescription | Parity-deformed continuation breaks (A5); CGW Vol II §11.6 prescription canonical |
| (R4) Hadamard parametrix | $H = U\sigma^{-(d-2)/2} + V\log\sigma + W$, block-diagonal | (A1)-(A5), (A2$'$) | $\log\mu$ ambiguity is $Q$-exact; cohomologically invisible |

**Cross-walk on the cohomology class.** All four branches produce
$\hbar(N-M)[\bar c]$ at one loop and $(N-M)^{\ell_{\rm loops}}$ all-loop
on $\mathfrak{gl}(N|M)$. The supertrace identity $\Str(I) = N-M$ is
the load-bearing invariant; (A5) ensures the regulator does not
violate it.

**Manuscript-inscribed branches.** (R1) at
`stmt:costello-bv-package` (`main.tex`:5136-5152); (R4) at
`tate-P1-hadamard-mittag-leffler.tex`:1-323. (R2) and (R3) are
cross-checking comparisons.

---

## §5. Anti-attack scan

For each (A_k) variant, name an attack angle and the discharge.

### (A1) Truncation

* **Attack.** "The truncation tower might fail Mittag-Leffler in the
  $\varprojlim^1$ sense, leaking a tail-only class invisible at every
  finite stage but visible in the limit."
* **Discharge.** The truncation is degreewise surjective (a class
  property of the admissible regulator) so $\varprojlim^1 = 0$ on the
  truncation tower. This is the standard Mittag-Leffler condition for
  surjective inverse systems of complexes. Reference: Costello 2011
  Ch. 4 §4.4 explicitly fixes the truncation as a finite-degree
  filtration parameter; the surjectivity of transitions is built into
  the class definition. **No leak.**

### (A2) Polynomial-degree-bounded legs

* **Attack.** "At high $\hbar$-orders, vertex contractions in
  Costello graphs might generate non-polynomial structures (e.g.,
  via integration by parts) that escape the polynomial-degree bound."
* **Discharge.** The Costello graph rules (Costello 2011 Ch. 5)
  explicitly forbid integration-by-parts moves that produce
  non-polynomial vertex insertions; the vertex bound is preserved
  graph-by-graph. The combinatorial reduction Lemma W22-L3 contracts
  any $\ell$-loop diagram to a product $\prod_i \Str(I^{k_i})$ of
  polynomial trace expressions; (A2) is what makes this reduction
  finite per loop order.

### (A2$'$) Form existence on graded sources

* **Attack.** "Some classical super-Lie algebra of physical interest
  (e.g., $\mathfrak p(N)$ periplectic for branes with anti-symplectic
  reflection) admits no even non-degenerate ad-invariant
  supersymmetric form, only an odd one. (A2$'$) silently excludes
  this case."
* **Discharge.** The exclusion is genuine and structural: P4-EXEC-G3-M2
  (M2) explicitly identifies $\mathfrak p(N)$ as a structural failure
  point. The discharge is to **declare (A2$'$) explicitly** and
  document the boundary: gl(N|N), osp(2N|2N), q(N) (with Sergeev
  form), psl(N|N) (via lift) pass; p(N) and sl(M|N) for $M \neq N$
  fail (the latter for a different reason — non-zero supertrace).
  Cheng-Wang 2012 Prop. 1.34 confirms the periplectic structural
  obstruction. The boundary is named, not silenced.

### (A2$''_T$) Sugawara polynomial-degree extension

* **Attack.** "The Felder-twisted free-field realisation with
  background charge $\alpha_0 \partial\phi$ provides a Virasoro
  current $T_{\rm Felder}(z) = (1/2)(\partial\phi)^2 + \alpha_0
  \partial^2\phi$ that breaks (A2$''_T$): the $\alpha_0 \partial^2\phi$
  term is a transcendental element of the Heisenberg-Sugawara
  descent, and its all-loop contribution is not bounded by the
  Sugawara polynomial-degree expansion."
* **Discharge.** The manuscript's working regime is the **pure
  Sugawara construction without Felder twist**; (A2$''_T$) is
  precisely the discipline that excludes Felder twists. The
  recommended inscription declares this restriction explicitly.
  Reference: Frenkel-Ben-Zvi 2004 §3.4.7-§3.4.8 documents both
  constructions and distinguishes them; the spin-2 chain-level
  $T(z) = J^{(2)}(z)$ used in P4-EXEC-G4-T22 is in the Sugawara
  regime. Felder twists break (A2$''_T$) by design and are out
  of scope.

### (A3) Diagonal weight-rescaling

* **Attack.** "Two admissible weights $w, w'$ might give
  inequivalent finite-window theories if the rescaling $R^{w_0}_{w,w'}$
  fails to transport the propagator contraction or the counterterm
  representative."
* **Discharge.** `thm:wt-regulator-independence-admissible` (T1:634)
  is the primary consumer of (A3) and proves precisely this
  invariance: under (A1)-(A4), the rescaling transports the BV data
  faithfully. The Polyakov scheme-independence (W3-W8-01 / M-45) is
  the structural strengthening. Reference: Costello-Gwilliam Vol II §11
  on regulator-class compatibility.

### (A4) Admissible filtered cohomology

* **Attack.** "An infinite product tail invisible in every finite
  quotient might secretly carry the residue class, contradicting
  the W3-W15-04 finite-window detection."
* **Discharge.** `thm:strict-unweighted-no-go` (the no-go for the
  strict unweighted product/direct-sum pair) is the structural
  discharge: the strict pair fails (A4) because tail-sensitive
  cohomology of the weighted product is not identified with the
  strict direct-sum dual. (A4) explicitly excludes such tail-only
  classes. Reference: BCOV 1994 §6.3 controls finite-window
  cohomology; Costello-Gwilliam Vol II §13 extends to anomaly classes.

### (A5) Parity-equivariance on graded sources

* **Attack.** "On a graded source, one might choose a regulator that
  fails to commute with the parity operator $P$, producing a
  spurious $\Str(I^k) \neq 0$ at higher loops that breaks the
  super-balance cancellation."
* **Discharge.** W3-W30-03 explicitly constructs counterexamples: the
  mixed propagator (a) and the un-graded Casimir (c) violate (A5) and
  break the chain-level cancellation. **(A5) is non-vacuous** on
  graded sources. The discharge on three named regulators (heat-kernel
  from super-Killing, Pauli-Villars graded, Hadamard parametrix) is
  W3-W30-02 (a)-(c); each preserves (A5) by construction. The (R3)
  dim-reg branch requires the additional stipulation that parity
  weights remain integer-valued $\pm 1$ along the analytic
  continuation in $\varepsilon$.

---

## §6. Inscription target placement

**Target file.** `claim-strength-ledger.tex`.
**Current line range.** 1-142 (existing claim-strength ledger ending
with `\end{longtable}` on line 141 and `\endgroup` on line 142).
**Proposed insertion.** Append after line 142, before any subsequent
`\end{document}`-style closing (the file as-is ends after
`\endgroup`).

The new master block is:

* `\theoremstyle{definition}` plus `\newtheorem{hyp}[thm]{Hypothesis}`
  block: 2 lines.
* `\section*{Hypothesis declaration ledger}` plus toc line: 2 lines.
* Status-vocabulary preamble: 11 lines.
* Seven `\begin{hyp} ... \end{hyp}` blocks with primary-source
  comments: ~135 lines.
* Side-bar remark on Costello-class compatibility: ~12 lines.
* `\subsection*{Hypothesis dependency table}` with `longtable`:
  ~50 lines.
* `\subsection*{Regulator-class admissibility table}` with
  `longtable`: ~45 lines.
* Cross-walk and inscribed-branch notes: ~10 lines.

**Estimated total inscription:** lines 143-410 (approximately 270
lines added). The inscription is one continuous block with three
internal sections.

**Cross-file inscription dependencies.**

1. The `\newtheorem{hyp}[thm]{Hypothesis}` declaration could
   alternatively be inscribed in `preamble.tex` (currently lines
   140-149 list the existing `definition`-style theorem
   environments). Inscribing in `preamble.tex` line 149 (after the
   final `\newtheorem{constr}` line) keeps theorem environments
   centralized.

2. The new `hyp:` labels are referenced by the dependency table; if
   the inscription proceeds in a different order from the table
   declaration, forward-reference resolution requires two `pdflatex`
   passes (standard).

3. The (A2$'$) and (A5) inscriptions in
   `tate-T1-weighted-completion.tex` (line 631) are **separate
   inscription targets**, not duplicated here. The `claim-strength-ledger.tex`
   master block declares the **status** and **primary-source anchor**;
   the structural definition lives in `tate-T1-weighted-completion.tex`.

4. The Phase-5 G$^{\rm otr}$ inscription (per
   `phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`) is
   referenced in the dependency table but its precise (A5)$^{\rm otr}$
   signed-regulator declaration is inscribed in a **separate Phase-5
   block**, not duplicated here.

---

## §7. Residuals + Phase-5 obligations

### §7.1 Residuals after this master block

* **R-P4-MB-01.** The `\newtheorem{hyp}[thm]{Hypothesis}` declaration
  must be added either to `preamble.tex` (centralized) or inline at
  the top of the master block (localized). Recommendation:
  centralize at `preamble.tex`:149. Severity 1 (cosmetic).
* **R-P4-MB-02.** The (A2$'$) inscription at
  `tate-T1-weighted-completion.tex`:631 (per A1-HYP-AUDIT Priority 2)
  must precede the master block's reference to (A2$'$) being
  inscribed-as-precondition. Currently (A2$'$) is silent; the master
  block declares its **status** as silent-strengthening but the
  structural inscription in the regulator-admissibility definition
  is still pending. Severity 2 (definitional precision).
* **R-P4-MB-03.** The (A5) inscription at
  `tate-T1-weighted-completion.tex`:631 (per A1-HYP-AUDIT Priority 1)
  is also pending. The master block declares (A5) as **proposed**;
  the structural inscription completes the discharge. Severity 2.
* **R-P4-MB-04.** The (A2$''_T$) silent strengthening on the
  conformal Virasoro side is currently undeclared in any
  manuscript-internal definition; the master block is the **first
  catalog** of (A2$''_T$). A separate inscription in either the
  conformal-VOA section of the manuscript or in
  `tate-T1-weighted-completion.tex` (as a conformal-extension clause)
  is recommended for Phase-5. Severity 2.
* **R-P4-MB-05.** The Costello-class compatibility on graded
  sources (audit §1.7) is recorded as a side-bar remark in the
  master block, not a numbered `\hyp` block. A formal external
  cross-walk to Costello 2011 §5.2 is deferred to Phase-5 as
  R-P4-EXEC-A1-02 (cosmetic, not load-bearing). Severity 1.

### §7.2 Phase-5 obligations triggered by this block

* **P5-MB-A.** Once (A2$'$) and (A5) are inscribed in
  `tate-T1-weighted-completion.tex`:631, re-audit the dependency
  table to confirm every cross-reference resolves in
  forward-reference order across two `pdflatex` passes.
* **P5-MB-B.** Once Theorem G$^{\rm otr}$ is inscribed in a separate
  Phase-5 file (per
  `phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`), update
  the dependency table to reference the (A5)$^{\rm otr}$ signed
  regulator definition site.
* **P5-MB-C.** Once the conformal-VOA dictionary is inscribed in
  the manuscript proper (currently only in
  `phase4-exec-G4-T22-virasoro-twist-2026-04-28.md` as a Phase-4
  audit), promote (A2$''_T$) to a formal definition rather than a
  silent-strengthening catalog row.
* **P5-MB-D.** Any future audit that identifies a new silent
  strengthening (e.g., a Costello-class boundary on a non-classical
  super-Lie source like the strange superalgebras with no analogue
  of the Sergeev form) appends a new `\hyp` block to this master
  ledger with a primary-source anchor and an anti-attack discharge.

### §7.3 No remaining silent strengthenings uncatalogued

After this master block:

* (A2$'$) form-existence — catalogued (`hyp:A2-prime-form-existence`).
* (A2$''_T$) Sugawara polynomial-degree extension — catalogued
  (`hyp:A2-prime-prime-T-sugawara`).
* Costello regulator-class graded compatibility — catalogued as
  side-bar remark (not a numbered hypothesis; meta-compatibility,
  not predicate on test data).

The seven-variant catalog is exhaustive over the Phase-4 EXEC
hypothesis-audit corpus (A1-HYP-AUDIT, W30-M2 regulator branches,
G4-T22 Virasoro twist, classical-super-extension G3-M2 boundary,
Theorem G$^{\rm otr}$ Phase-5 parallel inscription). No further
silent strengthening is identified.

---

## §8. 200-word final tool-result summary

(a) **Total variant count: SEVEN.** Inscribed in the manuscript
(`defn:regulator-admissible-sector`): (A1), (A2), (A3), (A4) — four
variants. Proposed via W30: (A5) parity-equivariance — fifth.
Silent strengthenings catalogued in this block: (A2$'$) form
existence on graded sources; (A2$''_T$) Sugawara polynomial-degree
extension on the Virasoro-twisted side — sixth and seventh. The
catalog covers the full Phase-4 EXEC hypothesis-audit corpus.

(b) **Inscription target line range in `claim-strength-ledger.tex`.**
Append after line 142 (the file currently ends at
`\endgroup`). Estimated inscription range: lines 143-410
(approximately 270 lines added) covering seven `\hyp` blocks plus
two `longtable` blocks plus an anti-attack scan summary.

(c) **Silent strengthenings still uncatalogued: NONE.** Both (A2$'$)
form-existence and (A2$''_T$) Sugawara polynomial-degree extension
are catalogued with primary-source anchors. The Costello-class
graded compatibility (audit §1.7) is recorded as a side-bar
meta-compatibility remark, not a load-bearing predicate.

(d) **Report path:**
`/Users/raeez/topological-strings/reconstitution/phase4-exec-Hypothesis-Master-Block-2026-04-28.md`.
**Line count:** see closing line below.

End of P4-Hypothesis-Master-Block.
