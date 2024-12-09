from aocd import data, submit
import sys
from collections import defaultdict, deque

def main(s):
    r = 0
    ctr = 0
    st = []
    q = []
    for i in range(0, len(s)):
        for j in range(int(s[i])):
            if i % 2 == 1:
                st.append(-1)
                q.append(len(st)-1)
            else:
                st.append(i//2)
    print(q)
    ctr = len(st)-1
    for i in q:
        while st[ctr] == -1:
            ctr -= 1
        if ctr < i:
            break
        st[i] = st[ctr]
        st[ctr] = -1
    for i in range(len(st)):
        if st[i] != -1:
            r += i*st[i]
    return r

def main(s):
    empty_blocks = []
    full_blocks = []
    st = []
    for i in range(0, len(s)):
        if i % 2 == 1:
            empty_blocks.append([len(st), int(s[i])])
            for j in range(int(s[i])):
                st.append(-1)
        else:
            full_blocks.append([len(st), int(s[i])])
            for j in range(int(s[i])):
                st.append(i//2)
    for i in range(len(s)-1, 0, -2):
        for k in range(len(empty_blocks)):
            if empty_blocks[k][0] > full_blocks[i//2][0]:
                break
            if empty_blocks[k][1] >= int(s[i]):
                empty_blocks[k][1] -= int(s[i])
                for j in range(int(s[i])):
                    st[j+empty_blocks[k][0]] = i//2
                for j in range(int(s[i])):
                    st[j+full_blocks[i//2][0]] = -1
                empty_blocks[k][0] += int(s[i])
                break
    r = 0
    for i in range(len(st)):
        if st[i] != -1:
            r += i*st[i]
    return r

if len(sys.argv) > 1:
    if sys.argv[1] == 'p':
        print(main(open('d9.txt','r').read()))
    elif sys.argv[1] == 's':
        a = main(data)
        print(a)
        submit(a)
else:
    print(main(data))