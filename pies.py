from tkinter import *
from tkinter import ttk
import math
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk as itk
from math import pi
import numpy as np
from matplotlib import pyplot as plt
#def calculate(*args):
 #   try:
   #     value = float(feet.get())
    #    meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    #except ValueError:
    #    pass
class Application(ttk.Frame):
	def __init__(self, main_window):
		super().__init__(main_window)
		main_window.title("Configurar Fuente")
		main_window.geometry("300x200")
		main_window.configure(width=300, height=200)
		
	#	self.combo = ttk.Combobox(self,width=50,state="readonly")
	#	self.combo.place(x=0, y=0)
	#	self.combo["values"] = ["Seleccione fuente","Fuente DC Directa","Puente 1F Completo Controlado", "Puente 1F Incompleto Controlado", "Puente 3F Completo Controlado", "Puente 3F Incompleto Controlado","Puente 3F Completo Controlado con Diodo Descarga","Chopper 4 Cuadrantes"]
	#	self.combo.current(0)
	#	self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
		self.caso=-1
	#	self.place(width=300, height=200)
		self.entry1=ttk.Entry(self,textvariable=dato1)
		self.entry2=ttk.Entry(self,textvariable=dato2)
		self.entry3=ttk.Entry(self,textvariable=dato3)
		
