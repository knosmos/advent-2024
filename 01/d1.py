from aocd import data, submit
import sys
from collections import defaultdict

def main(s):
    s = list(map(lambda i:list(map(int, i.split())), s.split("\n")))
    a = [i[0] for i in s]
    b = [i[1] for i in s]
    a.sort()
    b.sort()
    return sum([abs(a[i]-b[i]) for i in range(len(a))])

def main(s):
    s = list(map(lambda i:list(map(int, i.split())), s.split("\n")))
    a = [i[0] for i in s]
    b = [i[1] for i in s]
    m = defaultdict(int)
    for i in b:
        m[i] += 1
    return sum([i*m[i] for i in a])


if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d1.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))