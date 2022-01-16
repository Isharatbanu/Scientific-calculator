#Importing math module and tkinter

from tkinter import *
import math
import tkinter.messagebox

#Title
root = Tk()
root.title("Calculator")

root.configure(background="white")  #menu's background colour

root.geometry("480x568+0+0")   #width x Height + right + Left

#Adding widgets(Frame)
calc = Frame(root)
calc.grid()


#Defining class (calculator)
#Defining functions

class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.ip_val = True
        self.check_sum = False
        self.op = ''
        self.result = False
    
    def numberEnter(self,num):
        self.result = False
        first_num = txtDisplay.get()
        second_num = str(num)
        
        if self.ip_val:
            self.current = second_num
            self.ip_val = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)
    
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
    
    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        elif self.op == 'sub':
            self.total -= self.current
        elif self.op == 'mul':
            self.total *= self.current
        elif self.op == 'div':
            self.total /= self.current
        elif self.op == 'mod':
            self.total %= self.current
        
        self.ip_val = True
        self.check_sum = False
        self.display(self.total)

    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.ip_val = True
        self.check_sum = True
        self.op = op
        self.result = False

    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)

    def clear_entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.ip_val = True

    def back(self):
        current = txtDisplay.get()
        lenght = len(current)-1
        txtDisplay.delete(lenght, END)
            
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def P_M(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
    
    def sq_rt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    
    def log(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)
    
    def exp(self):
        self.result = False
        self.current = math.exp(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
    
    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)

    def abs(self):
        self.result=False
        self.current=math.fabs(float(txtDisplay.get()))
        self.display(self.current)

    def fact(self):
        self.result=False
        self.current=math.factorial(int(txtDisplay.get()))
        self.display(self.current)

    def square(self):
        self.result=False
        self.current=math.pow(float(txtDisplay.get()),2)
        self.display(self.current)

    def inverse(self):
        self.result=False
        self.current=1/(int(txtDisplay.get()))
        self.display(self.current)
   
        
#instance of class calculator
res = Calculator()

#GRID
txtDisplay = Entry(calc,font=('arial',20,'bold'),bd=30,bg='white',width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,'0')

numpad = '789456123'
i=0
btn = []

for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bd=4,text=numpad[i],bg="white"))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command'] = lambda x = numpad [i]:res.numberEnter(x)
        i+=1

#ADDING BUTTONS(standered calculator)
        
Button(calc,text='clear',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.clear_entry).grid(row=1,column=0,pady=1)
Button(calc,text=u'\u232B',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.back).grid(row=1,column=1,pady=1)
Button(calc,text=u'\u221A',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.sq_rt).grid(row=1,column=2,pady=1)
Button(calc,text='+',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = lambda: res.operation('add')).grid(row=1,column=3,pady=1)

Button(calc,text='-',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = lambda: res.operation('sub')).grid(row=2,column=3,pady=1)
Button(calc,text='*',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = lambda: res.operation('mul')).grid(row=3,column=3,pady=1)
Button(calc,text='/',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = lambda: res.operation('div')).grid(row=4,column=3,pady=1)
Button(calc,text='=',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.sum_of_total).grid(row=5,column=3,pady=1)

Button(calc,text='.',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = lambda: res.numberEnter('.')).grid(row=5,column=0,pady=1)
Button(calc,text='0',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = lambda: res.numberEnter(0)).grid(row=5,column=1,pady=1)
Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.P_M).grid(row=5,column=2,pady=1)


#ADDING BUTTONS(scientific calculator)

Button(calc,text='exp',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.exp).grid(row=1,column=4,pady=1)
Button(calc,text='1/x',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.inverse).grid(row=1,column=5,pady=1)
Button(calc,text='fact',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.fact).grid(row=1,column=6,pady=1)

Button(calc,text='sin',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.sin).grid(row=2,column=4,pady=1)
Button(calc,text='cos',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.cos).grid(row=2,column=5,pady=1)
Button(calc,text='tan',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.tan).grid(row=2,column=6,pady=1)


Button(calc,text='tan',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.tan).grid(row=3,column=4,pady=1)
Button(calc,text='mod',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = lambda: res.operation('mod')).grid(row=3,column=5,pady=1)
Button(calc,text='abs',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.abs).grid(row=3,column=6,pady=1)

Button(calc,text='log',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.log).grid(row=4,column=4,pady=1)
Button(calc,text='rad',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.radians).grid(row=4,column=5,pady=1)
Button(calc,text='x\u00b2',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.square).grid(row=5,column=6,pady=1)

Button(calc,text='deg',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.degrees).grid(row=5,column=4,pady=1)
Button(calc,text='e',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.e).grid(row=5,column=5,pady=1)
Button(calc,text=u'\u03C0',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="white",command = res.pi).grid(row=4,column=6,pady=1)


#Adding label as Scientific calculator
lblDisplay = Label(calc, text = "Scientific Calculator",font=('Times',30,'bold'),bg='light blue',fg='navy blue',justify=CENTER)
lblDisplay.grid(row=0, column= 4,columnspan=4)


# menubar functions

def Exit():
    if tkinter.messagebox.askyesno("Calculator","Please Confirm if you want to quit") >0 :
        root.destroy()
        return

def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("860x568+0+0")


def Standard():
    root.geometry("480x568+0+0")

menubar = Menu(calc)

file_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Menu",menu=file_menu)
file_menu.add_command(label="Standard",command=Standard)
file_menu.add_command(label="Scientific calculator",command=Scientific)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=Exit)

root.config(menu=menubar)
root.mainloop()
