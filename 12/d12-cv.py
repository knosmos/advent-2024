import cv2
import sys
import numpy as np
from aocd import data, submit
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
    # create an image
    for r in reg:
        img = np.zeros((len(s),len(s[0])), np.uint8)
        for p in r:
            img[p[0],p[1]] = 255
        cv2.sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        cv2.imshow('image', img)
        cv2.waitKey(0)

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d12.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))