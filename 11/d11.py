from aocd import data, submit
import sys
from collections import defaultdict, deque

def main(s):
    s = list(map(int, s.split()))
    s = {x:s.count(x) for x in set(s)}
    for i in range(75): # 25 for p1, 75 for p2
        ns = defaultdict(int)
        for j in s:
            if j == 0:
                ns[1] += s[j]
            elif len(str(j)) % 2 == 0:
                ns[int(str(j)[:len(str(j))//2])] += s[j]
                ns[int(str(j)[len(str(j))//2:])] += s[j]
            else:
                ns[j*2024] += s[j]
        s = ns
    return sum(s.values())

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d11.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))