from aocd import data, submit
from collections import defaultdict
import sys

def main1(s):
    s = s.split("\n")
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == "^":
                y,x = i,j
                break
    d = 0
    ds = [(-1,0),(0,1),(1,0),(0,-1)]
    pos = set()
    while True:
        pos.add((y,x))
        y2,x2 = y+ds[d][0], x+ds[d][1]
        if y2<0 or x2<0 or y2>=len(s) or x2>=len(s[0]):
            break
        if s[y2][x2] == "#":
            d = (d+1)%4
        else:
            y,x = y2,x2
        if y<0 or x<0 or y>=len(s) or x>=len(s[0]):
            break
    return len(pos)

def c(s,oy,ox):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == "^":
                y,x = i,j
                break
    d = 0
    ds = [(-1,0),(0,1),(1,0),(0,-1)]
    prev = set()
    while True:
        if (y,x,d) in prev:
            return True
        prev.add((y,x,d))
        y2,x2 = y+ds[d][0], x+ds[d][1]
        if y2<0 or x2<0 or y2>=len(s) or x2>=len(s[0]):
            return False
        if s[y2][x2] == "#" or (y2==oy and x2==ox):
            d = (d+1)%4
        else:
            y,x = y2,x2
        if y<0 or x<0 or y>=len(s) or x>=len(s[0]):
            return False

def main2(s):
    s = s.split("\n")
    r = 0
    for y in range(len(s)):
        for x in range(len(s[0])):
            r += c(s,y,x)
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d6.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))