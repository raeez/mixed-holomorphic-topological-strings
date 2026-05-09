# Attack-Heal Wave 6: Finite-\(N\) Radial Parts, All-\(N\) Normalization

Date: 2026-04-28.

Scope:

- `appendix-radial-parts-moyal.tex`
- `scripts/check_moyal_coefficients.py`
- `references/primary-sources/radial-parts-capelli-source-anchors-2026-04-28.md`
- `references/source-provenance.md`
- `references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.{pdf,txt}`

## Claim Attacked

The finite-\(N\) radial-parts theorem uses the exact Weyl-trace image

```tex
\operatorname{Rad}_0(J_N(f))
  =\Delta^{-1}\left(\sum_i
    \operatorname{Op}_{\mathrm W}
      (f)(\lambda_i,-\hbar\partial_{\lambda_i})\right)\Delta
```

with \(Y^i{}_j=-\hbar\partial_{X^j{}_i}\) on
\(\mathcal D_\hbar(\mathfrak{gl}_N)\) and
\(z_2=-\hbar\partial_\lambda\) on the Cartan.

## All-\(N\) Status

No all-\(N\) source closure was found.  The Harish-Chandra--Wallach--
Levasseur--Stafford line still sources the radial-component framework,
regular-Cartan landing, kernel/surjectivity context, and discriminant
lineage.  It does not state the manuscript's exact Weyl-trace generator
normalization with total Weyl ordering and the above signs.

The conditional input is now sharper.  Lemma
`lem:app-radial-pure-shear-extension` proves that it is enough to source:

1. the pure \(z_1\)-power images;
2. the pure \(z_2\)-power images;
3. compatibility with the Weyl adjoint shears
   \(Y\mapsto Y+p(X)\), equivalently
   \(-\hbar\partial_{\lambda_i}\mapsto
   -\hbar\partial_{\lambda_i}+p(\lambda_i)\).

Under those hypotheses, coefficient extraction from the shear of
\(J_N(z_2^{b+1})\) gives

```tex
[t]\;J_N((z_2+t z_1^a)^{b+1})
  =(b+1)J_N(z_1^az_2^b),
```

and the same coefficient extraction on the Cartan gives the exact
\(S_N(z_1^az_2^b)\) image.  This proves the pure-power/shear extension,
but the source for the pure-power/shear package itself remains missing.

## Exact Formulas and Constants

Moyal product:

```tex
f*g=m\exp((\hbar/2)P)(f\otimes g),
\qquad
P=\partial_{z_1}\otimes\partial_{z_2}
  -\partial_{z_2}\otimes\partial_{z_1}.
```

Raw commutator coefficients:

```tex
[f,g]_{\rm raw}
  =\sum_{r\ge1,\ r\ {\rm odd}}
    \frac{2}{2^r r!}\hbar^r P^r(f,g).
```

First, third, fifth odd coefficients checked by script:

```text
r=1: 1
r=3: 1/24
r=5: 1/1920
```

Capelli/Weyl triangular normalization:

```tex
J_N(z_1^az_2^b)\equiv
  \sum_{r=0}^{\min(a,b)}
    \left(-\frac{\hbar N}{2}\right)^r
    r!\binom ar\binom br\,T_{a-r,b-r}.
```

Normal-ordering defect checked:

```tex
\hbar^{-1}[T_{2,1},T_{0,2}]
  =4T_{1,2}-2\hbar N T_{0,1}.
```

Direct radial comparison used by the low-rank harness:

```text
Delta * (J_N(f)F)|_t = S_N(f)(Delta * F|_t)
```

This avoids a separate polynomial division by \(\Delta\).

## Low-Rank Tests

Command:

```bash
python3 scripts/check_moyal_coefficients.py
```

Result: pass.

Ranges and counts:

- Moyal monomial sweep: \(14641\) monomial pairs, exponents
  \(0,\ldots,10\), orders through \(11\).
- Capelli round trip: \(121\) monomials with \(a,b\leq10\).
- Direct radial restriction: \(80\) exact operator/test-polynomial
  comparisons for \(N=2\), and \(80\) for \(N=3\).
- Cartan Moyal commutator: primary cases plus higher-order cases with
  nonzero \(P^3\) and \(P^5\).
- Even commutator orders \(2,4,6,8,10\): vanish on tested primary cases.

Direct radial operators in each rank:

```text
z1, z1^2, z1^3, z2, z2^2, z2^3,
z1 z2, z1^2 z2, z1 z2^2, z1^2 z2^2.
```

Invariant test functions in each rank:

