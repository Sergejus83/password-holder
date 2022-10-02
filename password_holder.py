# sukurti kintamosios
# aprasyti funkcijas
# leisti vartuotojui ivesti duomenys
# issaugoti duomenys i faila
# from time import sleep
# from pickle import PickleBuffer

import pickle
from tkinter import *
langas = Tk()
langas.geometry("350x200")

sarasas=[]

def issaugoti():
    new_e_website = e_website.get()
    e_website.delete(0, len(new_e_website)) # istrina ivesta teksta, kad netrintu po kiek vieno ivesties
    new_e_account = e_account.get()
    e_account.delete(0, len(new_e_account))
    new_e_password = e_password.get()
    e_password.delete(0, len(new_e_password))
    ivestis = f"website: {new_e_website}, username: {new_e_account}, password: {new_e_password}"
    sarasas.append(ivestis)
    with open("add/sarasas.pkl", "wb") as failas:
        pickle.dump(sarasas, failas)
    l_confirmation["text"] = "New data is saved!"
    return sarasas


# vidinis langas - sarasas
def atidaryti():
    langas_sarasas = Tk()
    langas_sarasas.geometry("700x300")

    with open("add/sarasas.pkl", "rb") as failas:
        sarasas = pickle.load(failas)

    def pasirinkti():
            try:
                pasirinkta = sarasas[dezute.curselection()[0]]
            except: 
                l_choose["text"] = "Please shoose webside for password review!"
            else: 
                l_choose["text"] = pasirinkta



    dezute_scroll = Scrollbar(langas_sarasas)   
    dezute = Listbox(langas_sarasas, yscrollcommand=dezute_scroll.set, width=70)
    dezute_scroll.config(command=dezute.yview)
    dezute.insert(END, *sarasas)
    dezute.pack(side=LEFT, fill=Y)
    dezute_scroll.pack(side=RIGHT,fill=Y)
    l_choose = Label(langas_sarasas, text="Your chose is here:")
    b_choose = Button(langas_sarasas, text="login password view", command=pasirinkti)
    l_choose.pack()
    b_choose.pack()

 


# pagrindinis langas
l_confirmation = Label(langas, text="", anchor=N)
l_pavadinimas = Label(langas, text="   Input data and save:")
l_website = Label(langas, text="Website/object name:")
l_confirmation["text"] = "-"
e_website = Entry(langas)
l_account = Label(langas, text="Acount name:")
e_account = Entry(langas)
l_password = Label(langas, text="Password:")
e_password = Entry(langas)
b_save = Button(langas, text="Save", command = issaugoti)
b_sarasas = Button(langas, text="Saved password list", command = atidaryti)
langas.bind("<Return>", lambda event: issaugoti()) # naudojam "ENTER" patvirtinimui


l_pavadinimas.grid(row=0)
l_website.grid(row=1,column=0, sticky=E)
e_website.grid(row=1, column=1)
l_account.grid(row=2, column=0, sticky=E)
e_account.grid(row=2, column=1)
l_password.grid(row=3, column=0, sticky=E)
e_password.grid(row=3, column=1)
b_save.grid(row=4,column=1, sticky=N)
l_confirmation.grid(row=5, column=1, sticky=N)

b_sarasas.grid(row=7,column=1, sticky=N)

# b_save.pack(side=RIGHT)

langas.mainloop()