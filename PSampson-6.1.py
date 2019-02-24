import random

# Princess Sampson
# Program 6.1 1-17-19

def main():
    # store list length in variable
    length = 10
    
    # instantiate empty list
    li = []

    # using random class method, add as many random numbers as length's value
    for i in range(length):
        li.append(random.randint(1, length))

    # print the list
    print(li)

    # print every even indexed number
    for i in range(0, length, 2):
        print(li[i], end=" ")

    print()

    # print every even element
    for i in range(length):
        current = li[i]
        if current % 2 == 0:
            print(current, end=" ")

    print()

    # print the list in reverse
    for i in reversed(range(length)):
        print(li[i], end=" ")

    print()

    # print first and last element
    print(li[0], li[length - 1], end=" ")

    print()

    # print max and min
    print(max(li), min(li), end=" ")

# call main
main()



