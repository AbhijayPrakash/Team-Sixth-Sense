from tkinter import *
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
import numpy as np
import time
messagebox.showinfo('Introduction', '''You are a concerned citizen trying to make a positive impact on the environment.
You have a limited budget and must make choices to save the planet.
You have to lower the AQI to 0 and make 1000$ to win! Hope you have fun!!!''')
budget = 1000
win = Tk()
win.geometry('550x250')
win.title('Save the Enviroment')
#button/text
menubar = Menu(win)
win.config(menu=menubar)
a = [0, 1]
b = [500, 500]
def com1():
    global abc
    global budget
    if budget < 20:
        messagebox.showerror('Error', 'Not enough budget to plant a tree!')
        if budget == 0 or budget == 10:
            time.sleep(1)
            if budget == 0 or budget == 10:
                abc = messagebox.askretrycancel('You failed!', 'Do you want to try again?')
                if abc == True:
                    budget = 1020
                    f.config(text=(str(budget) + '$'))
                    a.clear()
                    b.clear()
                    a.append(0)
                    a.append(0)
                    b.append(500)
                    b.append(500)
                    
    budget -= 20
    a.append(a[-1] + 1)
    b.append(b[-1] - 5)
    xpoints = np.array(a)
    ypoints = np.array(b)
    plt.xlabel('Money spent:')
    plt.ylabel('AQI')
    plt.plot(xpoints, ypoints, 'o')
    plt.show()
    f.config(text=(str(budget) + ' $'))



    plt.plot(xpoints, ypoints, 'o')
    plt.show()
def decrease_budget_and_append():
    global budget
    a.append(a[-1] + 1)
    b.append(b[-1] - 5)
    budget -= 200
    func1()
def decrease_budget_and_append2():
    global budget
    a.append(a[-1] + 200)
    b.append(b[-1] - 30)
    budget -= 200
    func1()
def decrease_budget_and_append3():
    global budget
    a.append(a[-1] + 50)
    b.append(b[-1] - 15)
    budget -= 50
    func1()
def decrease_budget_and_append4():
    global budget
    a.append(a[-1] + 800)
    b.append(b[-1] - 175)
    budget -= 800
    func1()
def comm2():
    global budget
    budget += 1
    f.config(text=(str(budget) + '$'))
    win.after(1000, comm2)

def com2():
    global abc
    global budget
    if budget >= 200:
        decrease_budget_and_append2()
        comm2()
    else:
        messagebox.showerror('Error', 'Not enough budget to install a solar panel!')
        if budget == 0 or budget == 10:
            time.sleep(1)
        if budget == 0 or budget == 10:
            abc = messagebox.askretrycancel('You failed!', 'Do you want to try again?')
            if abc == True:
                budget = 1000
                f.config(text=(str(budget) + '$'))
                a.clear()
                b.clear()
                a.append(0)
                a.append(0)
                b.append(500)
                b.append(500)
    xpoints = np.array(a)
    ypoints = np.array(b)
    plt.xlabel('Money spent:')
    plt.ylabel('AQI')
    plt.plot(xpoints, ypoints, 'o')
    plt.show()

def com3():
    global abc
    global budget
    if budget >= 50:
        decrease_budget_and_append3()
        f.config(text=(str(budget) + '$'))
        func1()
    else:
        messagebox.showerror('Error', 'Not enough budget to reduce plastic waste!')
        if budget == 0 or budget == 10:
            time.sleep(1)
        if budget == 0 or budget == 10:
            abc = messagebox.askretrycancel('You failed!', 'Do you want to try again?')
            if abc == True:
                budget = 1000
                f.config(text=(str(budget) + '$'))
                a.clear()
                b.clear()
                a.append(0)
                a.append(0)
                b.append(500)
                b.append(500)
           
            
def com4():
    global budget
    if budget >= 800:
        a.append(a[-1] + 800)
        b.append(b[-1] - 175)
        for i in range(0, 5):
            comm2()
        budget -= 800
        f.config(text=(str(budget) + '$'))
        func1()
    else:
        messagebox.showerror('Error', 'Not enough budget to use electric cars!')
        if budget == 0 or budget == 10:
            time.sleep(1)
        if budget == 0 or budget == 10:
            abc = messagebox.askretrycancel('You failed!', 'Do you want to try again?')
            if abc == True:
                budget = 1000
                f.config(text=(str(budget) + '$'))
                a.clear()
                b.clear()
                a.append(0)
                a.append(0)
                b.append(500)
                b.append(500)
                

def func1():
    xpoints = np.array(a)
    ypoints = np.array(b)

    plt.plot(xpoints, ypoints, 'o')
    plt.show()

menubar.add_command(label='Plant a Tree (20$)', command=com1)
menubar.add_command(label='Install a Solar Panel (200$)‎', command=com2)
menubar.add_command(label='Reduce Plastic Waste‎ (50$)', command=com3)
menubar.add_command(label='Use Electric Cars (800$)', command=com4)
E = Label(win,text = 'Do the following to save the enviroment')
f = Label(win, text=(str(budget) + ' $'), font=('Arial', 80, 'bold'))
def func2():
    print(budget)
f.pack()
E.pack()

xpoints = np.array([0, 0])
ypoints = np.array([500, 500])

plt.xlabel('Money spent:')
plt.ylabel('AQI')
plt.plot(xpoints, ypoints, 'o')
plt.show()
def control(n):
    abc = messagebox.askretrycancel('You failed!', 'Do you want to try again?')
    if abc == True:
           
        KeyboardInterrupt()
        budget = 1000
    else:
        pass
window.bind('<Return>', control)
while b[-1] > 0 and budget < 1000:
    pass
else:
    messagebox.showerror('Congratulations!!!! You won!!!')


