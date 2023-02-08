#Import library to use Tkinter.
from tkinter import *

#Define a variable to use as a command.
def Yes():
    print("You have successfully killed EDP445.")

def No():
    print("You spared EDP445. (Why?)")

#Now for the creation of our window, we use 'window' as a variable.
window = Tk()

#We need to put a label in our window too, using the 'title = Label' component.
title = Label(window,text = "Would you like to kill EDP445?")
title.grid()

#To use buttons we need to create two more variables, 'buttonYes' and 'buttonNo'.
#Put 'window' variable first to affect those inside it
#Add 'command' to define a variable
buttonYes = Button(window,text = "Yes",bg = "Green",command = Yes)
buttonYes.grid()
buttonNo = Button(window,text = "No",bg = "Red",command = No)
buttonNo.grid()

#Now to set the size of the window and add a title.
#To set the bounds of the window, use 'geometry' and add ("nXn") where n is a number
#To set a title for the window, use 'title' and add a title
#Now add the event listener, 'mainloop' to listen for button clicks or keypresses
window.geometry("500x500")
window.title("EDP Killing Machine by Limewires")
window.mainloop()
