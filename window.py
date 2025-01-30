from tkinter import *
window=Tk()

window.title("sample window")
window.geometry("400x200")

greeting=Label(text="Hello", fg="black", bg="white")
button=Button(text="Click me", fg="blue", bg="pink")
entry=Entry(fg="green", bg="yellow", width=200)
text=Text(fg="red", bg="black")

greeting.pack()
button.pack()
entry.pack()
text.pack()

frame=Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label=Label(master=frame, text="sample frame")
label.pack()

window.mainloop()