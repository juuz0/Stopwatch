import tkinter as tk

secs = 0
mili_secs = 0
checker = False
root = tk.Tk()
root.geometry("375x50")
root.maxsize(375,50)
root.minsize(375,50)
root.title("Stopwatch!")


def counter_label(l):
    def count():
        global checker
        if checker == True:
            global mili_secs
            global secs
            mili_secs += 1
            if mili_secs == 100:
                mili_secs = 0
                secs += 1 
            l.config(text=str(secs) + "." + str(mili_secs))
            l.after(10,count)
    count()

def passer():
    pass

def stop():
    global checker,btn
    checker = False
    btn.config(command=start)
    btn.config(text="Resume")
   
def start():
    global checker,btn2,label,btn
    checker = True 
    btn2.config(command=stop)
    btn.config(command=passer)
    counter_label(label)

      
def reset():
    global checker,secs,mili_secs
    secs,mili_secs=0,0
    label.config(text="0.0")
    checker = False
    counter_label(label)
    btn.config(text="Start",command=start)
    btn2.config(command=passer)
   
    
label = tk.Label(root,fg="green",text="0.0")
label.grid(row=1,column=2)
btn2 = tk.Button(text="Stop",bg="green",fg="white",padx=5,width=15,command=passer)
btn = tk.Button(text="Start",bg="green",fg="white",padx=5,width=15,command=start)
btn3 = tk.Button(text="Reset",bg="green",fg="white",padx=5,width=15,command=reset)
btn.grid(row=2,column=1)
btn2.grid(row=2,column=2)
btn3.grid(row=2,column=3)
counter_label(label)
root.mainloop()