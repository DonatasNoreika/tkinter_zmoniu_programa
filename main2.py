from tkinter import (Tk,
                     Label,
                     Entry,
                     LEFT,
                     Frame,
                     Button,
                     Listbox,
                     END,
                     SINGLE)
import pickle


class Zmogus:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def __repr__(self):
        return f"{self.vardas} {self.pavarde}"

def gauti_is_failo():
    try:
        with open("zmones.pkl", 'rb') as file:
            zmones = pickle.load(file)
    except:
        zmones = []
    return zmones

zmones = gauti_is_failo()

def irasyti_i_faila():
    with open("zmones.pkl", "wb") as file:
        pickle.dump(zmones, file)


def ivesti():
    vardas = vardas_entry.get()
    pavarde = pavarde_entry.get()
    zmogus = Zmogus(vardas, pavarde)
    zmones.append(zmogus)
    boksas.delete(0, END)
    boksas.insert(END, *zmones)
    irasyti_i_faila()

def istrinti():
    zmones.pop(boksas.curselection()[0])
    boksas.delete(0, END)
    boksas.insert(END, *zmones)
    irasyti_i_faila()

langas = Tk()
langas.title("Žmonių administravimo programa")
langas.wm_iconbitmap("asmenys.ico")
langas.geometry("500x200")
remas1 = Frame(langas)
remas2 = Frame(langas)

remas1.pack()
remas2.pack()
vardas_label = Label(remas1, text="Vardas:")
vardas_entry = Entry(remas1)
vardas_label.pack(side=LEFT)
vardas_entry.pack(side=LEFT)
pavarde_label = Label(remas1, text="Pavardė:")
pavarde_entry = Entry(remas1)
pavarde_label.pack(side=LEFT)
pavarde_entry.pack(side=LEFT)
button1 = Button(remas1, text="Įvesti", command=ivesti)
button1.pack(side=LEFT)
button2 = Button(remas1, text="Ištrinti", command=istrinti)
button2.pack(side=LEFT)
boksas = Listbox(remas2, width=60, selectmode=SINGLE)
boksas.pack()
boksas.insert(END, *zmones)
langas.mainloop()