```text
1, Tr X, Tr X^2, Tr X^3, (Tr X)^2, (Tr X)(Tr X^2),
(Tr X)^3, 2(Tr X)^3 - 3(Tr X)(Tr X^2) + Tr X^3.
```

## Primary Anchors

- `references/primary-sources/levasseur-stafford-kernel-harish-chandra.txt:57-64`:
  Harish-Chandra homomorphism and Levasseur--Stafford surjectivity context.
- `references/primary-sources/levasseur-stafford-kernel-harish-chandra.txt:84-90`:
  Theorem 1.1 kernel statement \(J=\mathcal D(\mathfrak g)\tau(\mathfrak g)\).
- `references/primary-sources/levasseur-stafford-kernel-harish-chandra.txt:239-260`:
  discriminant/generic-locus passage and quotient context.
- `references/primary-sources/levasseur-stafford-kernel-harish-chandra.txt:492-500`:
  proof endpoint for Theorem 5.5.
- `references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.txt:27-38`:
  Harish-Chandra homomorphism, surjectivity, and kernel summary.
- `references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.txt:83-88`:
  diagonal adjoint case and the stronger kernel theorem.
- `references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.txt:151-156`:
  radial component map and kernel/image statement.
- `references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.txt:1194-1198`:
  radial component map by restriction plus Chevalley isomorphism.
- `references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.txt:1474-1480`:
  official bibliography entries for Levasseur--Stafford 1995 and 1996.

## Files Changed

- `appendix-radial-parts-moyal.tex`: added the pure-power/shear
  extension lemma and updated script evidence to \(N=2,3\).
- `scripts/check_moyal_coefficients.py`: generalized the direct radial
  harness from \(N=2\) to \(N=2,3\), added pure-power and \(z_2^3\)
  tests, and compared after multiplying by \(\Delta\).
- `references/primary-sources/radial-parts-capelli-source-anchors-2026-04-28.md`:
  recorded the wave-6 source failure and low-rank evidence.
- `references/source-provenance.md`: recorded the official AIF/NUMDAM
  source and the wave-6 computation.
- `references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.pdf`
  and `.txt`: official AIF/NUMDAM source copy and extracted text.
- `out/main.pdf` and `main.pdf`: regenerated by the session-end
  `make pdf` build.

## Commands Run

```bash
sed -n '1,240p' CLAUDE.md
test -f AGENTS.md && sed -n '1,240p' AGENTS.md || true
sed -n '1,220p' ~/ecosystem/INVARIANTS.md
sed -n '1,260p' ~/ecosystem/AGENTS-HARNESS.md
rg -n -e 'finite-n-reduced-moyal' -e 'radial' -e 'Moyal' ...
sed -n '1,260p' appendix-radial-parts-moyal.tex
sed -n '1,260p' scripts/check_moyal_coefficients.py
sed -n '4860,5060p' main.tex
python3 scripts/check_moyal_coefficients.py
curl -L --fail --silent --show-error https://aif.centre-mersenne.org/item/10.5802/aif.1736.pdf -o references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.pdf
pdftotext references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.pdf references/primary-sources/levasseur-stafford-symmetric-spaces-aif-1999.txt
python3 -m py_compile scripts/check_moyal_coefficients.py
python3 scripts/check_moyal_coefficients.py
make pdf
```

Web/source probes:

- AMS issue metadata for Levasseur--Stafford 1995, DOI
  `10.1090/S0894-0347-1995-1284849-8`.
- Official AIF/NUMDAM PDF for Levasseur--Stafford 1999, DOI
  `10.5802/aif.1736`.

## Proposed `main.tex` Edit

No `main.tex` edit was made.  The proof of
Theorem `thm:finite-n-reduced-moyal` still reports the older rank-two
script evidence.  A surgical update should replace the sentence saying
the script checks \(36\) rank-two comparisons by the current statement:
the script checks \(80\) direct comparisons for \(N=2\) and \(80\) for
\(N=3\), using
\(\Delta\,(J_N(f)F)|_{\mathfrak t}=S_N(f)(\Delta F|_{\mathfrak t})\).

## Remaining Open Questions

1. Find a primary all-\(N\) source, or write a self-contained proof, for
   the pure \(z_1,z_2\) images and Weyl-shear compatibility in the exact
   normalization above.
2. Decide whether Wallach 1993 or Levasseur--Stafford 1995 contains this
   statement in a form recoverable without extra convention choices.
3. Extend the direct test harness beyond \(N=3\) only if a new suspected
   failure mode appears; the next mathematical bottleneck is source or
   proof of the all-\(N\) shear compatibility, not more finite tests.
