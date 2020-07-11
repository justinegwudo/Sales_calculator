from tkinter import *
import random
import time
import math

root = Tk()
root.geometry("1600x800+0+0")
root.title("Sales Management System")

text_Input = StringVar()
operator = ""

# Header frame/container
Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

# Left frame/container
f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# right frame/container
f2 = Frame(root, width=300, height=700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

# Get local time
localtime = time.asctime(time.localtime(time.time()))

# Header content
lblinfo = Label(Tops, font=("arial", 50, "bold"), text="Sales Management Systems", fg="steel blue", bd=10, anchor="w")
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=("arial", 20, "bold"), text=localtime, fg="steel blue", bd=10, anchor="w")
lblinfo.grid(row=1, column=0)


# calc
def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF = int(Fries.get())
    CoB = int(Burger.get())
    CoE = int(Eba.get())
    CoD = int(Drinks.get())
    CoO = int(Okra.get())
    CoV = int(Vegetable.get())



    CostofFries = CoF * 599.99
    CostofBurger = CoB * 2599.99
    CostofEba = CoE * 599.00
    CostofDrink = CoD * 599.99
    CostofOkra = CoO * 2499.99
    CostofVegetable = CoV * 2199.99

    CostofMeal = "N", str("%.2f" % (CostofFries + CostofBurger + CostofEba + CostofDrink + CostofOkra + CostofVegetable))
    PayTax = ((CostofFries + CostofBurger + CostofEba + CostofDrink + CostofOkra + CostofVegetable) * 0.2)
    TotalCost = (CostofFries + CostofBurger + CostofEba + CostofDrink + CostofOkra + CostofVegetable)
    Ser_Charge = ((CostofFries + CostofBurger + CostofEba + CostofDrink + CostofOkra + CostofVegetable) / 99)
    Service = "N", str("%.2f" % Ser_Charge)
    OverAllCost = "N", str("%.2f" % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "N", str("%.2f" % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    rand.set(0)
    Fries.set(0)
    Burger.set(0)
    Eba.set(0)
    SubTotal.set(0)
    Total.set(0)
    Service_Charge.set(0)
    Drinks.set(0)
    Tax.set(0)
    Cost.set(0)
    Okra.set(0)
    Vegetable.set(0)


txtDisplay = Entry(f2, font=("arial", 20, "bold"), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue",
                   justify="right")
txtDisplay.grid(columnspan=4)

# buttons in column
btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="7", bg="powder blue",
              command=lambda: btnClick(7)).grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="8", bg="powder blue",
              command=lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="9", bg="powder blue",
              command=lambda: btnClick(9)).grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="+", bg="powder blue",
                  command=lambda: btnClick("+")).grid(row=2, column=3)

#
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="4", bg="powder blue",
              command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="5", bg="powder blue",
              command=lambda: btnClick(4)).grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="6", bg="powder blue",
              command=lambda: btnClick(4)).grid(row=3, column=2)

subtract = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="-", bg="powder blue",
                  command=lambda: btnClick("-")).grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="1", bg="powder blue",
              command=lambda: btnClick(1)).grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="2", bg="powder blue",
              command=lambda: btnClick(2)).grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="3", bg="powder blue",
              command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="*", bg="powder blue",
                  command=lambda: btnClick("*")).grid(row=4, column=3)

#
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="0", bg="powder blue",
              command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="c", bg="powder blue",
                  command=btnClearDisplay).grid(row=5, column=1)

btnEquals = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="=", bg="powder blue",
                   command=btnEqualsInput).grid(row=5, column=2)

division = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="/", bg="powder blue",
                  command=lambda: btnClick("/")).grid(row=5, column=3)

# majority of the left of the side
rand = IntVar()
Fries = IntVar()
Burger = IntVar()
Eba = IntVar()
SubTotal = IntVar()
Total = IntVar()
Service_Charge = IntVar()
Drinks = IntVar()
Tax = IntVar()
Cost = IntVar()
Okra = IntVar()
Vegetable = IntVar()

# reference
lblReference = Label(f1, font=("arial", 16, "bold"), text="Reference", bd=16, anchor="center")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=("arial", 16, "bold"), textvariable=rand, bd=16, insertwidth=4, bg="powder blue",
                     justify="right")
