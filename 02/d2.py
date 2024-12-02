from aocd import data, submit
import sys
from collections import defaultdict

def tst(i):
    prev = i[0]
    for j in i[1:]:
        if not(abs(j-prev) >= 1 and abs(j-prev) <= 3):
            break
        prev = j
    else:
        for j in range(len(i)-1):
            if i[j+1] < i[j]:
                for k in range(len(i)-1):
                    if i[k+1] > i[k]:
                        break
                else:
                    return True
                break
        else:
            return True
    return False

def main(s):
    s = list(map(lambda i:list(map(int, i.split())), s.split("\n")))
    c = 0
    for i in s:
        if tst(i):
            c += 1
        else:
            for k in range(len(i)):
                if tst(i[0:k] + i[k+1:]):
                    c += 1
                    break
    return c

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d2.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))