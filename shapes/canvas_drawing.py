# P Sampson
# Dr. Lawrence - Python II
# Big Ben canvas drawing

import tkinter

class BigBen:

    def __init__(self):
        # main window
        self.main_window = tkinter.Tk()

        # canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=400, background='sky blue')
        # spire
        self.canvas.create_line(200, 50, 200, 25)

        # top
        self.canvas.create_line(140, 100, 200, 50, 260, 100)

        # box
        self.canvas.create_rectangle(140, 100, 260, 150, fill='beige')

        # clock
        self.canvas.create_oval(175, 100, 225, 150, fill='white')
        self.canvas.create_oval(195, 125, 200, 130, fill='black')
        
        # base
        self.canvas.create_rectangle(150, 150, 250, 350, fill='beige')

        # windows
        for shift in range(0, 4):
            shifted = shift * 50
            self.canvas.create_rectangle(175, 150 + shifted, 225, 200 + shifted, fill='bisque2')

        # water
        self.canvas.create_rectangle(0, 350, 400, 400, fill='blue')

        # pack canvas
        self.canvas.pack()

        # mainloop
        tkinter.mainloop()



def main():
    bb = BigBen()

# call main
main()

