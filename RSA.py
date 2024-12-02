import tkinter as tk
from tkinter import messagebox
import os
import rsa

root = tk.Tk()
root.geometry("600x600")
root.title("RSA")

def limpiarVentana():
    for widget in root.winfo_children():
        widget.destroy()
    inicio() 

def inicio():
    labelTitulo= tk.Label(root, text="Práctica RSA", font=("Arial", 14, "bold"))
    labelTitulo.pack(pady=(20))

    labelPregunta = tk.Label(root, text="Ingresa lo que quieres realizar:")
    labelPregunta.pack()

    spinnerOpciones = tk.Spinbox(root, values=("Cifrar", "Descifrar", "Generar llaves"))
    spinnerOpciones.pack()

    buttonEnviar = tk.Button(root, text="Enviar", command = lambda:enviar(spinnerOpciones.get()))
    buttonEnviar.pack()

def enviar(opcion):
    if opcion == "Cifrar":
        cifrado()       
    if opcion == "Descifrar":
        descifrado()
    if opcion == "Generar llaves":
        llaves()
    
def cifrado():
    limpiarVentana()
    print("Estás en cifrado")
    labelPublica = tk.Label(root, text="Ingresa la llave públca de la persona a quien quieres enviar el mensaje:")
    labelPublica.pack()

    textPublica = tk.Text(root, width=60, height=5)
    textPublica.pack()

    buttonEnviar = tk.Button(root, text="Enviar")
    buttonEnviar.pack()

def descifrado():
    limpiarVentana()
    print("Estás en descifrado")
    labelMensaje = tk.Label(root, text="Ingresa el mensaje a descifrar")
    labelMensaje.pack()

    entryMensaje = tk.Entry(root)
    entryMensaje.pack()

    labelPrivada = tk.Label(root, text="Ingresa tu llave privada:")
    labelPrivada.pack()

    entryPrivada = tk.Entry(root, show="*", width=80)
    entryPrivada.pack()




def llaves():
    limpiarVentana()
    labelNombre = tk.Label(root,text="Ingresa tu nombre")
    labelNombre.pack()

    entryNombre = tk.Entry(root)
    entryNombre.pack()

    labelRuta = tk.Label(root, text="Ingresa la ruta donde vas a guardar tus llaves:")
    labelRuta.pack()

    entryRuta = tk.Entry(root)
    entryRuta.pack()

    buttonEnviar = tk.Button(root, text="Enviar",command=lambda: generarLlaves(entryNombre.get(),entryRuta.get()))
    buttonEnviar.pack()

def generarLlaves(nombre,ruta):
    # Generar un par de claves (2048 bits recomendados)
    publica, privada = rsa.newkeys(2048)

    # Convertir las claves a formato PEM
    publica_str = publica.save_pkcs1().decode('utf-8')
    privada_str = privada.save_pkcs1().decode('utf-8')

    # Asegúrate de que la ruta exista, si no, la creas
    if not os.path.exists(ruta):
        os.makedirs(ruta)

    # Guardar las claves en los archivos especificados
    with open(os.path.join(ruta, f"{nombre}_publica.txt"), "w") as pub_file:
        pub_file.write(publica_str)
    
    with open(os.path.join(ruta, f"{nombre}_privada.txt"), "w") as priv_file:
        priv_file.write(privada_str)

    print(f"Claves guardadas en: {ruta}")
    print(f"Clave pública guardada en: {os.path.join(ruta, f'{nombre}_publica.txt')}")
    print(f"Clave privada guardada en: {os.path.join(ruta, f'{nombre}_privada.txt')}")


inicio()
root.mainloop()