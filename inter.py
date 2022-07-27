from sys import implementation
from tkinter import *
import speedtest


def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" Mbps"
    upld=str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_upld.config(text=upld)


sp=Tk()
sp.title("Internet Speed Test")
sp.geometry("400x550")
sp.config(bg="cyan")
lab=Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="cyan",fg="black")
lab.place(x=15,y=30,height=50,width=380)

lab=Label(sp,text="Download Speed ...",font=("Time New Roman",25,"bold"),bg="cyan",fg="blue")
lab.place(x=25,y=120,height=50,width=380)

lab_down=Label(sp,text="0.0 kbps",font=("Time New Roman",25,"bold"),bg="cyan",fg="Red")
lab_down.place(x=10,y=180,height=50,width=380)

lab=Label(sp,text="Upload Speed ...",font=("Time New Roman",25,"bold"),bg="cyan",fg="blue")
lab.place(x=25,y=250,height=50,width=380)

lab_upld=Label(sp,text="0.0 kbps",font=("Time New Roman",25,"bold"),bg="cyan",fg="Red")
lab_upld.place(x=10,y=310,height=50,width=380)


button=Button(sp,text="START",font=("Time New Roman",25,"bold"),relief=RAISED,bg="yellow",command=speedcheck)
button.place(x=125,y=400,height=50,width=150)


sp.mainloop()