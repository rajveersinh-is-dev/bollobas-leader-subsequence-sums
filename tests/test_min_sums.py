import subprocess, sys

def run(n, t):
    out = subprocess.check_output([sys.executable, "src/min_sums.py", str(n), str(t)], text=True)
    # parse "min_count=K"
    for tok in out.split():
        if tok.startswith("min_count="):
            return int(tok.split("=",1)[1])
    raise RuntimeError(out)

def test_n3():
    assert run(3,0)==2
    assert run(3,1)==5
    assert run(3,2)==8

def test_n4():
    assert run(4,0)==3
    assert run(4,1)==7
    assert run(4,2)==11
    assert run(4,3)==15
