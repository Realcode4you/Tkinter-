from tkinter import *
import sqlite3
import os
from tkinter import messagebox

root = Tk()
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
 
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)



#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
 
def HomeWindow():
    #lbl.destroy()
    #Instructions.destroy()
    #btn.destroy()   
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    
    

    def home_page():
        lbl.destroy()
        Instructions.destroy()
        btn.destroy()
        
        def order_Drink():
            pass

        def order_dish():
            drink.destroy()
            meal.destroy()
            dish_button.destroy()
            lb.destroy()

            lbl1=Label(Home, text="Thanks for selecting dish", fg='white', bg = 'green', font=("Helvetica", 16))
            lbl1.pack(padx=20, pady=20)

            L1 = Label(Home, text="Enter Meal Name", bg = 'green', fg = 'white')
            L1.pack(padx=4, pady=4)

            E1 = Entry(Home, bd =5)
            E1.pack(padx=4, pady=4)

            L2 = Label(Home, text="Enter Quantity", bg = 'green', fg = 'white')
            L2.pack(padx=4, pady=4)
            E2 = Entry(Home, bd =5)
            E2.pack(padx=4, pady=4)
            
            L3 = Label(Home, text="Enter Price", bg = 'green', fg = 'white')
            L3.pack(padx=4, pady=4)

            E3 = Entry(Home, bd =5)
            E3.pack(padx=4, pady=4)

            def submit_dish():
                c = float(E2.get())*float(E3.get())
                #print(c)
                lbl2=Label(Home, text="Is the order final?", fg='white', bg = 'green', font=("Helvetica", 16))
                lbl2.pack()
            
                def order_confirm():
                    v = StringVar()
                    Label(Home, textvariable=v, bg = "green", fg = "white", font=("Helvetica", 10)).place(x=400, y=170)
                    v.set("Your total order price is!"+ " " +str(c))
                    #messagebox.showinfo('Press ok to confirm and exit')
                    #Home.destroy()
                    
                def back_to_menu():
                    HomeWindow()
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

                ReturnMenuFunc = Button(Home, text="No", command = back_to_menu, bg = 'yellow')
                ReturnMenuFunc.pack()
                final_order = Button(Home, text="Yes", command = order_confirm, bg = 'yellow')
                final_order.pack(padx=2, pady=2)
                ReturnMenu = ReturnMenuFunc
                ReturnMenu.pack()
            

            submit = Button(Home, text ="Order Now", command=submit_dish)
            submit.pack() 

        def order_Combo_meal():
            pass

        

        lb=Label(Home, text="OrderMenu", fg='white', bg = 'green', font=("Helvetica", 16))
        lb.pack(padx=20, pady=20)
        dish_button = Button(Home, text="order drink", command = order_Drink, bg = 'yellow', padx=8, pady=4)
        dish_button.pack(padx=8, pady=8)
        drink = Button(Home, text="order dish", command = order_dish, bg = 'yellow', padx=8, pady=4)
        drink.pack(padx=8, pady=8)
        meal = Button(Home, text="order meal", command = order_Combo_meal, bg = 'yellow', padx=8, pady=4)
        meal.pack(padx=8, pady=8)
   
    
    lbl=Label(Home, text="Welcome to online ordering system", fg='white', bg = 'green', font=("Helvetica", 16))
    lbl.pack(padx=20, pady=20)

    Instructions = Label(Home, text=""" Choose order from menu """,fg="black", font=("Calibri", 14))
    Instructions.pack(padx=10, pady=10)

    btn = Button(Home, text = "Go to order menu", command = home_page, bg = 'yellow')  
      
    btn.pack(padx=75, pady=75)
    btn_logout = Button(Home, text='Logout', command=Logout).place(x=500, y=25)
     
def Logout():
    Home.destroy()
    root.deiconify()

 
#==============================LABELS=========================================
lbl_title = Label(Top, text = "Python: Simple Login Application", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================
btn_login=Button(Form, text="Login", width=45, bg="blue", command = Login)
#btn_login = Button(Form, text="Login", width=45, command=Login_user)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)


#==============================INITIALIATION==================================
if __name__ == '__main__':
    root.mainloop()
