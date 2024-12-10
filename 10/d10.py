from aocd import data, submit
import sys
from collections import defaultdict, deque

def main(s):
    s = [list(map(int, list(x))) for x in s.split("\n")]
    r = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                rs = 0
                q = deque()
                vis = set()
                # bfs
                q.append((i,j,s[i][j]))
                vis.add((i,j))
                while q:
                    cur = q.popleft()
                    for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                        if 0 <= cur[0]+d[0] < len(s) and 0 <= cur[1]+d[1] < len(s[i]):
                            if (cur[0]+d[0],cur[1]+d[1]) not in vis: # disable this line for pt2
                                k = s[cur[0]+d[0]][cur[1]+d[1]]
                                if k == cur[2]+1:
                                    if k == 9:
                                        r += 1
                                        vis.add((cur[0]+d[0],cur[1]+d[1]))
                                    else:
                                        q.append((cur[0]+d[0],cur[1]+d[1],cur[2]+1))
                                        vis.add((cur[0]+d[0],cur[1]+d[1]))
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d10.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))