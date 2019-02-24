# Princess Sampson
# Python II - Dr. Lawrence
# Lab Jan 24 - Monkey Business

# determines average per day eaten by monkeys

# determine the least or greatest amount of food eaten by any one monkey during the week
# data: a 2d list
# greatest: boolean flag to determine whether to save larger or smaller numbers
def leastOrGreatest(data, greatest):
    # what was eaten on monday by the first monkey is the default smallest/largest
    leastOrGreatest = data[0][0]

    # for each monkey's row
    for monkey in range(len(data)):
        # for each day of the week
        for day in range(len(data[0])):
            # get the food eaten for the current monkey
            current = data[monkey][day]

            # if the current is less or greater than leastOrGreatest, reassign
            if greatest:
                if current > leastOrGreatest:
                    leastOrGreatest = current
            else:
                if current < leastOrGreatest:
                    leastOrGreatest = current
    
    return leastOrGreatest

# avg eaten per day by all monkeys
# data: a 2d list
def averagePerDay(data):
    # list for storing average per day
    average = [0] * len(data[0])

    # for each monkey
    for monkey in range(len(data)):
        # for the amount of food eaten per day
        for day in range(len(data[0])):
            # add the food eaten on the current day to its corresponding spot on avg
            average[day] += data[monkey][day]
     
    # turn into proper averages by dividing each total by the amount of monkeys
    for day in range(len(average)):
        average[day] /= len(data)

    return average

# get the user's input for a 3x7 array
def getDataFromUser():
    # initialize food table with starter values for each monkey
    data = [
        [0.0] * 7,
        [0.0] * 7,
        [0.0] * 7
    ]

    # for each monkey 
    for monkey in range(0, len(data)):
        # for each day of the week
        for day in range(0, len(data[0])):

            # prompt the user
            print("How many pounds of food did monkey %d eat on %d?" % (monkey + 1, day + 1))
            foodEatenOnCurrentDayFromUser = input("Enter a positive number:") 

            # prompt the user for input again if it's not exclusively a positive number
            while not foodEatenOnCurrentDayFromUser.isdigit():
                foodEatenOnCurrentDayFromUser = input("Enter a positive number: ")
            
            # save the user's input into the array as a float
            data[monkey][day] = float(foodEatenOnCurrentDayFromUser)

    return data

# print the rows and cols of a 2d list with tabs between the elements
# rowPrepend: text to label a row
# colAppend: text to append to each col element
def printTable(data, rowPrepend, colAppend):
    for row in range(len(data)):
        
        # print the given col prepend + row number
        print("%10s %d"  % (rowPrepend, (row + 1)), end="\t")
        printList(data[row], colAppend)

        # print a line of underscores between rows
        print()
        for _ in range(130):
            print("_", end = "")

        print()
    print()

# print the elements of a list with tabs between
def printList(data, append):
    for element in data:
        print("%12s" % str(element), end=(append + "\t"))

def main():
    # get food data from user
    monkeys = getDataFromUser()

    # compute the average per day
    averages = averagePerDay(monkeys)

    # round the averages to two decimal places
    averages = list(map(lambda avg: round(avg, 2), averages))

    # print weekday headings
    print("\t\t", end="")
    printList(["M", "T", "W", "Tr", "F", "Sa", "Su"], "")
    print()

    # print the food
    printTable(monkeys, "Monkey", "lbs")

    # print the average per day
    print("%12s:" % "Avg/day", end="\t")
    printList(averages, "lbs")
    print()

    # print least and greatest eaten
    
    print("%12s:\t\t%0.02flbs" % ("Least", leastOrGreatest(monkeys, False)))
    print("%12s:\t\t%0.02flbs" % ("Greatest", leastOrGreatest(monkeys, True)))

# call main
main()