import gdshortener
import tkinter

s = gdshortener.ISGDShortener()

def tbs():
    tbs.tobes=str(input("Qual link gostaria de encurtar?"))
    
def short():
    print(str(s.shorten(tbs.tobes)))

tbs()
short()