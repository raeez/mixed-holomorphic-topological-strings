# Regular-density / wavefront current graph branch construction target

Date: 2026-04-30.
Owner: Agent 237.
Scope: non-scalar Costello/QME realization for the local mixed holomorphic-topological SFT on
`R^2_top x C^2_hol`.

## Stable theorem surface

The strongest current theorem target is not a theorem over all compactly
supported distributions.  It is the following two-level construction.

1. Regular-density graph branch.  Work on
   `D_c^reg(I) = { b(t) dt : b in C_c^\infty(I) }`.  Under the finite-window
   Costello brane-defect graph calculus, weighted finite-scale propagator,
   BV Laplacian, locality estimates, interval/truncation/weight compatibility,
   and scalar-contact chain projection, the graph curvature residual is a
   genuine element of the regular-density obstruction complex.  The certificate
   target is
   `W = -o` and `C = 0` inside the regular-density closed-exchange complex,
   hence the regular classes
   `eta^reg`, `kappa^reg`, `beta^cl,reg`, `mu^cl,reg`, and `lambda^cl,reg`
   vanish.

2. Wavefront-admissible distributional branch.  For distributional labels,
   graph contractions are defined only on graphwise admissible tuples.  For a
   graph `Gamma`, finite window `M`, and labels `B_j`, form the pushed-forward
   current `B_Gamma` on the graph configuration space.  The tuple is admissible
   only when the incidence maps are non-characteristic/proper, each Hadamard
   coefficient `K^M_{Gamma,alpha}` satisfies
   `(WF(K^M_{Gamma,alpha}) + WF(B_Gamma)) cap 0 = empty`, the product has
   finite scaling degree along every small diagonal, and the final pushforward
   lands in the allowed local-functional wavefront class.  One-sided conormal
   cones can supply non-regular examples, but an arbitrary `D'_c(I)` label does
   not.

The full arbitrary-current graph theorem remains open unless one adds extra
renormalization data beyond the present canonical Costello/wavefront calculus.
The correct theorem is therefore a positive regular-density/wavefront theorem
plus an exact obstruction theorem for the non-admissible remainder.

## Correct habitats

Source current complex:

```tex
\mathfrak g^{w,cur}_{\hbar,I}
  =
  (\Omega_c^\bullet(I)\widehat\otimes \mathfrak h_{w,\hbar})
  \ltimes
  (\mathcal D'_c(I)\widehat\otimes \mathfrak h^\vee_{w,\hbar})[1].
```

The regular subsource replaces `D'_c(I)` by `D_c^reg(I)`.  A wavefront source is
not a linear source by default: it is first a finite-tuple relation
`D'_{c,WF}(I;Gamma,M)`.  It becomes a continuous CE source only after choosing a
linear subspace whose every finite tuple is admissible for the graphs and
windows used.

Target current/local-functional habitat:

```tex
\mathfrak Q^\bullet_{w,\partial,\hbar}(I)
  =
  \varprojlim_M
  \mathcal O^\bullet_{loc,bd}(\mathcal E_w|_I;
      \mathcal A^{pp,w}_{\partial,\hbar,M}(I)),
\qquad
d_M = Q + \{ I^w_{0,M}, - \}_{\hbar,M}.
```

The convolution habitat is

```tex
\mathfrak K^\bullet_{w,\hbar}(I)
  =
  \operatorname{Hom}_{cont}
  (CE_{cont}(\mathfrak g^{w,cur}_{\hbar,I}),
   \mathfrak Q^\bullet_{w,\partial,\hbar}(I)).
```

This is the unreduced non-scalar habitat.  The reduced principal-part current
model is obtained only after the scalar-contact chain projection and de Rham
current contraction.  It cannot be used as the native graph/QME target.

## Propagator and graph contraction class

The propagator must be a weighted finite-scale Costello brane-defect kernel
`P^{w,M}_{epsilon,L}` with BV Laplacian `Delta^{w,M}_L`, Hadamard expansion near
small diagonals, and a coefficient coevaluation compatible with the weighted
Tate completion.  Positive scale smoothness is insufficient: the
`epsilon -> 0` extension must produce local counterterms compatible with
interval extension, finite-window truncation, and weight restriction.

For a graph `Gamma`, the contraction map is the composite:

1. pull/push the external current labels through the incidence maps to
   `B_Gamma`;
2. multiply `B_Gamma` by the propagator/Hadamard coefficient product
   `K^M_{Gamma,alpha}` using Hormander's product criterion;
3. extend across every collision diagonal with finite scaling degree;
4. add local counterterms supported on diagonal strata;
5. push forward to the boundary local-functional target;
6. verify compatibility with interval inclusions, `M -> N` truncations, and
   weight maps.

If any product, extension, or pushforward step is undefined, there is no
canonical graph contraction map for that label tuple.

## Scalar-contact projection and non-scalar curvature

The scalar-contact filtration `F^\bullet` and the actual chain projection
`\widehat\sigma_{sc}` must be fixed before the residual obstruction is even a
class.  The associated-graded scalar symbol is only a diagnostic.  The first
test is

```tex
\widehat\sigma_{sc}
\left(
  d_{QME}\kappa + {1\over 2}[\kappa,\kappa]_\hbar
\right)
= 0.
```

