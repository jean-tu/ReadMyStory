from Story import Story
from tkinter import *
from tkinter import messagebox
from GUI import GUI

def main():

    root = Tk()
    root.title("Story Time")# set the title
    root.geometry("400x400")# set the size of the window
    root.configure() #Setting the background color

    app = GUI(root)

    # start the program -- once you run this, nothing else after it will get called
    root.mainloop()

main()