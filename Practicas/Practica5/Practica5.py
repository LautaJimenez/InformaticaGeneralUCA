'''
#Ejercicio 1

def Copia(Palabra):
    
    if(len(Palabra)<2):
        return "La función ha retornado una palabra vacía."
    
    else:
        return ("La función ha retornado: {}".format(Palabra[(len(Palabra)-2):]*3))
    
def main():
    Palabra = input("Ingrese palabra: ")
    print(Copia(Palabra))
main()

'''
'''
#Ejercicio 2

def UnirExtremos(Extremos,Palabra):

    if(len(Extremos)!=2 or len(Palabra) == 0 ):
        return "La función ha retornado una palabra vacía."

    else:
        PalabraNueva = Extremos[0] + Palabra + Extremos[1]
        return ("La función retornó: {}".format(PalabraNueva))

def main():
    Extremos = input("Ingrese los extremos: ")
    Palabra = input("Ingrese la palabra: ")
    print(UnirExtremos(Extremos,Palabra))
main()
'''
'''
#Ejercicio 3

def esLetra(Letra):
    if((Letra >= "a" and Letra <= "z") or (Letra >= "A" and Letra <= "Z")):
        return True
    else:
        return False

def EsPalabra(Palabra):
    for i in range(len(Palabra)):
        if(esLetra(Palabra[i]) == False):
            return False
    
    return True

def primeraMitad(Palabra):
    return ("La función ha retornado: {}".format(Palabra[0:len(Palabra)//2]))

def main():
    Palabra = input("Ingrese una palabra de longitud par: ")
    
    while((len(Palabra)%2 != 0) or not(EsPalabra(Palabra))):
        Palabra = input("ERROR. Ingrese una palabra de longitud par: ")

    print(primeraMitad(Palabra))

main()
'''

#Ejercicio 4
'''
def esLetra(Letra):
    if((Letra >= "a" and Letra <= "z") or (Letra >= "A" and Letra <= "Z")):
        return True
    else:
        return False

def EsPalabra(Palabra):
    for i in range(len(Palabra)):
        if(esLetra(Palabra[i]) == False):
            return False
    
    return True

def esMayuscula(Letra):
    if(Letra>="A" and Letra<="Z"):
        return True
    else:
        return False

def aMinuscula(Letra):
    Letra = chr(ord(Letra)+32)
    return Letra

def principioFin(Texto):

    TextoNuevo = ""
    PrimeraPalabra = ""
    Contador = 0
    TextoAux = ""

    print(Texto)

    for i in range(len(Texto)):
        if esMayuscula(Texto[i]):
            TextoAux += aMinuscula(Texto[i])
        else:
            TextoAux += Texto[i]

    for i in range(len(TextoAux)):
        if(esLetra(TextoAux[i]) and Contador<1):
            PrimeraPalabra += TextoAux[i]
        else:
            Contador += 1
    
    LargoPrimeraPalabra = len(PrimeraPalabra)

    for i in range(len(TextoAux)):
        if(esLetra(TextoAux[i])):
            TextoNuevo += TextoAux[i]
    

    if(PrimeraPalabra == TextoNuevo[len(TextoNuevo)-LargoPrimeraPalabra:]):
        return True
    else:
        return False

def main():
    Texto = "Hombre de poca fe, he dicho! Vamos, vamos hombre!"
    if(principioFin(Texto)):
        print("El texto cumple la condición.")
    else:
        print("El texto NO cumple la condición.")
main()
'''
'''
#Ejercicio 5

def Rotacion(Texto):
    PrimeraMitad = Texto[:len(Texto)//2]
    SegundaMitad = Texto[len(Texto)//2:]
    TextoNuevo = SegundaMitad + PrimeraMitad
    return TextoNuevo

def main():
    Texto = input("Ingrese un texto: ")
    while(len(Texto)%2 != 0 or len(Texto)<=2):
        Texto = input("ERROR. Ingrese un texto: ")
    print(Rotacion(Texto))
main()

'''

#Ejercicio 6
'''
def esLetra(Caracter):
    if((Caracter>="A" and Caracter<="Z") or (Caracter>="a" and Caracter<="z") or Caracter == "Á" or Caracter == "É" or Caracter == "Í" or Caracter == "Ó" or Caracter == "Ú" or Caracter == "á" or Caracter == "é" or Caracter == "í" or Caracter == "ó" or Caracter == "ú"):
        return True
    else:
        return False

def esMayuscula(Caracter):
    if((Caracter>="A" and Caracter<="Z") or Caracter == "Á" or Caracter == "É" or Caracter == "Í" or Caracter == "Ó" or Caracter == "Ú"):
        return True
    else:
        return False

def AMinuscula(Caracter):
    Caracter = chr(ord(Caracter)+32)
    return Caracter

def Palindroma(Frase):
    FraseAuxiliar = ""
    
    for i in range(len(Frase)):
        if(esMayuscula(Frase[i]) and esLetra(Frase[i])):
            FraseAuxiliar += AMinuscula(Frase[i])
        elif(esLetra(Frase[i])):
            FraseAuxiliar += Frase[i]
    
    if(FraseAuxiliar == FraseAuxiliar[::-1]):
        return True
    else:
        return False

def main():
    Frase = "Solo di sol a los idolos"
    if(Palindroma(Frase)):
        print("La frase es palíndroma!")
    else:
        print("La frase no es palíndroma!")
main()

'''

