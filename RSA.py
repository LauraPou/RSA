import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import rsa

root = tk.Tk()
root.geometry("600x600")
root.title("RSA")


labelTitulo= tk.Label(root, text="Práctica RSA", font=("Arial", 14, "bold"))
labelTitulo.pack()

root.mainloop()