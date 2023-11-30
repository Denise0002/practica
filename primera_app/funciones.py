from tkinter import *
from tkinter.messagebox import *

def f_limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)

    ventana.nombre_texto.focus()

def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellidos=ventana.apellidos_texto.get()
    celular=ventana.celular_texto.get()
    showinfo(title="nuevo",message="nuevo contacto agregado")

    ventana.tabla_datos.insert("",END,text=nombre,values=(apellidos,celular))
    f_limpiar(ventana)
    
def f_eliminar(ventana):
    elem_eliminar=ventana.tabla_datos.selection()
    showwarning(title="ELIMINAR",message="registro eliminado")

    ventana.tabla_datos.delete(elem_eliminar)

def f_actualizar(ventana):
    if ventana.nombre_texto.get()=="":
        print("que chucha voy actualizar si no hay nada")
        showerror(title="SIN DATOS", message="Eres huevon no hay nada para actualizar")
    else:
        nombre=ventana.nombre_texto.get()
        apellidos=ventana.apellidos_texto.get()
        celular=ventana.celular_texto.get()
        elem_actualizar=ventana.tabla_datos.selection()
        mensaje=askyesno(title="ACTUALIZAR",message="Estas seguro que deseas actualizar esta hvda")
        if mensaje==True:
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)
            return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,celular))
        else:
            showinfo(title="NO ACTUALIZO",message="No se actualizo nngun registro")
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)

def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askyesno(title="ACTUALIZAR",message="Desea actualizar los datos")
    if mensaje==True:
        nombre=captura_datos["text"]
        apellido=captura_datos["values"][0]
        celular=captura_datos["values"][1]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apellidos_texto.insert(0,apellido)
        ventana.celular_texto.insert(0,celular)
        ventana.tabla_datos.selection_remove(elem_actualizar)
    else:
        showinfo(title="ACTUALIZAR",message="Ningun registro seleccionado para actualizacion")
        ventana.tabla_datos.selection_remove(elem_actualizar)
