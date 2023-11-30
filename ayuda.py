#importamos un tk
from tkinter import *
#insertamos la clase Tk()
ventana=Tk()
ventana.geometry('400x500')
#creomis dos widget de orden inferior con la clase frame()
widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width=400,height=250)
widget_uno.config(bg='red')

# creacion de etiquetas
etiqueta=Label(ventana,text='Ingresa su nombre')
etiqueta.grid(row=1,column=0)

#creacion de cuadros de textos
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=0)
#usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()