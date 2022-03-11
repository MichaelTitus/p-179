#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:51:36 2021

Font color Manipulator
You have to build the game in such a way
that the user has to enter the font colour, and not the name of the colour being
displayed and accordingly the score will get updated for every right guessing of the
color.

@author: preethirajasekaran
"""

from tkinter import *
import random
root = Tk()
root.configure(background="Red")
#give suitable heading for application
root.title("Font Manipulator")
root.geometry("500x400")
root.config(bg="white")


label_name = Label(root,font=("Impact",40),bg="yellow")
label_name.place(relx=0.5,rely=0.3, anchor= CENTER)

score = Label(root,font=("Impact",40),bg="yellow")
score.place(relx=0.10,rely=0.1, anchor= CENTER)

input_value=Entry(root)
input_value.place(relx=0.5,rely=0.5,anchor=CENTER)


#define a class named game
class game:
    #define an init function, pass the method self to it
    def __init__(self):
        self.__score=0
        #assign value 0 to the private variable score
        
    def updateGame(self):
        #assign some values with color names to the list named text of the methid self 
        self.text = ["blue","green","yellow","purple","white","black","pink","brown"]
        
        #generate random number between 0 and 5 (if 5 colors are mentioned above) and assign it to self.random_number_for_text
        self.random_number_for_text=random.randint(0,7)
        #assign some values with color names to the list named self.color 
        self.color = ["blue","green","yellow","purple","white","black","pink","brown"]
        ##generate random number between 0 and 5 (if 5 colors are mentioned above) and assign it to self.random_number_for_color
        self.random_number_for_color=random.randint(0,7)
        #show the value of list self.text according to the random_number_for_text on the label_name
        label_name["text"] = self.text[self.random_number_for_text] 
        
        #show the foreground color of label from the list self.color according to the random_number_for_color
        label_name["fg"] = self.color[self.random_number_for_text] 
    def __updatescore(self,input_value):
       if(input_value==self.color[self.random_number_for_color]):
           self.__score=self.__score+random.randint(0,10)
           score["text"]="Score : "+str(self.__score)
    def getUserValue(self,input_value):
        self.__updatescore(input_value)
#define an object for the class game
obj = game()
def getInput():
    entervalue=input_value.get()
    obj.getUserValue(entervalue)
    obj.updateGame()
    input_value.delete(0,END)

#call the function updateGame for the button click
btn = Button(root, text="START" ,command=obj.updateGame, bg="dark olive green", fg="white", relief=FLAT,  padx=10, pady=1,  font=("Arial",15))
btn.place(relx=0.65,rely=0.65, anchor= CENTER)

btn_getinput = Button(root, text="Get Score" ,command=getInput, bg="dark olive green", fg="white", relief=FLAT,  padx=10, pady=1,  font=("Arial",15))
btn_getinput.place(relx=0.35,rely=0.65, anchor= CENTER)


root.mainloop()