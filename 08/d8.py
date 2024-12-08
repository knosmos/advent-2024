from aocd import data, submit
from collections import defaultdict
import sys

def main1(s):
    s = list(map(list, s.split("\n"))) 
    # find list of each type of antenna
    ant = defaultdict(list)
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != ".":
                ant[s[i][j]].append((i,j))
    loc = set()
    for t in ant:
        for i in range(len(ant[t])):
            for j in range(i):
                y1 = ant[t][i][0]
                y2 = ant[t][j][0] # because of the way ant is constructed
                                  # and how we are iterating, y2 <= y1
                x1 = ant[t][i][1]
                x2 = ant[t][j][1]
                # Case 1    ...#
                #           ..0.
                #           .0..
                #           #...
                if x2 > x1:
                    nx1, ny1 = x2 + (x2-x1), y2 - (y1-y2)
                    nx2, ny2 = x1 - (x2-x1), y1 + (y1-y2)
                # Case 2    #...
                #           .0..
                #           ..0.
                #           ...#
                else:
                    nx1, ny1 = x1 + (x1-x2), y1 + (y1-y2)
                    nx2, ny2 = x2 - (x1-x2), y2 - (y1-y2)
                # test for validity
                if nx1 >=0 and nx1 < len(s) and ny1 >= 0 and ny1 < len(s):
                    loc.add((ny1, nx1))
                if nx2 >=0 and nx2 < len(s) and ny2 >= 0 and ny2 < len(s):
                    loc.add((ny2, nx2))
    for i in loc:
        s[i[0]][i[1]] = "#"
    print("\n".join(["".join(j) for j in s]))
    return len(loc)

def main(s):
    s = list(map(list, s.split("\n")))
    ant = defaultdict(list)
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != ".":
                ant[s[i][j]].append((i,j))
    loc = set()
    for t in ant:
        for i in range(len(ant[t])):
            for j in range(i):
                y1 = ant[t][i][0]
                y2 = ant[t][j][0]
                x1 = ant[t][i][1]
                x2 = ant[t][j][1]
                for r in range(len(s)):
                    if x2 > x1:
                        nx1, ny1 = x2 + r*(x2-x1), y2 - r*(y1-y2)
                        nx2, ny2 = x1 - r*(x2-x1), y1 + r*(y1-y2)
                    else:
                        nx1, ny1 = x1 + r*(x1-x2), y1 + r*(y1-y2)
                        nx2, ny2 = x2 - r*(x1-x2), y2 - r*(y1-y2)
                    if nx1 >=0 and nx1 < len(s) and ny1 >= 0 and ny1 < len(s):
                        loc.add((ny1, nx1))
                    if nx2 >=0 and nx2 < len(s) and ny2 >= 0 and ny2 < len(s):
                        loc.add((ny2, nx2))
    for i in loc:
        s[i[0]][i[1]] = "#"
    print("\n".join(["".join(j) for j in s]))
    return len(loc)

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d8.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))