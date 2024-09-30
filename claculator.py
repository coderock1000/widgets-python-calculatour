from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl = Label(text="Let's Multiply Two Numbers", fg="white", bg="black", height=1, width=300)

num1_lbl = Label(text="Enter First number", bg="red")
num1_entry = Entry()

num2_lbl = Label(text="Enter Second number", bg="green")
num2_entry = Entry()

def multiply():

	n1 = int(num1_entry.get())
	n2 = int(num2_entry.get())
	product = n1*n2

	text_box.insert(END, "the final product is \n")
	text_box.insert(END, product)

text_box = Text(height=3)

btn = Button(text="Calculate", command=multiply, height=1, bg="blue", fg='white')

lbl.pack()
num1_lbl.pack()
num1_entry.pack()
num2_lbl.pack()
num2_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()