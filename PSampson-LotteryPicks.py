# Princess Sampson
# Dr. Lawrence - Python 2

import random

# generates a set of lottery numbers
def lottery_numbers():
    
    # storage for playing numbers
    numbers = set()

    # generate six random numbers
    for _ in range(6):
        number = random.randint(1, 36)

        # if the number is already in the storage, generate anotheer value
        while number in numbers:
            number = random.randint(1, 36)
        
        # save the number
        numbers.add(number)


    return numbers

def main():
    
    # generate a play for every day of the week
    plays = {
        "M": lottery_numbers(),
        "T": lottery_numbers(),
        "W": lottery_numbers(),
        "Tr": lottery_numbers(),
        "F": lottery_numbers(),
        "Sa": lottery_numbers(),
        "S": lottery_numbers()
    }

    # print each day and play
    for day, play in plays.items():
        print("%2s:\t" % day, end="")
        
        for num in play:
            print("%2d" % num, end=" ")
        print()
        
# call main
main()

