import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import rsa

root = tk.Tk()
root.geometry("600x600")
root.title("RSA")

def limpiarVentana():
    for widget in root.winfo_children():
        widget.destroy()

def inicio():
    labelTitulo= tk.Label(root, text="Práctica RSA", font=("Arial", 14, "bold"))
    labelTitulo.pack(pady=(20))

    labelPublica = tk.Label(root, text="Ingresa la llave públca de la persona a quien quieres enviar el mensaje:")
    labelPublica.pack()

    textPublica = tk.Text(root, width=60, height=5)
    textPublica.pack()

    labelPrivada = tk.Label(root, text="Ingresa tu llave privada:")
    labelPrivada.pack()

    entryPrivada = tk.Entry(root, show="*", width=80)
    entryPrivada.pack()

    buttonEnviar = tk.Button(root, text="Enviar")
    buttonEnviar.pack()

    labelGenerarLlaves = tk.Label(root, text="Si no tienes tus llaves selecciona 'Generar llaves'")
    labelGenerarLlaves.pack(pady=(50,0))

    buttonGenerarLlaves = tk.Button(root, text="Generar llaves")
    buttonGenerarLlaves.pack()



inicio()
root.mainloop()