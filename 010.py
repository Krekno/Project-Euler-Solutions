def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

sum = 0

for i in range(2000000):
    if isPrime(i):
        sum += i

print(sum)