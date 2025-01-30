import tkinter as tk
window=tk.Tk()

window.title("sample window")

for i in range(3):
    for j in range(4):
        frame=tk.Frame(master=window, relief=tk.RAISED, borderwidth=10)
        frame.grid(row=i, column=j, padx=5, pady=4)
        label=tk.Label(master=frame, text=f"row {i} \n column {j}")
        label.pack()
window.mainloop()