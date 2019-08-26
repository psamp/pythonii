# P Sampson
# Python II - Dr. Lawrence
# This program creates labels in two diff. frames

import tkinter

class MyGUI:
    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()

        # two frames, one for top of window
        # and one for the botttom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # three Label widgets for top frame
        self.label1 = tkinter.Label(self.top_frame, text='Winken')
        self.label2 = tkinter.Label(self.top_frame, text='Blinken')
        self.label3 = tkinter.Label(self.top_frame, text='Nod')

        # pack labels that are in the top frame
        # use side='top' arg to stack them atop each other
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # label widgets for bottom frame
        # three Label widgets for bottom frame
        self.label4 = tkinter.Label(self.bottom_frame, text='Winken')
        self.label5 = tkinter.Label(self.bottom_frame, text='Blinken')
        self.label6 = tkinter.Label(self.bottom_frame, text='Nod')

        # pack labels that are in the bottom frame
        # use side='left' arg to arrange them horizontally from left
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter tkinter main loop
        tkinter.mainloop()

def main():
    my_gui = MyGUI()

# call main
main()