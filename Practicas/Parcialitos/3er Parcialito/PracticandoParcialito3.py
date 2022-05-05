# IG.21.1C.BM.PP3.T1

def EsLetra(Caracter):
    if((Caracter>="a" and Caracter<="z") or (Caracter>="A" and Caracter<="Z")):
        return True
    else:
        return False

def VocalAbierta(Caracter):
    if(Caracter == "a" or Caracter == "A" or Caracter == "e" or Caracter == "E" or Caracter == "o" or Caracter == "O"):
        return True
    else:
        return False

def VocalCerrada(Caracter):
    if(Caracter == "i" or Caracter == "I" or Caracter == "u" or Caracter == "U"):
        return True
    else:
        return False

def Maxima(Secuencia):
    Palabra = ""
    i = 0
    ContadorVocalesAbiertas = 0
    ContadorVocalesCerradas = 0
    while(i<len(Secuencia)):
        
        while(i<len(Secuencia) and EsLetra(Secuencia[i])):
            Palabra += Secuencia[i]
            i+=1
        LongitudPalabra = len(Palabra)
        i+=1
        for j in range(len(Palabra)):
            if(VocalAbierta(Palabra[j])):
                ContadorVocalesAbiertas += 1
            if(VocalCerrada(Palabra[j])):
                ContadorVocalesCerradas += 1
        
        if(ContadorVocalesCerradas == ContadorVocalesAbiertas and ContadorVocalesAbiertas!=0 and ContadorVocalesCerradas !=0):
            return Palabra
        
        Palabra = ""
        ContadorVocalesAbiertas = 0
        ContadorVocalesCerradas = 0

    return Palabra

def main():
    Secuencia = "zqui.hui-?raiz.&ravhvrwlil"
    print(Maxima(Secuencia))
main()