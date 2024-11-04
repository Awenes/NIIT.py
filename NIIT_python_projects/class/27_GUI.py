from tkinter import *

root = Tk()
root.title("27_gui.py")
root.geometry("400x400")

label = Label(root, text="Username :")
label.pack()

textbox = Entry()
textbox.pack()

btn1 = Button(root, text="OK")
btn1.pack()

btn2 = Button(root, text="Cancel")
btn2.pack()

root.mainloop()
