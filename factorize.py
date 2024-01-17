from primes import primes

def factorize(states, size, num):
    f = open("./pi.txt","r")
    f.read(2)
    g = open("./e.txt","r")
    g.read(2)
    ps = f.read(size)
    es = g.read(size)[::-1]
    f.close()
    g.close()
    c = 0
    rnum = num[::-1]
    pos = 0
    count = 0
    primes_states = []
    count_states = []
    for x in states:
        if x == 0:
            x = 10
        c = c + x
        pp = ps[c]
        ee = es[c]
        print(pp)
        nn = rnum[pos]
        ss = ee + nn + pp
        if int(ss) in primes:
            c = c + 1
            count = count + 1
            count_states.append(count)
            count = 0
            pos = pos + 1
            primes_states.append(ss)
        else:
            count = count + 1
    print(primes_states)
    print(count_states)
