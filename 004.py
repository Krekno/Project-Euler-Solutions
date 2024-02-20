for i in range(999999, 100000, -1):
    if str(i) == str(i)[::-1]:
        for j in range(999, 100, -1):
            if i % j == 0 and len(str(i // j)) == 3:
                print(i)
                exit(0)