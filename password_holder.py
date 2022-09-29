# sukurti kintamosios
# aprasyti funkcijas
# leisti vartuotojui ivesti duomenys
# issaugoti duomenys i faila

from tkinter import *
langas = Tk()
langas.geometry("350x200")

def issaugoti():
    new_e_website = e_website.get()
    e_website.delete(0, len(new_e_website)) # istrina ivesta teksta, kad netrintu po kiek vieno ivesties
    new_e_account = e_account.get()
    e_account.delete(0, len(new_e_account))
    new_e_password = e_password.get()
    e_password.delete(0, len(new_e_password))
    l_confirmation["text"] = "Relax, new data is saved!"

l_pavadinimas = Label(langas, text="   Input data and save:")
l_website = Label(langas, text="Website/object name:")
e_website = Entry(langas)
l_account = Label(langas, text="Acount name:")
e_account = Entry(langas)
l_password = Label(langas, text="Password:")
e_password = Entry(langas)
b_save = Button(langas, text="Save", command = issaugoti)
langas.bind("<Return>", lambda event: issaugoti()) # naudojam "ENTER" patvirtinimui
l_confirmation = Label(langas, text="", anchor=N)


l_pavadinimas.grid(row=0)
l_website.grid(row=1,column=0, sticky=E)
e_website.grid(row=1, column=1)
l_account.grid(row=2, column=0, sticky=E)
e_account.grid(row=2, column=1)
l_password.grid(row=3, column=0, sticky=E)
e_password.grid(row=3, column=1)
b_save.grid(row=4,column=1, sticky=N)
l_confirmation.grid(row=5, column=1, sticky=N)
# b_save.pack(side=RIGHT)

langas.mainloop()