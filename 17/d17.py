a = int(input().split(":")[1])
b = int(input().split(":")[1])
c = int(input().split(":")[1])

ops = list(map(int, input().split(",")))
for i in range(0, len(ops), 2):
    op, val = ops[i], ops[i+1]
    match op:
        case 0:
            a = a // 