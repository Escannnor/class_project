from tkinter import *



root = Tk()
root.title("Simple Calculator")
root.config(bg="azure")
v = Entry(root, width=35, borderwidth=5)
v.grid(row=0, columnspan=3, padx=40, pady=20)


# funtions
def button_click(david):
    current = v.get()
    v.delete(0, END)
    v.insert(0,str(current) + str(david))
    
def button_subtact():
    first_number = v.get()
    global math
    global f_num
    math = "subtraction"
    f_num =int(first_number)
    v.delete(0,END)
    
def button_div():
    first_number = v.get()
    global math
    global f_num
    math = "division"
    f_num = int(first_number)
    v.delete(0, END)
    
    
def button_clear():
    v.delete(0, END)
    
def button_plus():
    first_number = v.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    v.delete(0, END)
    
def button_multi():
    first_number = v.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    v.delete(0, END)
    
def equal_to():
    second_number = v.get()
    v.delete(0, END)
    if math == "addition":
        v.insert(0, f_num + int(second_number))
    elif math =="subtraction":
        v.insert(0,f_num - int(second_number))
    elif math == "division":
        v.insert(0, f_num / int(second_number))
    elif math == "multiplication":
        v.insert(0, f_num * int(second_number))
    
    pass

# buttons

button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1), font="bold")
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2), font="bold")
button_3 = Button(root, text='3', padx=40, pady=20, command= lambda: button_click(3), font="bold")
button_4 = Button(root, text='4', padx=40, pady=20, command= lambda: button_click(4), font="bold")
button_5 = Button(root, text='5', padx=40, pady=20, command= lambda: button_click(5), font="bold")
button_6 = Button(root, text='6', padx=40, pady=20, command= lambda: button_click(6), font="bold")
button_7 = Button(root, text='7', padx=40, pady=20, command= lambda: button_click(7), font="bold")
button_8 = Button(root, text='8', padx=40, pady=20, command= lambda: button_click(8), font="bold")
button_9 = Button(root, text='9', padx=40, pady=20, command= lambda: button_click(9), font="bold")
button_0 = Button(root, text='0', padx=40, pady=20, command= lambda: button_click(0), font="bold")
button_add = Button(root, text="+", padx=40, pady=20, command= button_plus, font="bold")
button_sub = Button(root, text="-", padx=40, pady=20, command= button_subtact, font="bold")
button_multiply = Button(root, text="x", padx=40, pady=20, command= button_multi, font="bold")
button_divide = Button(root, text="/", padx=40, pady=20, command= button_div, font="bold")
button_equal = Button(root, text="=", padx=79, pady=20, command= equal_to, font="bold")
button_c = Button(root, text="c", padx=88, pady=20, command= button_clear, font="bold")


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_add.grid(row=5, column=0)
button_sub.grid(row=5, column=1)
button_divide.grid(row=5, column=2)
button_multiply.grid(row=6, column=1)
button_equal.grid(row=7, column=0)
button_c.grid(row=8, column=0)

root.mainloop()