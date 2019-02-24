a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

for i in range (1, 5):
    a[i] = a[9-i] 

for element in a:
    print(element, end=", ")