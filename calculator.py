from tkinter import *

root = Tk()
root.title("calculator")



e = Entry(root, width =40, borderwidth = 7)
e.grid(row=0, column=0, columnspan=4, padx = 8, pady=8)

def button_click(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0,END)

def button_modulo():
	first_number = e.get()
	global f_num 
	global math
	math = "modulo"
	f_num = float(first_number)
	e.delete(0,END)

def button_sign():
	first_number = e.get()
	global f_num 
	global math
	math = "sign"
	f_num = float(first_number)
	e.delete(0,END)


def button_decimal():
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current)+'.')

def button_add():
	first_number = e.get()
	global f_num 
	global math
	math = "addition"
	f_num = float(first_number)
	e.delete(0,END)

def button_subtract():
	first_number = e.get()
	global f_num 
	global math
	math = "subtraction"
	f_num = float(first_number)
	e.delete(0,END)

def button_multiply():
	first_number = e.get()
	global f_num 
	global math
	math = "multiplication"
	f_num = float(first_number)
	e.delete(0,END)

def button_divide():
	first_number = e.get()
	global f_num 
	global math
	math = "divide"
	f_num = float(first_number)
	e.delete(0,END)


def button_equal():
	second_number = e.get()
	e.delete(0,END)

	if math == 'addition':
		e.insert(0,f_num + float(second_number))
	elif math == 'subtraction':
		e.insert(0,f_num - float(second_number))
	elif math == 'multiplication':
		e.insert(0,f_num * float(second_number))
	elif math == 'divide':
		e.insert(0,f_num / float(second_number))
	elif math == 'modulo':
		e.insert(0, f_num%float(second_number))
	elif math == 'sign':
		e.insert(0, f_num* -1)

	

button_0= Button(root, text = "0", padx = 102, pady = 20, command =lambda:button_click(0))
button_1= Button(root, text = "1", padx = 46, pady = 20, command =lambda:button_click(1))
button_2= Button(root, text = "2", padx = 46, pady = 20, command =lambda:button_click(2))
button_3= Button(root, text = "3", padx = 44, pady = 20, command =lambda:button_click(3))
button_4= Button(root, text = "4", padx = 46, pady = 20, command =lambda:button_click(4))
button_5= Button(root, text = "5", padx = 46, pady = 20, command =lambda:button_click(5))
button_6= Button(root, text = "6", padx = 44, pady = 20, command =lambda:button_click(6))
button_7= Button(root, text = "7", padx = 46, pady = 20, command =lambda:button_click(7))
button_8= Button(root, text = "8", padx = 46, pady = 20, command =lambda:button_click(8))
button_9= Button(root, text = "9", padx = 44, pady = 20, command =lambda:button_click(9))
button_add = Button(root, text = "+", padx = 40, pady = 20, command =button_add)
button_equal = Button(root, text = "=", padx = 40, pady = 20, command =button_equal)
button_clear = Button(root, text = "AC", padx = 41, pady = 20, command = button_clear)
button_subtract = Button(root, text = "-", padx=40, pady=20,command =button_subtract )
button_decimal = Button(root, text = ".", padx=46, pady=20,command =button_decimal)
button_sign = Button(root, text = "+/-", padx=39, pady=20,command =button_sign)
button_multiply = Button(root, text = "x", padx=40, pady=20,command = button_multiply)
button_modulo = Button(root, text = "%", padx=44, pady=20,command = button_modulo)
button_divide= Button(root, text = "/", padx=42, pady=20,command =lambda:button_click())




button_clear.grid(row=1, column =0)
button_sign.grid(row=1, column=1)
button_modulo.grid(row=1, column=2)
button_divide.grid(row=1,column=3)



button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_add.grid(row = 4, column = 3)


button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_subtract.grid(row=3,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_multiply.grid(row=2,column=3)

button_0.grid(row=5,column=0, columnspan=2)
button_equal.grid(row=5,column=3)
button_decimal.grid(row=5,column=2)






root.mainloop()