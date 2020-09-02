from tkinter import *
#importing tkinter

from datetime import datetime
#inporting datetime module to have access over time.

counter = 66600
#initilizing the counter value to 66600

run=False
#Setting a variable with Bool False

def counter_label(label):
    def count():
        if run:
        #Checks for True or False.
            global counter
            if counter == 66600:
                display = "Starting..."
                #Displays Staring for a while
            else:
                t=datetime.fromtimestamp(counter)
                #getting time and date
                
                s = t.strftime("%H:%M:%S")
                #converting the time in string
                display = s
                #Assigning s in display
            
            label['text'] = display
            #Time run in the label of tkinter window
            
            label.after(1000,count)
            #After 1 sec it repeats again.
            
            counter+=1
            #It is incremented to break the if condition.
    count()

def Start(label):
    global run
    #Global variable
    
    run = True
    counter_label(label)
    #Function call
    
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    #States of the button

def Stop():
    global run
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    #States of the button
    
    run = False
    #Setting the run value to False

def Reset():
    global counter
    counter = 66600
    if run == False:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
        #Setting the label value as 00:00:00 to be displayed.
    else:
        label['text'] = 'Starting...'
        #Setting the label value as 00:00:00 to be displayed.

m=Tk()
#Assigning Tkinter window root variable

m.title("StopWatch")
#Title for tkinter window.

label = Label(m, text="00:00:00",fg="black",font=("Arial",15))
label.pack()
#Creating label to display the stopwatch time in the tkinter window.

f=Frame(m)
#creating frame for tkinter window

start = Button(m, text="Start", width=12, height=2, command=lambda : Start(label))
#creating start button with the function call Start and an argument label.

stop = Button(m, text="Stop", width=12,height=2,state="disabled",command = Stop)
#creating Stop button with the function call Stop.
#Setting the button disabled initially.

reset = Button(m, text="Reset", width=12, height=2, state="disabled", command=lambda:Reset())
#Creating Reser button with the function call Reset()
#Setting the button disabled intially.

f.pack(anchor="center", pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
#arranging the button in the tkinter window

m.mainloop()
#Tkinter window completes with mainloop.
