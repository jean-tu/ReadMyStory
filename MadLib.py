from Story import Story


class MadLib(Story):
    def __init__(self):
        super().__init__()


    # returns the list of stories for the user to select
    def getListOfStories(self): #will go though the master.txt file to get the file names of the files
        listofStories = [] #creating a blank list
        fileIn = open("Stories/master.txt", "r") #go into the folder to get the stories
        for line in fileIn:
            # print(line)
            listofStories.append(line)
        return listofStories