Only after this scalar-contact equation holds does the residual live in

```tex
H^1(\ker \widehat\sigma_{sc}, d_{QME}).
```

For a finite window `M` and first unsolved order `n_0`, the non-scalar residual
has the form

```tex
o^{ns}_{n_0,M}
 =
[\hbar^{n_0}]
\left(
 Ob^{red}_{w,\partial,\hbar,M}
 + d_M C_{<n_0,M}
 + {1\over 2}\{ C_{<n_0,M}, C_{<n_0,M}\}_{\hbar,M}
\right).
```

The fixed-window problem is a counterterm equation `A^M c = -r^M`.  The exact
fixed-window obstruction is a left-null covector `ell` with
`ell A^M = 0` and `ell(r^M) != 0`.  Tower compatibility is the corresponding
Roos / `varprojlim^1` obstruction.

## Wavefront obstruction theorem

Let

```tex
S_c(I) = D'_c(I) / D_c^reg(I).
```

At the first order/window where a non-regular wavefront component survives,
write the singular quotient residual as

```tex
s^{WF}_{n_0,M}
 =
q_M[\hbar^{n_0}]
\left(
 Ob^{red,neg\,rd}_{w,\partial,\hbar,M}
 + d_M C^{neg\,rd}_{<n_0,M}
 + \{ C^{reg}_{<n_0,M}, C^{neg\,rd}_{<n_0,M}\}_{\hbar,M}
 + {1\over 2}
   \{ C^{neg\,rd}_{<n_0,M}, C^{neg\,rd}_{<n_0,M}\}_{\hbar,M}
\right).
```

The exact regular-density obstruction class is

```tex
\eta^{reg}_{n_0,M} = [s^{WF}_{n_0,M}]
  \in H^1(\mathfrak Q^\bullet_{w,M}(I) / X^{reg}_{w,M}(I)).
```

The wavefront branch is obstructed in the original complex unless there is a
degree-zero distributional counterterm `C^{sing}_{n_0,M}` such that

```tex
\bar d_M q_M(C^{sing}_{n_0,M}) = -s^{WF}_{n_0,M}.
```

Adjoining a formal primitive cone with `d p^{WF}_{n_0,M} = -\hat s^{WF}_{n_0,M}`
is an extension of the complex, not a proof that the original current graph
branch is exact.

For arbitrary `D'_c(I)`, the stronger obstruction is microlocal before
cohomological: a pair such as `B_1 = B_2 = delta_{t_0}` against a boundary
propagator with conormal wavefront directions violates the product criterion.
Thus no canonical product `K^M_{Gamma,alpha} B_Gamma`, no canonical diagonal
extension, and no intrinsic graph weight exist without an additional
renormalization rule.

## Construction target

The remaining construction target is:

1. construct a current-compatible finite-scale Costello graph calculus on
   `D_c^reg(I)` and on a named wavefront-admissible subspace;
2. prove the propagation, product, diagonal-extension, counterterm,
   interval-extension, truncation, and weight-compatibility estimates;
3. construct `\widehat\sigma_{sc}` as a chain projection on that habitat;
4. solve the finite-window non-scalar counterterm equations or exhibit the
   fixed-window left-null obstruction;
5. solve the Roos tower compatibility equations or exhibit the
   `varprojlim^1` obstruction;
6. for non-regular wavefront labels, either find the original degree-zero
   singular primitive above or record `\eta^{reg}_{n_0,M}` as the exact
   obstruction class;
7. for arbitrary `D'_c(I)`, either supply extra renormalization data defining
   the failed products/extensions functorially, or state the microlocal
   no-canonical-graph-contraction obstruction theorem.

## Checkable anchors

- `local-dictionary.tex:781`, `local-dictionary.tex:798`,
  `local-dictionary.tex:876`, `local-dictionary.tex:911`,
  `local-dictionary.tex:955`, `local-dictionary.tex:1046`,
  `local-dictionary.tex:1063`.
- `claim-strength-ledger.tex:247`, `claim-strength-ledger.tex:413`,
  `claim-strength-ledger.tex:974`, `claim-strength-ledger.tex:1066`.
- `open-obligations.tex:342`, `open-obligations.tex:413`,
  `open-obligations.tex:436`, `open-obligations.tex:501`.
- `main.tex:7251`, `main.tex:7403`, `main.tex:7441`,
  `main.tex:7495`, `main.tex:8022`.
- `theorem-lanes.tex:3212`, `theorem-lanes.tex:3234`,
  `theorem-lanes.tex:3325`.
- `appendix-factorization-current-conventions.tex:912`,
  `appendix-factorization-current-conventions.tex:1029`,
  `appendix-factorization-current-conventions.tex:1199`,
  `appendix-factorization-current-conventions.tex:1394`,
  `appendix-factorization-current-conventions.tex:1482`,
  `appendix-factorization-current-conventions.tex:1614`.
- `tate-T1-weighted-completion.tex:2030`,
  `tate-T1-weighted-completion.tex:2175`,
  `tate-T1-weighted-completion.tex:2398`.
- `scripts/finite_window_graph_array.py:1`,
  `scripts/finite_window_graph_array.py:1872`.
