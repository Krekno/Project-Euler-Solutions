fibonacci = [1, 2]
i = 1

while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[i] + fibonacci[i - 1])
    i+=1

sum = 0
for i in fibonacci:
    if i % 2 == 0:
        sum += i

print(sum)