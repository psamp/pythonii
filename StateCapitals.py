# Princess Sampson
# Dr. Lawrence - Python II
# State Capitals Game

import random

# manages the game loop
def quiz(states):
    # game loop control
    playing = True

    # correct answers count
    correct = 0

    # until the user quits
    while playing:
        # select a random state
        state = random.choice(list(states.keys()))

        # get input
        answer = input("What is the capital of %s?\n" % state)

        # pull the capital from the dictionary
        capital = states[state]

        # if the answer is correct, inform the user and update the answers count
        if capital == answer:
            correct += 1
            print('You got it right!')
        # otherwise inform the user of the correct answer
        else:
            print('That is incorrect! The capital of %s is %s.' % (state, capital))

        print('Your score is: ', correct)

        # remove the state we've asked about
        states.pop(state)

        # ask the player if they want to play again
        choice = input('Would you like to play again? (Y/N)')
        playing = True if choice is "Y" else False
    
    # goodbye
    print("Thanks for playing!")

def main():
    # {state : capitals}
    capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau',
    'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover',
    'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis',
    'Massachusetts': 'Boston', 'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena',
    'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany',
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
    'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond',
    'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    # start the game
    quiz(capitals)

# call main
main()
