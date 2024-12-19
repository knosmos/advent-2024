'''
Register A: 22817223
Register B: 0
Register C: 0

Program: 2,4, 1,2, 7,5, 4,5, 0,3, 1,7, 5,5, 3,0
'''
a = 2560#22817223
b = 0
c = 0

r = []

# jmp 0
while a != 0:
    # bst 4
    b = a % 8
    # bxl 2
    b = b ^ 2
    # cdv 5
    c = a // (2**b)
    # bxc 5
    b = b ^ c
    # adv 3
    a = a // (2**3)
    # bxl 7
    b = b ^ 7
    # out 5
    r.append(b%8)
    print(a,b,c)

print(",".join(map(str, r)))