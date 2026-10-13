# Proof attempts

## Attempt 1: Partial sums ($t=0$)

Succeeded. See Lemma in `research/known_results.md`. Gives the conjectured lower bound $n-1$ for $t=0$.

## Attempt 2: Induction by appending one element

Idea: If $S$ is zero-free of length $n-1+t$ and $\mathbf a = S \cup \{x\}$, then the number of distinct subsequence sums grows by at least $n$:
$$
|\Sigma^\circ(\mathbf a)| \ge |\Sigma^\circ(S)| + n.
$$
If true, iterating from $t=0$ would prove the conjecture. However, no proof of this stronger growth statement was found. The obstacle is that the shifted set $x+\Sigma^\circ(S)\cup\{0\}$ may intersect the original set, and zero-freeness only rules out $0\in x+\Sigma^\circ(S)\cup\{0\}$ (i.e. $-x\notin \Sigma^\circ(S)\cup\{0\}$), not further collisions. A collision $y=x+z$ does not necessarily create a zero-sum: it would mean a subsequence summing to $y$ and another (of disjoint? not necessarily disjoint) summing to $z$ with difference $x$; the corresponding difference of selected terms need not be a subsequence, because common terms may not cancel in subset-sum notation. This is the central difficulty.

## Attempt 3: Exhaustive verification for small cases

Succeeded for $n\le 5$ as recorded. This does not prove the universal statement.

## Current status

The full Bollobás–Leader conjecture remains unresolved by this project. The only proved result is the $t=0$ lemma. The remaining obstacle is controlling collisions when adding elements in the induction.
