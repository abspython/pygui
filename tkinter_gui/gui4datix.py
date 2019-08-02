from tkinter import *

root = Tk()
root.option_add('*tearOff', FALSE)  # Removes dashed line
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Log",menu=filemenu)
filemenu.add_command(label="Open Log")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As..")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="Help")
helpmenu.add_command(label="About")
mainloop()