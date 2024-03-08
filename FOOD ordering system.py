from tkinter import *
import customtkinter as ctk


root = Tk()
root.geometry("1600x900+0+0")



root.title("ESANCONR'S food ordeing system")
root.config(bg="azure4")

top_frame = Frame(root, bd=10, relief=RIDGE, bg="antiquewhite")
top_frame.pack(side="top")

label_Tille = Label(top_frame, text="Food Ordering System", font=('arial', 30, 'bold'),fg="red", width=61, bd=8)
label_Tille.grid(row=0, column=0)

menu_frame = Frame(root, bd=10, relief=RIDGE)
menu_frame.pack(side=LEFT)

cost_frame = Frame(menu_frame, bd=4, relief=RIDGE)
cost_frame.pack(side=BOTTOM)

food_frame = LabelFrame(menu_frame, text="Food", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="red")
food_frame.pack(side=LEFT)

drink_frame = LabelFrame(menu_frame, text="Drink", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="red")
drink_frame.pack(side=LEFT)

snacks_frame = LabelFrame(menu_frame, text="Snacks", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="red")
snacks_frame.pack(side=LEFT)

right_frame = Frame(root, bd=15, relief=RIDGE)
right_frame.pack(side=RIGHT)

calcualtor_frame = Frame(right_frame, bd=1, relief=RIDGE)
calcualtor_frame.pack()

receipt_frame = Frame(right_frame, bd=4, relief=RIDGE)
receipt_frame.pack()

button_frame = Frame(right_frame, bd=3, relief=RIDGE)
button_frame.pack()


# variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()

e_rice = StringVar()
e_beans = StringVar()
e_amala = StringVar()
e_jollof_rice = StringVar()
e_fried_rice = StringVar()
e_coconut_rice = StringVar()
e_spaghetti = StringVar()
e_macaroni = StringVar()
e_peppersoup = StringVar()
e_pounded_yam = StringVar()
e_semo = StringVar()
e_yam = StringVar()
e_chinese_rice = StringVar()
e_alomo_bitters = StringVar()
e_fanta = StringVar()
e_henessey = StringVar()
e_pepsi = StringVar()
e_mirinda = StringVar()
e_chivita = StringVar()
e_zobo = StringVar()
e_red_wine = StringVar()
e_yoghurt = StringVar()
e_nutri_milk = StringVar()
e_maltina = StringVar()
e_mirinda = StringVar()
e_doughnurt = StringVar()
e_cake = StringVar()
e_puff_puff = StringVar()
e_shawarma = StringVar()
e_pizza = StringVar()

e_rice.set('0')
e_beans.set('0')
e_amala.set('0')
e_jollof_rice.set('0')
e_fried_rice.set('0')
e_coconut_rice.set('0')
e_spaghetti.set('0')
e_macaroni.set('0')
e_peppersoup.set('0')
e_pounded_yam.set('0')
e_semo.set('0')
e_yam.set('0')
e_chinese_rice.set('0')


e_alomo_bitters.set('0')
e_henessey.set('0')
e_red_wine.set('0')
e_fanta.set('0')
e_pepsi.set('0')
e_mirinda.set('0')
e_nutri_milk.set('0')
e_maltina.set('0')
e_yoghurt.set('0')
e_chivita.set('0')
e_zobo.set('0')

e_cake.set('0')
e_shawarma.set('0')
e_pizza.set('0')
e_puff_puff.set('0')
e_doughnurt.set('0')
# food
rice = Checkbutton(food_frame, text="Rice", font=("Bradley Hand ITC", 15, "bold",),  onvalue=1, offvalue=0, variable=var1)
rice.grid(row=0, column=0, sticky=W)

beans = Checkbutton(food_frame, text="Beans", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var2)
beans.grid(row=1, column=0, sticky=W)

amala = Checkbutton(food_frame, text="Amala", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var3)
amala.grid(row=2, column=0, sticky=W)

jollof_rice = Checkbutton(food_frame, text="Jollof Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var4)
jollof_rice.grid(row=3, column=0, sticky=W)

fried_rice = Checkbutton(food_frame, text="Fried Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var5)
fried_rice.grid(row=4, column=0, sticky=W)

coconut_rice = Checkbutton(food_frame, text="Cononut Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var6)
coconut_rice.grid(row=5, column=0, sticky=W)

spaghetti = Checkbutton(food_frame, text="Spaghetti", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var7)
spaghetti.grid(row=6, column=0, sticky=W)

macaroni = Checkbutton(food_frame, text="Macaroni", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var8)
macaroni.grid(row=7, column=0, sticky=W)

peppersoup = Checkbutton(food_frame, text="Peppersoup", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var9)
peppersoup.grid(row=8, column=0, sticky=W)

pounded_yam = Checkbutton(food_frame, text="PoundedYam", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var10)
pounded_yam.grid(row=9, column=0, sticky=W)

semo = Checkbutton(food_frame, text="Semo", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var11)
semo.grid(row=10, column=0, sticky=W)

yam = Checkbutton(food_frame, text="Yam", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var12)
yam.grid(row=11, column=0, sticky=W)

chinese_rice = Checkbutton(food_frame, text="Chinese Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var13)
chinese_rice.grid(row=12, column=0, sticky=W)

# food entry

text_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_rice)
text_rice.grid(row=0, column=1,)

text_beans = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_beans)
text_beans.grid(row=1, column=1,)

text_amala = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_amala)
text_amala.grid(row=2, column=1,)

text_jollof_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_jollof_rice)
text_jollof_rice.grid(row=3, column=1,)

