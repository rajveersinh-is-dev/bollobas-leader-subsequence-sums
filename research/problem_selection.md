# Problem selection

## Selected problem

**The Bollobás–Leader conjecture on few subsequence sums in $(\mathbb{Z}_n)^2$.**

Let $\mathbb{Z}_n^2$ denote $(\mathbb{Z}/n\mathbb{Z})^2$. A sequence $\mathbf a=(a_1,\dots,a_\ell)$ of elements of $\mathbb{Z}_n^2$ is *zero-free* if no nonempty subsequence of $\mathbf a$ sums to $0\in\mathbb{Z}_n^2$.

For a sequence $\mathbf a$, a *subsequence sum* is any group element obtainable as the sum of a nonempty subsequence of $\mathbf a$ (terms chosen by position, with multiplicity from the sequence).

**Conjecture (Bollobás–Leader).** For every $0\le t\le n-1$, the zero-free sequence in $\mathbb{Z}_n^2$ of length $n-1+t$ consisting of $n-1$ copies of $(1,0)$ and $t$ copies of $(0,1)$ has the fewest distinct subsequence sums among all zero-free sequences in $\mathbb{Z}_n^2$ of length $n-1+t$.

Its number of distinct subsequence sums is $n(t+1)-1$.

Equivalently, every zero-free sequence of length $n-1+t$ in $\mathbb{Z}_n^2$ has at least $n(t+1)-1$ distinct nonempty subsequence sums.

## Why this problem was selected

1. **Genuinely open.** The conjecture is listed as open in the Open Problem Garden and is implicit in work of Olsen and Bollobás–Leader.
2. **Insight-oriented.** The decisive issue is a combinatorial lower bound, not a massive search. Small cases can be verified by exact computation, but the claim is universal.
3. **Precise and testable.** The extremal construction and the predicted count $n(t+1)-1$ are explicit.
4. **Tractable partial progress.** The case $t=0$ is immediate, and small cases can be verified exhaustively for $n\le 5$.

## Selection scores (subjective)

- Mathematical depth: high.
- Plausible route: moderate.
- Independence from large computation: high (small computation used only for verification).
- Precision: high.
- Existing frontier quality: good (Olsen's theorem provides an upper bound $2n-1$ on zero-free length).
