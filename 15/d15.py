from aocd import data, submit
import sys
from rich import print
from collections import defaultdict, deque

def main(s):
    m, d = s.split("\n\n")
    d = d.replace("\n","")
    m = list(map(list, m.split("\n")))
    # find @
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '@':
                pos = (i,j)
    # simulate
    for i in d:
        m[pos[0]][pos[1]] = "."
        if i == "^":
            # move any boxes in the way
            if m[pos[0]-1][pos[1]] == "#":
                continue
            x = 0
            fail = False
            while m[pos[0]-x-1][pos[1]] == "O":
                if m[pos[0]-x-2][pos[1]] == "#":
                    fail = True
                x += 1
            if fail:
                continue
            # move
            m[pos[0]-1][pos[1]] = "."
            m[pos[0]-x-1][pos[1]] = "O"
            pos = (pos[0]-1,pos[1])
        elif i == "v":
            # move any boxes in the way
            if m[pos[0]+1][pos[1]] == "#":
                continue
            x = 0
            fail = False
            while m[pos[0]+x+1][pos[1]] == "O":
                if m[pos[0]+x+2][pos[1]] == "#":
                    fail = True
                x += 1
            if fail:
                continue
            # move
            m[pos[0]+1][pos[1]] = "."
            m[pos[0]+x+1][pos[1]] = "O"
            pos = (pos[0]+1,pos[1])
        elif i == ">":
            # move any boxes in the way
            if m[pos[0]][pos[1]+1] == "#":
                continue
            x = 0
            fail = False
            while m[pos[0]][pos[1]+x+1] == "O":
                if m[pos[0]][pos[1]+x+2] == "#":
                    fail = True
                x += 1
            if fail:
                continue
            # move
            m[pos[0]][pos[1]+1] = "."
            m[pos[0]][pos[1]+x+1] = "O"
            pos = (pos[0],pos[1]+1)
        elif i == "<":
            # move any boxes in the way
            if m[pos[0]][pos[1]-1] == "#":
                continue
            x = 0
            fail = False
            while m[pos[0]][pos[1]-x-1] == "O":
                if m[pos[0]][pos[1]-x-2] == "#":
                    fail = True
                x += 1
            if fail:
                continue
            # move
            m[pos[0]][pos[1]-1] = "."
            m[pos[0]][pos[1]-x-1] = "O"
            pos = (pos[0],pos[1]-1)
        m[pos[0]][pos[1]] = "@"
        # print matrix
        #for i in m:
        #    print("".join(i))
        #print()
    r = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "O":
                r += 100 * i + j
    return r 

def main(s):
    m, d = s.split("\n\n")
    d = d.replace("\n","")
    m = m.replace("#","##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    m = list(map(list, m.split("\n")))
    # find @
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '@':
                pos = (i,j)
    # simulate
    for i in d:
        m[pos[0]][pos[1]] = "."
        if i == "^":
            # move any boxes in the way
            if m[pos[0]-1][pos[1]] == "#":
                continue
            fail = False
            q = deque([(pos[0]-1,pos[1])])
            moved = []
            while q:
                a, b = q.popleft()
                if m[a][b] == "[":
                    if m[a-1][b] == "]":
                        q.append((a-1,b-1))
                    if m[a-1][b] == "[":
                        q.append((a-1,b))
                    if m[a-1][b] == "#" or m[a-1][b+1] == "#":
                        fail = True
                    if m[a-1][b+1] == "[":
                        q.append((a-1,b+1))
                    moved.append((a,b))
                if m[a][b] == "]":
                    if m[a-1][b] == "]":
                        q.append((a-1,b-1))
                    if m[a-1][b] == "[":
                        q.append((a-1,b))
                    if m[a-1][b] == "#" or m[a-1][b-1] == "#":
                        fail = True
                    if m[a-1][b-1] == "]":
                        q.append((a-1,b-1))
                    moved.append((a,b-1))
            if fail:
                continue
            for a, b in moved:
                m[a][b] = "."
                m[a][b+1] = "."
            for a, b in moved:
                m[a-1][b] = "["
                m[a-1][b+1] = "]"
            pos = (pos[0]-1,pos[1])
        elif i == "v":
            # move any boxes in the way
            if m[pos[0]+1][pos[1]] == "#":
                continue
            fail = False
            q = deque([(pos[0]+1,pos[1])])
            moved = []
            while q:
                a, b = q.popleft()
                if m[a][b] == "[":
                    if m[a+1][b] == "]":
                        q.append((a+1,b-1))
                    if m[a+1][b] == "[":
                        q.append((a+1,b))
                    if m[a+1][b] == "#" or m[a+1][b+1] == "#":
                        fail = True
                    if m[a+1][b+1] == "[":
                        q.append((a+1,b+1))
                    moved.append((a,b))
                if m[a][b] == "]":
                    if m[a+1][b] == "]":
                        q.append((a+1,b-1))
                    if m[a+1][b] == "[":
                        q.append((a+1,b))
                    if m[a+1][b] == "#" or m[a+1][b-1] == "#":
                        fail = True
                    if m[a+1][b-1] == "]":
                        q.append((a+1,b-1))
                    moved.append((a,b-1))
            if fail:
                continue
            for a, b in moved:
                m[a][b] = "."
                m[a][b+1] = "."
            for a, b in moved:
                m[a+1][b] = "["
                m[a+1][b+1] = "]"
            pos = (pos[0]+1,pos[1])
        elif i == ">":
            # move any boxes in the way
            if m[pos[0]][pos[1]+1] == "#":
                continue
            x = 0
            fail = False
            while m[pos[0]][pos[1]+x+1] in "[]":
                if m[pos[0]][pos[1]+x+2] == "#":
                    fail = True
                x += 1
            if fail:
                continue
            # move
            m[pos[0]][pos[1]+1] = "."
            for i in range(0,x+1):
                m[pos[0]][pos[1]+i+1] = "]["[i%2]
            pos = (pos[0],pos[1]+1)
        elif i == "<":
            # move any boxes in the way
            if m[pos[0]][pos[1]-1] == "#":
                continue
            x = 0
            fail = False
            while m[pos[0]][pos[1]-x-1] in "[]":
                if m[pos[0]][pos[1]-x-2] == "#":
                    fail = True
                x += 1
            if fail:
                continue
            # move
            m[pos[0]][pos[1]-1] = "."
            for i in range(0,x+1):
                m[pos[0]][pos[1]-i-1] = "[]"[i%2]
            pos = (pos[0],pos[1]-1)
        m[pos[0]][pos[1]] = "@"
        # print matrix
    for i in m:
        print("".join(i))
    print()
    r = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "[":
                r += 100 * i + j
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d15.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))