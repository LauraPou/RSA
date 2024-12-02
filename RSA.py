import tkinter as tk
from tkinter import messagebox
import os
from tkinter import filedialog
import rsa
import base64

root = tk.Tk()
root.geometry("600x600")
root.title("RSA")

rutaSeleccionada =""

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
    buttonEnviar.pack(pady=(0,20))

def enviar(opcion):
    if opcion == "Cifrar":
        cifrado()       
    if opcion == "Descifrar":
        descifrado()
    if opcion == "Generar llaves":
        llaves()
    
def cifrado():
    global rutaSeleccionada
    
    limpiarVentana()
    print("Estás en cifrado")
    
    labelPublica = tk.Label(root, text="Elige el archivo de la llave públca de la persona a quien quieres enviar el mensaje")
    labelPublica.pack()

    labelRutaPublica = tk.Label(root, text="Ruta seleccionada :")
    labelRutaPublica.pack()

    buttonArchivo = tk.Button(root, text="Elegir archivo", command=lambda: guardarRuta(labelRutaPublica))
    buttonArchivo.pack(pady=(0,20))
    
    labelMensaje =tk.Label(root, text="Ingresa el mensaje que quieres cifrar:")
    labelMensaje.pack()

    entryMensaje = tk.Entry(root)
    entryMensaje.pack(pady=(0,20))

    labelMensaje = tk.Label(root, text="Ingresa la ruta donde quieres guardar el mensaje:")
    labelMensaje.pack()
    labelRutaMensaje = tk.Label(root, text="Ruta seleccionada :")
    labelRutaMensaje.pack()


    buttonRutaMensaje = tk.Button(root, text="Elegir ruta", command=lambda: guardarDirectorio(labelRutaMensaje))
    buttonRutaMensaje.pack(pady=(0,20))

    buttonEnviar = tk.Button(root, text="Enviar",command=lambda: cifrarMensaje(labelRutaPublica.cget("text"),entryMensaje.get(),labelRutaMensaje.cget("text")))
    buttonEnviar.pack()

def cifrarMensaje(rutaPublica, mensaje, rutaMensaje):
    if not os.path.exists(rutaPublica):
        messagebox.showerror("Error", "La ruta de la clave pública no existe.")
        return

    with open(rutaPublica, "r") as archivo:
        public_key_data = archivo.read().encode('utf-8')
        publica = rsa.PublicKey.load_pkcs1(public_key_data)
        mensaje_cifrado = rsa.encrypt(mensaje.encode('utf-8'), publica)
        
    # Convertir mensaje cifrado a base64 para guardarlo como texto
    mensaje_cifrado_b64 = base64.b64encode(mensaje_cifrado).decode('utf-8')

    with open(os.path.join(rutaMensaje, f"mensaje_c.txt"), "w") as pub_file:
        pub_file.write(mensaje_cifrado_b64)
    messagebox.showinfo("Éxito", f"Mensaje cifrado guardado en {rutaMensaje}")

def descifrado():
    limpiarVentana()
    print("Estás en descifrado")

    labelMensaje = tk.Label(root, text="Elige la ruta del archivo del mensaje a descifrar:")
    labelMensaje.pack()
    labelRutaMensaje = tk.Label(root, text="Ruta seleccionada :")
    labelRutaMensaje.pack()

    buttonArchivo = tk.Button(root, text="Elegir archivo", command=lambda: guardarRuta(labelRutaMensaje))
    buttonArchivo.pack(pady=(0,20))

    #entryRutaMensaje = tk.Entry(root, width=60)
    #entryRutaMensaje.pack()

    labelLlave = tk.Label(root, text="Elige la ruta del archivo de tu llave privada:")
    labelLlave.pack()
    labelRutaLlave = tk.Label(root, text="Ruta seleccionada :")
    labelRutaLlave.pack()

    buttonArchivo = tk.Button(root, text="Elegir archivo", command=lambda: guardarRuta(labelRutaLlave))
    buttonArchivo.pack(pady=(0,20))

    labelMensajeO = tk.Label(root, text="Ingresa la ruta donde quieres guardar el mensaje:")
    labelMensajeO.pack()
    labelRutaMensajeO = tk.Label(root, text="Ruta seleccionada :")
    labelRutaMensajeO.pack()


    buttonRutaMensajeO = tk.Button(root, text="Elegir ruta", command=lambda: guardarDirectorio(labelRutaMensajeO))
    buttonRutaMensajeO.pack(pady=(0,20))


    buttonDescifrar = tk.Button(root, text="Descifrar", command=lambda: descifrarMensaje(labelRutaLlave.cget("text"), labelRutaMensaje.cget("text"),labelRutaMensajeO.cget("text") ))
    buttonDescifrar.pack()

def descifrarMensaje(rutaPrivada, rutaMensaje, rutaMensajeDescifrado):
    if not os.path.exists(rutaPrivada):
        messagebox.showerror("Error", "La ruta de la clave privada no existe.")
        return

    with open(rutaPrivada, "r") as archivo:
        private_key_data = archivo.read().encode('utf-8')
        privada = rsa.PrivateKey.load_pkcs1(private_key_data)
    
    with open(rutaMensaje, "r") as archivo:
        mensaje_cifrado_b64 = archivo.read()
        mensaje_cifrado = base64.b64decode(mensaje_cifrado_b64.encode('utf-8'))
    
    try:
        mensaje_descifrado = rsa.decrypt(mensaje_cifrado, privada).decode('utf-8')
        messagebox.showinfo("Mensaje descifrado", f"El mensaje es: {mensaje_descifrado}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo descifrar el mensaje. {str(e)}")
    
    
    with open(os.path.join(rutaMensajeDescifrado, "mensaje_d.txt"), "w") as pub_file:
        pub_file.write(mensaje_descifrado)
    
def llaves():
    limpiarVentana()
    labelNombre = tk.Label(root,text="Ingresa tu nombre")
    labelNombre.pack()

    entryNombre = tk.Entry(root)
    entryNombre.pack()

    labelLlaves = tk.Label(root, text="Elige la ruta del directorio donde vas a guardar tus llaves:")
    labelLlaves.pack()

    labelRutaLlaves = tk.Label(root, text="Ruta seleccionada :")
    labelRutaLlaves.pack()

    buttonArchivo = tk.Button(root, text="Elegir directorio", command=lambda: guardarDirectorio(labelRutaLlaves))
    buttonArchivo.pack(pady=(0,20))

    buttonEnviar = tk.Button(root, text="Enviar",command=lambda: generarLlaves(entryNombre.get(),labelRutaLlaves.cget("text")))
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

    messagebox.showinfo("Éxito", "Llaves guardadas en "+ruta)
    print(f"Claves guardadas en: {ruta}")
    print(f"Clave pública guardada en: {os.path.join(ruta, f'{nombre}_publica.txt')}")
    print(f"Clave privada guardada en: {os.path.join(ruta, f'{nombre}_privada.txt')}")

def guardarDirectorio(labelDirectorio):
    global rutaSeleccionada
    rutaSeleccionada
    directorio = filedialog.askdirectory(title="Selecciona un directorio")
    rutaSeleccionada = directorio
    labelDirectorio.config(text=rutaSeleccionada+"/")
    print(directorio)                                  

def guardarRuta(labelRuta):
    global rutaSeleccionada
    rutaSeleccionada = filedialog.askopenfilename(title="Selecciona un archivo", 
                                         filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    print(rutaSeleccionada)
     # Esta línea se actualiza dinámicamente al seleccionar el archivo
    labelRuta.config(text=rutaSeleccionada )


inicio()
root.mainloop()