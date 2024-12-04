from aocd import data, submit
import sys
from collections import defaultdict

def main(s):
    r = 0
    en = True
    for i in range(len(s)-3):
        if s[i:i+4] == "do()":
            en = True
        if s[i:i+7] == "don't()":
            en = False
        if s[i:i+3] == "mul":
            try:
                a, b = s[i+4:i+3+s[i+3:].index(")")].split(",")
                if a.isnumeric() and b.isnumeric():
                    if en: r += int(a)*int(b)
            except:pass
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d3.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))