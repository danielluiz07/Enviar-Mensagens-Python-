from tkinter import *
import pyautogui
import time

def pegarTexto():
    a = Entrada1.get()
    z = int(Entrada2.get())
    x = 0

    time.sleep(5)
    while x<z:
        pyautogui.write(f'{a}\n')
        x+=1

root =Tk()

root.geometry("300x550")
root.title("MyApp")
root.config(bg="lightblue")

Entrada1 = Entry(root)
Entrada1.place(relx=0.32, rely=0.05)
Entrada2 = Entry(root)
Entrada2.place(relx=0.32, rely=0.1)

btn = Button(root, text="Enviar", 
             foreground="white",
             bg="darkgreen",
             command=pegarTexto)
btn.place(relx=0.45, rely=0.15)

root.mainloop()