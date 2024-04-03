import gdshortener
import sys
import pyperclip
import re



s = gdshortener.ISGDShortener()
n="Gostaria de encurtar outro link? (S/N) "

def tbs():
    tbs.tobes=str(input("Qual link gostaria de encurtar? "))
    
def short():
    final=(str(s.shorten(tbs.tobes)))
    url = r"[^,()'']+"
    correspondencia = re.search(url, final)
    if correspondencia :
        final_url = correspondencia.group()
        pyperclip.copy(final_url)
        print("O link encurtado foi copiado para a área de transferência! ")
    else:
        print('Erro')


def novo():
    a=input(n)
    if a == "n" or a == "N":
        sys.exit()
    else:
        return
        
while True:
    tbs()
    short()
    novo()