# P Sampson - Dr. Lawrence Python II
# This program displays two labels with text.

import tkinter

class MyGUI:
    def __init__(self):
        # main window widget
        self.main_window = tkinter.Tk()

        # two label widgets
        self.label1 = tkinter.Label(self.main_window, text='Hello World')
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program')

        # call both labels' pack methods
        self.label1.pack()
        self.label2.pack()

        # enter main loop
        tkinter.mainloop()


my_gui = MyGUI()