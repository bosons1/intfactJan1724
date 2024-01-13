import sys
from mpmath import mp
from mpmath import zetazero
from primes import primes

PREC=1024
def get_zero(i):
    global PREC
    mp.prec = PREC
    mp.dps = PREC
    zero = str(zetazero(i).imag)
    idx = zero.index(".")
    zero = zero[idx + 1:]
    return zero

if __name__ == "__main__":
    num = str(sys.argv[1])
    c = 0
    l = len(num)
    nn = num[c % l]
    zero_index = 1
    zero = get_zero(zero_index)
    pos = 0
    f = open("./pi.txt","r")
    f.read(2)
    g = open("./e.txt","r")
    g.read(2)
    count = 0
    while True:
        pp = f.read(1)
        nn = num[c % l]
        c = c + 1
        ee = g.read(1)
        ss = pp + nn + ee
        zz = zero[pos]
        pos = pos + 1
        if int(ss) in primes:
            print(ss, zz)
        if int(ss) in primes and zz == '0':
            input([ss, zz])
            zero_index = zero_index + 1
            zero = get_zero(zero_index)
            pos = 0
    f.close()
    g.close()
