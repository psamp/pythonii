import tkinter

class Sisters:
    def __init__(self):
        # main window
        self.main_window = tkinter.Tk()

        # canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=400)

        # frame and window
        self.canvas.create_rectangle(100, 150, 300, 350, fill='beige')
        self.canvas.create_oval(175, 175, 225, 225, fill='light blue')

        # door
        self.canvas.create_rectangle(150, 250, 250, 350, fill='white')
        self.canvas.create_line(250, )

        # columns
        self.canvas.create_rectangle(125, 150, 140, 350)
        self.canvas.create_rectangle(260, 150, 275, 350)

        # roof
        self.canvas.create_line(200, 50, 100, 150)
        self.canvas.create_line(200, 50, 300, 150)

        # pack canvas
        self.canvas.pack()

        # mainloop
        tkinter.mainloop()

def main():
    sisters = Sisters()

# call main
main()