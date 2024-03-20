from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.geometry("900x500")
#----------------------------Imagen de la carga------------ 

place_image = ImageTk.PhotoImage(Image.open ("image3.png"))
place_image=Label(root)
place_image["image"]=place
place_image.place(relx=0.7, rely=0.5,anchor=CENTER)

#----------------------------Encabezado de la app--------------
#Establece la familia de fuente del texto en la etiqueta según tu elección de tamaño 20, ponla en bold y establece el color del foreground de la etiqueta.
label = Label(root, text="Asignar trabajos", font="times", 20 ,"bold", fg="pink")

label.place(relx=0.01, rely=0.06,anchor=W)


#------------------Etiqueta para la cadena Doctor-------------
label_doctor=Label(root,text="Doctor : ")
#Coloca la etiqueta label_doctor en 0.04 y 0.15 de los valores relx y rely respectivamente y establece anchor en center.
label_doctor.place(relx=0.04, rely=0.15, anchor=CENTER)


#------------------Etiqueta para la cadena Profesionista de TI-------------
label_IT=Label(root,text="Profesionista de TI : ")
#Coloca la etiqueta label_IT at 0.06 en 0.45 de los valores relx y rely respectivamente y establece anchor en center.
label_IT.place(relx=0.06, rely=0.45, anchor=CENTER)


#------------------Etiqueta para la cadena Ingeniero químico ------------
label_chemical=Label(root,text="Ingeniero químico : ")
#Coloca la etiqueta label_chemical en 0.07 y 0.75 de los valores relx y rely respectivamente y establece anchor en center.
label_chemical.place(relx=0.07, rely=0.75, anchor=CENTER)

#---------------------Elementos entry--------------------------------
entry_doctor = Entry(root)
entry_doctor.place(relx=0.25, rely=0.15,anchor=CENTER)

entry_IT = Entry(root)
entry_IT.place(relx=0.25, rely=0.45,anchor=CENTER)

entry_chemical = Entry(root)
entry_chemical.place(relx=0.25, rely=0.75,anchor=CENTER)
#------------------------Label selected--------------------------
label_selected_doctor=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_doctor.place(relx=0.01, rely=0.3,anchor=W)

label_selected_IT=Label(root,font=("times",12,"bold"),fg="dark olive green")
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)

label_selected_chemical=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)

class parent():
    def __init__(self):
        print("Esta es la clase padre")
        
    def doctor(doctor_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor['text'] = "A "+doctor_name+" se le asignó "+hospital_list[random_hospital]
        
    def softwareEngineer(it_professional_name):
        IT_company_list = ["I code", "Web Access", "Dotcom Services", "ATOS"]
        random_IT_company = random.randint(0,3)
        label_selected_IT['text'] = "A "+it_professional_name+" se le asignó "+IT_company_list[random_IT_company]
        
    def chemicalEngineer(chemical_engineer_name):
        company_list = ["Air Liquide", "BASF", "Albemarle Corporation", "DuPont"]
        random_company = random.randint(0,3)
        label_selected_chemical['text'] = "A "+chemical_engineer_name+" se le asignó "+company_list[random_company]
        
class child1(parent):
    def __init__(self):
        print("Esta es la clase child1")
    def getDoctor(self):
        name = entry_doctor.get()
        parent.doctor(name)
        
class child2(parent):
    def __init__(self):
        print("Esta es la clase child2")
    def getIT(self):
        name = entry_IT.get()
        parent.softwareEngineer(name)
        
class child3(parent):
    def __init__(self):
        print("Esta es la clase child3")
    def getChemical(self):
        name = entry_chemical.get()
        parent.chemicalEngineer(name)
        
obj1 = child1()
obj2 = child2() 
obj3 = child3()


btn_doctor = Button(root, text="Mostrar el hospital asignado", command=obj1.getDoctor,bg="#1763A5", fg="white",relief = FLAT)

btn_doctor.place(relx=0.1, rely=0.23,anchor=CENTER)
btn_it = Button(root, text="Mostrar la compañía TI asignada", command=obj2.getIT,bg="#1763A5", fg="white",relief = FLAT)

btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)
btn_chemical = Button(root, text="Mostrar la compañía química asignada", command=obj3.getChemical, bg="#1763A5", fg="white",relief = FLAT)

btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)
root.mainloop()