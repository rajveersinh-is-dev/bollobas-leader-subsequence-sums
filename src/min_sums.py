"""
Brute-force minimisation of the number of distinct nonempty subsequence sums
of a zero-free sequence in (Z_n)^2.

A "sequence" is treated as a multiset of elements of G = Z_n^2 \ {(0,0)},
with order irrelevant for the set of subsequence sums and for the zero-free
property.  We exhaust all multisets of size L from the nonzero group elements
and, for each, compute the set of all nonempty subset sums (positions
distinguished).  The number of distinct residues is recorded; the smallest
value over zero-free multisets is the minimum for that (n,L).

Usage:
    python src/min_sums.py n t       # prints min count for length n-1+t
"""
from __future__ import annotations

from itertools import combinations_with_replacement
import sys



def group_elements(n):
    """Group elements.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return [(a, b) for a in range(n) for b in range(n) if not (a == 0 and b == 0)]


def subseq_sums(seq, n):
    # set of residues of nonempty subset sums (positions distinguished)
    """Subseq sums.
    
    Args:
        seq (list):
        n:
    
    Returns:
        The computed result
    
    """
    sums = set()
    # iterate over all subsets of positions via bitmask
    L = len(seq)
    for mask in range(1, 1 << L):
        a = 0
        b = 0
        for i in range(L):
            if mask & (1 << i):
                x, y = seq[i]
                a = (a + x) % n
                b = (b + y) % n
        sums.add((a, b))
    return sums


def zero_free(seq, n) -> bool:
    # no nonempty subsequence (subset of positions) sums to (0,0)
    """Zero free.
    
    Args:
        seq (list):
        n:
    
    Returns:
        bool: Result of type bool
    
    """
    L = len(seq)
    for mask in range(1, 1 << L):
        a = 0
        b = 0
        for i in range(L):
            if mask & (1 << i):
                x, y = seq[i]
                a = (a + x) % n
                b = (b + y) % n
        if a == 0 and b == 0:
            return False
    return True


def min_count(n, L) -> tuple:
    """Min count.
    
    Args:
        n:
        L:
    
    Returns:
        tuple: Result of type tuple
    
    """
    elems = group_elements(n)
    best = None
    count = 0
    # multisets of size L from elems (non-decreasing indices)
    for combo in combinations_with_replacement(range(len(elems)), L):
        seq = [elems[i] for i in combo]
        if not zero_free(seq, n):
            continue
        s = subseq_sums(seq, n)
        k = len(s)
        if best is None or k < best:
            best = k
        count += 1
    return best, count


if __name__ == "__main__":
    n = int(sys.argv[1])
    t = int(sys.argv[2])
    L = n - 1 + t
    best, c = min_count(n, L)
    conj = n * (t + 1) - 1
    print(f"n={n} t={t} L={L} min_count={best} conjectured={conj} combos_checked={c}")
