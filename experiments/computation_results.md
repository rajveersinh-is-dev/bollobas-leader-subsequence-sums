# Computational verification

## Method

`src/min_sums.py` exhaustively enumerates multisets (position order irrelevant) of nonzero elements of $\mathbb Z_n^2$ of the specified size, discards those that are not zero-free, and records the minimum cardinality of the set of nonempty subsequence sums. Distinctness is taken in $\mathbb Z_n^2$.

## Results

| $n$ | $t$ | length $n-1+t$ | minimum found | conjectured $n(t+1)-1$ | agreement |
|---|---|---|---|---|---|
| 3 | 0 | 2 | 2 | 2 | yes |
| 3 | 1 | 3 | 5 | 5 | yes |
| 3 | 2 | 4 | 8 | 8 | yes |
| 4 | 0 | 3 | 3 | 3 | yes |
| 4 | 1 | 4 | 7 | 7 | yes |
| 4 | 2 | 5 | 11 | 11 | yes |
| 4 | 3 | 6 | 15 | 15 | yes |
| 5 | 0 | 4 | 4 | 4 | yes |
| 5 | 1 | 5 | 9 | 9 | yes |
| 5 | 2 | 6 | 14 | 14 | yes |

## Extremal examples (illustrative)

- $n=4$, $t=1$ (length $4$): three copies of $(0,1)$ and one copy of $(1,0)$ attains $7$ distinct sums.
- $n=4$, $t=3$ (length $6$): three copies of $(0,1)$ and three copies of $(1,0)$ attains $15$ distinct sums.

These are coordinate swaps of the conjectured extremals and attain the same counts, consistent with the symmetry of the problem between the two coordinates (there is no asymmetry in the bound).

## Limitations

The enumeration is exponential in $n$ and $t$; it establishes finite cases only and does not prove the general conjecture.
