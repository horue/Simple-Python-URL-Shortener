import gdshortener
import sys
import pyperclip
import re
from art import *

s = gdshortener.ISGDShortener()
n="Gostaria de encurtar outro link? (S/N) "
text=text2art("Simple Python URL Shortener - By horue")

def tbs():
    tbs.tobes=str(input("Qual link gostaria de encurtar? "))
    
def short():
    try:
        final=(str(s.shorten(tbs.tobes)))
        url = r"[^,()'']+"
        correspondencia = re.search(url, final)
        if correspondencia :
            final_url = correspondencia.group()
            pyperclip.copy(final_url)
            print("O link encurtado foi copiado para a área de transferência! ")
        else:
            print('Erro')
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")


def novo():
    a=input(n)
    if a == "n" or a == "N":
        sys.exit()
    else:
        return


print(text)        
while True:
    tbs()
    short()
    novo()