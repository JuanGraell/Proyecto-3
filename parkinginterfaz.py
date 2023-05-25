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
        # imgP1 = tk.PhotoImage(file="piso1.png")
        # canvasP1 = tk.Canvas(ventana_p1, width=650, height=450)
        # canvasP1.pack(fill="both", expand="True")
        # canvasP1.create_image(0, 0, image=imgP1, anchor="nw")

        #imagen de fondo del parqueadero del piso 1
        imgP1 = tk.PhotoImage(file="piso1.png")
        imgCarP1= tk.PhotoImage(file="carro.png")
        imgCarReverseP1 = tk.PhotoImage(file="carroReverse.png")
        canvasP1 = tk.Canvas(ventana_p1, width=650, height=450)
        canvasP1.pack(fill="both", expand="True")
        canvasP1.create_image(0, 0, image=imgP1, anchor="nw")


        #del 130 al 209 el slotStatus que permite saber si el parqueadero esta ocupado o no.
        slotStatus1=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus1.place(x=75,y=110)
        if self.slots[0] != None: 
            lblcar1=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar1.place(x=77,y=28)
            slotStatus1.configure(bg="red",text=self.slots[0],font=("Arial",7))
        
        slotStatus2=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus2.place(x=135,y=110)
        if self.slots[1] != None:
            lblcar2=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar2.place(x=137,y=28)
            slotStatus2.configure(bg="red",text=self.slots[1],font=("Arial",7))
        

        slotStatus3=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus3.place(x=193,y=110)
        if self.slots[2] != None:
            lblcar3=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar3.place(x=195,y=28)
            slotStatus3.configure(bg="red",text=self.slots[2],font=("Arial",7))

        slotStatus4=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus4.place(x=251,y=110)
        if self.slots[3] != None:
            lblcar4=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar4.place(x=253,y=28)
            slotStatus4.configure(bg="red",text=self.slots[3],font=("Arial",7))

        slotStatus5=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus5.place(x=309,y=110)
        if self.slots[4] != None:
            lblcar5=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar5.place(x=311,y=28)
            slotStatus5.configure(bg="red",text=self.slots[0],font=("Arial",7))

        slotStatus6=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus6.place(x=366,y=110)
        if self.slots[5] != None:
            lblcar6=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar6.place(x=368,y=28)
            slotStatus6.configure(bg="red",text=self.slots[5],font=("Arial",7))

        slotStatus7=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus7.place(x=424,y=110)
        if self.slots[6] != None:
            lblcar7=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar7.place(x=426,y=28)
            slotStatus7.configure(bg="red",text=self.slots[6],font=("Arial",7))

        slotStatus8=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus8.place(x=482,y=110)
        if self.slots[7] != None:
            lblcar8=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar8.place(x=484,y=28)
            slotStatus8.configure(bg="red",text=self.slots[7],font=("Arial",7))

        slotStatus9=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus9.place(x=540,y=110)
        if self.slots[8] != None: 
            lblcar9=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar9.place(x=542,y=28)
            slotStatus9.configure(bg="red",text=self.slots[8],font=("Arial",7))

        slotStatus10=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus10.place(x=601,y=110)
        if self.slots[9] != None:
            lblcar10=tk.Label(ventana_p1,image=imgCarReverseP1)
            lblcar10.place(x=603,y=28)
            slotStatus10.configure(bg="red",text=self.slots[9],font=("Arial",7))

        slotStatus11=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus11.place(x=75,y=205)
        if self.slots[10] != None:
            lblcar11=tk.Label(ventana_p1,image=imgCarP1)
            lblcar11.place(x=78,y=230)
            slotStatus11.configure(bg="red",text=self.slots[10],font=("Arial",7))

        slotStatus12=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus12.place(x=135,y=205)
        if self.slots[11] != None:
            lblcar12=tk.Label(ventana_p1,image=imgCarP1)
            lblcar12.place(x=138,y=130)
            slotStatus12.configure(bg="red",text=self.slots[11],font=("Arial",7))

        slotStatus13=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus13.place(x=193,y=205)
        if self.slots[12] != None:
            lblcar13=tk.Label(ventana_p1,image=imgCarP1)
            lblcar13.place(x=196,y=230)
            slotStatus13.configure(bg="red",text=self.slots[12],font=("Arial",7))

        slotStatus14=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus14.place(x=251,y=205)
        if self.slots[13] != None:
            lblcar14=tk.Label(ventana_p1,image=imgCarP1)
            lblcar14.place(x=254,y=230)
            slotStatus14.configure(bg="red",text=self.slots[13],font=("Arial",7))

        slotStatus15=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus15.place(x=309,y=205)
        if self.slots[14] != None:
            lblcar15=tk.Label(ventana_p1,image=imgCarP1)
            lblcar15.place(x=312,y=230)
            slotStatus15.configure(bg="red",text=self.slots[14],font=("Arial",7))

        slotStatus16=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus16.place(x=366,y=205)
        if self.slots[15] != None:
            lblcar16=tk.Label(ventana_p1,image=imgCarP1)
            lblcar16.place(x=369,y=230)
            slotStatus16.configure(bg="red",text=self.slots[16],font=("Arial",7))

        slotStatus17=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus17.place(x=424,y=205)
        if self.slots[16] != None:
            lblcar17=tk.Label(ventana_p1,image=imgCarP1)
            lblcar17.place(x=427,y=230)
            slotStatus17.configure(bg="red",text=self.slots[16],font=("Arial",7))

        slotStatus18=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus18.place(x=482,y=205)
        if self.slots[17] != None:
            lblcar18=tk.Label(ventana_p1,image=imgCarP1)
            lblcar18.place(x=485,y=230)
            slotStatus18.configure(bg="red",text=self.slots[17],font=("Arial",7))

        slotStatus19=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus19.place(x=540,y=205)
        if self.slots[18] != None:
            lblcar19=tk.Label(ventana_p1,image=imgCarP1)
            lblcar19.place(x=543,y=230)
            slotStatus19.configure(bg="red",text=self.slots[18],font=("Arial",7))

        slotStatus20=tk.Label(ventana_p1, width=5,height=1,bg="green")
        slotStatus20.place(x=601,y=205)
        if self.slots[19] != None:
            lblcar20=tk.Label(ventana_p1,image=imgCarP1)
            lblcar20.place(x=604,y=230)
            slotStatus20.configure(bg="red",text=self.slots[19],font=("Arial",7))
        
        #Botones para pasar de ventanas.
        btnp2=tk.Button(ventana_p1,text="Piso 2",command=abrirVentanaP2)
        btnp2.place(x=603,y=375)
        
        #botones (insertar, borrar, buscar) y entry
        entryp1=tk.Entry(ventana_p1)
        entryp1.place(x=210,y=375)
        InsBtnp1=tk.Button(ventana_p1,text="Insertar Auto",command=obtenerEntryIns)
        InsBtnp1.place(x=350,y=344)
        FindBtnp1=tk.Button(ventana_p1,text="Buscar Auto", command=ObtenerEntryFind)
        FindBtnp1.place(x=352,y=372)
        DelBtnp1=tk.Button(ventana_p1,text="Borrar Auto",command=obtenerEntryDel)
        DelBtnp1.place(x=353,y=400)

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
        #propiedades de la ventana del piso 2
        ventana_p2 = tk.Tk()
        ventana_p2.geometry("650x430")
        ventana_p2.title("Piso 2")
        ventana_p2.resizable(0,0)

        #imagen de fondo del parqueadero del piso 2
        imgP2 = tk.PhotoImage(file="piso2.png")
        imgCarP2= tk.PhotoImage(file="carro.png")
        imgCarReverseP2 = tk.PhotoImage(file="carroReverse.png")
        canvasP2 = tk.Canvas(ventana_p2, width=650, height=450)
        canvasP2.pack(fill="both", expand="True")
        canvasP2.create_image(0, 0, image=imgP2, anchor="nw")

        #del 276 al 355 el slotStatus que permite saber si el parqueadero esta ocupado o no.
        slotStatus21=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus21.place(x=75,y=110)
        if self.slots[20] != None:
            lblcar21=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar21.place(x=77,y=28) #1
            slotStatus21.configure(bg="red",text=self.slots[20],font=("Arial",7))

        slotStatus22=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus22.place(x=135,y=110)
        if self.slots[21] != None:
            lblcar22=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar22.place(x=137,y=28) #2
            slotStatus22.configure(bg="red",text=self.slots[21],font=("Arial",7))

        slotStatus23=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus23.place(x=193,y=110) 
        if self.slots[22] != None:
            lblcar23=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar23.place(x=195,y=28) #3
            slotStatus23.configure(bg="red",text=self.slots[22],font=("Arial",7))

        slotStatus24=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus24.place(x=251,y=110) 
        if self.slots[23] != None:
            lblcar24=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar24.place(x=253,y=28) #4
            slotStatus24.configure(bg="red",text=self.slots[23],font=("Arial",7))

        slotStatus25=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus25.place(x=309,y=110) 
        if self.slots[24] != None:
            lblcar25=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar25.place(x=311,y=28) #5
            slotStatus25.configure(bg="red",text=self.slots[24],font=("Arial",7))

        slotStatus26=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus26.place(x=366,y=110) 
        if self.slots[25] != None:
            lblcar26=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar26.place(x=368,y=28) #6
            slotStatus26.configure(bg="red",text=self.slots[25],font=("Arial",7))

        slotStatus27=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus27.place(x=424,y=110)
        if self.slots[26] != None:
            lblcar27=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar27.place(x=426,y=28) #7
            slotStatus27.configure(bg="red",text=self.slots[26],font=("Arial",7))

        slotStatus28=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus28.place(x=482,y=110)
        if self.slots[27] != None:
            lblcar28=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar28.place(x=484,y=28) #8
            slotStatus28.configure(bg="red",text=self.slots[27],font=("Arial",7))

        slotStatus29=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus29.place(x=540,y=110)
        if self.slots[28] != None:
            lblcar29=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar29.place(x=542,y=28) #9
            slotStatus29.configure(bg="red",text=self.slots[28],font=("Arial",7))

        slotStatus30=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus30.place(x=601,y=110)
        if self.slots[29] != None: 
            lblcar30=tk.Label(ventana_p2,image=imgCarReverseP2)
            lblcar30.place(x=603,y=28) #10
            slotStatus30.configure(bg="red",text=self.slots[29],font=("Arial",7))

        slotStatus31=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus31.place(x=75,y=205)
        if self.slots[30] != None:
            lblcar31=tk.Label(ventana_p2,image=imgCarP2)
            lblcar31.place(x=78,y=230) #11
            slotStatus31.configure(bg="red",text=self.slots[30],font=("Arial",7))

        slotStatus32=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus32.place(x=135,y=205)
        if self.slots[31] != None:
            lblcar32=tk.Label(ventana_p2,image=imgCarP2)
            lblcar32.place(x=138,y=230) #12
            slotStatus32.configure(bg="red",text=self.slots[31],font=("Arial",7))

        slotStatus33=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus33.place(x=193,y=205)
        if self.slots[32] != None:
            lblcar33=tk.Label(ventana_p2,image=imgCarP2)
            lblcar33.place(x=196,y=230) #13
            slotStatus33.configure(bg="red",text=self.slots[32],font=("Arial",7))

        slotStatus34=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus34.place(x=251,y=205)
        if self.slots[33] != None:
            lblcar34=tk.Label(ventana_p2,image=imgCarP2)
            lblcar34.place(x=254,y=230) #14
            slotStatus34.configure(bg="red",text=self.slots[33],font=("Arial",7))

        slotStatus35=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus35.place(x=309,y=205)
        if self.slots[34] != None:
            lblcar35=tk.Label(ventana_p2,image=imgCarP2)
            lblcar35.place(x=312,y=230) #15
            slotStatus35.configure(bg="red",text=self.slots[34],font=("Arial",7))

        slotStatus36=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus36.place(x=366,y=205)
        if self.slots[35] != None: 
            lblcar36=tk.Label(ventana_p2,image=imgCarP2)
            lblcar36.place(x=369,y=230) #16
            slotStatus36.configure(bg="red",text=self.slots[35],font=("Arial",7))

        slotStatus37=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus37.place(x=424,y=205)
        if self.slots[36] != None:
            lblcar37=tk.Label(ventana_p2,image=imgCarP2)
            lblcar37.place(x=427,y=230) #17
            slotStatus37.configure(bg="red",text=self.slots[36],font=("Arial",7))

        slotStatus38=tk.Label(ventana_p2, width=5,height=1,bg="green",text="")
        slotStatus38.place(x=482,y=205)
        if self.slots[37] != None:
            lblcar38=tk.Label(ventana_p2,image=imgCarP2)
            lblcar38.place(x=485,y=230) #18
            slotStatus38.configure(bg="red",text=self.slots[37],font=("Arial",7))

        slotStatus39=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus39.place(x=540,y=205)
        if self.slots[38] != None: 
            lblcar39=tk.Label(ventana_p2,image=imgCarP2)
            lblcar39.place(x=543,y=230) #19
            slotStatus39.configure(bg="red",text=self.slots[38],font=("Arial",7))

        slotStatus40=tk.Label(ventana_p2, width=5,height=1,bg="green")
        slotStatus40.place(x=601,y=205)
        if self.slots[39] != None:
            lblcar40=tk.Label(ventana_p2,image=imgCarP2)
            lblcar40.place(x=604,y=230) #20
            slotStatus40.configure(bg="red",text=self.slots[39],font=("Arial",7))

        #Botones para pasar de ventanas.
        btnp1=tk.Button(ventana_p2,text="Piso 1",command=abrirVentanaP1)
        btnp1.place(x=5,y=375)
        btnp3=tk.Button(ventana_p2,text="Piso 3",command=abrirVentanaP3)
        btnp3.place(x=603,y=375)

        #botones (insertar, borrar, buscar) y entry
        entryp2=tk.Entry(ventana_p2)
        entryp2.place(x=210,y=375)
        InsBtnp2=tk.Button(ventana_p2,text="Insertar Auto",command=obtenerEntryIns)
        InsBtnp2.place(x=350,y=344)
        FindBtnp2=tk.Button(ventana_p2,text="Buscar Auto", command=ObtenerEntryFind)
        FindBtnp2.place(x=352,y=372)
        DelBtnp2=tk.Button(ventana_p2,text="Borrar Auto",command=obtenerEntryDel)
        DelBtnp2.place(x=353,y=400)

        ventana_p2.mainloop()
    
    #Funcion interfaz piso 3
    def piso3(self):

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
        imgCarP3= tk.PhotoImage(file="carro.png")
        imgCarReverseP3 = tk.PhotoImage(file="carroReverse.png")
        canvasP3 = tk.Canvas(ventana_p3, width=650, height=450)
        canvasP3.pack(fill="both", expand="True")
        canvasP3.create_image(0, 0, image=imgP3, anchor="nw")
        
        #del 421 al 500 el slotStatus que permite saber si el parqueadero esta ocupado o no.
        slotStatus41=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus41.place(x=75,y=110)
        if self.slots[40] != None:
            lblcar41=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar41.place(x=77,y=28) #1
            slotStatus41.configure(bg="red",text=self.slots[40],font=("Arial",7))

        slotStatus42=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus42.place(x=135,y=110)
        if self.slots[41] != None:
            lblcar42=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar42.place(x=137,y=28) #2
            slotStatus42.configure(bg="red",text=self.slots[41],font=("Arial",7))


        slotStatus43=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus43.place(x=193,y=110)
        if self.slots[42] != None:
            lblcar43=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar43.place(x=195,y=28) #3
            slotStatus43.configure(bg="red",text=self.slots[42],font=("Arial",7))


        slotStatus44=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus44.place(x=251,y=110)
        if self.slots[43] != None:
            lblcar44=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar44.place(x=253,y=28) #4
            slotStatus44.configure(bg="red",text=self.slots[43],font=("Arial",7))

        slotStatus45=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus45.place(x=309,y=110)
        if self.slots[44] != None:
            lblcar45=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar45.place(x=311,y=28) #5
            slotStatus45.configure(bg="red",text=self.slots[44],font=("Arial",7))

        slotStatus46=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus46.place(x=366,y=110)
        if self.slots[45] != None:
            lblcar46=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar46.place(x=368,y=28) #6
            slotStatus46.configure(bg="red",text=self.slots[45],font=("Arial",7))

        slotStatus47=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus47.place(x=424,y=110)
        if self.slots[46] != None:
            lblcar47=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar47.place(x=426,y=28) #7
            slotStatus47.configure(bg="red",text=self.slots[46],font=("Arial",7))

        slotStatus48=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus48.place(x=482,y=110)
        if self.slots[47] != None:
            lblcar48=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar48.place(x=484,y=28) #8
            slotStatus48.configure(bg="red",text=self.slots[47],font=("Arial",7))

        slotStatus49=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus49.place(x=540,y=110)
        if self.slots[48] != None:
            lblcar49=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar49.place(x=542,y=28) #9
            slotStatus49.configure(bg="red",text=self.slots[48],font=("Arial",7))

        slotStatus50=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus50.place(x=601,y=110)
        if self.slots[49] != None:
            lblcar50=tk.Label(ventana_p3,image=imgCarReverseP3)
            lblcar50.place(x=603,y=28) #10
            slotStatus50.configure(bg="red",text=self.slots[49],font=("Arial",7))

        slotStatus51=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus51.place(x=75,y=205)
        if self.slots[50] != None:
            lblcar51=tk.Label(ventana_p3,image=imgCarP3)
            lblcar51.place(x=78,y=230) #11
            slotStatus51.configure(bg="red",text=self.slots[50],font=("Arial",7))

        slotStatus52=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus52.place(x=135,y=205)
        if self.slots[51] != None:
            lblcar52=tk.Label(ventana_p3,image=imgCarP3)
            lblcar52.place(x=138,y=230) #12
            slotStatus52.configure(bg="red",text=self.slots[51],font=("Arial",7))

        slotStatus53=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus53.place(x=193,y=205)
        if self.slots[52] != None:
            lblcar53=tk.Label(ventana_p3,image=imgCarP3)
            lblcar53.place(x=196,y=230) #13
            slotStatus53.configure(bg="red",text=self.slots[52],font=("Arial",7))

        slotStatus54=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus54.place(x=251,y=205)
        if self.slots[53] != None:
            lblcar54=tk.Label(ventana_p3,image=imgCarP3)
            lblcar54.place(x=254,y=230) #14
            slotStatus54.configure(bg="red",text=self.slots[53],font=("Arial",7))

        slotStatus55=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus55.place(x=309,y=205)
        if self.slots[54] != None: 
            lblcar55=tk.Label(ventana_p3,image=imgCarP3)
            lblcar55.place(x=312,y=230) #15
            slotStatus55.configure(bg="red",text=self.slots[54],font=("Arial",7))

        slotStatus56=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus56.place(x=366,y=205)
        if self.slots[55] != None:
            lblcar56=tk.Label(ventana_p3,image=imgCarP3)
            lblcar56.place(x=369,y=230) #16
            slotStatus56.configure(bg="red",text=self.slots[55],font=("Arial",7))

        slotStatus57=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus57.place(x=424,y=205)
        if self.slots[56] != None:
            lblcar57=tk.Label(ventana_p3,image=imgCarP3)
            lblcar57.place(x=427,y=230) #17
            slotStatus57.configure(bg="red",text=self.slots[56],font=("Arial",7))

        slotStatus58=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus58.place(x=482,y=205)
        if self.slots[57] != None:
            lblcar58=tk.Label(ventana_p3,image=imgCarP3)
            lblcar58.place(x=485,y=230) #18
            slotStatus58.configure(bg="red",text=self.slots[57],font=("Arial",7))

        slotStatus59=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus59.place(x=540,y=205)
        if self.slots[58] != None:
            lblcar59=tk.Label(ventana_p3,image=imgCarP3)
            lblcar59.place(x=543,y=230) #19
            slotStatus59.configure(bg="red",text=self.slots[58],font=("Arial",7))

        slotStatus60=tk.Label(ventana_p3, width=5,height=1,bg="green")
        slotStatus60.place(x=601,y=205)
        if self.slots[59] != None:
            lblcar60=tk.Label(ventana_p3,image=imgCarP3)
            lblcar60.place(x=604,y=230) #20
            slotStatus60.configure(bg="red",text=self.slots[59],font=("Arial",7))

        #Botones para pasar de ventanas o pisos
        btnp2=tk.Button(ventana_p3,text="Piso 2",command=abrirVentanaP2)
        btnp2.place(x=5,y=375)

        #botones (insertar, borrar, buscar) y entry
        entryp3=tk.Entry(ventana_p3)
        entryp3.place(x=210,y=375)
        InsBtnp3=tk.Button(ventana_p3,text="Insertar Auto",command=obtenerEntryIns)
        InsBtnp3.place(x=350,y=344)
        FindBtnp3=tk.Button(ventana_p3,text="Buscar Auto", command=ObtenerEntryFind)
        FindBtnp3.place(x=352,y=372)
        DelBtnp3=tk.Button(ventana_p3,text="Borrar Auto",command=obtenerEntryDel)
        DelBtnp3.place(x=353,y=400)

        ventana_p3.mainloop()

parqueadero = ParkingLot()
carro = Vechiculo("MOR069")
carro2 = Vechiculo("MOR070")
parqueadero.insert_Vechiculo(carro)
parqueadero.insert_Vechiculo(carro2)

parqueadero.piso1()