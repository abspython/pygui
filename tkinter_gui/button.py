import tkinter as tk

m = tk.Tk()
m.title("Button")  # Cant see title in Unix
but = tk.Button(m, text="Stop", width=25, command=m.destroy)
but.pack()
m.mainloop()
