total = 0
a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
for i in range(9, -1, -1):
    total = total + a[i]
    print(i)

print(total)