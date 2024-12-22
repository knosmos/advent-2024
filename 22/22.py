r = 0
for i in open("22.txt").read().split("\n"):
    x = i
    for j in range(2000):
        x = int(x)
        y = x * 64
        x = x ^ y
        x %= 16777216
        y = x // 32
        x = x ^ y
        x %= 16777216
        y = x * 2048
        x = x ^ y
        x %= 16777216
    r += x
print(r)