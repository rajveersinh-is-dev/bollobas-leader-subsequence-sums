import sys
sys.argv = sys.argv
exec(open('src/min_sums.py').read().split('if __name__')[0])

def find_example(n, L):
    elems = group_elements(n)
    best=None; example=None
    for combo in combinations_with_replacement(range(len(elems)), L):
        seq=[elems[i] for i in combo]
        if not zero_free(seq,n): continue
        s=subseq_sums(seq,n); k=len(s)
        if best is None or k<best:
            best=k; example=list(seq)
    return best, example

if __name__=='__main__':
    n=int(sys.argv[1]); t=int(sys.argv[2]); L=n-1+t
    best, ex = find_example(n, L)
    print(f"n={n} t={t} L={L} min={best} example={ex}")