def selection_changed(self):
	global boxsel
	print("Nuevo elemento seleccionado:", boxsel.get())
	global dato1
	global dato2
	global dato3
	global app
	global numerovalor
	numerovalor=boxsel.current()
	if numerovalor==0:
		print("nada")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.caso=0
	if numerovalor==1:
		print("Fuente DC Directa")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)
		app.labelv1=ttk.Label(app,text="Voltaje DC")
		app.labelv1.place(x=80,y=30)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.caso=1

	if numerovalor==2:
		print("Puente Monofasico Completo Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)
		app.labelv1=ttk.Label(app,text="Voltaje (RMS)")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=2

	if numerovalor==3:
		print("Puente Monofasico incompleto Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)
		app.labelv1=ttk.Label(app,text="Voltaje (RMS)")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=3
	if numerovalor==4:
		print("Puente Trifasico Completo Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje (RMS)")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=4
	if numerovalor==5:
		print("Puente Trifasico Incompleto Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje (RMS)")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=5
	if numerovalor==6:
		print("Puente Trifasico Completo con Diodo de Descarga")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje (RMS)")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=6
	if numerovalor==7:
		print("Chopper 4 Cuadrantes")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Ciclo Util (0-1)")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Frecuencia(Hz)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=7
def selection_changed2(self):
	global boxsel2,ventconfig
	mensaje=boxsel2.get()

	copia=[]
	for i in range(0,8):
		copia1=mensaje.find(":")
		copia2=mensaje.find(" ")
		copia.append(mensaje[copia1+1:copia2])
		mensaje=mensaje[copia2+1:len(mensaje)]

	ventconfig.entrym1.insert(0, copia[0])
	ventconfig.entrym2.insert(0, copia[1])
	ventconfig.entrym3.insert(0, copia[2])
	ventconfig.entrym4.insert(0, copia[3])
	ventconfig.entrym5.insert(0, copia[4])
	ventconfig.entrym6.insert(0, copia[5])
	ventconfig.entrym7.insert(0, copia[6])
	ventconfig.entrym8.insert(0, copia[7])


root = Tk()
root.title("Simulador")
root.config(bg="#05000B")
imagen1=PhotoImage(file="p1.png")
#fondo=Label(ventana,image=imagen1)

imagen2=PhotoImage(file="p2.png")
#fondo=Label(ventana,image=imagen2)

imagen3=PhotoImage(file="p3.png")
#fondo=Label(ventana,image=imagen3)

imagen4=PhotoImage(file="p4.png")
#fondo=Label(ventana,image=imagen4)

imagen5=PhotoImage(file="p5.png")
#fondo=Label(ventana,image=imagen5)

dato1=StringVar()
dato2=StringVar()
dato3=StringVar()
dato1m=StringVar()
dato2m=StringVar()
dato3m=StringVar()
dato4m=StringVar()
dato5m=StringVar()
dato6m=StringVar()
dato7m=StringVar()
dato8m=StringVar()
datoslistos1=DoubleVar()
datoslistos2=DoubleVar()
dato1mm=DoubleVar()
datoslistos3=DoubleVar()
dato2mm=DoubleVar()
dato3mm=DoubleVar()
dato4mm=DoubleVar()
dato5mm=DoubleVar()
dato6mm=DoubleVar()
dato7mm=DoubleVar()
dato8mm=DoubleVar()
cc1=StringVar()
cc2=StringVar()
cc3=StringVar()
cc4=StringVar()
auxili=0




axx=0
s1 = ttk.Style()
s1.configure('new.TFrame', background='#6904A6')
mainframe = ttk.Frame(root, padding="3 3 12 12",style='new.TFrame')
mainframe.grid(column=0, row=0,sticky=(N,W, E))
s2 = ttk.Style()
s2.configure('new1.TFrame', background='#FFFFFF')
secondframe=ttk.Frame(root,style='new1.TFrame')
secondframe.grid(column=0,row=1,sticky=(N,W))
root.columnconfigure(0, weight=1)

fuenteusada=font.Font(family='@Microsoft YaHei',size=12)
font.families()


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.resizable(True,True)
root.geometry("800x768")


def ventaliment():
	global app
	global main_window
	main_window = tk.Tk()
	app = Application(main_window)
	global boxsel
	boxsel = ttk.Combobox(app,width=100,state="readonly")
	boxsel.place(x=0, y=0)
	boxsel["values"] = ["Seleccione fuente","Fuente DC Directa","Puente 1F Completo Controlado", "Puente 1F Incompleto Controlado", "Puente 3F Completo Controlado", "Puente 3F Incompleto Controlado","Puente 3F Completo Controlado con Diodo Descarga","Chopper 4 Cuadrantes"]
	boxsel.current(0)
	boxsel.bind("<<ComboboxSelected>>", selection_changed)
	app.caso=0
	app.place(width=400, height=200)
	app.entry1=ttk.Entry(app,textvariable=dato1)
	app.entry2=ttk.Entry(app,textvariable=dato2)
	app.entry3=ttk.Entry(app,textvariable=dato3)

def configperturb():
	global numerovalor,cc1,cc11,cc2,cc3,cc4
	global ccperturb
	global ccperturb2
	ccperturb= tk.Tk()
	ccperturb2 =Application(ccperturb)
	ccperturb.title("Perturbacion")
	ccperturb.geometry("400x300")
	ccperturb.ccetq1=ttk.Label(ccperturb, text="Aplicar Perturbacion")
	ccperturb.ccetq2=ttk.Label(ccperturb, text="En t=")
	ccperturb.ccentry1=ttk.Entry(ccperturb, textvariable=cc1)
	ccperturb.ccentry1.place(x=60,y=40)
	ccperturb.ccetq1.place(x= 10, y=10)
	ccperturb.ccetq2.place(x= 10, y=40)

	if numerovalor==1:
		ccperturb.ccetq3=ttk.Label(ccperturb, text="Voltaje DC")
		ccperturb.ccetq3.place(x=10,y=70)
		ccperturb.ccentry2=ttk.Entry(ccperturb, textvariable=cc2)
		ccperturb.ccentry2.place(x=80,y=70)
		#ccperturb.ccetq3=ttk.Entry(ccperturb, textvariable=datpert1)
	
	if numerovalor>1:
		if numerovalor<7:
			print(numerovalor)
			ccperturb.ccetq3=ttk.Label(ccperturb, text="Voltaje")
			ccperturb.ccetq3.place(x=10,y=70)
			ccperturb.ccetq4=ttk.Label(ccperturb, text="Angulo alfa")
			ccperturb.ccetq4.place(x=10,y=100)
			ccperturb.ccetq5=ttk.Label(ccperturb, text="Ancho pulso")
			ccperturb.ccetq5.place(x=10,y=130)
			ccperturb.ccentry2=ttk.Entry(ccperturb, textvariable=cc2)
			ccperturb.ccentry2.place(x=100,y=70)
			ccperturb.ccentry3=ttk.Entry(ccperturb, textvariable=cc3)
			ccperturb.ccentry3.place(x=100,y=100)
			ccperturb.ccentry4=ttk.Entry(ccperturb, textvariable=cc4)
			ccperturb.ccentry4.place(x=100,y=130)

	if numerovalor==7:
		ccperturb.ccetq3=ttk.Label(ccperturb, text="Voltaje")
		ccperturb.ccetq3.place(x=10,y=70)
		ccperturb.ccetq4=ttk.Label(ccperturb, text="Frecuencia")
		ccperturb.ccetq4.place(x=10,y=100)
		ccperturb.ccetq5=ttk.Label(ccperturb, text="Ciclo Util")
		ccperturb.ccetq5.place(x=10,y=130)
		ccperturb.ccentry2=ttk.Entry(ccperturb, textvariable=cc2)
		ccperturb.ccentry2.place(x=100,y=70)
		ccperturb.ccentry3=ttk.Entry(ccperturb, textvariable=cc3)
		ccperturb.ccentry3.place(x=100,y=100)
		ccperturb.ccentry4=ttk.Entry(ccperturb, textvariable=cc4)
		ccperturb.ccentry4.place(x=100,y=130)

	ccperturb.ccboton=ttk.Button(ccperturb,text="Aceptar",command=cccpertb)
	ccperturb.ccboton.place(x=10,y=160)



def cccpertb():
	global ccperturb,ventconfig,app,auxili,app,fondo
	
	if auxili==1:
		pertetq11.grid_forget()
		pertetq12.grid_forget()
		pertetq13.grid_forget()
		pertetq1.grid_forget()
		pertetq2.grid_forget()
	if auxili==2:
		pertetq11.grid_forget()
		pertetq12.grid_forget()
		pertetq13.grid_forget()
		pertetq14.grid_forget()
		pertetq15.grid_forget()
		pertetq1.grid_forget()
		pertetq2.grid_forget()
		pertetq3.grid_forget()
		pertetq4.grid_forget()


	if app.caso==1:
		cc11=float(ccperturb.ccentry1.get())
		cc12=float(ccperturb.ccentry2.get())

		pertetq11=ttk.Label(secondframe, text="Perturbacion:",background="white",font=fuenteusada)
		pertetq11.grid(row=1,column=5,sticky=NSEW)
		pertetq12=ttk.Label(secondframe, text="En t=",background="white",font=fuenteusada)
		pertetq12.grid(row=2,column=5,sticky=NSEW)
		pertetq13=ttk.Label(secondframe, text="Voltaje",background="white",font=fuenteusada)
		pertetq13.grid(row=3,column=5,sticky=NSEW)
		pertetq1=ttk.Label(secondframe, text=str(cc11),background="white",font=fuenteusada)
		pertetq1.grid(row=2,column=6,sticky=NSEW)
		pertetq2=ttk.Label(secondframe, text=str(cc12),background="white",font=fuenteusada)
		pertetq2.grid(row=3,column=6,sticky=NSEW)
		auxili=1
	if app.caso>1:
		if app.caso<7:
			cc11=float(ccperturb.ccentry1.get())
			cc12=float(ccperturb.ccentry2.get())
			cc13=float(ccperturb.ccentry3.get())
			cc14=float(ccperturb.ccentry4.get())
			pertetq11=ttk.Label(secondframe, text="Perturbacion:",background="white",font=fuenteusada)
			pertetq11.grid(row=1,column=5,sticky=NSEW)
			pertetq12=ttk.Label(secondframe, text="En t=",background="white",font=fuenteusada)
			pertetq12.grid(row=2,column=5,sticky=NSEW)
			pertetq13=ttk.Label(secondframe, text="Voltaje",background="white",font=fuenteusada)
			pertetq13.grid(row=3,column=5,sticky=NSEW)
			pertetq1=ttk.Label(secondframe, text=str(cc11),background="white",font=fuenteusada)
			pertetq1.grid(row=2,column=6,sticky=NSEW)
			pertetq2=ttk.Label(secondframe, text=str(cc12),background="white",font=fuenteusada)
			pertetq2.grid(row=3,column=6,sticky=NSEW)
			pertetq3=ttk.Label(secondframe, text=str(cc13),background="white",font=fuenteusada)
			pertetq3.grid(row=4,column=6,sticky=NSEW)
			pertetq4=ttk.Label(secondframe, text=str(cc14),background="white",font=fuenteusada)
			pertetq4.grid(row=5,column=6,sticky=NSEW)
			pertetq14=ttk.Label(secondframe, text="Angulo alfa",background="white",font=fuenteusada)
			pertetq14.grid(row=4,column=5,sticky=NSEW)
			pertetq15=ttk.Label(secondframe, text="Ancho de pulso",background="white",font=fuenteusada)
			pertetq15.grid(row=5,column=5,sticky=NSEW)
			auxili=2
	if app.caso==7:
		cc11=float(ccperturb.ccentry1.get())
		cc12=float(ccperturb.ccentry2.get())
		cc13=float(ccperturb.ccentry3.get())
		cc14=float(ccperturb.ccentry4.get())
		pertetq11=ttk.Label(secondframe, text="Perturbacion:",background="white",font=fuenteusada)
		pertetq11.grid(row=1,column=5,sticky=NSEW)
		pertetq12=ttk.Label(secondframe, text="En t=",background="white",font=fuenteusada)
		pertetq12.grid(row=2,column=5,sticky=NSEW)
		pertetq13=ttk.Label(secondframe, text="Voltaje",background="white",font=fuenteusada)
		pertetq13.grid(row=3,column=5,sticky=NSEW)
		pertetq1=ttk.Label(secondframe, text=str(cc11),background="white",font=fuenteusada)
		pertetq1.grid(row=2,column=6,sticky=NSEW)
		pertetq2=ttk.Label(secondframe, text=str(cc12),background="white",font=fuenteusada)
		pertetq2.grid(row=3,column=6,sticky=NSEW)
		pertetq3=ttk.Label(secondframe, text=str(cc13),background="white",font=fuenteusada)
		pertetq3.grid(row=4,column=6,sticky=NSEW)
		pertetq4=ttk.Label(secondframe, text=str(cc14),background="white",font=fuenteusada)
		pertetq4.grid(row=5,column=6,sticky=NSEW)
		pertetq14=ttk.Label(secondframe, text="Ciclo Util",background="white",font=fuenteusada)
		pertetq14.grid(row=4,column=5,sticky=NSEW)
		pertetq15=ttk.Label(secondframe, text="Frecuencia",background="white",font=fuenteusada)
		pertetq15.grid(row=5,column=5,sticky=NSEW)
		auxili=2



def configalimentacion():
	global datoslistos1,datoslistos2,datoslistos3,app,axx,resultado1,resultado2,resultado3,etq1,etq2,etq3,etqfuente,fondo

	if axx==1:
		resultado1.grid_forget()
		etq1.grid_forget()
		etqfuente.grid_forget()
	if axx==2:
		etqfuente.grid_forget()
		etq1.grid_forget()
		etq2.grid_forget()
		etq3.grid_forget()
		resultado1.grid_forget()
		resultado2.grid_forget()
		resultado3.grid_forget()
	if app.caso==1:
		datoslistos1=float(app.entry1.get())
		resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
		resultado1.grid(row=2,column=2,sticky=(W,N))
		etq1=ttk.Label(secondframe,text="Voltaje DC:",font=fuenteusada,background="white")
		etq1.grid(row=2,column=1,sticky=(W))
		axx=1
	if app.caso>1:
		if app.caso<7:
			datoslistos1=float(app.entry1.get())
			datoslistos2=float(app.entry2.get())
			datoslistos3=float(app.entry3.get())	
			resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
			resultado1.grid(row=2,column=2,sticky=(W,N))
			resultado2=ttk.Label(secondframe, text=str(datoslistos2),background="white",font=fuenteusada)
			resultado2.grid(row=3,column=2,sticky=(W,N))
			resultado3=ttk.Label(secondframe, text=str(datoslistos3),background="white",font=fuenteusada)
			resultado3.grid(row=4,column=2,sticky=(W,N))
			etq1=ttk.Label(secondframe,text="Voltaje (RMS):",font=fuenteusada,background="white")
			etq1.grid(row=2,column=1,sticky=(W))
			etq2=ttk.Label(secondframe,text="Angulo de disparo:",font=fuenteusada,background="white")
			etq2.grid(row=3,column=1,sticky=(W))
			etq3=ttk.Label(secondframe,text="Ancho de pulso (grados):",background="white",font=fuenteusada)
			etq3.grid(row=4,column=1,sticky=(W))
			if app.caso==2:
				fondo=Label(secondframe,image=imagen1)
			if app.caso==3:
				fondo=Label(secondframe,image=imagen2)
			if app.caso==4:
				fondo=Label(secondframe,image=imagen4)
			if app.caso==5:
				fondo=Label(secondframe,image=imagen5)
			if app.caso==6:
				fondo=Label(secondframe,image=imagen3)

			fondo.grid(row=9,column=1,sticky=NSEW,rowspan=1)


			axx=2
	if app.caso==7:
		datoslistos1=float(app.entry1.get())
		datoslistos2=float(app.entry2.get())
		datoslistos3=float(app.entry3.get())	
		resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
		resultado1.grid(row=2,column=2,sticky=NSEW)
		resultado2=ttk.Label(secondframe, text=str(datoslistos2),background="white",font=fuenteusada)
		resultado2.grid(row=3,column=2,sticky=NSEW)
		resultado3=ttk.Label(secondframe, text=str(datoslistos3),background="white",font=fuenteusada)
		resultado3.grid(row=4,column=2,sticky=NSEW)
		etq1=ttk.Label(secondframe,text="Voltaje: ",background="white",font=fuenteusada)
		etq1.grid(row=2,column=1,sticky=NSEW)
		etq2=ttk.Label(secondframe,text="Ciclo Util(0-1):",background="white",font=fuenteusada)
		etq2.grid(row=3,column=1,sticky=NSEW)
		etq3=ttk.Label(secondframe,text="Frecuencia(Hz):",background="white",font=fuenteusada)
		etq3.grid(row=4,column=1,sticky=NSEW)
		axx=2		
	
	etqfuente=ttk.Label(secondframe,text='Datos Fuente',background="white",font=fuenteusada)
	etqfuente.grid(row=1,column=1,sticky=(W))

	pass

def configmotor():
	global ventconfig,dato1m,dato2m,dato3m,dato4m,dato5m,dato6m,dato7m,dato8m
	global ventconfig2
	ventconfig= tk.Tk()
	ventconfig2 =Application(ventconfig)
	ventconfig.title("Configurar Motor")
	ventconfig.geometry("400x300")
	global archivo
	global boxsel2
	boxsel2 = ttk.Combobox(ventconfig,width=120,state="readonly")
	boxsel2.place(x=0, y=0)
	valmotores=archivo.readline()
	boxsel2["values"] = valmotores2
	boxsel2.current(0)
	boxsel2.bind("<<ComboboxSelected>>", selection_changed2)
	bcm=ttk.Button(ventconfig,text="Aceptar",command=setmotor)
	labelm1=ttk.Label(ventconfig,text="Voltaje Nom")
	labelm2=ttk.Label(ventconfig,text="R.P.M.")
	labelm3=ttk.Label(ventconfig,text="HpNom")
	labelm4=ttk.Label(ventconfig,text="Psal")
	labelm5=ttk.Label(ventconfig,text="IaNom")
	labelm6=ttk.Label(ventconfig,text="Ra(ohm)")
	labelm7=ttk.Label(ventconfig,text="La(mH)")
	labelm8=ttk.Label(ventconfig,text="Inercia(Kg-m^2):")
	ventconfig.entrym1=ttk.Entry(ventconfig,textvariable=dato1m)
	ventconfig.entrym2=ttk.Entry(ventconfig,textvariable=dato2m)
	ventconfig.entrym3=ttk.Entry(ventconfig,textvariable=dato3m)
	ventconfig.entrym4=ttk.Entry(ventconfig,textvariable=dato4m)
	ventconfig.entrym5=ttk.Entry(ventconfig,textvariable=dato5m)
	ventconfig.entrym6=ttk.Entry(ventconfig,textvariable=dato6m)
	ventconfig.entrym7=ttk.Entry(ventconfig,textvariable=dato7m)
	ventconfig.entrym8=ttk.Entry(ventconfig,textvariable=dato8m)
	
	labelm1.place(x=140,y=30)
	labelm2.place(x=140,y=60)
	labelm3.place(x=140,y=90)
	labelm4.place(x=140,y=120)
	labelm5.place(x=140,y=150)
	labelm6.place(x=140,y=180)
	labelm7.place(x=140,y=210)
	labelm8.place(x=140,y=240)
	bcm.place(x=140,y=270)
	ventconfig.entrym1.place(x=10,y=30)
	ventconfig.entrym2.place(x=10,y=60)
	ventconfig.entrym3.place(x=10,y=90)
	ventconfig.entrym4.place(x=10,y=120)
	ventconfig.entrym5.place(x=10,y=150)
	ventconfig.entrym6.place(x=10,y=180)
	ventconfig.entrym7.place(x=10,y=210)
	ventconfig.entrym8.place(x=10,y=240)
def setmotor():
	global dato1m,dato2m,dato3m,dato4m,dato5m,dato6m,ventconfig,dato7m,dato8m
	dato1mm=float(ventconfig.entrym1.get())
	dato2mm=float(ventconfig.entrym2.get())
	dato3mm=float(ventconfig.entrym3.get())
	dato4mm=float(ventconfig.entrym4.get())
	dato5mm=float(ventconfig.entrym5.get())
	dato6mm=float(ventconfig.entrym6.get())
	dato7mm=float(ventconfig.entrym7.get())
	dato8mm=float(ventconfig.entrym8.get())
	print("ok")
	dato1mmm=ttk.Label(secondframe, text=str(dato1mm),background="gray",font=fuenteusada)
	dato1mmm.grid(row=1,column=4,sticky=NSEW)
	dato2mmm=ttk.Label(secondframe, text=str(dato2mm),background="gray",font=fuenteusada)
	dato2mmm.grid(row=2,column=4,sticky=NSEW)
	dato3mmm=ttk.Label(secondframe, text=str(dato3mm),background="gray",font=fuenteusada)
	dato3mmm.grid(row=3,column=4,sticky=NSEW)
	dato4mmm=ttk.Label(secondframe, text=str(dato4mm),background="gray",font=fuenteusada)
	dato4mmm.grid(row=4,column=4,sticky=NSEW)
	dato5mmm=ttk.Label(secondframe, text=str(dato5mm),background="gray",font=fuenteusada)
	dato5mmm.grid(row=5,column=4,sticky=NSEW)
	dato6mmm=ttk.Label(secondframe, text=str(dato6mm),background="gray",font=fuenteusada)
	dato6mmm.grid(row=6,column=4,sticky=NSEW)
	dato7mmm=ttk.Label(secondframe, text=str(dato7mm),background="gray",font=fuenteusada)
	dato7mmm.grid(row=7,column=4,sticky=NSEW)
	dato8mmm=ttk.Label(secondframe, text=str(dato8mm),background="gray",font=fuenteusada)
	dato8mmm.grid(row=8,column=4,sticky=NSEW)

	etqdato1mmm=ttk.Label(secondframe, text="Voltaje Nom:",background="gray",font=fuenteusada)
	etqdato1mmm.grid(row=1,column=3,sticky=NSEW)
	etqdato2mmm=ttk.Label(secondframe, text="R.P.M:",background="gray",font=fuenteusada)
	etqdato2mmm.grid(row=2,column=3,sticky=NSEW)
	etqdato3mmm=ttk.Label(secondframe, text="HPNom:",background="gray",font=fuenteusada)
	etqdato3mmm.grid(row=3,column=3,sticky=NSEW)
	etqdato4mmm=ttk.Label(secondframe, text="Psal:",background="gray",font=fuenteusada)
	etqdato4mmm.grid(row=4,column=3,sticky=NSEW)
	etqdato5mmm=ttk.Label(secondframe, text="IaNom:",background="gray",font=fuenteusada)
	etqdato5mmm.grid(row=5,column=3,sticky=NSEW)
	etqdato6mmm=ttk.Label(secondframe, text="Ra:",background="gray",font=fuenteusada)
	etqdato6mmm.grid(row=6,column=3,sticky=NSEW)
	etqdato7mmm=ttk.Label(secondframe, text="La(mH):",background="gray",font=fuenteusada)
	etqdato7mmm.grid(row=7,column=3,sticky=NSEW)
	etqdato8mmm=ttk.Label(secondframe, text="Inercia(Kg-m^2):",background="gray",font=fuenteusada)
	etqdato8mmm.grid(row=8,column=3,sticky=NSEW)
	etqextra=ttk.Label(secondframe,text=" ",background="gray")
	etqextra.grid(row=9,column=3,sticky=NSEW)
	etqextra2=ttk.Label(secondframe,text=" ",background="gray")
	etqextra2.grid(row=9,column=4,sticky=NSEW)



etq1=ttk.Label(secondframe,text="Voltaje DC")
etq2=ttk.Label(secondframe,text="Voltaje DC")
etq3=ttk.Label(secondframe,text="Voltaje DC")
#graficar()
#grapha()
archivo=open("valoresmotor.txt","r")
valmotores=[]
valmotores=archivo.readline()
valmotores2=[]
valmotores2.append("Carga R-L-E")
while valmotores != "":
	valmotores2.append(valmotores)
	valmotores=archivo.readline()

#def calcular():


def f1(x,y):
	if cq1==0:
		if cq2==0:
			return 0
	if cq1==1:
		return -y*R/L-(E/L)+V1/L*math.sin((x*w))
	if cq2==1:
		return -y*R/L-(E/L)+V1/L*math.sin((x*w)+pi)
def f2(x,y):
	return ((x)-Tm)/J

def f3(x):
	global kan1,kan2,pcq1,pcq2,cq1,cq2,E
	volt1=V1*math.sin(w*x)
	volt2=V1*math.sin(w*x+pi)

	if x>adisparo1+(kan1/60):
		pcq1=1
	if x>anchdisparo+adisparo1+(kan1/60):
		pcq1=0
		kan1=kan1+1

	if x>adisparo2+(kan2/60):
		pcq2=1
	if x>anchdisparo+adisparo2+(kan2/60):
		pcq2=0
		kan2=kan2+1

	if pcq1==1:
		if volt1>E:
			if volt1>volt2:
				cq1=1
				cq2=0
	if pcq2==1:
		if volt2>E:
			if volt2>volt1:
				cq2=1
				cq1=0
	if cq1==1:
		return volt1
	if cq2==1:
		return volt2
	if cq1==0:
		if cq2==0:
			return E
			
def rk4(f1,f2,f3,a,b,y0,h):
	global cq1, cq2, E
	x=np.arange(a,b+h,h)
	n=len(x)
	y=np.zeros(n)
	v=np.zeros(n)
	v1=np.zeros(n)
	volts=np.zeros(n)
	torque=np.zeros(n)
	y[0]=y0
	
	v[0]=0
	v1[0]=0
	for i in range(0,n-1):
		k11=f1(x[i],y[i])
		k12=f1(x[i]+h/2,y[i]+k11*h/2)
		k13=f1(x[i]+h/2,y[i]+k12*h/2)
		k14=f1(x[i]+h,y[i]+k13*h)
		y[i+1]=y[i]+(h/6)*(k11+2*k12+2*k13+k14)
		torque=y*K
		v1[i+1]=f2(torque[i],v[i])*paso
		v1[i+1]=v1[i]+v1[i+1]
		volts[i+1]=f3(x[i])
		E=v1[i+1]/K
	
		if cq1==1:
			if y[i+1]<0:	
				y[i+1]=0
				torque=y*K
				cq1=0
		if cq2==1:
			if y[i+1]<0:	
				y[i+1]=0
				torque=y*K
				cq2=0

	plt.plot(x,torque)
	plt.plot(x,y)
	plt.plot(x,v1)
	plt.plot(x,volts)
	plt.show()

etqfuente  =ttk.Label(secondframe,text="Voltaje DC")
resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
resultado2=ttk.Label(secondframe, text=str(datoslistos2),background="white",font=fuenteusada)
resultado3=ttk.Label(secondframe, text=str(datoslistos3),background="white",font=fuenteusada)
label1= ttk.Label(mainframe,font="fuenteusada", text=" " ,background="#6904A6").grid(column=1, row=1, sticky=N)
boton1= Button(mainframe, font='fuenteusada', text="Simular",fg="#6904A6",bg="#FFFFFF",relief="ridge").grid(column=3, row=1,rowspan=3,sticky=NSEW,padx=3,pady=1)
boton2= Button(mainframe, font='fuenteusada', text="Alimentacion",command=ventaliment,fg="white",bg="#6904A6",relief="ridge").grid(column=1, row=1,sticky=NSEW,padx=3,pady=1)
boton3= Button(mainframe, font='fuenteusada', text="Motor",command=configmotor,fg="white",bg="#6904A6", relief="ridge").grid(column=1, row=2,sticky=NSEW,padx=3,pady=1,)
boton4= Button(mainframe, font='fuenteusada', text="Perturbacion",command=configperturb,fg="white",bg="#6904A6",relief="ridge").grid(column=1, row=3,sticky=NSEW,padx=3,pady=1)
boton112= Button(mainframe, font='fuenteusada', text="Permanente",fg="white",bg="#6904A6",relief="ridge").grid(column=5, row=1,sticky=NSEW,padx=3,pady=1)
boton111= Button(mainframe, font='fuenteusada', text="Transitorio",fg="white",bg="#6904A6",relief="ridge").grid(column=6, row=1,sticky=NSEW,padx=3,pady=1)
boton11= Button(mainframe, font='fuenteusada', text="Voltaje",fg="white",bg="#6904A6",relief="ridge").grid(column=5, row=2,sticky=NSEW,padx=3,pady=1)
boton21= Button(mainframe, font='fuenteusada', text="Corriente",fg="white",bg="#6904A6",relief="ridge").grid(column=5, row=3,sticky=NSEW,padx=3,pady=1)
boton31= Button(mainframe, font='fuenteusada', text="Velocidad",fg="white",bg="#6904A6", relief="ridge").grid(column=6, row=2,sticky=NSEW,padx=3,pady=1)
boton41= Button(mainframe, font='fuenteusada', text="Torque",fg="white",bg="#6904A6",relief="ridge").grid(column=6, row=3,sticky=NSEW,padx=3,pady=1)



def main():
	root.mainloop()	

if __name__ == "__main__":

	main()

