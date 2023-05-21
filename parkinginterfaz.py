import tkinter as tk
from tkinter import messagebox
import re

class Vechiculo:
    def __init__(self, placa):
        self.placa = placa
class ParkingLot:
    def __init__(self):
        self.capacity = 60  # Capacidad del parking
        self.slots = [None] * self.capacity  # Inicializar todos los slots como vacíos
    def validar_formato_placa(self, placa):
        """
        Función para verificar el formato de la placa.
        Utiliza el formato AAA000 para verificar que el usuario no meta una placa incorrecta.
        """
        formato_placa = r'^[A-Z]{3}\d{3}$'
        if re.match(formato_placa, placa):
            return True
        else:
            return False
        
    def hash_function(self, placa):
        """
        Función de hash que determina el índice para almacenar un vehículo en la tabla hash.
        Utiliza la suma de los caracteres ASCII de la placa y aplica una operación módulo para obtener el índice.
        """
        total = sum(ord(char) for char in placa)
        return total % self.capacity

    def insert_Vechiculo(self, Vechiculo):
        """
        Inserta un vehículo en el parqueadero utilizando una tabla hash con manejo de colisiones.
        """
        if not self.validar_formato_placa(Vechiculo.placa):
            messagebox.showinfo("Advertencia", "El formato de la placa es incorrecto.")
        elif Vechiculo.placa in self.slots:
            messagebox.showinfo("Advertencia", "El vehículo ya está en el parqueadero.")
        else:
            index = self.hash_function(Vechiculo.placa)

            if self.slots[index] is None:
                self.slots[index] = Vechiculo.placa
                messagebox.showinfo("Advertencia", f"Vehículo con placa {Vechiculo.placa} estacionado en el puesto {index+1}.")
            else:
                # Manejo de colisiones mediante búsqueda lineal
                i = index + 1
                while i != index:
                    if i >= self.capacity:
                        i = 0  # Volver al principio del array

                    if self.slots[i] is None:
                        self.slots[i] = Vechiculo.placa
                        messagebox.showinfo("Advertencia", f"Vehículo con placa {Vechiculo.placa} se estacionó en el puesto {i+1}.")
                        return
                    i += 1
                messagebox.showinfo("Advertencia", "El parking está lleno. No se puede estacionar el vehículo.")

    def find_Vechiculo(self, placa):
        """
        Busca un vehículo en el parqueadero dado su número de placa.
        """
        index = self.hash_function(placa)

        if self.slots[index] is not None and self.slots[index] == placa:
            return index
        else:
            # Búsqueda lineal
            i = index + 1
            while i != index:
                if i >= self.capacity:
                    i = 0

                if self.slots[i] is not None and self.slots[i] == placa:
                    return i
                i += 1
        
        messagebox.showinfo("Advertencia","El vehiculo no se encuentra en el parqueadero.")
        return None

    def remove_Vechiculo(self, placa):
        """
        Remueve un vehículo del parqueadero dado su número de placa.
        """
        index = self.find_Vechiculo(placa)

        if index is not None:
            self.slots[index] = None
            messagebox.showinfo("Advertencia",f"Vehículo con placa {placa} acaba de salir del parqueadero y ahora el puesto: {index+1} se encuentra disponible.")
        else:
            messagebox.showinfo("Advertencia","El vehículo no está estacionado en el parqueadero.")

    #Funcion para el piso 1
    def piso1(self):
        #Funcion para boton para cambiar a la ventana del piso 2
        def abrirVentanaP2():
            ventana_p1.destroy()
            self.piso2()
        #Funcion para boton para cambiar a la ventana del piso 3
        def abrirVentanaP3():
            ventana_p1.destroy()
            self.piso3()
        #Funcion para obtener el entry de la ventana del piso 1 y eliminar el carro
        def obtenerEntryDel():
            if entryp1.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            else:
                self.remove_Vechiculo(entryp1.get())
                ventana_p1.destroy()
                self.piso1()
        #Funcion para obtener el entry de la ventana del piso 1 e insertar el vehiculo
        def obtenerEntryIns():
            Carro = Vechiculo(entryp1.get())
            #Compara si el entry esta vacio
            if entryp1.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            #Compara si en el entry hay algo
            elif entryp1.get()!= "":
                self.insert_Vechiculo(Carro)
                ventana_p1.destroy()
                self.piso1()
        #Funcion para obtener el entry de la ventana del piso 1 y buscar el vehiculo en el parqueadero
        def ObtenerEntryFind():
            if entryp1.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            elif entryp1.get()!= "":
                x=self.find_Vechiculo(entryp1.get())
                if x != None:
                    messagebox.showinfo("Advertencia",f"El vehiculo esta en el puesto {x+1}")

        #propiedades de la ventana del piso 1
        ventana_p1 = tk.Tk()
        ventana_p1.geometry("650x430")
        ventana_p1.title("Piso 1")
        ventana_p1.resizable(0,0)

        #imagen de fondo del parqueadero del piso 1
        imgP1 = tk.PhotoImage(file="piso1.png")
        canvasP1 = tk.Canvas(ventana_p1, width=650, height=450)
        canvasP1.pack(fill="both", expand="True")
        canvasP1.create_image(0, 0, image=imgP1, anchor="nw")

        #del 130 al 209 el slotStatus que permite saber si el parqueadero esta ocupado o no.
        slotStatus1=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus1.place(x=80,y=110)
        if self.slots[0] != None: slotStatus1.configure(bg="red",text=self.slots[0],font=("Arial",7))

        slotStatus2=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus2.place(x=139,y=110)
        if self.slots[1] != None: slotStatus2.configure(bg="red",text=self.slots[1],font=("Arial",7))

        slotStatus3=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus3.place(x=196,y=110)
        if self.slots[2] != None: slotStatus3.configure(bg="red",text=self.slots[2],font=("Arial",7))

        slotStatus4=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus4.place(x=255,y=110)
        if self.slots[3] != None: slotStatus4.configure(bg="red",text=self.slots[3],font=("Arial",7))

        slotStatus5=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus5.place(x=313,y=110)
        if self.slots[4] != None: slotStatus5.configure(bg="red",text=self.slots[4],font=("Arial",7))

        slotStatus6=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus6.place(x=370,y=110)
        if self.slots[5] != None: slotStatus6.configure(bg="red",text=self.slots[5],font=("Arial",7))

        slotStatus7=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus7.place(x=428,y=110)
        if self.slots[6] != None: slotStatus7.configure(bg="red",text=self.slots[6],font=("Arial",7))

        slotStatus8=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus8.place(x=486,y=110)
        if self.slots[7] != None: slotStatus8.configure(bg="red",text=self.slots[7],font=("Arial",7))

        slotStatus9=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus9.place(x=544,y=110)
        if self.slots[8] != None: slotStatus9.configure(bg="red",text=self.slots[8],font=("Arial",7))

        slotStatus10=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus10.place(x=605,y=110)
        if self.slots[9] != None: slotStatus10.configure(bg="red",text=self.slots[9],font=("Arial",7))

        slotStatus11=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus11.place(x=80,y=205)
        if self.slots[10] != None: slotStatus11.configure(bg="red",text=self.slots[10],font=("Arial",7))

        slotStatus12=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus12.place(x=139,y=205)
        if self.slots[11] != None: slotStatus12.configure(bg="red",text=self.slots[11],font=("Arial",7))

        slotStatus13=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus13.place(x=196,y=205)
        if self.slots[12] != None: slotStatus13.configure(bg="red",text=self.slots[12],font=("Arial",7))

        slotStatus14=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus14.place(x=255,y=205)
        if self.slots[13] != None: slotStatus14.configure(bg="red",text=self.slots[13],font=("Arial",7))

        slotStatus15=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus15.place(x=313,y=205)
        if self.slots[14] != None: slotStatus15.configure(bg="red",text=self.slots[14],font=("Arial",7))

        slotStatus16=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus16.place(x=370,y=205)
        if self.slots[15] != None: slotStatus16.configure(bg="red",text=self.slots[15],font=("Arial",7))

        slotStatus17=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus17.place(x=428,y=205)
        if self.slots[16] != None: slotStatus17.configure(bg="red",text=self.slots[16],font=("Arial",7))

        slotStatus18=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus18.place(x=486,y=205)
        if self.slots[17] != None: slotStatus18.configure(bg="red",text=self.slots[17],font=("Arial",7))

        slotStatus19=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus19.place(x=544,y=205)
        if self.slots[18] != None: slotStatus19.configure(bg="red",text=self.slots[18],font=("Arial",7))

        slotStatus20=tk.Label(ventana_p1, width=4,height=1,bg="green")
        slotStatus20.place(x=605,y=205)
        if self.slots[19] != None: slotStatus20.configure(bg="red",text=self.slots[19],font=("Arial",7))
        
        #Botones para pasar de ventanas.
        btnp2=tk.Button(ventana_p1,text="Piso 2",command=abrirVentanaP2)
        btnp2.place(x=5,y=375)
        btnp3=tk.Button(ventana_p1,text="Piso 3",command=abrirVentanaP3)
        btnp3.place(x=603,y=375)
        
        #botones (insertar, borrar, buscar) y entry
        entryp1=tk.Entry(ventana_p1)
        entryp1.place(x=210,y=375)
        InsBtnp1=tk.Button(ventana_p1,text="Insertar Auto",command=obtenerEntryIns)
        InsBtnp1.place(x=350,y=350)
        DelBtnp1=tk.Button(ventana_p1,text="Borrar Auto",command=obtenerEntryDel)
        DelBtnp1.place(x=353,y=395)
        FindBtnp1=tk.Button(ventana_p1,text="Buscar Auto", command=ObtenerEntryFind)
        FindBtnp1.place(x=440,y=376)

        ventana_p1.mainloop()

    #Funcion interfaz piso 2
    def piso2(self):
        #Funcion para boton para cambiar a la ventana del piso 1
        def abrirVentanaP1():
            ventana_p2.destroy()
            self.piso1()
        #Funcion para boton para cambiar a la ventana del piso 3
        def abrirVentanaP3():
            ventana_p2.destroy()
            self.piso3()
        #Funcion para obtener el entry de la ventana del piso 2 y borrar el vehiculo del parqueadero
        def obtenerEntryDel():
            if entryp2.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            else:
                self.remove_Vechiculo(entryp2.get())
                ventana_p2.destroy()
                self.piso2()
        #Funcion para obtener el entry de la ventana del piso 2 e insertar el vehiculo en el parqueadero
        def obtenerEntryIns():
            Carro = Vechiculo(entryp2.get())
            if entryp2.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            elif entryp2.get()!= "":
                self.insert_Vechiculo(Carro)
                ventana_p2.destroy()
                self.piso2()
        #Funcion para obtener el entry de la ventana del piso 2 y buscar el vehiculo en el parqueadero
        def ObtenerEntryFind():
            if entryp2.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            elif entryp2.get()!= "":
                x=self.find_Vechiculo(entryp2.get())
                if x != None:
                    messagebox.showinfo("Advertencia",f"El vehiculo esta en el puesto {x+1}")
        #propiedades de la ventana del piso 1
        ventana_p2 = tk.Tk()
        ventana_p2.geometry("650x430")
        ventana_p2.title("Piso 2")
        ventana_p2.resizable(0,0)

        #imagen de fondo del parqueadero del piso 1
        imgP2 = tk.PhotoImage(file="piso2.png")
        canvasP2 = tk.Canvas(ventana_p2, width=650, height=450)
        canvasP2.pack(fill="both", expand="True")
        canvasP2.create_image(0, 0, image=imgP2, anchor="nw")

        #del 276 al 355 el slotStatus que permite saber si el parqueadero esta ocupado o no.
        slotStatus21=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus21.place(x=80,y=110)
        if self.slots[20] != None: slotStatus21.configure(bg="red",text=self.slots[20],font=("Arial",7))

        slotStatus22=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus22.place(x=139,y=110)
        if self.slots[21] != None: slotStatus22.configure(bg="red",text=self.slots[21],font=("Arial",7))

        slotStatus23=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus23.place(x=196,y=110)
        if self.slots[22] != None: slotStatus23.configure(bg="red",text=self.slots[22],font=("Arial",7))

        slotStatus24=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus24.place(x=255,y=110)
        if self.slots[23] != None: slotStatus24.configure(bg="red",text=self.slots[23],font=("Arial",7))

        slotStatus25=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus25.place(x=313,y=110)
        if self.slots[24] != None: slotStatus25.configure(bg="red",text=self.slots[24],font=("Arial",7))

        slotStatus26=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus26.place(x=370,y=110)
        if self.slots[25] != None: slotStatus26.configure(bg="red",text=self.slots[25],font=("Arial",7))

        slotStatus27=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus27.place(x=428,y=110)
        if self.slots[26] != None: slotStatus27.configure(bg="red",text=self.slots[26],font=("Arial",7))

        slotStatus28=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus28.place(x=486,y=110)
        if self.slots[27] != None: slotStatus28.configure(bg="red",text=self.slots[27],font=("Arial",7))

        slotStatus29=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus29.place(x=544,y=110)
        if self.slots[28] != None: slotStatus29.configure(bg="red",text=self.slots[28],font=("Arial",7))

        slotStatus30=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus30.place(x=605,y=110)
        if self.slots[29] != None: slotStatus30.configure(bg="red",text=self.slots[29],font=("Arial",7))

        slotStatus31=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus31.place(x=80,y=205)
        if self.slots[30] != None: slotStatus31.configure(bg="red",text=self.slots[30],font=("Arial",7))

        slotStatus32=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus32.place(x=139,y=205)
        if self.slots[31] != None: slotStatus32.configure(bg="red",text=self.slots[31],font=("Arial",7))

        slotStatus33=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus33.place(x=196,y=205)
        if self.slots[32] != None: slotStatus33.configure(bg="red",text=self.slots[32],font=("Arial",7))

        slotStatus34=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus34.place(x=255,y=205)
        if self.slots[33] != None: slotStatus34.configure(bg="red",text=self.slots[33],font=("Arial",7))

        slotStatus35=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus35.place(x=313,y=205)
        if self.slots[34] != None: slotStatus35.configure(bg="red",text=self.slots[34],font=("Arial",7))

        slotStatus36=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus36.place(x=370,y=205)
        if self.slots[35] != None: slotStatus36.configure(bg="red",text=self.slots[35],font=("Arial",7))

        slotStatus37=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus37.place(x=428,y=205)
        if self.slots[36] != None: slotStatus37.configure(bg="red",text=self.slots[36],font=("Arial",7))

        slotStatus38=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus38.place(x=486,y=205)
        if self.slots[37] != None: slotStatus38.configure(bg="red",text=self.slots[37],font=("Arial",7))

        slotStatus39=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus39.place(x=544,y=205)
        if self.slots[38] != None: slotStatus39.configure(bg="red",text=self.slots[38],font=("Arial",7))

        slotStatus40=tk.Label(ventana_p2, width=4,height=1,bg="green")
        slotStatus40.place(x=605,y=205)
        if self.slots[39] != None: slotStatus40.configure(bg="red",text=self.slots[39],font=("Arial",7))

        #Botones para pasar de ventanas.
        btnp1=tk.Button(ventana_p2,text="Piso 1",command=abrirVentanaP1)
        btnp1.place(x=5,y=375)
        btnp3=tk.Button(ventana_p2,text="Piso 3",command=abrirVentanaP3)
        btnp3.place(x=603,y=375)

        #botones (insertar, borrar, buscar) y entry
        entryp2=tk.Entry(ventana_p2)
        entryp2.place(x=210,y=375)
        InsBtnp2=tk.Button(ventana_p2,text="Insertar Auto",command=obtenerEntryIns)
        InsBtnp2.place(x=350,y=350)
        DelBtnp2=tk.Button(ventana_p2,text="Borrar Auto",command=obtenerEntryDel)
        DelBtnp2.place(x=353,y=395)
        FindBtnp2=tk.Button(ventana_p2,text="Buscar Auto", command=ObtenerEntryFind)
        FindBtnp2.place(x=440,y=376)

        ventana_p2.mainloop()
    
    #Funcion interfaz piso 3
    def piso3(self):

        #Funciones para funcionamiento de botones 
        def abrirVentanaP1():
            ventana_p3.destroy()
            self.piso1()
        #Funcion para boton para cambiar a la ventana del piso 2
        def abrirVentanaP2():
            ventana_p3.destroy()
            self.piso2()
        def obtenerEntryDel():
            if entryp3.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            else:
                self.remove_Vechiculo(entryp3.get())
                ventana_p3.destroy()
                self.piso3()
        def obtenerEntryIns():
            Carro = Vechiculo(entryp3.get())
            if entryp3.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            elif entryp3.get()!= "":
                self.insert_Vechiculo(Carro)
                ventana_p3.destroy()
                self.piso3()
        def ObtenerEntryFind():
            if entryp3.get() == "":
                messagebox.showwarning("Error","El campo de texto esta vacio.")
            elif entryp3.get()!= "":
                x=self.find_Vechiculo(entryp3.get())
                if x != None:
                    messagebox.showinfo("Advertencia",f"El vehiculo esta en el puesto {x+1}")

        #Creacion de ventana y propiedades
        ventana_p3 = tk.Tk()
        ventana_p3.geometry("650x430")
        ventana_p3.title("Piso 3")
        ventana_p3.resizable(0,0)

        #Imagen de fondo con sus propiedades
        imgP3 = tk.PhotoImage(file="piso3.png")
        canvasP3 = tk.Canvas(ventana_p3, width=650, height=450)
        canvasP3.pack(fill="both", expand="True")
        canvasP3.create_image(0, 0, image=imgP3, anchor="nw")
        
        #del 421 al 500 el slotStatus que permite saber si el parqueadero esta ocupado o no.
        slotStatus41=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus41.place(x=80,y=110)
        if self.slots[40] != None: slotStatus41.configure(bg="red",text=self.slots[40],font=("Arial",7))

        slotStatus42=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus42.place(x=139,y=110)
        if self.slots[41] != None: slotStatus42.configure(bg="red",text=self.slots[41],font=("Arial",7))

        slotStatus43=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus43.place(x=196,y=110)
        if self.slots[42] != None: slotStatus43.configure(bg="red",text=self.slots[42],font=("Arial",7))

        slotStatus44=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus44.place(x=255,y=110)
        if self.slots[43] != None: slotStatus44.configure(bg="red",text=self.slots[43],font=("Arial",7))

        slotStatus45=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus45.place(x=313,y=110)
        if self.slots[44] != None: slotStatus45.configure(bg="red",text=self.slots[44],font=("Arial",7))

        slotStatus46=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus46.place(x=370,y=110)
        if self.slots[45] != None: slotStatus46.configure(bg="red",text=self.slots[45],font=("Arial",7))

        slotStatus47=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus47.place(x=428,y=110)
        if self.slots[46] != None: slotStatus47.configure(bg="red",text=self.slots[46],font=("Arial",7))

        slotStatus48=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus48.place(x=486,y=110)
        if self.slots[47] != None: slotStatus48.configure(bg="red",text=self.slots[47],font=("Arial",7))

        slotStatus49=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus49.place(x=544,y=110)
        if self.slots[48] != None: slotStatus49.configure(bg="red",text=self.slots[48],font=("Arial",7))

        slotStatus50=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus50.place(x=605,y=110)
        if self.slots[49] != None: slotStatus50.configure(bg="red",text=self.slots[49],font=("Arial",7))

        slotStatus51=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus51.place(x=80,y=205)
        if self.slots[50] != None: slotStatus51.configure(bg="red",text=self.slots[50],font=("Arial",7))

        slotStatus52=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus52.place(x=139,y=205)
        if self.slots[51] != None: slotStatus52.configure(bg="red",text=self.slots[51],font=("Arial",7))

        slotStatus53=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus53.place(x=196,y=205)
        if self.slots[52] != None: slotStatus53.configure(bg="red",text=self.slots[52],font=("Arial",7))

        slotStatus54=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus54.place(x=255,y=205)
        if self.slots[53] != None: slotStatus54.configure(bg="red",text=self.slots[53],font=("Arial",7))

        slotStatus55=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus55.place(x=313,y=205)
        if self.slots[54] != None: slotStatus55.configure(bg="red",text=self.slots[54],font=("Arial",7))

        slotStatus56=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus56.place(x=370,y=205)
        if self.slots[55] != None: slotStatus56.configure(bg="red",text=self.slots[55],font=("Arial",7))

        slotStatus57=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus57.place(x=428,y=205)
        if self.slots[56] != None: slotStatus57.configure(bg="red",text=self.slots[56],font=("Arial",7))

        slotStatus58=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus58.place(x=486,y=205)
        if self.slots[57] != None: slotStatus58.configure(bg="red",text=self.slots[57],font=("Arial",7))

        slotStatus59=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus59.place(x=544,y=205)
        if self.slots[58] != None: slotStatus59.configure(bg="red",text=self.slots[58],font=("Arial",7))

        slotStatus60=tk.Label(ventana_p3, width=4,height=1,bg="green")
        slotStatus60.place(x=605,y=205)
        if self.slots[59] != None: slotStatus60.configure(bg="red",text=self.slots[59],font=("Arial",7))

        #Botones para pasar de ventanas o pisos
        btnp1=tk.Button(ventana_p3,text="Piso 1",command=abrirVentanaP1)
        btnp1.place(x=5,y=375)
        btnp2=tk.Button(ventana_p3,text="Piso 2",command=abrirVentanaP2)
        btnp2.place(x=603,y=375)

        #botones (insertar, borrar, buscar) y entry
        entryp3=tk.Entry(ventana_p3)
        entryp3.place(x=210,y=375)
        InsBtnp3=tk.Button(ventana_p3,text="Insertar Auto",command=obtenerEntryIns)
        InsBtnp3.place(x=350,y=350)
        DelBtnp3=tk.Button(ventana_p3,text="Borrar Auto",command=obtenerEntryDel)
        DelBtnp3.place(x=353,y=395)
        FindBtnp3=tk.Button(ventana_p3,text="Buscar Auto", command=ObtenerEntryFind)
        FindBtnp3.place(x=440,y=376)

        ventana_p3.mainloop()

parqueadero = ParkingLot()
carro = Vechiculo("MOR069")
parqueadero.insert_Vechiculo(carro)
parqueadero.piso1()