text_fried_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_fried_rice)
text_fried_rice.grid(row=4, column=1,)

text_coconut_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_coconut_rice)
text_coconut_rice.grid(row=5, column=1,)

text_spaghetti = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_spaghetti)
text_spaghetti.grid(row=6, column=1,)

text_macaroni = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_macaroni)
text_macaroni.grid(row=7, column=1,)

text_peppersoup = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_peppersoup)
text_peppersoup.grid(row=8, column=1,)

text_pounded_yam = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_pounded_yam)
text_pounded_yam.grid(row=9, column=1,)

text_semo = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_semo)
text_semo.grid(row=10, column=1,)

text_yam = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_yam)
text_yam.grid(row=11, column=1,)

text_chinese_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_chinese_rice)
text_chinese_rice.grid(row=12, column=1,)

# drinks

alomo_bitters = Checkbutton(drink_frame, text="Alomo Bitters", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var14)
alomo_bitters.grid(row=0, column=0, sticky=W)

henessey = Checkbutton(drink_frame, text="Henessey", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var15)
henessey.grid(row=1, column=0, sticky=W)

red_wine = Checkbutton(drink_frame, text="Red wine", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var16)
red_wine.grid(row=2, column=0, sticky=W)

fanta = Checkbutton(drink_frame, text="Fanta", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var17)
fanta.grid(row=3, column=0, sticky=W)

pepsi = Checkbutton(drink_frame, text="Pepsi", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var18)
pepsi.grid(row=4, column=0, sticky=W)

mirinda = Checkbutton(drink_frame, text="Mirinda", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var19)
mirinda.grid(row=5, column=0, sticky=W)

nutri_milk = Checkbutton(drink_frame, text="Nutri Milk", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var20)
nutri_milk.grid(row=6, column=0, sticky=W)

yoghurt = Checkbutton(drink_frame, text="Yoghurt", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var21)
yoghurt.grid(row=7, column=0, sticky=W)

chivita = Checkbutton(drink_frame, text="Chivita", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var22)
chivita.grid(row=8, column=0, sticky=W)

zobo = Checkbutton(drink_frame, text="Zobo", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var23)
zobo.grid(row=9, column=0, sticky=W)

maltina = Checkbutton(drink_frame, text="Maltina", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var24)
maltina.grid(row=10, column=0, sticky=W)

# drink_entry
t_alomo_bitters = Entry(drink_frame, font=("arial", 15, "bold"),bd=7, width=6, state=DISABLED, textvariable=e_alomo_bitters)
t_alomo_bitters.grid(row=0, column=1,)

t_chivita = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_chivita)
t_chivita.grid(row=1, column=1,)

t_zobo = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_zobo)
t_zobo.grid(row=2, column=1,)

t_yoghurt = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_yoghurt)
t_yoghurt.grid(row=3, column=1,)

t_fanta = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_fanta)
t_fanta.grid(row=4, column=1,)

t_pepsi = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_pepsi)
t_pepsi.grid(row=5, column=1,)

t_nutri_milk = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_nutri_milk)
t_nutri_milk.grid(row=6, column=1,)

t_maltina = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_maltina)
t_maltina.grid(row=7, column=1,)

t_red_wine = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_red_wine)
t_red_wine.grid(row=8, column=1,)

t_henessey = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_henessey)
t_henessey.grid(row=9, column=1,)

t_mirinda = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_mirinda)
t_mirinda.grid(row=10, column=1,)

# snacks

shawarma = Checkbutton(snacks_frame, text="sharwama", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var25)
shawarma.grid(row=0, column=0, sticky=W)

pizza = Checkbutton(snacks_frame, text="pizza", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var26)
pizza.grid(row=1, column=0, sticky=W)

puff_puff = Checkbutton(snacks_frame, text="PuffPuff", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var27)
puff_puff.grid(row=2, column=0, sticky=W)

doughnurt = Checkbutton(snacks_frame, text="doughnurt", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var28)
doughnurt.grid(row=3, column=0, sticky=W)

cake = Checkbutton(snacks_frame, text="Caket", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var29)
cake.grid(row=4, column=0, sticky=W)

# snacks_entry

t_doughnurt = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_doughnurt)
t_doughnurt.grid(row=0, column=1,)

t_pizza = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_pizza)
t_pizza.grid(row=1, column=1,)

t_puff_puff = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_puff_puff)
t_puff_puff.grid(row=2, column=1,)

t_shawarma = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_shawarma)
t_shawarma.grid(row=3, column=1,)

t_cake = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_cake)
t_cake.grid(row=4, column=1,)

# costlabels and entry fields

label_cost_food = Label(cost_frame, text="cost of foods",font=('arial', 16, 'bold'))
label_cost_food.grid(row=0, column=0, sticky=W)

label_cost_food = Entry(cost_frame, font=('arial', 16, 'bold'))
label_cost_food.grid(row=0, column=1)

label_cost_drinks = Label(cost_frame, text="cost of drinks",font=('arial', 16, 'bold'))
label_cost_drinks.grid(row=1, column=0, sticky=W)

label_cost_drinks = Entry(cost_frame, font=('arial', 16, 'bold'))
label_cost_drinks.grid(row=1, column=1)

label_cost_snacks = Label(cost_frame, text="cost of snacks",font=('arial', 16, 'bold'))
label_cost_snacks.grid(row=2, column=0)

label_cost_snacks = Entry(cost_frame, font=('arial', 16, 'bold'))
label_cost_snacks.grid(row=2, column=1)

root.mainloop()
