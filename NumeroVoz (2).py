import tkinter as tk
import pyttsx3
import sys

class Aplicacion:
	def __init__(self):
		self.ventana1=tk.Tk()
		self.ventana1.title("Linea de profundización 1")
		self.ventana1.geometry("400x100")
		self.label1=tk.Label(self.ventana1, text="		Laboratorio Número 1")
		self.label1.grid(column=0, row=1)
		self.label2=tk.Label(self.ventana1, text="Ingrese un número del 1 al 9 -> ")
		self.label2.grid(column=0, row=2)
		self.numero=tk.StringVar()
		self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.numero)
		self.entry1.grid(column=1, row=2)
		self.boton1=tk.Button(self.ventana1, text="Cerrar", command=self.cerrar)
		self.boton1.grid(column=0, row=3)
		self.boton3=tk.Button(self.ventana1, text="Voz", command=self.Voz) 
		self.boton3.grid(column=1, row=3)
		self.ventana1.resizable(False, False)
		self.ventana1.mainloop()
	
	def Voz(self):
		engine = pyttsx3.init()
		engine.setProperty("rate", 150)
		engine.setProperty("voice", "spanish-latin-am")
		engine.say("Usted digito el numero" + self.numero.get())
		engine.runAndWait()
		engine.stop()
		
		
		
	def cerrar(self):
        	sys.exit(0)

aplicacion1 = Aplicacion()
