import tkinter
import time

root = tkinter.Tk()
root.title('Stopwatch')
root.geometry("400x200+300+200")
frame1 = tkinter.Frame(root)
frame1.pack()
timestr = tkinter.StringVar()
timestr.set('0:0')

running = False
starttime = 0
elapsedtime = 0.0
timer = None

def update():
    global elapsedtime
    global timestr
    global timer
    elapsedtime = time.time() - starttime
    timestr.set(elapsedtime)
    timer = root.after(50,update)
    
def Start():
    global running
    global starttime
    if not running:
        starttime = time.time() - elapsedtime
        running = True
        update()
        pass

def Stop():
    global running
    global timer
    if running:
        root.after_cancel(timer)
        elapsedtime = time.time() - starttime
        timestr.set(elapsedtime)
        running = False
        pass
  
def Reset():
    global elapsedtime
    global timestr
    global starttime
    elapsedtime = 0.0
    starttime = time.time()
    timestr.set(elapsedtime)


tkinter.Label(frame1,textvariable=timestr).pack()
tkinter.Button(frame1,text='Start',command=Start).pack(side=tkinter.LEFT)
tkinter.Button(frame1,text='Stop',command=Stop).pack(side=tkinter.LEFT)
tkinter.Button(frame1,text='Reset',command=Reset).pack(side=tkinter.LEFT)


root.mainloop()
