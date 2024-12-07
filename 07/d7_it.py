# iterative approach to p1

def main(s):
    s = s.split("\n")
    r = 0
    for l in s:
        t, ns = l.split(":")
        t = int(t)
        ns = list(map(int, ns.split()))
        n = len(ns)
        for op in range(2**(n-1)):
            cur = ns[0]
            for j in range(n-1):
                if (op >> j) & 1 == 0: cur += ns[j+1]
                else: cur *= ns[j+1]
            if cur == t:
                r += t
                break
    return r