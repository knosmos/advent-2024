from aocd import data, submit
import sys
from collections import defaultdict, deque

def main(s):
    s = s.split("\n")
    w = 70
    grid = [[0] * (w+1) for i in range(w+1)]
    for i, l in enumerate(s[:1024]):
        a, b = map(int, l.split(","))
        grid[a][b] = 1
    q = deque()
    q.append((0,0,0))
    while q:
        cur = q.popleft()
        if cur[0] == w and cur[1] == w:
            return cur[2]
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= cur[0]+d[0] <= w and 0 <= cur[1]+d[1] <= w:
                k = grid[cur[0]+d[0]][cur[1]+d[1]]
                if k == 0:
                    q.append((cur[0]+d[0],cur[1]+d[1],cur[2]+1))
                    grid[cur[0]+d[0]][cur[1]+d[1]] = 2

def main(s):
    s = s.split("\n")
    w = 70
    grid = [[0] * (w+1) for i in range(w+1)]
    for i, l in enumerate(s):
        a, b = map(int, l.split(","))
        grid[a][b] = 1
        q = deque()
        q.append((0,0,0))
        vis = set((0,0))
        viable = False
        while q:
            cur = q.popleft()
            if cur[0] == w and cur[1] == w:
                viable = True
                break
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                x, y = cur[0]+d[0], cur[1]+d[1]
                if 0 <= x <= w and 0 <= y <= w:
                    if grid[x][y]==0 and (x,y) not in vis:
                        q.append((x, y, cur[2]+1))
                        vis.add((x, y))
        if not viable:
            return a,b

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d18.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))