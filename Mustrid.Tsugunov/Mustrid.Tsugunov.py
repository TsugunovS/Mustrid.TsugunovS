from cmath import sqrt
from importlib.metadata import PackagePath
from math import fabs
from modulefinder import packagePathMap
from msilib.schema import RadioButton
from secrets import choice
from struct import pack
from tkinter import * 
from tkinter import font # vajalik teksti fondi muutmiseks
from random import * 

def valik():
    num=var.get()
    lbox.insert(END,num)

def valik_2():
    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-": lbox.insert(END,val1)
    if val2!="-": lbox.insert(END,val2)
    if val3!="-": lbox.insert(END,val3)

#Harjutus. Lipud.
raam1 = Tk()
raam1.title("Estonia")
tahvel1 = Canvas(raam1, width=500, height=400, background="white")
tahvel1.grid()

#1-Флаг Естонии
#30-отступ от края, 50-отступ сверху, 300-ширина, 100-нижния линия
tahvel1.create_rectangle(400,50, 120,100,fill="#1F85DE")
tahvel1.create_rectangle(400,100, 120,150,fill="#000000")
tahvel1.create_rectangle(400,200, 120,150,fill="#ffffff")







############
raam2 = Tk()
raam2.title("еее")
tahvel2 = Canvas(raam2, width=500, height=400, background="white")
tahvel2.grid()
#2-Флаг
tahvel2.create_rectangle(400,50, 120,100,fill="#17a2c0")
tahvel2.create_rectangle(400,100, 120,150,fill="#e2da27")
tahvel2.create_rectangle(400,200, 120,150,fill="#17a2c0")
#треугольник
tahvel2.create_polygon(30,50, 100,125, 30,200,fill="black")






###########
raam = Tk()
raam.title("Адфп")
tahvel = Canvas(raam, width=500, height=400, background="white")
tahvel.grid()
#3-Флаг
tahvel.create_rectangle(40,240,  300,300,fill="white")
tahvel.create_rectangle(40,360,  300,300,fill="red")



#27/03/23
aken=Tk()
aken.title("Erinevad nupud")
aken.geometry("200x300")

var=IntVar() #StringVar()
r1=Radiobutton(aken,text="Esimene",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Teine",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kolmas",variable=var,value=3,command=valik)
lbox=Listbox(aken,height=9,width=30)
var1=StringVar()
var2=StringVar()
var3=StringVar()
c1=Checkbutton(aken,text="Esimene",variable=var1,onvalue="Esimene",offvalue="-",command=valik_2)
c2=Checkbutton(aken,text="Teine",variable=var2,onvalue="Teine",offvalue="--",command=valik_2)
c3=Checkbutton(aken,text="Kolmas",variable=var3,onvalue="Kolmas",offvalue="---",command=valik_2)
c1.deselect() #Чтобы небыли выделины ячейки
c2.deselect()
c3.deselect()

# вниз r в сторону с
lbox.grid(row=0,column=0,columnspan=2)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
c1.grid(row=1,column=1)
c2.grid(row=2,column=1)
c3.grid(row=3,column=1)



#круг
#raam = Tk()
#raam.title("Tahvel")
#tahvel = Canvas(raam, width=600, height=600, background="white")
#tahvel.grid()

#x0=0
#y0=0
#x1=600
#y1=600
#a=300
#r=(a**2+a**2)**(1/2)
#p=(a-r)

#for i in range(7):
#    x0+=p
#    y0+=p
#    x1-=p
#    y1-=p
#    tahvel.create_rectangle(x0,y0,x1,y1, width=1, outline="blue", fill="red")
#    tahvel.create_oval(x0,y0,x1,y1, width=1, outline="blue", fill="yellow")
#    p=r-a
#    r=r-p
#    a=((r)*sqrt(2))/2
#tahvel.grid()





#Шахматная доска
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.grid()
a=50 #размер клетки каждого квадрата
b=25 #расстояние от бортиков
for row in range(8):
    for i in range(8):
        x1=i*a+b # ab - расстояние от бортиков
        y1=row*a+b
        x2=x1+a
        y2=y1+a
        if (row+i)%2==0:
            tahvel.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            tahvel.create_rectangle(x1, y1, x2, y2, fill="black")
raam.mainloop() #
    




#.title("Tahvel")
#tahvel = Canvas(raam, width=600, height=600, background="pink")
#tahvel.grid()
#colors=["black",
#        "cyan",
#        "magenta",
#        "red",
#        "blue",
#        "grey",
#        "yellow",
#        "green",
#        "lightblue",
#        "pink",
#        "gold",]
#raam2 = Tk()
#raam2.title("Tahvel")
#tahvel2 = Canvas(raam, width=600, height=600, background="white")
#x0=0
#y0=0
#x1=600
#y1=600
#p==5
#for i in range(55):
#    x0+=p
#    y0+=p
#    x1-=p
#    y1-=p
#    tahvel.create_oval(x0,y0,x1,y1, width=1, outline="blue", fill=choice(colors))
#    #sleep(1)
#tahvel2.grid()
#raam2.mainloop()

#
#27/03/23









#Пример с moodle
#from tkinter import *
#from tkinter import font # vajalik teksti fondi muutmiseks

#raam = Tk()
#raam.title("Tahvel")
#tahvel = Canvas(raam, width=600, height=600, background="white")
#tahvel.grid()

## üksik kriips (x0, y0, x1, y1)
#tahvel.create_line(30, 40, 300, 40)

# ühendatud kriipsud (suvaline arv koordinaatide paare)
#tahvel.create_line(30,60,  300,60,  300,100,  70,100)

## võimalik on muuta joone paksust (width) ja sisu värvi (fill)
#tahvel.create_line(30, 130, 300, 130, width=4, fill="red")

## teistsugune joone stiil
#tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=LAST)

## tõmbab kriipsud, ühendab otsapunktid ja värvib sisu
## värve saab määrata ka rgb komponentidena
## vt. http://www.colorpicker.com/
#tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#95BD9D")

## ristkülik
#tahvel.create_rectangle(30,260,  300,450)

## ovaal
#tahvel.create_oval(30,260,  300,450, width=2, outline="blue", fill="wheat")

## proovi liigutada hiirt selle ovaali kohale
#tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")

## kui soovid teksti esitamisel ise fonti valida, siis tuleb enne vastav font luua
#suur_font = font.Font(family='Helvetica', size=32, weight='bold')
#tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=NW)

#raam.mainloop()
raam.mainloop()
aken.mainloop()