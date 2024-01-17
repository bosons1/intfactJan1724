import sys
from primes import primes

def define(num):
    f = open("./pi.txt","r")
    f.read(2)
    g = open("./e.txt","r")
    g.read(2)
    l = len(num)
    probable_next_states = []
    probable_next_indices = []
    length_increment = []
    num2 = num + num
    l2 = len(num2)
    c = 0
    last_prime_index = -1 
    n1 = ""
    n2 = ""
    if l2 - c > 2:
        n1 = num2[c:(c+3)]
    if l2 - c > 1:
        n2 = num2[c:(c+2)]
    if l2 - c > 0:
        n3 = num2[c:(c+1)]
        if int(n3) == 0:
            n3 = 10
    if n1 != "" and (last_prime_index + int(n1) + 1 < 167 or last_prime_index - int(n1) - 1 >= 0):
        if last_prime_index + int(n1) + 1< 167:
            probable_next_states.append(primes[last_prime_index+int(n1) + 1])
            probable_next_indices.append(last_prime_index + int(n1)+ 1)
            length_increment.append(3)
        if last_prime_index - int(n1) - 1 >= 0:
            probable_next_states.append(primes[last_prime_index-int(n1)-1])
            probable_next_indices.append(last_prime_index - int(n1)-1)
            length_increment.append(3)
    if n2 != "" and (last_prime_index + int(n2) + 1 < 167 or last_prime_index - int(n2) - 1 >= 0):
        if last_prime_index + int(n2) + 1 < 167:
            probable_next_states.append(primes[last_prime_index + int(n2) + 1])
            probable_next_indices.append(last_prime_index + int(n2)+ 1)
            length_increment.append(2)
        if last_prime_index - int(n2) - 1 >= 0:
            probable_next_states.append(primes[last_prime_index - int(n2) - 1])
            probable_next_indices.append(last_prime_index - int(n2) - 1)
            length_increment.append(2)
    if last_prime_index + int(n3) + 1 < 167 or last_prime_index - int(n3) - 1 >= 0:
        if last_prime_index + int(n3) + 1 < 167:
            probable_next_states.append(primes[last_prime_index+int(n3) + 1])
            probable_next_indices.append(last_prime_index + int(n3) + 1)
            length_increment.append(1)
        if last_prime_index - int(n3) >= 0:
            probable_next_states.append(primes[last_prime_index-int(n3) - 1])
            probable_next_indices.append(last_prime_index - int(n3) - 1)
            length_increment.append(1)
    pos = 0
    states = []
    while c < l2:
        pp = f.read(1)
        ee = g.read(1)
        pos = pos + 1
        for x in range(0, 10):
            ss = pp + str(x) + ee
            if int(ss) in primes and int(ss) in probable_next_states:
                states.append(x)
                idx = probable_next_states.index(int(ss))
                last_prime_index = probable_next_indices[idx]
                c = c + length_increment[idx]
                if c == l2 - 1:
                    break
                probable_next_indices = []
                probable_next_states = []
                length_increment = []
                n1 = ""
                n2 = ""
                n3 = ""
                if l2 - c > 2:
                    n1 = num2[c:(c+3)]
                if l2 - c > 1:
                    n2 = num2[c:(c+2)]
                if l2 - c > 0:
                    n3 = num2[c:(c+1)]
                    if int(n3) == 0:
                        n3 = 10
                else:
                    break
                if n1 != "" and (last_prime_index + int(n1) + 1 < 167 or last_prime_index - int(n1) - 1 >= 0):
                    if last_prime_index + int(n1) + 1 < 167:
                        probable_next_states.append(primes[last_prime_index+int(n1) + 1])
                        probable_next_indices.append(last_prime_index + int(n1) + 1)
                        length_increment.append(3)
                    if last_prime_index - int(n1) - 1 >= 0:
                        probable_next_states.append(primes[last_prime_index-int(n1) - 1])
                        probable_next_indices.append(last_prime_index - int(n1) - 1)
                        length_increment.append(3)
                if n2 != "" and (last_prime_index + int(n2) + 1 < 167 or last_prime_index - int(n2) - 1 >= 0):
                    if last_prime_index + int(n2) + 1 < 167:
                        probable_next_states.append(primes[last_prime_index + int(n2) + 1])
                        probable_next_indices.append(last_prime_index + int(n2) + 1)
                        length_increment.append(2)
                    if last_prime_index - int(n2) - 1 >= 0:
                        probable_next_states.append(primes[last_prime_index - int(n2) - 1])
                        probable_next_indices.append(last_prime_index - int(n2) - 1) 
                        length_increment.append(2)
                if n3 != "" and (last_prime_index + int(n3) + 1 < 167 or last_prime_index - int(n3) - 1 >= 0):
                    if last_prime_index + int(n3) + 1 < 167:
                        probable_next_states.append(primes[last_prime_index+int(n3) + 1])
                        probable_next_indices.append(last_prime_index + int(n3) + 1)
                        length_increment.append(1)
                    if last_prime_index - int(n3) - 1 >= 0:
                        probable_next_states.append(primes[last_prime_index-int(n3) - 1])
                        probable_next_indices.append(last_prime_index - int(n3) - 1)
                        length_increment.append(1)
    return states, pos
    
if __name__ == "__main__":
    num = str(sys.argv[1])
    states, size = define(num)
    print(states, size)
    #factor = factorize(states, size, num)
