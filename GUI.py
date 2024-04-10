import tkinter
import pyperclip
import re
import gdshortener


s = gdshortener.ISGDShortener()




def short(e1):
    print(1)
    link=e1.get
    final=(str(s.shorten(link)))
    url = r"[^,()'']+"
    correspondencia = re.search(url, final)
    if correspondencia :
        final_url = correspondencia.group()
        pyperclip.copy(final_url)


def gui():
    root = tkinter.Tk()
    root.title("Simple URL Shortener - 0.1")
    root.resizable(True, True)


    e1 = tkinter.Entry(root)
    e1.bind("<Return>", short(e1))
    e1.pack()

    res = tkinter.Label(root)
    res.pack()


    quit = tkinter.Button(root, text="Quit", command=root.destroy)
    quit.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()  

gui()
