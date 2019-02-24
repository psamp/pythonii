# Princess Sampson
# Python II - Dr. Lawrence
# R6.8 Solution
# Write for loops that iterate over the elements of a list without the use of the range
# function for the following tasks: a, b, and c.

def sixEight():
    numbers = [4, -67, 8, 90, 17, 10, 2, -9, 42, 15]

# a. Printing all elements of a list in a single row, separated by spaces.
    # print every element with a space appended
    for number in numbers:
        print(number, end=" ")
    print()

# b. Computing the product of all elements in a list.
    # start the product at one because 0 will result in 0
    product = 1
    
    # multiply product's value by every value in the list and update its value 
    for number in numbers:
        product *= number

    # print the result
    print("The product of all the numbers in the list is", product)

# c. Counting how many elements in a list are negative.
    negativeCount = 0

    # if an element is negative, increase the count by 1
    for number in numbers:
        if number < 0:
            negativeCount += 1
    
    print("The number of negative numbers is", negativeCount)

def main():
    sixEight()

# call main
main()