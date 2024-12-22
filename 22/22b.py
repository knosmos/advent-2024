from tqdm import tqdm
from collections import defaultdict
patterns = defaultdict(int)
opt = 0
for i in open("22.txt").read().split("\n"):
    x = int(i)
    s = [x%10]
    for j in range(2000):
        y = x * 64
        x = x ^ y
        x %= 16777216
        y = x // 32
        x = x ^ y
        x %= 16777216
        y = x * 2048
        x = x ^ y
        x %= 16777216
        s.append(x%10)
    p = set()
    for j in range(2000-3):
        t = tuple([s[x+1]-s[x] for x in range(j, j+4)])
        if t not in p:
            p.add(t)
            patterns[t] += s[j+4]
print(max(patterns.values()))