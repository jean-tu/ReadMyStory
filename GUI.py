from tkinter import *
import tkinter.messagebox
from MadLib import MadLib
from Story import Story

from tkinter import font

class GUI(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.__master = master
        #First window information
        self.readMyStoryLabel = Label(self, text="readMyStory", font=("Courier", 30))
        # self.readMyStoryLabel.grid(row=0, column=2)
        self.readMyStoryLabel.grid()

        img = PhotoImage(Image.open("bookEmoji.png"))
        panel = Label(self, image=img)
        self.panel.grid()


        self.infoText1 = Label(self, text="You have the option of creating your own story or \n "
                                          "filling in a MadLibs that will then be read out for you \n"
                                          "at the end! You will even get the option to \n"
                                          "save your wonderful story!",
                              font=("Courier", 12))
        self.infoText1.grid()
        # self.infoText1.grid(row=1, column=2)
        # buttons
        self.createOwnButton = Button(self, text="Create Own!", command=self.createOwn)#.pack(side=LEFT)
        self.createOwnButton.grid()
        # self.createOwnButton.grid(row=2, column=2)
        self.madLibsButton = Button(self, text="MadLibs!", command=self.madLibs)#.pack(side=RIGHT)
        self.madLibsButton.grid()
        # self.madLibsButton.grid(row=2, column=2)

    def createOwn(self): #user decided to create their own story
        tkinter.messagebox.showinfo("Create Own!", "You have chosen to create your own story!")
        self.infoText1.grid_remove() #this is to remove the information text
        # remove the buttons
        self.madLibsButton.grid_remove()
        self.createOwnButton.grid_remove()

        #create story object
        self.story = Story()

        # The default text for the window
        content = StringVar()
        self.storyBox = Entry(self, width=40, textvariable=content) #adding it to the box
        self.storyBox.bind('<FocusIn>', self.on_entry_click)
        content.set("Story here")
        self.storyBox.config(fg='grey')
        self.storyBox.grid()

        self.readButton = Button(self, text="Read aloud", command=self.callRead)
        self.readButton.grid()

        self.saveLabel = Label(self, text="Enter a filename to save your story")
        self.saveLabel.grid()
        self.saveFileName = Entry(self, width=35)
        self.saveFileName.grid()
        self.saveButton = Button(self, text="Save Story", command=self.saveStory)
        self.saveButton.grid()

    def on_entry_click(self, event): #will clear the default text
        if self.storyBox.get() == "Story here":
            self.storyBox.delete(0, "end")  # delete all the text in the entry
            self.storyBox.insert(0, '')  # Insert blank for user input
            self.storyBox.config(fg='black')

    # def on_focusout(self):

    def madLibs(self): #user wanted to do the mad libs version
        tkinter.messagebox.showinfo("MadLibs!", "You have chosen to do a MadLib Story!")
        # clear the main and start
        self.infoText1.grid_remove()  # this is to remove the information text
        # remove the buttons
        self.madLibsButton.grid_remove()
        self.createOwnButton.grid_remove()

        #create the MadLib object
        self.mlObject = MadLib()
        listofStories = self.mlObject.getListOfStories()

        self.selectStoryText= Label(self, text="Please select a story below")
        self.madLibsStoryList = Listbox(self.__master) #passing in the window to add it
        for item in listofStories: #iterate to add
            self.madLibsStoryList.insert(END, item)

        self.madLibsStoryList.grid()
        self.selectStoryButton = Button(self, text="Select", command=self.setSelected)
        self.selectStoryButton.grid()

    def callRead(self):
        if self.storyBox.get() != "": #will only call on it if the box is filled out
            if self.storyBox.get() != "Story here": #will only read it if it's not default text
                self.story.read(self.storyBox.get()) #will read the text
        else:
            msg = "Please enter some text to be read!"
            # self.story.read(msg)  # will read the text to tell the user to enter text
            tkinter.messagebox.showinfo("Nothing to Read!", msg)

    def saveStory(self):
        if self.storyBox.get() != "": #will only call on it if the box is filled out
            #get the text from the save box
            if self.saveFileName.get() != "":
                #check if the end of the file is a .txt, if not add it
                print("old filename " + self.saveFileName.get()) #debugg
                self.fileName = self.saveFileName.get()
                if ".txt" not in self.fileName:
                    self.fileName += ".txt" #append it at the end
                self.story.save(self.storyBox.get(), self.fileName)
            else:
                tkinter.messagebox.showinfo("No filename!", "Please enter a filename!")

        else:
            msg = "Please write a story to be saved!"
            # self.story.read(msg)  # will read the text to tell the user to enter text
            tkinter.messagebox.showinfo("Nothing to Save!", msg)

    def setSelected(self):
        selected = self.madLibsStoryList.get(ACTIVE)
        print(selected)
        #call on the next action command from here
        self.showStory(selected)
        return selected

    def showStory(self, selectedStory): #this will grab the text from the sotyr
        storyFile =  open("Stories/" + selectedStory.rstrip(), "r") #go into the folder to get the stories

        #remove the items from previous window
        self.madLibsStoryList.grid_remove()
        self.selectStoryButton.grid_remove()


        story = "" #starts off blank
        for line in storyFile:
            story += line
        storyFile.close() #close the file after done reading from it
        self.madLibLabel = Label(self, text="Replace all of the words with _someWord_ and hear your story by clicking the Read button",
                                 wraplength=250)
        self.madLibLabel.grid()

        self.storyTextBox = Text(self, width= 50, height=10)
        self.storyTextBox.config(background="beige")
        self.storyTextBox.grid()
        self.storyTextBox.insert(END, story)  # adding the liens to the file

        #buttons to read & save
        self.readButton2 = Button(self, text="Read aloud", command=self.callReadMadLib)
        self.readButton2.grid()

        self.saveLabel2 = Label(self, text="Enter a filename to save your story")
        self.saveLabel2.grid()
        self.saveFileName2 = Entry(self, width=20)
        self.saveFileName2.grid()
        self.saveButton2 = Button(self, text="Save File!", command=self.saveStory)
        self.saveButton2.grid()


    def callReadMadLib(self):
        if self.storyTextBox.get("0.0",END) != "": #will only call on it if the box is filled out
            if self.storyTextBox.get("0.0",END) != "Story here": #will only read it if it's not default text
                self.mlObject.read(self.storyTextBox.get("0.0",END)) #will read the text
        else:
            msg = "Please enter some text to be read!"
            tkinter.messagebox.showinfo("Nothing to Read!", msg)