# Mathematics

## Definitions

Let $n\ge 2$ be an integer and let $G_n=(\mathbb Z/n\mathbb Z)^2$.

**Definition (zero-free sequence).** A sequence $\mathbf a=(a_1,\dots,a_\ell)$ of elements of $G_n$ is *zero-free* if no nonempty subsequence $(a_{i_1},\dots,a_{i_r})$ (term positions distinct) has sum $a_{i_1}+\cdots+a_{i_r}=0$ in $G_n$.

**Definition (subsequence sum).** A *subsequence sum* of $\mathbf a$ is any element of $G_n$ of the form $a_{i_1}+\cdots+a_{i_r}$ with $1\le r\le \ell$ and $1\le i_1<\cdots<i_r\le \ell$.

## Main targets

**Target A (full).** For every $n\ge2$ and $0\le t\le n-1$, every zero-free sequence of length $n-1+t$ in $G_n$ has at least $n(t+1)-1$ distinct nonempty subsequence sums.

**Target B.** Prove the stated lower bound for all $t$ with a clean induction. (Blocked; see `research/proof_attempts.md`.)

**Target C (proved here).** The case $t=0$ of Target A.

## Theorem proved here

**Theorem.** If $\mathbf a$ is a zero-free sequence of length $n-1$ in $G_n$, then $\mathbf a$ has at least $n-1$ distinct nonempty subsequence sums.

*Proof.* See Lemma in `research/known_results.md`: the $n$ partial sums $S_0=0,S_1,\dots,S_{n-1}$ are distinct by zero-freeness, hence $S_1,\dots,S_{n-1}$ give $n-1$ distinct nonempty subsequence sums. $\square$

Status: **PROVED HERE**. Scope: $t=0$ only. The full conjecture remains open.
