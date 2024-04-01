import tkinter
from short import shorturl


def gui():
    root = tkinter.Tk()
    root.title("Simple URL Shortener")
    root.resizable(True, True)


    quit = tkinter.Button(root, text="QUIT", command=root.destroy)
    quit.pack()

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs

gui()
