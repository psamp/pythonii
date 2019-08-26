# P Sampson
# Python II - Dr. Lawrence
# This program converts distances in kilometers to miles.
# The result is displayed in an info dialog box.

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        # main window
        self.main_window = tkinter.Tk()

        # two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # widgets for top frame
        self.prompt_label = tkinter.Label(self.top_frame, \
            text='Enter a distance in kilomters')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # pack top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # button widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, \
            text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy)


        # pack the buttons
        self.calc_button.pack()
        self.quit_button.pack()

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # convert is callback function for calculate button
    def convert(self):
        # value entered by user into kilo_entry
        kilo = float(self.kilo_entry.get())

        # kilos to miles
        miles = kilo * 0.6214

        # display results in info dialog
        info = '%0.2f kilometers is equal to %0.2f miles.' % (kilo, miles)
        tkinter.messagebox.showinfo('Results', info)

def main():
    kilo_converter = KiloConverterGUI()

# call main
main()