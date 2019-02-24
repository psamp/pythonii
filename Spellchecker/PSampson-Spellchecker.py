# Princess Sampson
# Dr. Lawrence - Python II
# Spellchecker

# read words in from the file and return as list
def get_dict():
    words = open("words.txt", "r")
    dictionary = []

    # for every word in the file
    for line in words:

        #strip the line of newline
        stripped = line.rstrip('\n')
        
        # append the word to the dictionary
        dictionary.append(stripped)
    
    return dictionary

def main():
    # get dictionary
    dictionary = get_dict()

    # get sentence from user
    sentence = input("Enter the sentence you would like to spellcheck:").split()

    # storage for misspelled words
    misspelled = []

    # if any word in the sentence is not in the dictionary, save to misspelled
    for word in sentence:
        if word not in dictionary:
            misspelled.append(word)
    
    # if there are misspelled words, notify the user and print them
    if len(misspelled) > 0:
            print("The following words are incorrectly spelled:")
        
            for word in misspelled:
                print(word)

# call main
main()

    

