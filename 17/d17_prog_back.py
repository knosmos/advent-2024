'''
Register A: 22817223
Register B: 0
Register C: 0

Program: 2,4, 1,2, 7,5, 4,5, 0,3, 1,7, 5,5, 3,0

Continuously read last three bits of a

'''
a = 0
b = 0
c = 0

#r = [2,4, 1,2, 7,5, 4,5, 0,3, 1,7, 5,5, 3,0][::-1]
r = [1,2,3,4]
# reverse engineering

def rfn(a,b,c,n):
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

# jmp 0
for i in r:
    b = i
    b ^= 7 # reverses all the bits in b
    a *= 8
    b ^= c
    c = a // (2**b)
    b ^= 2
    a += b
    print(a,b,c)
    


    '''
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
    '''

print(a)