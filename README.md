# Few Subsequence Sums in $\mathbb Z_n \times \mathbb Z_n$

**Problem.** Bollobás–Leader conjecture: for $0\le t\le n-1$, the zero-free sequence in $(\mathbb Z/n\mathbb Z)^2$ of length $n-1+t$ with $n-1$ copies of $(1,0)$ and $t$ copies of $(0,1)$ has the *fewest* distinct nonempty subsequence sums among all zero-free sequences of that length; equivalently, every such sequence has at least $n(t+1)-1$ distinct nonempty subsequence sums.

**What is proved here.** A rigorous proof of the case $t=0$: every zero-free sequence of length $n-1$ in $(\mathbb Z/n\mathbb Z)^2$ has at least $n-1$ distinct nonempty subsequence sums. The general conjecture is *not* proved here; it remains open. The remaining obstruction is identified in `research/proof_attempts.md`.

**Computational support.** Exhaustive enumeration verifies the conjectured minimum for $n=3$ (all $t$), $n=4$ (all $t$), and $n=5$ ($t=0,1,2$). See `experiments/computation_results.md`.

## Exact statement

Let $G_n=(\mathbb Z/n\mathbb Z)^2$. A sequence is *zero-free* if no nonempty subsequence sums to $0$. For $0\le t\le n-1$ and any zero-free sequence of length $n-1+t$, conjecture:
\[
|\{\text{nonempty subsequence sums}\}|\ge n(t+1)-1.
\]

## Repository layout

- `research/` — problem selection, literature, known results, proof attempts, log.
- `mathematics/` — definitions and main results.
- `experiments/` — brute-force enumeration and results.
- `src/` — verification code.
- `tests/` — unit tests for the verification code.
- `paper/` — LaTeX paper/report.

## Reproducibility

Run the verifier:
```bash
python src/min_sums.py n t   # e.g. python src/min_sums.py 4 2
```
Run tests:
```bash
python -m pytest tests/
```

## Limitations

Only the $t=0$ case is proved. No claim is made that the full conjecture is resolved.

## License

MIT.
