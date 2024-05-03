# %%
from tkinter import * #Importar funciones y símbolos
from tkinter import ttk
window = Tk()
window.title("Test de Personalidad")
window.geometry('400x400') #Establecemos el tamaño del recuadro
window.configure(background = "grey");
a = Label(window ,text = "Nombre completo").grid(row = 0,column = 0) #Establecemos el primer apartado donde preguntaremos el nombre de la persona
b = Label(window ,text = "Hobbie favorito").grid(row = 1,column = 0) #Establecemos el segundo apartado donde preguntaremos el el hobbie de la persona
c = Label(window ,text = "Describete en 1 palabra").grid(row = 2,column = 0) #Establecemos el tercer apartado donde preguntaremos su descipción personal
d = Label(window ,text = "Numero de contacto").grid(row = 3,column = 0) #Establecemos el cuarto apartado donde preguntaremos el correo de la persona
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1) 
def clicked(): #Se agrega un botón/ventana con el texto "Test"
   res = "Personalidad" + txt.get() #Texto del botón
   lbl.configure(text= res) #configurar el texto de "Personalidad"
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0) #Con esto establecemos el botón de submit y poder picarle
window.mainloop() #Poder mantener la ventana abierta


