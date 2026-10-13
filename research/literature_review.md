# Literature review

## Source of the problem

- B. Bollobás and I. Leader, *work on subsequence sums in finite abelian groups*, quoted in the Open Problem Garden entry "Few subsequence sums in $\mathbb Z_n \times \mathbb Z_n$".
- The problem is also related to a theorem of J.E. Olson showing that every sequence of length $\ge 2n-1$ in $\mathbb Z_n^2$ contains a nonempty zero-sum subsequence.

## Known results recorded here

1. **Olsen's zero-sum theorem.** Every sequence of length at least $2n-1$ in $\mathbb Z_n^2$ contains a nonempty subsequence summing to $0$. Consequently, zero-free sequences in $\mathbb Z_n^2$ have length at most $2n-2$, which matches the range $t=0,\dots,n-1$ in the conjecture.
2. **One-dimensional analogue.** For $\mathbb Z_n$, the sequence consisting of $t$ copies of $1$ has the fewest distinct subsequence sums among all zero-free sequences of length $t$ in $\mathbb Z_n$; the count is $t$. This is proved by the standard partial-sums argument.
3. **Extremal construction.** The sequence with $n-1$ copies of $(1,0)$ and $t$ copies of $(0,1)$ is zero-free for $0\le t\le n-1$, because any nonempty selection has first coordinate in $[1,n-1]$ and second coordinate in $[0,t]\subseteq[0,n-1]$, so the residue is not $0$ unless both counts are $0$. Its distinct subsequence sums are all pairs $(a,b)$ with $0\le a\le n-1$, $0\le b\le t$ except $(0,0)$, numbering $n(t+1)-1$.
4. **Computational verification.** Exhaustive enumeration of all multisets (up to position order) of nonzero elements of $\mathbb Z_n^2$ confirms the conjectured minimum for:
   - $n=3$, $t=0,1,2$ (lengths $2,3,4$): minima $2,5,8$;
   - $n=4$, $t=0,1,2,3$: minima $3,7,11,15$;
   - $n=5$, $t=0,1,2$: minima $4,9,14$.

## Status classification

- **Apparently open.** No proof of the full conjecture is known to this project. The available literature in this snapshot establishes the one-dimensional case and Olsen's upper bound on length, but not the exact minimisation.

## What the gap is

The gap is the lower bound: there is no known proof that an arbitrary zero-free sequence in $\mathbb Z_n^2$ of length $n-1+t$ has at least $n(t+1)-1$ distinct nonempty subsequence sums. The existing theorem of Olsen only bounds the length of zero-free sequences, and the partial-sums argument of the one-dimensional case does not lift multiplicatively to two dimensions.
