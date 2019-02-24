# Princess Sampson
# InClassFilePractice - Nums
# 1/31/18

# reads in a list of numbers and returns as a sorted array
def getNumbers():
    # list for numbers
    numbers = []

    # open the numbers file
    inputFile = open('C:\\Users\\psampson\\Documents\\Python II\\PSampson-LabJanuary31\\nums.txt', 'r')
    
    # read in the first line
    line = inputFile.readline()

    # until the end of the file
    while line != "":
        # convert the no. string to a number
        number = line.rstrip()
    
        # append to the list
        numbers.append(float(number))

        # read in the next line
        line = inputFile.readline()

    # close the input file
    inputFile.close()

    return sorted(numbers)

def main():
    # read in the numbers and sort them
    numbers = getNumbers()

    # compute sum and avg
    summation = sum(numbers)
    avg = summation / len(numbers)

    # open outfile
    outfile = open('C:\\Users\\psampson\\Documents\\Python II\\PSampson-LabJanuary31\\nums-output.txt', 'w')

    # read out sorted list
    for num in numbers:
        outfile.write(str(num) +"\n")

    # read out sum and avg
    outfile.write("Sum: " + str(summation) + "\n")
    outfile.write("Avg: " + str(avg))

    # close the outfile
    outfile.close()

    print(numbers)

# call main
main()
    