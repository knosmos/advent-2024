from aocd import data, submit
import sys
from collections import defaultdict, deque
import re
from numpy.linalg import solve

def main(s):
    s = s.split("\n\n")
    r = 0
    for block in s:
        a,b,c = block.split("\n")
        # Button A: X+94, Y+34
        a1, a2 = map(int, re.findall(r'Button A: X\+(\d+), Y\+(\d+)', a)[0])
        b1, b2 = map(int, re.findall(r'Button B: X\+(\d+), Y\+(\d+)', b)[0])
        c1, c2 = map(int, re.findall(r'Prize: X=(\d+), Y=(\d+)', c)[0])

        print(a1,a2,b1,b2,c1,c2)
        for i in range(100):
            for j in range(100):
                if i*a1 + j*b1 == c1 and i*a2 + j*b2 == c2:
                    print(i,j)
                    r += i*3 + j
                    break
    return r

def main(s):
    s = s.split("\n\n")
    r = 0
    for block in s:
        a,b,c = block.split("\n")

        a1, a2 = map(int, re.findall(r'Button A: X\+(\d+), Y\+(\d+)', a)[0])
        b1, b2 = map(int, re.findall(r'Button B: X\+(\d+), Y\+(\d+)', b)[0])
        c1, c2 = map(int, re.findall(r'Prize: X=(\d+), Y=(\d+)', c)[0])

        c1 += 10000000000000 # comment out for p1
        c2 += 10000000000000

        x = solve([[a1,b1],[a2,b2]],[c1,c2])
        i, j = map(round, x)
        if a1*i + b1*j == c1 and a2*i + b2*j == c2:
            r += i*3 + j
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d13.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))