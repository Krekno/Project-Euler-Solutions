list = []
sum = 0

for i in range(0, 1000, 3):
    list.append(i)

for i in range(0, 1000, 5):
    list.append(i)

for i in range(0, 1000, 15):
    list.remove(i)

for i in list:
    sum += i

print(sum)