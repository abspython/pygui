from tkinter import *
from tkinter import filedialog


class Window(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.option_add('*tearOff', FALSE)
        self.master.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu) 
        fileMenu.add_command(label="Open Log", underline=6, command=self.onOpen)
        fileMenu.add_command(label="Save", underline=0)
        fileMenu.add_command(label="Save As..")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit",underline=1, command=self.quit)

        helpmenu = Menu(menubar)
        menubar.add_cascade(label="Help", underline=0, menu=helpmenu)
        helpmenu.add_command(label="Help",underline=0)
        helpmenu.add_command(label="About")

    def onOpen(self):
        self.dlg = filedialog.askopenfilename(initialdir="~/", title="Select log file", filetypes=(("text files","*.txt"),("all files","*.*")))
        fn = self.dlg
        print(fn)
        try:
            with open(fn, 'r') as UseFile:
                print(UseFile.read())  # Reads to terminal?
                # Need to fix this
                # to be printed in scrollbox
        except:
            print("No file exists")


def main():
    root = Tk()
    root.option_add('*tearOff', FALSE)
    w = Window()
    root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
