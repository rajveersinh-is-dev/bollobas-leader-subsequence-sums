# Known results and conventions

## Notation

- $G_n = (\mathbb{Z}/n\mathbb{Z})^2$.
- A sequence $\mathbf a=(a_1,\dots,a_\ell)$ over $G_n$ is *zero-free* if $0$ is not a nonempty subsequence sum.
- For a sequence $\mathbf a$, let $\Sigma^\circ(\mathbf a)$ be the set of nonempty subsequence sums. The conjecture asserts $|\Sigma^\circ(\mathbf a)| \ge n(t+1)-1$ when $\ell=n-1+t$ and $\mathbf a$ is zero-free.

## Established here as PROVED

**Lemma (partial sums, $t=0$ base).** Let $\mathbf a=(a_1,\dots,a_{n-1})$ be zero-free in $G_n$. Define $S_0=0$ and $S_i=a_1+\cdots+a_i$ for $1\le i\le n-1$. Then $S_0,\dots,S_{n-1}$ are distinct. Hence $\{S_1,\dots,S_{n-1}\}\subseteq \Sigma^\circ(\mathbf a)$ has size $n-1$.

*Proof.* If $S_i=S_j$ with $0\le i<j\le n-1$, then $a_{i+1}+\cdots+a_j=0$, a nonempty subsequence summing to $0$, contradicting zero-freeness. Therefore the $n$ partial sums are distinct. Removing $S_0=0$ gives $n-1$ distinct nonzero subsequence sums. This is the case $t=0$ of the conjecture. $\square$

## Established in prior work

- Olsen's theorem (length bound $2n-2$ for zero-free sequences).
- One-dimensional analogue.

## Computationally verified

See `experiments/computation_results.md` and `src/min_sums.py`.

## Evidence categories

- The Lemma above is **PROVED HERE**.
- Olsen's bound and the one-dimensional analogue are **ESTABLISHED IN PRIOR WORK**.
- Small-case minima are **COMPUTATIONALLY VERIFIED**.
- The general conjecture is **CONJECTURED/OPEN**; it is not proved here.
