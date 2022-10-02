# programele issaugo vartotojo vebsaitu logina ir slaptazodi

from tkinter import*
import pickle
langas = Tk()
langas.geometry("350x200")

def issaugoti():
    new_e_website = e_website.get()
    e_website.delete(0, len(new_e_website)) # istrina ivesta teksta, kad netrintu po kiek vieno ivesties
    new_e_account = e_account.get()
    e_account.delete(0, len(new_e_account))
    new_e_password = e_password.get()
    e_password.delete(0, len(new_e_password))
    ivestis = f"Website:   {new_e_website}     ||     Username:  {new_e_account}     ||     Password:  {new_e_password}"        
    sarasas.append(ivestis)
    with open("Sarasas/issaugotas_sarasas.pkl", "wb") as failas:
        pickle.dump(sarasas, failas)
    l_confirmation["text"] = "New data is saved!"
    return sarasas
    
sarasas=[]
    
def atidaryti():
    langas_sarasas = Tk()
    langas_sarasas.geometry("800x300")
   
    with open("Sarasas/issaugotas_sarasas.pkl", "rb") as failas:
        sarasas = pickle.load(failas)
    
    def pasirinkti():
        try:
            pasirinkta = sarasas[dezute.curselection()[0]]
        except: 
            l_choose["text"] = "Choose a webside for full review!"
        else: 
            l_choose["text"] = pasirinkta
             
    dezute_scroll = Scrollbar(langas_sarasas)   
    dezute = Listbox(langas_sarasas, yscrollcommand=dezute_scroll.set, width=30)
    dezute_scroll.config(command=dezute.yview)
    dezute.insert(END, *sarasas)
    dezute.pack(side=LEFT, fill=Y)
    dezute_scroll.pack(side=RIGHT,fill=Y)
    l_choose = Label(langas_sarasas, text="Your chose is here:")
    b_choose = Button(langas_sarasas, text="full Login and Password review", command=pasirinkti)
    l_choose.pack()
    b_choose.pack()
           
def iseiti():
        langas.destroy()

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
langas.bind("<Return>", lambda event: issaugoti()) # naudojam "ENTER" patvirtinimui
b_sarasas = Button(langas, text="password review", command = atidaryti)
langas.bind("<Escape>", lambda event: iseiti())
l_exit = Label(langas, text="For EXIT press Escape")

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
l_exit.grid(row=9,column=1, sticky=N)

langas.mainloop()