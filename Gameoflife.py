from tkinter import *
import random

class GameOfLife:

    def __init__(self):
        window = Tk()
        window.title("Game of Life")

        self.cardList = []
        for i in range(1, 10):
            self.cardList.append(PhotoImage(file="C:\Python34\Myexamples\GameOfLife\People\person"+str(i)+".png"))


        frame1 = Frame(window)
        frame1.grid(row=1,column=1,pady=10)
       
       
        self.labelList = []
        for i in range(9):
            self.labelList.append(Label(frame1,image=self.cardList[i]))
            self.labelList[i].pack(side=LEFT)


# This is where frame 2 stars where row 2 is suppose to happen, you know what I mean
        self.cardList1 = []
        for i in range(1, 10):
            self.cardList1.append(PhotoImage(file="C:\Python34\Myexamples\GameOfLife\People\person"+str(i)+".png"))
            
        frame2 = Frame(window)
        frame2.grid(row=2,column=1,pady=10)

       
        self.labelList1 = []
        for i in range(9):
            self.labelList1.append(Label(frame2,image=self.cardList1[i]))
            self.labelList1[i].pack(side=LEFT)


# This one right here is the button thingy for the shuffling part
        Button(window, text = "Shuffle", command=self.shuffle).grid(row=3,column=1)
        window.mainloop()

# This is the function for shuffling
    def shuffle(self):
        random.shuffle(self.cardList)
        random.shuffle(self.cardList1)
        for i in range(9):
            self.labelList[i]["image"]= self.cardList[i]
        for i in range(9):
            self.labelList1[i]["image"]= self.cardList1[i]

            
#Underconstruction 
