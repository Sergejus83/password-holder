# sukurti kintamosios
# aprasyti funkcijas
# leisti vartuotojui ivesti duomenys
# issaugoti duomenys i faila

from tkinter import *
langas = Tk()
langas.geometry("400x200")


l_website = Label(langas, text="Website:")
e_website = Entry(langas)
l_acount = Label(langas, text="Acount:")
e_acount = Entry(langas)
l_password = Label(langas, text="Password:")


l_website.grid(row=0,column=0)
e_website.grid()

langas.mainloop()