# Princess Sampson
# Dr Lawrence - Python 2
# 2-28-19
# Character Frequency - Determine the frequencey of the individual
# letters of a user-given word

def main():
    # get user input, lowercase it
    word = input('Enter a word: ').lower()

    # use a generator expression to iterate over each character
    # and place it in a tuple with the default frequency value, 0
    # the tuples will then decompose into a dictionary entry when passed
    freq_dict = dict((char, 0) for char in word)

    print(freq_dict)

# call main
main()
