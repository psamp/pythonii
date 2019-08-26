# P Sampson
# Dr. Lawrence - Python II
# Freddy's Fast Food menu utilizing checkbuttons and radio buttons to order
import tkinter
import tkinter.messagebox
from tkinter import StringVar
from tkinter import Radiobutton

class FastFood:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # total
        self._total = 0

        # sandwich options
        self._menu = {
            'BLT': 5.00,
            'Turkey': 4.50,
            'Veggie': 4.00
        }

        # frame for sandwich list and menu button
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # radio buttons for menu
        self.selection = StringVar()
        for sandwich in self._menu:
            Radiobutton(self.top_frame, text=sandwich, variable=self.selection,value=sandwich).pack()

        # condiment checkbutton int vars
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()

        # condiments
        self._condiments = ['Brown Mustard', 'Mayo', 'Chipotle Sauce', 'Jalapenos', 'Spinach']

        # list of checkbutton int vars
        self.checkbuttons_val = [self.cb_var1, self.cb_var2, self.cb_var3, self.cb_var4, self.cb_var5]

        # initialize checkbutton values to 0
        for val in self.checkbuttons_val:
            val.set(0)

        # for each checkbutton value, create and pack a button with the proper label
        for count in range(0, 5):
            val = self.checkbuttons_val[count]
            condiment = self._condiments[count]

            tkinter.Checkbutton(self.top_frame, text=condiment, \
            variable=val).pack(side='left')

        # total and quit button
        tkinter.Button(self.bottom_frame, \
            text='Total', command=self.show_total).pack(side='left')
        tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy).pack(side='left')

        # pack top and bottom frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_total(self):
        # selected sandwhich
        sandwich = self.selection.get()

        # base price
        total = self._menu[sandwich]

        # list of selected condiments
        extras = []

        # for each condiment
        for count in range(0, 5):

            # pull value of checkbutton value for that condiment out
            condiment = self.checkbuttons_val[count].get()

            # if a condiment was selected
            if condiment == 1:
                # add 20 cents for every condiment
                total += .20

                # save the selected condiment
                extras.append(self._condiments[count])
        
        # message to show the user
        message = 'Your total is $%0.2f for the %s with %s' % (total, sandwich, str(extras))

        # display the message
        tkinter.messagebox.showinfo('Selection', message)

def main():
    ff = FastFood()

# call main
main()