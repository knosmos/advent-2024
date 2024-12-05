from aocd import data, submit
from collections import defaultdict
from itertools import permutations
import sys

def main1(s):
    a, b = s.split("\n\n")
    rules = [list(map(int, i.split("|"))) for i in a.split()]
    b = [list(map(int, i.split(","))) for i in b.split()]
    print(b)
    r = 0
    for x in b:
        for rule in rules:
            try:
                i,j = x.index(rule[0]), x.index(rule[1])
                if j<i:
                    break
            except:
                pass
        else:
            r += int(x[len(x)//2])
            print(x)
    return r

def main2(s):
    a, b = s.split("\n\n")
    rules = [list(map(int, i.split("|"))) for i in a.split()]
    b = [list(map(int, i.split(","))) for i in b.split()]
    r = 0
    for x in b:
        good = False
        for rule in rules:
            try:
                i,j = x.index(rule[0]), x.index(rule[1])
                if j<i:
                    break
            except:
                pass
        else:
            continue
        adj = defaultdict(list)
        deg = defaultdict(int)
        for rule in rules:
            if rule[0] in x and rule[1] in x:
                adj[rule[0]].append(rule[1])
                deg[rule[1]] += 1
        L = []
        S = []
        for i in x:
            if deg[i] == 0:
                S.append(i)
        while S:
            p = S.pop()
            L.append(p)
            for i in adj[p]:
                deg[i] -= 1
                if deg[i] == 0:
                    S.append(i)
        r += L[len(L)//2]
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d5.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))