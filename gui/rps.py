# P Sampson
# Dr. Lawrence - Python II
# GUI Rock paper scissors

import tkinter
import tkinter.messagebox
from tkinter import IntVar
from tkinter import Radiobutton
import random

class RockPaperScissors:
    def __init__(self):

        # options
        self.options = ['Rock', 'Paper', 'Scissors']
        
        # main window
        self.main_window = tkinter.Tk()

        # top frame for radio buttons and bottom frame for menu
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # radio buttons for options
        self.selection = IntVar()

        for choice in self.options:
            Radiobutton(self.top_frame, text=choice, variable=self.selection, value=self.options.index(choice)).pack()

        # create a play and quit button
        self.play_button = tkinter.Button(self.bottom_frame, \
            text='Play', command=self.play)
        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.play_button.pack()
        self.quit_button.pack()

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # start the mainloop
        tkinter.mainloop()

    # show_choice is the callback for the play button
    def play(self):
        choice = self.selection.get()
        result = self.rps(choice)

        # display the message
        tkinter.messagebox.showinfo('Selection', result)

    # rps vs random selection
    def rps(self, option):
        # each option mapped to what can beat it
        matching = {
            0 : 1,
            1 : 2,
            2 : 0
        }

        # random option
        computer = random.randint(0, 2)

        # base message
        message = 'Computer chose %s! ' % (self.options[computer])

        # if the computer's choice matches what beats the player's option
        # then computer wins
        if computer == matching[option]:
            return message + 'Computer wins!'
        # if the computer chose the same thing, then there's a tie
        elif computer == option:
            return message + 'Tie!'
        # otherwise, the player wins
        else:
            # otherwise player wins
            return message + 'You win!' 

def main():
    rps = RockPaperScissors()

# call main
main()