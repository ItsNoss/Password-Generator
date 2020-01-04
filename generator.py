import random
from random import shuffle
import tkinter as tk
from tkinter import *

def click():
	numbers = '0123456789'
	letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	entered_purpose = textentry.get()
	entered_length = int(textentry2.get())
	entered_letters = int(textentry3.get())
	entered_numbers = int(textentry4.get())
	n = random.choices(numbers, k=entered_numbers)
	l = random.choices(letters, k=entered_letters)
	passlist = n + l
	total = entered_letters+entered_numbers
	output.delete(0.0, END)
	output.insert(END, entered_purpose+'\n')
	if entered_length < 6:
		output.insert(END, 'Password must be at least 6 characters long!')
	elif total != entered_length:
		output.insert(END, 'The amount of numbers and letters does not equal the length you set!')
	elif total == entered_length:
		def passToString(passlist):

			password = ''

			for ele in passlist:
				password += ele
			return password
		output.insert(END, passToString(passlist))
		def saveClick():
			with open(entered_purpose+'.txt', 'w') as wf:
				wf.write(entered_purpose+': '+passToString(passlist))
		Button(window, text='SAVE', width=6, command=saveClick).grid(row=9, column=0, sticky=W) 

# Creating the window
window = tk.Tk()
window.title('Password Generator')
window.configure(background = 'black')

# Creating the first Label
Label (window, text = 'What will this password be used for?', bg = 'black', fg = 'white', font = 'none 12 bold').grid(row = 1, column = 0, sticky = W)
Label (window, text = 'How long should the password be?', bg = 'black', fg = 'white', font = 'none 12 bold').grid(row = 3, column = 0, sticky = W)
Label (window, text = 'How many letters should be in the password?', bg = 'black', fg = 'white', font = 'none 12 bold').grid(row = 5, column = 0, sticky = W)
Label (window, text = 'How many numbers should be in the password?', bg = 'black', fg = 'white', font = 'none 12 bold').grid(row = 7, column = 0, sticky = W)

# Creating the text entry
textentry = Entry(window, width = 20, bg = 'white')
textentry.grid(row = 2, column = 0, sticky = W)
textentry2 = Entry(window, width = 20, bg = 'white')
textentry2.grid(row = 4, column = 0, sticky = W)
textentry3 = Entry(window, width = 20, bg = 'white')
textentry3.grid(row = 6, column = 0, sticky = W)
textentry4 = Entry(window, width = 20, bg = 'white')
textentry4.grid(row = 8, column = 0, sticky = W)

# Creating a submit button
Button(window, text='SUBMIT', width=6, command=click).grid(row=9, column=0, sticky=W)

# Creating an output box
output = Text (window, width = 50, height = 3, wrap = WORD, background = 'white')
output.grid(row = 10, column = 0, columnspan = 2, sticky = W)
window.mainloop()
