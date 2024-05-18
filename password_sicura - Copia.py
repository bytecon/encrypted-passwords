##### script Password sicura v1.1- by bytecon - https://www.bytecon.it/utility #####

from tkinter import *
from tkinter import ttk
import hashlib


def verifica_input(event=None): # abilita i bottoni solo se il campo di testo non è vuoto
    
    if password.get().strip():
        button_genera.config(state='normal')
        button_copia.config(state='normal')
    else:
        button_genera.config(state='disable')
        button_copia.config(state='disable')


def genera():

    password_cript.config(state="normal")
    password1=str(password.get())
    password_cript1=(hashlib.md5(password1.encode('utf-8')).hexdigest()) # cripta
    special_characters='!V10' # aggiunge caratteri speciali e maiuscole
    password_cut=password_cript1[:9] # taglia a 9 caratteri
    password_out=(password_cut + special_characters) # password ottenuta
    password_cript.delete(0, END)
    password_cript.insert(0, str(password_out)) 

def reset():

    password_cript.delete(0, END)
    password_cript.config(state="readonly")
    password.delete(0, END)
    button_genera.config(state='disable')
    button_copia.config(state='disable')
    password.focus()

def copia():

    password_copy=password_cript.get()
    root.clipboard_clear()  # pulisce gli appunti
    root.clipboard_append(password_copy) # copia

    
root = Tk()
root.title('bytecon Password Sicura v1.1')
root.geometry('300x300+400+400')
#root.iconbitmap(your path)
root.resizable(False, False)

root.minsize(340, 300)
root.maxsize(1920, 1080)
#root.attributes('-alpha' , 0.9) # trasparenza

# testo password
label_password=Label(root, text='Password')
label_password.pack(padx=5, pady=5)

# campo password
password=ttk.Entry(root)
password.pack(padx=5, pady=5)
password.focus()
password.bind('<KeyRelease>', verifica_input)

# testo password criptata
label_password_cript=Label(root, text='Password criptata')
label_password_cript.pack(padx=5, pady=5)



# campo password criptata
password_cript=ttk.Entry(root)
password_cript.pack(padx=5, pady=5)
password_cript.config(state='readonly')

# bottone genera
button_genera=ttk.Button(root, text='Genera', command=genera)
button_genera.pack(padx=5, pady=5)
button_genera.config(state="disable")

# bottone copia
button_copia=ttk.Button(root, text='Copia', command=copia)
button_copia.pack(padx=5, pady=5)
button_copia.config(state="disable")

# bottone reset
button_reset=ttk.Button(root, text="Reset", command=reset)
button_reset.pack(padx=5, pady=5)

# testo footer
label_footer=Label(root, text='© www.bytecon.it')
label_footer.pack(padx=10, pady=10)

verifica_input()

root.mainloop()


