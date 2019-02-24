# P Sampson
# Spanglish

def even(number):
    return number % 2 == 0

def main():

    #counter to keep track of odd and even
    counter = 0

    # read in spanglish
    spanglish = open('C:\\Users\\psampson\\Documents\\Python II\\Spanglish\\Bamba-Spanglish_v1.txt', 'r')

    # open file to write out english
    english = open('C:\\Users\\psampson\\Documents\\Python II\\Spanglish\\english.txt', 'w')

    # open file to write out english spanish
    spanish = open('C:\\Users\\psampson\\Documents\\Python II\\Spanglish\\spanish.txt', 'w')
    
    line = spanglish.readline()

    # until the end of the file
    while line != "":
        
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