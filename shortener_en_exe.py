import gdshortener
import sys
import pyperclip
import re
from art import *

v="1.0"
s = gdshortener.ISGDShortener()
n="Would you like to shorten another link? (Y/N) "
text=text2art(f"Simple URL Shortener\n Version {v} - By horue")



def tbs():
    tbs.tobes=str(input("Enter the link to be shortened: "))
    
def short():
    try:
        final=(str(s.shorten(tbs.tobes)))
        url = r"[^,()'']+"
        correspondencia = re.search(url, final)
        if correspondencia :
            final_url = correspondencia.group()
            pyperclip.copy(final_url)
            print("Shortened link copied to clipboard! ")
        else:
            print('Erro')
    except Exception as e:
        print(f"An error occurred: {e}")


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