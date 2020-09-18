'''
Created on Aug 17, 2020

@author: rabel
'''
import tkinter

from egyptianMul import EgyptianMu

#create a window
root = tkinter.Tk()
#window size
root.geometry("500x700")
canvas = tkinter.Canvas(root, width = 500, height = 100)
canvas.pack()
root.wm_title("Egyptian Multiplication")

##funtions 

def clearText():
    #function that clears text entries
    s_num.delete(first=0, last=len(s_num.get()))
    f_num.delete(first=0, last=len(f_num.get()))

def multiply():
    try:
        
        n1 = int(f_num.get())
        n2 = int(s_num.get())
        e = EgyptianMu(n1,n2)
        e.createHash()
        r = e.getMul()
        
        res = tkinter.Label(root, text = str(r))
        res.pack()
        res.config(font = ("Times New Roman",20))
        res.place(x = 200, y = 130)
    
    except ValueError:
        clearText()
        res1 = tkinter.Label(root, text = "Wrong Values!", fg = 'red')
        res1.pack()
        res1.config(font = ("Times New Roman",12))
        res1.place(x = 200, y = 130)
    
    finally:
        clearText()   
        

##text boxes and labels
wel_mes = tkinter.Label(root, text = "Please Select Two Numbers")
wel_mes.pack()
wel_mes.config(font = ("Times New Roman",15))
wel_mes.place(x = 140 , y = 10)

f_num_l = tkinter.Label(root, text = "first number:")
f_num_l.pack()
f_num_l.place(x = 10, y = 60)

f_num = tkinter.Entry(root)
f_num.pack()
f_num.place(x = 90, y = 60) 

s_num_l = tkinter.Label(root, text = "second number:")
s_num_l.pack()
s_num_l.place(x = 220, y = 60)

s_num = tkinter.Entry(root)
s_num.pack()
s_num.place(x =320, y = 60) 

##button creation

get_mul = tkinter.Button(root,text = "Multiply", command = multiply)
get_mul.pack()
get_mul.place(x = 200, y = 90)


root.mainloop()