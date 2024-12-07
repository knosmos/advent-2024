from aocd import data, submit
import sys

def rfn(b, t, cur, i):
    if i == len(b):
        if cur == t:
            return True
        return False
    if cur > t:
        return False
    if rfn(b, t, cur+b[i], i+1): return True
    if rfn(b, t, cur*b[i], i+1): return True
    if rfn(b, t, int(str(cur)+str(b[i])), i+1): return True
    return False

def main2(s):
    s = s.split("\n")
    r = 0
    for l in s:
        a, b = l.split(":")
        b = list(map(int, b.split()))
        a = int(a)
        if rfn(b, a, b[0], 1):
            r += a
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d7.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))