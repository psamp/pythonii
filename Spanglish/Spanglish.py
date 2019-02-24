# P Sampson
# Dr Lawrence
# Spanglish

# is a number even or odd?
def even(number):
    return number % 2 == 0

def main():
    #counter to keep track of odd and even
    counter = 1

    # read in spanglish
    spanglish = open('Bamba-Spanglish_v1.txt', 'r')

    # open file to write out english
    english = open('english.txt', 'w')

    # open file to write out english spanish
    spanish = open('spanish.txt', 'w')
    
    for line in spanglish:

        # if counter is even, write to english
        if even(counter):
            english.write(line)
        # else write to spanish
        else:
            spanish.write(line)
        
        # increment the counter
        counter += 1

    # close open files
    spanglish.close()
    english.close()
    spanish.close()

# call main
main()