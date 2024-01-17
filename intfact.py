import sys
from definition import define
from factorize import factorize

if __name__ == "__main__":
    num = str(sys.argv[1])
    states, size = define(num)
    print(states, size)
    factor = factorize(states, size, num)
