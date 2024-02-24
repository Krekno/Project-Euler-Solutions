def isPrime(n):
    if n == 0 or n == 1: return 0
    if n == 2: return 1
    for i in range(2, n):
        if n % i == 0: return 0
    else: return 1

n = 0
count = 0
while count < 10001:
    if isPrime(n) == 1:
        count += 1
        print(n)
        if count == 10001: break
    n += 1

print(n)