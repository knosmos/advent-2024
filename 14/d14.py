from aocd import data, submit
import sys
from collections import defaultdict, deque
import re
import cv2
import numpy as np

def main(s):
    s = s.split("\n")
    p = []
    for i in s:
        print(i)
        p.append(list(map(int, re.findall(r'(?:-)*\d+', i))))
    w = 101
    h = 103
    t = 100
    q = [0, 0, 0, 0]
    for i in p:
        i[0] = (i[0] + i[2]*t) % w
        i[1] = (i[1] + i[3]*t) % h
        # find quadrant
        if i[0] < w//2:
            if i[1] < h//2:
                q[0] += 1
            elif i[1] > h//2:
                q[1] += 1
        elif i[0] > w//2:
            if i[1] < h//2:
                q[2] += 1
            elif i[1] > h//2:
                q[3] += 1
    # print matrix
    for i in range(h):
        for j in range(w):
            if [j, i] in [x[:2] for x in p]:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print(q)
    return q[0]*q[3]*q[1]*q[2]

def main(s):
    s = s.split("\n")
    p = []
    for i in s:
        p.append(list(map(int, re.findall(r'(?:-)*\d+', i))))
    w = 101
    h = 103
    opt = float("inf")
    for t in range(10000):
        q = [0, 0, 0, 0]
        for i in p:
            i[0] = (i[0] + i[2]) % w
            i[1] = (i[1] + i[3]) % h
        # floodfill find largest region
        vis = set()
        max_reg = 0
        pos = set([tuple(x[:2]) for x in p])
        for st in pos:
            if st in vis:
                continue
            q = deque()
            q.append(st)
            vis.add(st)
            r_size = 1
            while q:
                cur = q.popleft()
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if (cur[0]+d[0],cur[1]+d[1]) not in vis:
                        if (cur[0]+d[0],cur[1]+d[1]) in pos:
                            q.append((cur[0]+d[0],cur[1]+d[1]))
                            vis.add((cur[0]+d[0],cur[1]+d[1]))
                            r_size += 1
            max_reg = max(max_reg, r_size)
        if max_reg > 100:
            print(t+1)
            mat = np.zeros((h,w,3), np.uint8)
            for i in p:
                mat[i[1],i[0]] = [255,255,255]
            cv2.imshow('image', mat)
            cv2.waitKey(0)

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d14.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))