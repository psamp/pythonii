# Princess Sampson
# Dr Lawrence - Python 2
# 2-28-19
# Character Frequency - Determine the frequencey of the individual
# letters of a user-given word using a dictionary

def main():
    # get user input, lowercase it
    word = input('Enter a word: ').lower()

    # dict for storing letters and frequenches
    character_freq = {}

    # for each character
    for char in word:
        # if previously found, increment the frequency counter
        if char in character_freq:
            character_freq[char] += 1
        # else update the freq counter from zero
        else:
            character_freq[char] = 1

    # print character freq's keys and values
    for char, freq in character_freq.items():
        print('%s:\t%d' % (char, freq))

# call main
main()
