def generateCow(index, prime, period):
    cow_numbers = []
    for _ in range(3):
        cow_numbers.append(1)
    p1 = 0
    p2 = 2
    count = 1
    while count <= period - 3:
        number = (cow_numbers[p1] + cow_numbers[p2]) % prime
        cow_numbers.append(number)
        p1 += 1
        p2 += 1
        count += 1
    return cow_numbers[index]

def deSierpinskify(factor, residue, prime):
    for num in range(factor):
        if (residue*(2**num)+1) % prime == 0:
            return num
    return -1

def mod(n, m):
    return n % m



def main():
    """print(mod(283717, 8))
    print(mod(283717, 31))
    print(mod(283717, 57))
    print(mod(283717, 168))
    print(mod(283717, 288))
    print(mod(283717, 9680))"""
    '''print(generateCow(5, 3, 8))
    print(generateCow(5, 5, 31))
    print(generateCow(28, 7, 57))
    print(generateCow(133, 13, 168))
    print(generateCow(37, 17, 288))
    print(generateCow(2997, 241, 9680))'''
    print(deSierpinskify(2, 1, 3))
    print(deSierpinskify(4, 4, 5))
    print(deSierpinskify(3, 6, 7))
    print(deSierpinskify(12, 3, 13))
    print(deSierpinskify(8, 4, 17))
    print(deSierpinskify(24, 237, 241))

if __name__ == "__main__":
    main()
    
    
