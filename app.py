from tkinter import *
import time
import asyncio

ws = Tk()
ws.geometry('350x400+1000+300')
ws.title('Work Timer')
ws.config(bg='black')
ws.resizable(height=False,width=False)

counter = -1
running = False
def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter==-1:             
                display="0"
            else:
                display=str(counter)

            lbl['text']=time.strftime('%H:%M:%S', time.gmtime(int(display)))    
            
            CalculateValues(counter)
            lbl.after(1000, count)    
            counter += 1
    count()     

def Count(lblCount):
    count = lblCount['text']
    countIncremented = int(count) + 1
    lblCount['text'] = countIncremented

def CountDecrement(lblCount):
    count = lblCount['text']
    countIncremented = int(count) - 1
    lblCount['text'] = countIncremented

def StartTimer(lbl):
    global running
    running=True
    counter_label(lbl)
    tap_btn['state'] = 'normal'
    tapDown_btn['state'] = 'normal'
    start_btn['state']='disabled'
    stop_btn['state']='normal'
    reset_btn['state']='normal'

def StopTimer():
    global running
    start_btn['state']='normal'
    stop_btn['state']='disabled'
    reset_btn['state']='normal'
    running = False

def ResetTimer(lbl, lblCount):
    global counter
    counter=-1
    if running==False:      
        reset_btn['state']='disabled'
        lbl['text']='0'
    else:                          
        lbl['text']=''
        lblCount['text']='0'

def CalculateValues(seconds):
    timeValue = e1.get()
    hours = seconds / 3600
    lblExpected['text'] = round(float(hours) * float(timeValue), 2)
    label_countDiff['text'] = round(float(label_count['text']) - round(float(hours) * float(timeValue), 2), 2)

label_time = Label(
    ws, 
    text="0", 
    fg="white", 
    bg='black', 
    font="Verdana 30 bold"
    )

label_count = Label(
    ws, text="0", 
    fg="white", 
    bg='black', 
    font="Verdana 40 bold"
)

label_countDiff = Label(
    ws, text="0", 
    fg="white", 
    bg='black', 
    font="Verdana 40 bold"
)

label_countDiffLabel = Label(
    ws, text="Diff    Exp.", 
    fg="white", 
    bg='black', 
    font="Verdana 40 bold"
)
label_countDiffLabel.place(x=10, y=10)
label_count.place(x=10, y=180)
label_countDiff.place(x=10, y=70)

label_time.place(x=150, y=190)

start_btn=Button(
    ws, 
    text='Start', 
    width=15, 
    command=lambda:StartTimer(label_time)
    )

stop_btn = Button(
    ws, 
    text='Stop', 
    width=15, 
    state='disabled', 
    command=StopTimer
    )

reset_btn = Button(
    ws, 
    text='Reset', 
    width=15, 
    state='disabled', 
    command=lambda:ResetTimer(label_time, label_count)
    )

tap_btn = Button(
    ws, 
    text='Count Up', 
    width=20, 
    bg='white',
    height=5, 
    state='disabled', 
    command=lambda:Count(label_count)
)

tapDown_btn = Button(
    ws, 
    text='Count Down', 
    width=20, 
    height=4,
    bg='white',
    state='disabled', 
    command=lambda:CountDecrement(label_count)
)

lblExpected = Label(
    ws, 
    text="0", 
    fg="white", 
    bg='black', 
    font="Verdana 40 bold"
    )
lblExpected.place(x=185, y=70)

e1 = Entry(ws)

e1.grid(row=0, column=1)
e1.insert(10, '70')
start_btn.place(x=0, y=340)
stop_btn.place(x=120, y=340)
reset_btn.place(x=240, y=340)
tap_btn.place(x=0, y=250)
tapDown_btn.place(x=200, y=260)

ws.mainloop()