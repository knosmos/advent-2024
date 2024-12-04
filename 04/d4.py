from aocd import data, submit
import sys
from collections import defaultdict

def main1(s):
    s = s.split("\n")
    q = []
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == "X":
                q.append([i,j])
    r = 0
    q2 = []
    for i in q:
        for a in [-1,0,1]:
            for b in [-1,0,1]:
                if i[0]+a < len(s) and i[0]+a >= 0 and i[1]+b < len(s[0]) and i[1]+b >= 0:
                    if s[i[0]+a][i[1]+b] == "M":
                        q2.append([i[0]+a, i[1]+b, a, b, 2])
    while q2:
        a = q2.pop()
        if a[4] == 4:
            r += 1
            continue
        if a[0]+a[2] >= 0 and a[0]+a[2] < len(s) and a[1]+a[3] >= 0 and a[1]+a[3] < len(s):
            if s[a[0]+a[2]][a[1]+a[3]] == "XMAS"[a[4]]:
                q2.append([a[0]+a[2], a[1]+a[3], a[2], a[3], a[4]+1])
    return r

def main2(s):
    s = s.split()
    r = 0
    for i in range(1, len(s)-1):
        for j in range(1, len(s[0])-1):
            if s[i][j] == "A":
                # /
                f = 0
                if s[i-1][j-1] == "M" and s[i+1][j+1] == "S":
                    f += 1
                if s[i-1][j-1] == "S" and s[i+1][j+1] == "M":
                    f += 1
                # \
                if s[i+1][j-1] == "M" and s[i-1][j+1] == "S":
                    f += 1
                if s[i+1][j-1] == "S" and s[i-1][j+1] == "M":
                    f += 1
                if f == 2:
                    r += 1
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d4.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))