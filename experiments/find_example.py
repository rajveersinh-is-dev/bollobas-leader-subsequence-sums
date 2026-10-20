'''Utility script to find an example sequence achieving the minimal number of distinct subsequence sums for given parameters n and t.

The script can be executed directly:
    python experiments/find_example.py <n> <t>
'''

from __future__ import annotations

import argparse
import sys
from itertools import combinations_with_replacement
from typing import List, Tuple, Optional

# Import core functions from the package
try:
    from src.min_sums import group_elements, zero_free, subseq_sums
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "Failed to import required functions from src.min_sums. "
        "Make sure the package layout is correct."
    ) from exc


def find_example(n: int, L: int) -> Tuple[Optional[int], Optional[List[Tuple[int, int]]]]:
    """
    Exhaustively search all multisets of ``L`` elements from ``Z_n × Z_n`` and
    return the smallest number of distinct subsequence sums together with an
    example achieving it.

    Parameters
    ----------
    n: int
        Modulus defining the group ``Z_n × Z_n``.
    L: int
        Length of the sequence to be examined.

    Returns
    -------
    best: Optional[int]
        Minimal number of distinct subsequence sums found, or ``None`` if no
        zero‑free sequence exists.
    example: Optional[List[Tuple[int, int]]]
        One sequence attaining ``best`` (as a list of group elements) or ``None``.
    """
    elems = group_elements(n)
    best: Optional[int] = None
    example: Optional[List[Tuple[int, int]]] = None

    # ``combinations_with_replacement`` yields each multiset exactly once.
    for combo in combinations_with_replacement(range(len(elems)), L):
        seq = [elems[i] for i in combo]

        if not zero_free(seq, n):
            continue

        sums = subseq_sums(seq, n)
        k = len(sums)

        if best is None or k < best:
            best = k
            example = list(seq)

            # Early exit: the theoretical lower bound is ``L + 1`` (empty
            # subsequence plus each element). When we hit that bound we cannot
            # improve further.
            if best == L + 1:
                break

    return best, example


def _parse_cli() -> Tuple[int, int]:
    parser = argparse.ArgumentParser(
        description="Find an example sequence with minimal distinct subsequence sums."
    )
    parser.add_argument(
        "n",
        type=int,
        help="Modulus defining the group Z_n × Z_n (positive integer).",
    )
    parser.add_argument(
        "t",
        type=int,
        help="Parameter t; the sequence length will be L = n - 1 + t.",
    )
    args = parser.parse_args()
    if args.n <= 0:
        parser.error("n must be a positive integer.")
    return args.n, args.t


def main() -> None:
    n, t = _parse_cli()
    L = n - 1 + t
    best, example = find_example(n, L)

    if best is None:
        print(f"No zero‑free sequence of length {L} exists for n={n}.", file=sys.stderr)
        sys.exit(1)

    print(f"n={n} t={t} L={L} min={best} example={example}")


if __name__ == "__main__":
    main()