#Ejercicio 7
'''
def CantidadDeCortoEnLargo(TextoLargo,TextoCorto):
    
    Contador = 0
    
    LongitudDeTextoCorto = len(TextoCorto)

    for i in range(len(TextoLargo)):
        if(TextoLargo[i:i+LongitudDeTextoCorto] == TextoCorto):
            Contador += 1
    
    return Contador

def main():
    TextoLargo = "Bueno, yo o sea, este ... o sea, o sea, o sea, o se, o sea"
    TextoCorto = "o sea"
    print("El texto corto se encontró {} veces en el texto largo.".format(CantidadDeCortoEnLargo(TextoLargo,TextoCorto)))
main()

'''

#Ejercicio 8
'''
def esLetra(Caracter):
    if((Caracter>="A" and Caracter<="Z") or (Caracter>="a" and Caracter<="z") or Caracter == "Á" or Caracter == "É" or Caracter == "Í" or Caracter == "Ó" or Caracter == "Ú" or Caracter == "á" or Caracter == "é" or Caracter == "í" or Caracter == "ó" or Caracter == "ú"):
        return True
    else:
        return False

def esMayuscula(Caracter):
    if((Caracter>="A" and Caracter<="Z") or Caracter == "Á" or Caracter == "É" or Caracter == "Í" or Caracter == "Ó" or Caracter == "Ú"):
        return True
    else:
        return False

def AMayuscula(Caracter):
    Caracter = chr(ord(Caracter)+32)
    return Caracter

def PrimerCaracterAMayuscula(Texto):
    
    TextoNuevo = ""
    Palabra = ""
    i=0
    
    while(i<len(Texto)):
        
        while(i<len(Texto) and not esLetra(Texto[i])):
            Palabra = ""
            i+=1
        while(i<len(Texto) and esLetra(Texto[i])):
            Palabra += Texto[i]
            i+=1
        
        if not(esMayuscula(Palabra[0])):
            TextoNuevo += chr(ord(Palabra[0])-32) + Palabra[1:] + ' '
        else:
            TextoNuevo += Palabra + ' '
    
    return TextoNuevo
    

def main():
    Texto = input("Ingrese un texto: ")
    print("La función ha retornado: {}".format(PrimerCaracterAMayuscula(Texto)))
main()

'''
'''
#Ejercicio 9

def esLetra(Caracter):
    if((Caracter>="a" and Caracter<="z") or (Caracter>="A" and Caracter<="Z") or Caracter == "Á" or Caracter == "É" or Caracter == "Í" or Caracter == "Ó" or Caracter == "Ú" or Caracter == "á" or Caracter == "é" or Caracter == "í" or Caracter == "ó" or Caracter == "ú"):
        return True
    else:
        return False

def Informe(Texto):
    LongitudMinima = len(Texto)
    LongitudMaxima = 0
    Contador = 0
    i = 0
    Palabra = ""
    PalabraMayor = ""
    PalabraMenor = ""
    
    while(i<len(Texto)):
    
        while(i<len(Texto) and not esLetra(Texto[i])):
            Palabra = ""
            i+=1
        while(i<len(Texto) and esLetra(Texto[i])):
            Palabra += Texto[i]
            i+=1

        Contador += 1
        
        if(len(Palabra)>LongitudMaxima):
            LongitudMaxima = len(Palabra)
            PalabraMayor = Palabra

        if(len(Palabra)<LongitudMinima):
            LongitudMinima = len(Palabra)
            PalabraMenor = Palabra   
        

    print("El texto contiene {} palabras, y su palabra mayor es "'"{}"'", y la menor es "'"{}"'".".format((Contador),PalabraMayor,PalabraMenor))
def main():
    Texto = input("Ingrese un texto: ")
    Informe(Texto)
main()

'''

'''
#Ejercicio 10

def esLetra(Caracter):
    if((Caracter>="a" and Caracter<="z") or (Caracter>="A" and Caracter<="Z") or Caracter == "Á" or Caracter == "É" or Caracter == "Í" or Caracter == "Ó" or Caracter == "Ú" or Caracter == "á" or Caracter == "é" or Caracter == "í" or Caracter == "ó" or Caracter == "ú"):
        return True
    else:
        return False

def Condicion(Texto,Palabra):

    Pal = ""
    i=0
    Respuesta = False

    while(i<len(Texto)):
        
        while(i<len(Texto) and not esLetra(Texto[i])):
            Pal = ""
            i+=1
        while(i<len(Texto) and esLetra(Texto[i])):
            Pal += Texto[i]
            i+=1
        
        if(len(Pal) == len(Palabra)):
            for Caracter in range(len(Pal)):
                if(Pal[Caracter]) in Palabra:
                    Respuesta = True
                else:
                    Respuesta = False
    
    return Respuesta

def main():
    Texto = input("Ingrese el texto: ")
    Palabra = input("Ingrese la palabra: ")
    if(Condicion(Texto,Palabra)):
        print("Se cumple con la condición.")
    else:
        print("No se cumple con la condición.")
main()


'''