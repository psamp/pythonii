# Princess Sampson
# InClassFilePractice - Words
# 1/31/18

# reads in a list of words and returns as a sorted array
def getWords():
    # list for words
    words = []

    # open the words file
    inputFile = open('C:\\Users\\psampson\\Documents\\Python II\\PSampson-LabJanuary31\\words.txt', 'r')
    
    # read in the first line
    line = inputFile.readline()

    # until the end of the file
    while line != "":
        # convert the no. string to a number
        word = line.rstrip()
    
        # append to the list
        words.append(word)

        # read in the next line
        line = inputFile.readline()

    # close the input file
    inputFile.close()

    return sorted(words)

def main():
    words = getWords()

    # open outfile
    outfile = open('C:\\Users\\psampson\\Documents\\Python II\\PSampson-LabJanuary31\\words-output.txt', 'w')

    for word in words:
        outfile.write(word + "\n")


# call main
main()