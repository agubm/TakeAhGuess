# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:36:35 2021

@author: aguboshimec
"""
import tkinter as tk
import tkinter.tix as tix
import sys
import time
import numpy as np
from random import randint
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog, Tk, Button, Canvas
import tkinter.font as font


root  = tix.Tk()
root.title("#Take-A-Guess")
root.geometry('600x400')
root.iconbitmap('WhatsAppDP.ico')
root.resizable(False, False) #makes window non-resizable

display = Entry(root, state=DISABLED)


def About():
    tk.messagebox.showinfo("About", 
                                'You hopefully had fun\n'
                                ' \n'
                                'Kindly send your feedbacks to:\n'
                                'e.agub@aol.com\n'
                                'Thank you.\n' )
    
def Game_Guide():
    tk.messagebox.showinfo("Game Guide ", 
                                'Hints: Simply guess a number: \n'
                                ' \n'
                                ' easy: between 0 & 1 \n'
                                ' meduim: between 0 & 4 \n'
                                ' hard: between 0 & 9 \n'
                                ' \n' )

def on_closing():
    if messagebox.askokcancel("Exit", "Do you want to exit Game?",  icon = 'warning'):
        root.destroy()
        sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

def close_window(): 
    MsgBox = tk.messagebox.askquestion ('Quit?',"Do you want to quit Game?")
    if MsgBox == 'yes':
       root.destroy()
       sys.exit()
    else:
        tk.messagebox.showinfo('Back to Game',' You will return to the main window')  

#add textbox: 
myentry = Entry(root, text = "?", justify= CENTER, width = 3, font = ('Helvetica', 50), bg="#E3E7FA")
myentry.place(x = 220, y= 140)
myentry.bind("<Key>", lambda e: "break") #disables keyboard strokes


#displays the generated random number
mydisplay = Label(root, justify= CENTER, width = 3, font = ('Helvetica', 50), bg = '#EEEEEF')
mydisplay.place(x = 460, y= 140)
mydisplay.bind("<Key>", lambda e: "break") #disables keyboard strokes


timer_box = Label(root, justify= CENTER, width = 8, font = ('Helvetica', 20), bg = 'white')
timer_box.place(x = 450, y= 40)
timer_box.bind("<Key>", lambda e: "break") #disables keyboard strokes


scores = Label(root, justify= CENTER, width = 8, font = ('Helvetica', 18), bg = '#EEEEEF')
scores.place(x = 450, y= 300)
scores.bind("<Key>", lambda e: "break") #disables keyboard strokes

def button_click(number):
    myentry.delete(0, 'end')
    myentry.insert(0, number)
    return

space = tk.Label(root, text = "", font = "Raleway")
space.grid(column= 0, row= 1)

def press():
    myFont = font.Font(family='Lucida Handwriting', size=15, weight='bold')
    
    b0 = Button(root,text = "0", padx = 30, pady = 10, command = lambda: button_click(0))
    b1 = Button(root,text = "1", padx = 30, pady = 10, command = lambda: button_click(1))
    b2 = Button(root,text = "2", padx = 30, pady = 10, command = lambda: button_click(2))
    b3 = Button(root,text = "3", padx = 30, pady = 10, command = lambda: button_click(3))
    b4 = Button(root,text = "4", padx = 30, pady = 10, command = lambda: button_click(4))
    b5 = Button(root,text = "5", padx = 30, pady = 10, command = lambda: button_click(5))
    b6 = Button(root,text = "6", padx = 30, pady = 10, command = lambda: button_click(6))
    b7 = Button(root,text = "7", padx = 30, pady = 10, command = lambda: button_click(7))
    b8 = Button(root,text = "8", padx = 30, pady = 10, command = lambda: button_click(8))
    b9 = Button(root,text = "9", padx = 30, pady = 10, command = lambda: button_click(9))
    
    b0['font'] = myFont
    b1['font'] = myFont
    b2['font'] = myFont
    b3['font'] = myFont
    b4['font'] = myFont
    b5['font'] = myFont
    b6['font'] = myFont
    b7['font'] = myFont
    b8['font'] = myFont
    b9['font'] = myFont
    
    #place buttons on screen:
    b0.grid(row =3 , column = 1)
    b1.grid(row =3 , column = 2)
    b2.grid(row =4 , column = 1)
    b3.grid(row =4 , column = 2)
    b4.grid(row =5 , column = 1)
    b5.grid(row =5 , column = 2)
    b6.grid(row =6 , column = 1)
    b7.grid(row =6 , column = 2)
    b8.grid(row =7 , column = 1)
    b9.grid(row =7 , column = 2)

press()

t = 3
def delete_entry():
    global t
    t = 3
    myentry.delete(0, 'end')
    mydisplay.config(text = "")
    countdown()
    press()
 
# timer function call 
point = 0
def countdown():
    global t, point
    if t>0:
        mydisplay.config(text = " ? ")
        timer_box.config(text = ("{}{}".format('00:0', t)), fg = 'green')
        t = t - 1
        timer_box.after(1000, countdown)
        
    elif t ==0:
        print ("end")
        timer_box.config(text = "00:00", fg = 'red' )         
        #displays random numbers:
        #generate random numbers:
        random_number = int(np.random.randint(low=0, high=max_val, size=(1,)))     
        mydisplay.config(text = random_number)
        
        number = myentry.get()
        if len(myentry.get()) == 0:  # empty!
            number = int(100)
        elif len(myentry.get()) > 0:
            number = int(myentry.get())
            #print (number)
        #print (len(myentry.get()))
        
        
        if number == random_number:
            point = point + 5
            
            scores.config(text = ("{}{}".format('Points: ', point)), fg = 'black')
            #print (point) 
        else:
            point = point
            #print(point)  
        
       
        #if point == 30:
           # print("excellent job!")
            
def clicked(value):
    global max_val 
    max_val = value
    print (max_val)
    return max_val


 #makes the Start_Game timer to start ticking            
def Start_countdown():
    global t
    if t>0:
        mydisplay.config(text = " ? ")
        timer_box.config(text = ("{}{}".format('00:0', t)), fg = 'green')
        t = t - 1
        timer_box.after(1000, countdown)
    elif t ==0:
        print ("end")
        timer_box.config(text = "00:00", fg = 'red' )         
        #displays random numbers:
        #generate random numbers:
        random_number = int(np.random.randint(low=0, high= max_val, size=(1,)))     
        mydisplay.config(text = random_number)

#call the Start_Game button function.       
def startgame():  
    
    global t, point, int_point
    int_point = 0
    point = int_point
    t = 3
    myentry.delete(0, 'end')
    mydisplay.config(text = " ")
    scores.config(text = ("{}{}".format('Points: ', point)), fg = 'black')
    time.sleep(0.3)
    Start_countdown()
    press()

   

# create balloon (tooltip) instance
balloon = tix.Balloon(root)
    
#button to continue:
button1 = Button(root, text="Continue",bg='#0052cc', fg='#ffffff', command = delete_entry)
button1.place(relx=0.46, rely= 0.68, anchor=CENTER, height=30, width=100)

#start button
button2 = Button(root, text=">> start >>",fg='#ffffff', bg='#14941C', command = startgame)
button2.place(x = 280, y= 60, anchor=CENTER, height=30, width=100)


# bind balloon to buttons
balloon.bind_widget(button2, balloonmsg='start new game')

menubar = tk.Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game", command= startgame)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=close_window)



menubar.add_cascade(label="File", menu=filemenu)
    
submenu = tk.Menu(menubar)
sb1 = submenu.add_radiobutton(label="easy",value = 2, command = lambda: clicked(2)) #max value intiated to 2-1
sb2 = submenu.add_radiobutton(label="medium", value = 5, command = lambda: clicked(5)) #max value intiated to 5-1
submenu.add_radiobutton(label="hard",  value = 10, command = lambda: clicked(10)) #max value intiated to 10-1

menubar.add_cascade(label="Level", menu=submenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=About)
helpmenu.add_command(label="Guide", command=Game_Guide)
menubar.add_cascade(label="Help", menu=helpmenu)


inst_label = tk.Label(root, text= "more correct guesses, more points!", justify = CENTER, fg='#0B0766')
inst_label.config(font=("Chiller", 14))
inst_label.place(relx=0.63, rely= 0.88, height=30, width=220)


root.config(menu=menubar)

clicked(2) # this make the difficult level to  be at easy, ie. value = 5

root.mainloop() #end of window


