# Princess Sampson
# Python II - Dr. Lawrence
# P8.9

def main():
    # get user input
    one = input("Enter your first word:")
    two = input("Enter your second word:")

    # alphabet, set for storage
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    notInWords = set()

    # sets from the words
    oneList = set(one)
    twoList = set(two)

    # letters in both
    both = oneList.intersection(twoList)

    # letters only in first
    first = oneList.difference(twoList)

    # letters only in second
    second = twoList.difference(oneList)

    # which letters of the alphabet are not in either word
    for letter in alphabet:
        if letter not in oneList and letter not in twoList:
            notInWords.add(letter)

    # display output
    print("Letters in both: ", both)
    print("Only in first: ", first)
    print("Only in second: ", second)
    print("Not in either: ", notInWords)


# call main
main()
