# P Sampson
# Python 2 - Dr. Lawrence
# Demonstates a group of checkbutton widgets.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Two frames, one for the Checkbuttons
        # and another for the regular Button widnets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create three IntVars for the Checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()

        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)

        # Create the Checkbutton widgets in the top_frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Small', \
            variable=self.cb_var1)

        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Medium', \
            variable=self.cb_var2)

        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Large', \
            variable=self.cb_var3)

        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Humongous', \
            variable=self.cb_var4)

        # Pack the checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()

        # Create an ok and quit button
        self.ok_button = tkinter.Button(self.bottom_frame, \
            text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.ok_button.pack()
        self.quit_button.pack()

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloo
        tkinter.mainloop()

    # show_choice is the callback for the ok button
    def show_choice(self):
        # message string
        self.message = 'You selected:\n'

        # determine message string based on selection
        if self.cb_var1.get() == 1:
            self.message += '%s\n' % (self.cb1.cget('text'))
        
        if self.cb_var2.get() == 1:
            self.message += '%s\n' % (self.cb2.cget('text'))
        
        if self.cb_var3.get() == 1:
            self.message += '%s\n' % (self.cb3.cget('text'))
        
        if self.cb_var4.get() == 1:
            self.message += '%s\n' % (self.cb4.cget('text'))

        # display the message
        tkinter.messagebox.showinfo('Selection', self.message)

def main():
    main_gui = MyGUI()

# call main
main()

        


