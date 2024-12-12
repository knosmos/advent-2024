from aocd import data, submit
import sys

def main1(s):
    s = s.split()
    ds = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    r = 0
    for i in range(len(s)):
        for j in range(len(s[0])):
            for d in ds:
                for ind, char in enumerate("XMAS"):
                    y, x = i+d[0]*ind, j+d[1]*ind
                    if x<0 or x>=len(s[0]) or y<0 or y>=len(s) or s[y][x] != char:
                        break
                else:
                    r += 1
    return r

def main2(s):
    s = s.split()
    r = 0
    for i in range(1, len(s)-1):
        for j in range(1, len(s[0])-1):
            if s[i][j] == "A":
                if {s[i-1][j-1], s[i+1][j+1]} != {"M","S"}:
                    continue
                if {s[i+1][j-1], s[i-1][j+1]} != {"M","S"}:
                    continue
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