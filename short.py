import gdshortener

s = gdshortener.ISGDShortener()

def shorturl():
    tobes=str(input("Qual a url que você gostaria de encurtar?"))
    print (s.shorten(tobes))

shorturl()