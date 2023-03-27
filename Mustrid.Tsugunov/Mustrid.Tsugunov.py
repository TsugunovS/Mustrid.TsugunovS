from cmath import sqrt
from importlib.metadata import PackagePath
from math import fabs
from secrets import choice
from struct import pack
from tkinter import * 
from tkinter import font # vajalik teksti fondi muutmiseks
from random import * 

#def valik_2():
#    val1=var1.get()
#    val2=var2.get()
#    val3=var3.get()
#    if val1!="-": lbox.insert(END,val1)
#    if val2!="-": lbox.insert(END,val2)
#    if val3!="-": lbox.insert(END,val3)

def valik():
    num=var.get()
    if num == 1:
        raam = Tk()
        raam.title("Flags")
        aken = Canvas(raam, width=450, height=600, background="white")
        Estonia(aken)
        Flag(aken)
        Polsha(aken)
    elif num==2:
         raam = Tk()
         raam.title("Krug")
         aken = Canvas(raam, width=600, height=600, background="white")
         krug(aken)
         aken.pack()
    elif num==3:
        raam1 = Tk()
        raam1.title("Kvadrat")
        aken1 = Canvas(raam1, width=300, height=300, background="white")
        kvadrat(aken1)
        aken1.pack()
    elif num==4:
        raam = Tk()
        raam.title("Sahmatnaia")
        aken = Canvas(raam, width=600, height=600, background="white")
        sahmatnaia(aken)
        aken.grid()
    elif num==5:
        raam = Tk()
        raam.title("Svetafor")
        aken = Canvas(raam, width=400, height=500, background="lightgrey")
        svetafor(aken)


def Estonia(aken):
    #30-отступ от края, 50-отступ сверху, 300-ширина, 100-нижния линия
    aken.create_rectangle(320,250, 40,300,fill="#1F85DE")
    aken.create_rectangle(320,300, 40,350,fill="#000000")
    aken.create_rectangle(320,350, 40,400,fill="#ffffff")
    aken.pack()

def Flag(aken):
    #2-Флаг
    aken.create_rectangle(300,50, 30,100,fill="#17a2c0")
    aken.create_rectangle(300,100, 30,150,fill="#e2da27")
    aken.create_rectangle(300,200, 30,150,fill="#17a2c0")
    #треугольник
    aken.create_polygon(30,50, 100,125, 30,200,fill="black")
    aken.pack()

def Polsha(aken):
    #3-Флаг
    aken.create_rectangle(40,450,  300,500,fill="white")
    aken.create_rectangle(40,500,  300,550,fill="red")



def kvadrat(aken1):
    k=14
    x0=0
    y0=0
    x1=300
    y1=300
    a=150
    r=(a**2+a**2)**(1/2)
    p=(a-r)
    for i in range(k):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        aken1.create_rectangle(x0, y0, x1, y1, width=1, outline="blue", fill="red")
        aken1.create_oval(x0, y0, x1, y1, width=1, outline="blue", fill="yellow")  
        p = r - a
        r = r - p
        a = ((r) * sqrt(2)) / 2


def sahmatnaia(aken):
    a=50 #размер клетки каждого квадрата
    b=25 #расстояние от бортиков
    for row in range(8):
        for i in range(8):
            x1=i*a+b # ab - расстояние от бортиков
            y1=row*a+b
            x2=x1+a
            y2=y1+a
            if (row+i)%2==0:
                aken.create_rectangle(x1, y1, x2, y2, fill="white")
            else:
                aken.create_rectangle(x1, y1, x2, y2, fill="black")
    

def krug(aken):
    colors=["black",
            "cyan",
            "red",
            "blue",
            "gray",
            "yellow",
            "green",
            "lightblue",
            "pink",
            "gold"]
    x0=0
    y0=0
    x1=600
    y1=600
    p=5
    for i in range(55):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        aken.create_oval(x0,y0,x1,y1, fill=choice(colors))


def svetafor(aken):
    aken.create_text(30, 0, text="VALGUSFOOR",font="Algerian 12", anchor=NW,)
    aken.create_line(80,50,  100,50,  width=40 , fill="red")
    aken.create_line(60,50,  100,50,  width=40 , fill="red")
    aken.create_line(60,100,  100,100,  width=40 , fill="yellow")
    aken.create_line(60,150,  100,150,  width=40 , fill="green")
    aken.create_line(80 ,180,  80,300,  width=8 , fill="black")
    aken.create_line(30,310,  140,310,  width=4 , fill="black")
    aken.pack()



#27/03/23
aken=Tk()
aken.title("Erinevad nupud")
aken.geometry("200x300")

var=IntVar() #StringVar()
r1=Radiobutton(aken,text="Flags",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Krug",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kvadrat",variable=var,value=3,command=valik)
r4=Radiobutton(aken,text="Sahmatnaia",variable=var,value=4,command=valik)
r5=Radiobutton(aken,text="Svetafor",variable=var,value=5,command=valik)
lbox=Listbox(aken,height=5,width=50)
var1=StringVar()
var2=StringVar()
var3=StringVar()
#c1=Checkbutton(aken,text="krug",variable=var1,onvalue="krug",offvalue="-",command=valik)
#c2=Checkbutton(aken,text="Teine",variable=var2,onvalue="Teine",offvalue="--",command=valik)
#c3=Checkbutton(aken,text="Kolmas",variable=var3,onvalue="Kolmas",offvalue="---",command=valik)
#c1.deselect() #Чтобы небыли выделины ячейки
#c2.deselect()
#c3.deselect()

# вниз r в сторону с
lbox.grid(row=0,column=0,columnspan=2)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
r4.grid(row=4,column=0)
r5.grid(row=5,column=0)
#c1.grid(row=1,column=1)
#c2.grid(row=2,column=1)
#c3.grid(row=3,column=1)


#raam.mainloop()
aken.mainloop()