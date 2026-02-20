import math

def is_prime(data):
    if data < 2:
        return False
    
    for i in range(2, int(math.sqrt(data)+1)):
        if data % i == 0:
            return False
    
    return True
        

M, N = map(int,input().split())

prime_list = []

for num in range(M, N + 1):
    prime_list.append(num)

for elem in prime_list:
    if is_prime(elem):
        print(elem)
