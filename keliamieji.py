from tkinter import Tk, Label, Entry, Button
import calendar

langas = Tk()

def patikrinti():
    if calendar.isleap(int(laukas1.get())):
        rezultatas1["text"] = "Keliamieji"
    else:
        rezultatas1["text"] = "NEKeliamieji"
    laukas1.delete(0, 'end')

uzrasas1 = Label(langas, text="Įveskite metus")
laukas1 = Entry(langas)
mygtukas1 = Button(langas, text="Patvirtinti", command=patikrinti)
laukas1.bind("<Return>", lambda e: patikrinti())
rezultatas1 = Label(langas, text="")

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
rezultatas1.grid(row=1, columnspan=3)

langas.mainloop()
