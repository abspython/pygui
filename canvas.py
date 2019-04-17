from tkinter import *

m = Tk()
m.title("Canvas")  # Cant see title in Unix
c = Canvas(m,width=40,height=60)
c.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
c.create_line(0, y, canvas_width, y)
m.mainloop() 