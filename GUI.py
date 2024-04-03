import tkinter
from short import tbs, short


def gui():
    root = tkinter.Tk()
    root.title("Simple URL Shortener - 0.1")
    root.resizable(True, True)


    e1 = tkinter.Entry(root)
    e1.bind("<Return>", short)
    e1.pack()

    res = tkinter.Label(root)
    res.pack()


    quit = tkinter.Button(root, text="QUIT", command=root.destroy)
    quit.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()  

gui()
