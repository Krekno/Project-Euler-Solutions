def primeFactors(n):
    factors = []
    divisor = 2
    while n >= 2:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors

def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result

list = []

for i in range(1, 21):
    arr = primeFactors(i)
    for j in arr:
        if j not in list:
            list.append(j)
        if j in list:
            if list.count(j) < arr.count(j):
                list.append(j)


print(multiplyList(list))
print(sorted(list))