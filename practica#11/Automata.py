import re
import sys
from itertools import count
from tkinter import *
raiz=Tk()
raiz.title("Validacion")
raiz.geometry("650x350")
raiz.config(bg="purple")


miframe=Frame(raiz, width=500, height=400)
miframe.pack()

milabel=Label(miframe, text="Valida:", bg="red")
milabel.pack()

texto=Entry(raiz)
texto.pack()

def codigoboton():
    txt=texto.get()
    txt = "/"+txt+"/g"
    x = re.search(r"/[a,b]*/g", txt)

    longitud = (len(txt)-3)
    miltiplo = longitud % 4 == 0

    if (x and miltiplo):
        milabel = Label(miframe, bg="light green", text="cadena valida")
        milabel.pack()
    else:
        milabel = Label(miframe, bg="pink", text="cadena invalida")
        milabel.pack()
    
boton=Button(raiz, text="Validar", command=codigoboton)
boton.pack()

raiz.mainloop()



