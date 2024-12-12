from aocd import data, submit
import sys
from collections import defaultdict, deque

def main(s):
    s = s.split("\n")
    reg = []
    vis = set()
    # floodfill
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (i,j) in vis:
                continue
            t = s[i][j]
            q = deque()
            q.append((i,j))
            vis.add((i,j))
            k = {(i,j)}
            while q:
                cur = q.popleft()
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= cur[0]+d[0] < len(s) and 0 <= cur[1]+d[1] < len(s[i]):
                        if (cur[0]+d[0],cur[1]+d[1]) not in vis:
                            if s[cur[0]+d[0]][cur[1]+d[1]] == t:
                                q.append((cur[0]+d[0],cur[1]+d[1]))
                                k.add((cur[0]+d[0],cur[1]+d[1]))
                                vis.add((cur[0]+d[0],cur[1]+d[1]))
            reg.append(k)
    print(reg)
    res = 0
    for r in reg:
        area = len(r)
        perimeter = len(r)*4
        for p in r:
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                if (p[0]+d[0],p[1]+d[1]) in r:
                    perimeter -= 1
        res += area*perimeter
        print(area, perimeter)
    return res

def main(s):
    s = s.split("\n")
    reg = []
    vis = set()
    # floodfill
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (i,j) in vis:
                continue
            t = s[i][j]
            q = deque()
            q.append((i,j))
            vis.add((i,j))
            k = {(i,j)}
            while q:
                cur = q.popleft()
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= cur[0]+d[0] < len(s) and 0 <= cur[1]+d[1] < len(s[i]):
                        if (cur[0]+d[0],cur[1]+d[1]) not in vis:
                            if s[cur[0]+d[0]][cur[1]+d[1]] == t:
                                q.append((cur[0]+d[0],cur[1]+d[1]))
                                k.add((cur[0]+d[0],cur[1]+d[1]))
                                vis.add((cur[0]+d[0],cur[1]+d[1]))
            reg.append(k)
    print(reg)
    res = 0
    for r in reg:
        area = len(r)
        # number of sides of region
        sides = 0
        for p in r:
            # count number of corners
            c = 0
            x, y = p
            # outer
            c += ((x+1,y) not in r and (x,y+1) not in r)
            c += ((x-1,y) not in r and (x,y+1) not in r)
            c += ((x-1,y) not in r and (x,y-1) not in r)
            c += ((x+1,y) not in r and (x,y-1) not in r)
            # inner
            c += ((x+1,y) in r and (x,y+1) in r and (x+1,y+1) not in r)
            c += ((x-1,y) in r and (x,y+1) in r and (x-1,y+1) not in r)
            c += ((x-1,y) in r and (x,y-1) in r and (x-1,y-1) not in r)
            c += ((x+1,y) in r and (x,y-1) in r and (x+1,y-1) not in r)
            sides += c
        print(area, sides)
        res += area*sides
    return res

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d12.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))