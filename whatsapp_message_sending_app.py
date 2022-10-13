from tkinter import *
import pywhatkit as py
def send():
    py.sendwhatmsg(num.get(),msg.get(),hrs.get(),mins.get())
def Exit():
    kj.destroy()
kj = Tk()
kj.geometry("800x600")
fnr = 'Copperplate Gothic Bold',15
Label(kj,text = "Whatsapp Message Sender Uing Python",fg='black',bg='yellow',font = fnr).place(x=180,y=0)
Label(kj,text = "Phone Number With Country Code And + ",fg='blue',bg='orange').place(x=25,y=100)
Label(kj,text = "Type The MEssage ",fg='blue',bg='orange',width = 30).place(x=25,y=150)
Label(kj,text = "Time(Hours)in 24 Hours Timing  ",fg='blue',bg='orange',width = 30).place(x=25,y=200)
Label(kj,text = "Time(Minutes) ",fg='blue',bg='orange',width = 30).place(x=25,y=250)
num = StringVar()
msg = StringVar()
hrs = IntVar()
mins = IntVar()
Entry(kj,textvariable = num,font = fnr).place(x=300,y=100)
Entry(kj,textvariable = msg,font = fnr).place(x=300,y=150)
Entry(kj,textvariable = hrs,font = fnr).place(x=300,y=200)
Entry(kj,textvariable = mins,font = fnr).place(x=300,y=250)
Button(kj,text = "Send",fg='blue',bg='pink',width =- 15,command = send).place(x=0,y=500)
Button(kj,text = "Exit",fg='blue',bg='pink',width =- 15,command = Exit).place(x=700,y=500)
kj.mainloop()