txtReference.grid(row=0, column=1)

# fries
lblFries = Label(f1, font=("arial", 16, "bold"), text="Large Fries", bd=16, anchor="center")
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=("arial", 16, "bold"), textvariable=Fries, bd=16, insertwidth=4, bg="powder blue",
                 justify="right")
txtFries.grid(row=1, column=1)

# Burger
lblBurger = Label(f1, font=("arial", 16, "bold"), text="Burger Meal", bd=16, anchor="center")
lblBurger.grid(row=2, column=0)
txtBurger = Entry(f1, font=("arial", 16, "bold"), textvariable=Burger, bd=16, insertwidth=4, bg="powder blue",
                  justify="right")
txtBurger.grid(row=2, column=1)

# Eba
lblEba = Label(f1, font=("arial", 16, "bold"), text="Eba", bd=16, anchor="center")
lblEba.grid(row=3, column=0)
txtEba = Entry(f1, font=("arial", 16, "bold"), textvariable=Eba, bd=16, insertwidth=4, bg="powder blue",
               justify="right")
txtEba.grid(row=3, column=1)

# Okra soup
lblOkra = Label(f1, font=("arial", 16, "bold"), text="Okra", bd=16, anchor="center")
lblOkra.grid(row=4, column=0)
txtOkra = Entry(f1, font=("arial", 16, "bold"), textvariable=Okra, bd=16, insertwidth=4, bg="powder blue",
                justify="right")
txtOkra.grid(row=4, column=1)

# Vegetable soup
lblVegetable = Label(f1, font=("arial", 16, "bold"), text="Vegetable Soup", bd=16, anchor="center")
lblVegetable.grid(row=4, column=0)
txtVegetable = Entry(f1, font=("arial", 16, "bold"), textvariable=lblVegetable, bd=16, insertwidth=4, bg="powder blue",
                     justify="right")
txtVegetable.grid(row=4, column=1)

# Second block of items
# Drink
lblDrinks = Label(f1, font=("arial", 16, "bold"), text="Drinks", bd=16, anchor="center")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=("arial", 16, "bold"), textvariable=Drinks, bd=16, insertwidth=4, bg="powder blue",
                  justify="right")
txtDrinks.grid(row=0, column=3)

# Cost
lblCost = Label(f1, font=("arial", 16, "bold"), text="Cost of Meal", bd=16, anchor="center")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=("arial", 16, "bold"), textvariable=Cost, bd=16, insertwidth=4, bg="powder blue",
                justify="right")
txtCost.grid(row=1, column=3)

# Service
lblService = Label(f1, font=("arial", 16, "bold"), text="Service Charge", bd=16, anchor="center")
lblService.grid(row=2, column=2)
txtService = Entry(f1, font=("arial", 16, "bold"), textvariable=Service_Charge, bd=16, insertwidth=4, bg="powder blue",
                   justify="right")
txtService.grid(row=2, column=3)

# Tax
lblTax = Label(f1, font=("arial", 16, "bold"), text="Tax", bd=16, anchor="center")
lblTax.grid(row=3, column=2)
txtTax = Entry(f1, font=("arial", 16, "bold"), textvariable=Tax, bd=16, insertwidth=4, bg="powder blue",
               justify="right")
txtTax.grid(row=3, column=3)

# SubTotal
lblSubTotal = Label(f1, font=("arial", 16, "bold"), text="Sub Total", bd=16, anchor="center")
lblSubTotal.grid(row=4, column=3)
txtlblSubTotal = Entry(f1, font=("arial", 16, "bold"), textvariable=SubTotal, bd=16, insertwidth=4, bg="powder blue",
                       justify="right")
txtlblSubTotal.grid(row=4, column=3)

# Total
lblTotalCost = Label(f1, font=("arial", 16, "bold"), text="Total Cost", bd=16, anchor="center")
lblTotalCost.grid(row=4, column=2)
txtTotalCost = Entry(f1, font=("arial", 16, "bold"), textvariable=Total, bd=16, insertwidth=4, bg="powder blue",
                     justify="right")
txtTotalCost.grid(row=4, column=3)

# Buttons
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Total",
                  bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Reset",
                  bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Exit",
                 bg="powder blue", command=qExit).grid(row=7, column=3)

root.mainloop()