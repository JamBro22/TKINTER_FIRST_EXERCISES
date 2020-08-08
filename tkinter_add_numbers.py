# import modules
from tkinter import *
import sys

# creating new tkinter window
root = Tk()
# resizing the window
root.geometry("500x400")
# creating a new title
root.title("Add Numbers")


# initialising variables
answer = StringVar()
num1 = StringVar()
num2 = StringVar()


# creating a function to add numbers from user input when add button is clicked
def add_numbers():
    res = int(num1_entry.get()) + int(num2_entry.get())  # gets input values and adds them
    answer.set(res)  # sets added values into answer field


# creating a function to clear the input boxes when clear button is clicked
def clear_boxes():
    res = ""
    num1.set(res)  # sets input value to empty string
    num2.set(res)
    answer.set(res)


# creating a function that closes the program when exit button is clicked
def btn_exit():
    return sys.exit()


# creating and packing frames into root to configure layout
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.config(pady="20")
frame4.pack()

# creating a label to enter first number
num1_label = Label(frame1, text="Enter first number")
# styling label
num1_label.config(font="50")
# creating an input field for first number
num1_entry = Entry(frame1, textvariable=num1)

# creating a label for second number
num2_label = Label(frame2, text="Enter second number")
# styling label
num2_label.config(font="50", pady="20")
# creating an input field for second number
num2_entry = Entry(frame2, textvariable=num2)

# creating a label for answer
answer_label = Label(frame3, text="Answer")
# styling label
answer_label.config(font="50")
# creating an output field for answer
answer_entry = Entry(frame3, text=0, textvariable=answer, state="disabled")

btn_add = Button(frame4, text="Add", command=add_numbers, borderwidth="8")
btn_add.config(width="6", height="3")
btn_clear = Button(frame4, text="Clear", command=clear_boxes, borderwidth="8")
btn_clear.config(width="6", height="3")
btn_exit = Button(frame4, text="Exit", command=btn_exit, borderwidth="8")
btn_exit.config(width="6", height="3")


num1_label.pack(side=LEFT)
num1_entry.pack(side=RIGHT)
num2_label.pack(side=LEFT)
num2_entry.pack(side=RIGHT)
answer_label.pack(side=LEFT)
answer_entry.pack(side=RIGHT)
btn_add.pack(side=LEFT)
btn_clear.pack(side=LEFT)
btn_exit.pack(side=RIGHT)


root.mainloop()
