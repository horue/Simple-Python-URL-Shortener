import tkinter
from short import tbs, short


def gui():
    root = tkinter.Tk()
    root.title("Simple URL Shortener")
    root.resizable(True, True)


    quit = tkinter.Button(root, text="QUIT", command=root.destroy)
    quit.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()  

gui()
