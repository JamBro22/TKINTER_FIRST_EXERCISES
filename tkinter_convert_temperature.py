# importing modules
from tkinter import *
import sys


# opening new tkinter window
root = Tk()
# resizing window
root.geometry("500x400")
# changing window title
root.title("Convert Temperature")

# initialising tkinter variables
radio_variable = IntVar()
f_answer = IntVar()
c_answer = IntVar()


# function to return converted temperatures based on radio buttons when convert button is clicked
def convert():
    if radio_variable.get() == 0:
        res = (int(f_entry.get()) - 32) * 5/9
        c_answer.set(res)
    else:
        res = int(c_entry.get()) * 9/5 + 32
        f_answer.set(res)


# function to exit program when quit button is clicked
def btn_quit():
    return sys.exit()

# adding a title as a label
title = Label(root, text="Convert Temperature")
# styling the title/label
title.config(font="50", pady="10")
# packing title into root
title.pack()

# creating a new frame within root
frame1 = Frame(root)
# packing the frame into root
frame1.pack()

# creating a label for fahrenheit
f_label = Label(frame1, text="F:", padx="5")
# packing f label into frame 1 to the left
f_label.pack(side=LEFT)
# creating a user entry box for fahrenheit
f_entry = Entry(frame1, textvariable=f_answer)
# packing entry into frame 1 to the left
f_entry.pack(side=LEFT)

# creating an entry box from celsius
c_entry = Entry(frame1, textvariable=c_answer, state=convert())
# packing the entry box into frame 1 to the right
c_entry.pack(side=RIGHT)
# creating a label for celsius
c_label = Label(frame1, text="C:", padx="5")
# packing the label into frame 1 to the right
c_label.pack(side=RIGHT)

# creating a second frame in root
frame2 = Frame(root)
# adding padding to frame along the y axis
frame2.config(pady="10")
# packing the frame into root
frame2.pack()

# creating a radio button for fahrenheit to celsius
f_radio = Radiobutton(frame2, text="Fahrenheit to Celsius", value=0, variable=radio_variable)
# packing the radio button to the left of frame 2
f_radio.pack(side=LEFT)
# creating a radio button for celsius to fahrenheit
c_radio = Radiobutton(frame2, text="Celsius to Fahrenheit", value=1, variable=radio_variable)
# packing radio button to the right of frame 2
c_radio.pack(side=RIGHT)

# creating a third frame
frame3 = Frame(root)
# packing the third frame into root
frame3.pack()
# creating a button to convert the temperature when clicked
btn_convert = Button(frame3, text="Convert", command=convert)
# styling the button
btn_convert.config(width="7", height="2")
# packing the button into frame 3
btn_convert.pack(side=LEFT)
# creating a button to quit the program when quit
btn_quit = Button(frame3, text="Quit", command=btn_quit)
# styling the button
btn_quit.config(width="7", height="2")
# packing the button to the right of frame 3
btn_quit.pack(side=RIGHT)

# creating a loop so the window can be viewed
root.mainloop()
