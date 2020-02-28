from tkinter import *
#from tkinter import messagebox
  
root = Tk()  
  
root.geometry("610x400")
root.title(70*' ' + 'Food ordering System')
root.configure(background='green')
root.resizable(0, 0)

list_order_price = []
def home_page():
    lbl.destroy()
    Instructions.destroy()
    btn.destroy()

    def order_dish():
        drink.destroy()
        meal.destroy()
        dish_button.destroy()
        lb.destroy()

        lbl1=Label(root, text="Thanks for selecting dish", fg='white', bg = 'green', font=("Helvetica", 16))
        lbl1.pack(padx=20, pady=20)

        L1 = Label(root, text="Enter Meal Name", bg = 'green', fg = 'white')
        L1.pack(padx=4, pady=4)

        E1 = Entry(root, bd =5)
        E1.pack(padx=4, pady=4)

        L2 = Label(root, text="Enter Quantity(int)", bg = 'green', fg = 'white')
        L2.pack(padx=4, pady=4)
        
        E2 = Entry(root, bd =5)
        E2.pack(padx=4, pady=4)

        L3 = Label(root, text="Enter Price Range", bg = 'green', fg = 'white')
        L3.pack(padx=4, pady=4)
    
        E3 = Entry(root, bd =5)
        E3.pack(padx=4, pady=4)

        def submit_dish():
            a = int(E2.get())*float(E3.get())
            #h = 6
            list_order_price.append(a)
            lbl2=Label(root, text="Is the order final?", fg='white', bg = 'green', font=("Helvetica", 16))
            lbl2.pack()
                        
            def back_to_menu():
                home_page()
                lbl1.destroy()
                lbl2.destroy()
                E1.destroy()
                L1.destroy()
                E2.destroy()
                L2.destroy()
                E3.destroy()
                L3.destroy()
                            
                submit.destroy()
                ReturnMenuFunc.destroy()
                final_order.destroy()                     
                            
            ReturnMenuFunc = Button(root, text="No", command = back_to_menu, bg = 'yellow')
            ReturnMenuFunc.pack()
            ReturnMenu = ReturnMenuFunc
            ReturnMenu.pack()

        submit = Button(root, text ="Order Now", command=submit_dish, bg = 'yellow')
        submit.pack(padx=5, pady=5)

    def order_Drink():
        drink.destroy()
        meal.destroy()
        dish_button.destroy()
        lb.destroy()

        lbl1=Label(root, text="Thanks for selecting Drink", fg='white', bg = 'green', font=("Helvetica", 16))
        lbl1.pack(padx=20, pady=20)

        L1 = Label(root, text="Enter Meal Name", bg = 'green', fg = 'white')
        L1.pack(padx=4, pady=4)
        E1 = Entry(root, bd =5)
        E1.pack(padx=4, pady=4)

        L2 = Label(root, text="Enter Quantity", bg = 'green', fg = 'white')
        L2.pack(padx=4, pady=4)
        E2 = Entry(root, bd =5)
        E2.pack(padx=4, pady=4)

        L3 = Label(root, text="Enter Price", bg = 'green', fg = 'white')
        L3.pack(padx=4, pady=4)
        E3 = Entry(root, bd =5)
        E3.pack(padx=4, pady=4)
        
        def submit_drink():
            b = int(E2.get())*float(E3.get())
            list_order_price.append(b)
            lbl2=Label(root, text="Is the order final?", fg='white', bg = 'green', font=("Helvetica", 16))
            lbl2.pack()

            def back_to_menu():
                home_page()
                lbl1.destroy()
                lbl2.destroy()
                E1.destroy()
                L1.destroy()
                E2.destroy()
                L2.destroy()
                E3.destroy()
                L3.destroy()
                submit.destroy()
                ReturnMenuFunc.destroy()
                final_order.destroy()
                
            ReturnMenuFunc = Button(root, text="No", command = back_to_menu, bg = 'yellow')
            ReturnMenuFunc.pack()
            ReturnMenu = ReturnMenuFunc
            ReturnMenu.pack()

        submit = Button(root, text ="Order Now", command=submit_drink)
        submit.pack()

        
    def order_Combo_meal():
        drink.destroy()
        meal.destroy()
        dish_button.destroy()
        lb.destroy()

        lbl1=Label(root, text="Thanks for selecting Meal", fg='white', bg = 'green', font=("Helvetica", 16))
        lbl1.pack(padx=20, pady=20)

        L1 = Label(root, text="Enter Meal Name", bg = 'green', fg = 'white')
        L1.pack(padx=4, pady=4)
        E1 = Entry(root, bd =5)
        E1.pack(padx=4, pady=4)

        L2 = Label(root, text="Enter Quantity", bg = 'green', fg = 'white')
        L2.pack(padx=4, pady=4)
        E2 = Entry(root, bd =5)
        E2.pack(padx=4, pady=4)

        L3 = Label(root, text="Enter Price", bg = 'green', fg = 'white')
        L3.pack(padx=4, pady=4)
        E3 = Entry(root, bd =5)
        E3.pack(padx=4, pady=4)
        

        def submit_meal():
            c = int(E2.get())*float(E3.get())
            list_order_price.append(c)
            lbl2=Label(root, text="Is the order final?", fg='white', bg = 'green', font=("Helvetica", 16))
            lbl2.pack()
            

            def back_to_menu():
                home_page()
                lbl1.destroy()
                lbl2.destroy()
                E1.destroy()
                L1.destroy()
                E2.destroy()
                L2.destroy()
                E3.destroy()
                L3.destroy()
                submit.destroy()
                ReturnMenuFunc.destroy()
                final_order.destroy()
                
            ReturnMenuFunc = Button(root, text="No", command = back_to_menu, bg = 'yellow')
            ReturnMenuFunc.pack()
            ReturnMenu = ReturnMenuFunc
            ReturnMenu.pack()

        submit = Button(root, text ="Order Now", command=submit_meal)
        submit.pack()

    def final_order():
        result = sum(list_order_price)
        v1 = StringVar()
        v2 = StringVar()
        Label(root, textvariable=v2, bg = "green", fg = "white", font=("Helvetica", 10)).place(x=400, y=170)
        Label(root, textvariable=v1, bg = "green", fg = "white", font=("Helvetica", 10)).place(x=400, y=190)
        v2.set("Thanks your order is confirmed!")
        v1.set("Your total order price is!"+ " " +str(result))

    def exit_window():
        root.destroy()

    final_order = Button(root, text="Final_order", command = final_order, bg = 'yellow')
    final_order.place(x = 230, y=360)

    exit_window = Button(root, text="Exit_window", command = exit_window, bg = 'yellow')
    exit_window.place(x = 310, y=360)
                    
        
    lb=Label(root, text="OrderMenu", fg='white', bg = 'green', font=("Helvetica", 16))
    lb.pack(padx=20, pady=20)

    dish_button = Button(root, text="order drink", command = order_Drink, bg = 'yellow', padx=8, pady=4)
    dish_button.pack(padx=8, pady=8)

    drink = Button(root, text="order dish", command = order_dish, bg = 'yellow', padx=8, pady=4)
    drink.pack(padx=8, pady=8)

    meal = Button(root, text="order meal", command = order_Combo_meal, bg = 'yellow', padx=8, pady=4)
    meal.pack(padx=8, pady=8)

    
  
lbl=Label(root, text="Welcome to online ordering system", fg='white', bg = 'green', font=("Helvetica", 16))
lbl.pack(padx=20, pady=20)

Instructions = Label(root, text=""" Choose order by clicking on order menu""",fg="black", font=("Calibri", 14))
Instructions.pack(padx=10, pady=10)

btn = Button(root, text = "Go to order menu", command = home_page, bg = 'yellow')  
  
btn.pack(padx=75, pady=75)
  
root.mainloop()  
