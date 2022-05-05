import random

'''
# IG.21.1C.JT.RPP2.T1

def CumpleRequisitos(Numero):
    
    Suma = 0

    while(Numero>0):
        Cifra = Numero&10
        Suma += Cifra
        Numero = Numero//10
    
    Promedio = Suma / len(str(Numero))

    if(Promedio<5):
        return True
    else:
        return False

def GenerarNumero(a,b):

    Numero = random.randint(a,b)
    while not CumpleRequisitos(Numero):
        Numero = random.randint(a,b)
    return Numero

def main():
    A = int(input("Ingrese intervalo inferior: "))
    while(A<=0):
        A = int(input("Error, A debe ser positivo, re-ingrese intervalo inferior: "))
    B = int(input("Ingrese intervalo superior: "))
    while(B<=0 or B<=A):
        B = int(input("Error, B debe ser positivo y mayor que A, re-ingrese intervalo inferior:"))

    print("El numero generado es {:d}".format(GenerarNumero(A,B)))
main()
'''
'''

# IG.21.1C.JT.PP2.T1

def sumatoria(Numero1,Numero2):

    Suma = 0
    while(Numero1<=Numero2):
        Suma += Numero1
        Numero1 += 1
    
    return Suma

def main():
    Numero1 = int(input("Ingrese el primer numero: "))
    while(Numero1<=1):
        Numero1 = int(input("Error. Ingrese el primer numero mayor a 1: "))
    Numero2 = int(input("Ingrese el segundo numero: "))
    while(Numero2<=1):
        Numero2 = int(input("Error. Ingrese el segundo numero mayor a 1: "))
    print("La sumatoria de {:d} hasta {:d} es {:d}".format(Numero1,Numero2,sumatoria(Numero1,Numero2)))
main()

'''
'''
# IG.21.1C.IT.RPP2.T1

def figura(Numero):
    for fila in range(Numero):
        for columna in range(Numero):
            if (columna == Numero//2) or (fila-columna >= Numero//2) or (fila == 0 and columna>=Numero//2) or (columna == Numero-1 and fila<=Numero//2) or (columna-fila == Numero//2):
                print("* ",end="")
            else:
                print("  ",end="")
        print()

def main():
    #Numero = int(input("Ingrese un número impar, mayor o igual que 9: "))
    Numero = 9
    while(Numero%2 == 0 or Numero<9):
        Numero = int(input("Error. Ingrese un número impar, mayor o igual que 9: "))
    figura(Numero)
main()
'''
'''
# IG.21.1C.IT.PP2.T1 (Repasar!!!)

def Fibonacci(Numero):
    Contador = 3
    Inferior = 0
    Superior = 1
    Suma = 0
    
    if(Numero == 0):
        Suma = 0
    elif(Numero == 1):
        Suma = 1
    
    else:
        while(Contador<=Numero):
            Suma = Inferior + Superior
            Inferior = Superior
            Superior = Suma
            Contador += 1
    
    return Suma

def main():
    Numero = int(input("Ingrese número menor que 20: "))
    while(Numero>=20):
        Numero = int(input("Error. Ingrese número menor que 20: "))
    print("El termino {:d} de la serie de Fibonacci es {:d}".format(Numero,Fibonacci(Numero)))
main()

'''
'''
#IG.21.1C.GT.RPP2.T1

def dosPares(Numero):
    Contador = 0
    while(Numero>0):
        Digito = Numero%10
        Numero = Numero//10
        if(Digito%2 == 0 and Digito!=0):
            Contador += 1
    
    if(Contador >= 2):
        return True
    else:
        return False

def ingresar():
    Numero = int(input("Ingrese numero: "))
    while (dosPares(Numero) == False):
        Numero = int(input("Error. Ingrese numero: "))
    return Numero

def main():
    Resultado = ingresar()
    print(Resultado)
main()

'''
'''
#IG.21.1C.GT.PP2.T1

def figura(Base):
    for fila in range(Base):
        for col in range(Base):
            if((fila>=col and fila+col >= Base-1) or (fila == 0) or (fila+col == Base-1) or (fila == col)):
                print("* ",end="")
            else:
                print("  ",end="")
        print("")

def main():
    Base = int(input("Ingresar base: "))
    while(Base%2 == 0 or Base<7):
        Base = int(input("Error. Ingresar base: "))
    figura(Base)
main()

'''
'''

# IG.21.1C.DM.RPP2.T1

def validarT1(num):

    Suma = 0
    Contador = 0
    DigitoIzquierda = num%10
    NumAux = num

    while(num>0):
        Digito = num%10
        num = num//10
        Suma += Digito
        Contador += 1
    
    DigitoDerecha = NumAux//(10**(Contador-1))

    Suma = Suma - DigitoDerecha - DigitoIzquierda

    if(Suma == (DigitoIzquierda*DigitoDerecha)):
        return True
    else:
        return False

def main():
    Numero = int(input("Ingrese numero: "))
    print("{:d} -> {}".format(Numero,validarT1(Numero)))
main()

'''
'''
# IG.21.1C.DM.PP2.T1


def Contador(Numero):
    contador = 0
    while(Numero>0):
        Numero = Numero//10
        contador += 1
    return contador 

def primerDigito(Numero):
     
    numAux = Numero
    Contador = 0
     
    while(Numero>0):
        Numero = Numero//10
        Contador += 1
    
    PrimerDigito = numAux // (10**(Contador-1))
    
    return PrimerDigito

def miFuncion(numA):
    
    numAux = numA

    UltimoDigito = numA % 10
    PrimerDigito = primerDigito(numA)
    
    
    numAux = numAux//10
    
    CifrasMedia = numAux - (PrimerDigito * (10**(Contador(numA)-2))) 
    CifrasExtremos = PrimerDigito * 10 + UltimoDigito

    Maximo = 0
    i = 1

    while(i<CifrasMedia):
        if(CifrasMedia%i == 0):
            Maximo = i
        i+=1
    
    if(Maximo == CifrasExtremos):
        return True
    else:
        return False


def main():
    Numero = int(input("Ingrese numero: "))
    print("{:d} -> {}".format(Numero,miFuncion(Numero)))
main()

'''
'''
# IG.21.1C.BM.RPP2.T1


def Contador(Numero):
    
    contador = 0
    
    while(Numero>0):
        Numero = Numero//10
        contador+=1

    return contador

def PrimerCifra(Numero):
    
    contador = Contador(Numero)
    PrimeraCifra = Numero // (10**(contador-1))
    return PrimeraCifra

def CifrasMedias(Numero):
    Numero = Numero//10
    primerCifra = PrimerCifra(Numero)
    contador = Contador(Numero)
    
    CifraMedia = Numero - primerCifra * (10**(contador-2))

    return CifraMedia

def validar(num):

    UltimaCifra = num%10
    primerCifra = PrimerCifra(num)
    CifraMedia = CifrasMedias(num)
    MultiplicacionExtremos = primerCifra * UltimaCifra

    if(MultiplicacionExtremos == 0 or CifraMedia % MultiplicacionExtremos != 0):
        return False
    else:
        return True

def main():
    Numero = int(input("Ingrese numero: "))
    print("{:d} -> {}".format(Numero,validar(Numero)))
main()
'''
'''
# El de WhatsApp

def CambiarBase(Numero,Base):
    Potencia = 1
    NumeroNuevo = 0
    while(Numero>0):
        Resto = Numero%Base
        Numero = Numero//Base
        NumeroNuevo = NumeroNuevo+(Resto*Potencia)
        Potencia = Potencia*10
    return NumeroNuevo

def Tabla(Base):
    CantidadDeNumeros = 0
    for i in range(1,51):
        if(CantidadDeNumeros<9):
            print("{:8}".format(CambiarBase(i,Base)),end="")
            CantidadDeNumeros += 1
        
        else:
            print("{:8}".format(CambiarBase(i,Base)))
            CantidadDeNumeros = 0

def main():
    Base = int(input("Ingrese base: "))
    Tabla(Base)
main()

'''
'''
def esPrimo(Numero):
    
    i = 1
    Contador = 0

    while(i<=Numero):
        if(Numero%i == 0):
            Contador += 1
        i+=1
    
    if(Contador == 2):
        return True
    else:
        return False

def Tabla(Cantidad):

    CantidadColumnas = 0

    print("\nPrimeros {:d} primos: \n".format(Cantidad))

    Contador = 0
    i = 1

    while(Contador<Cantidad):
        if(esPrimo(i)):
            
            if(CantidadColumnas<9):
                print("{:8d}".format(i),end="")
                CantidadColumnas += 1
            else:
                print("{:8d}".format(i))
                CantidadColumnas = 0
            i+=1
            Contador += 1
        
        else:
            i+=1

    print("\n\nPrimos entre 1 y {}: \n".format(Cantidad))

    CantidadColumnas = 0

    for i in range(1,Cantidad+1):
        if(esPrimo(i)):
            if(CantidadColumnas<9):
                print("{:8d}".format(i),end="")
                CantidadColumnas += 1
            else:
                print("{:8d}".format(i))
                CantidadColumnas = 0

def main():
    Cantidad = int(input("Ingrese cantidad: "))
    Tabla(Cantidad)
main()

'''

#FIGURAS
'''
def figura(Base):
    for fila in range(Base):
        for columna in range(Base):
            if (fila-columna>=0):
                print("* ",end="")
            else:
                print("  ",end="")
        print("")

def main():
    Base = int(input("Ingrese base: "))
    while(Base<3):
        Base = int(input("ERROR. Ingrese base: "))
    figura(Base)
main()
'''
'''
def figura(Base):
    for fila in range((Base//2)+1):
        for columna in range(Base):
            if (columna<=Base//2 and fila+columna>=Base//2) or (columna>=Base//2 and columna-fila<=Base//2):
                print("* ",end="")
            else:
                print("  ",end="")
        print("")

def main():
    Base = int(input("Ingrese base: "))
    while(Base%2 == 0 or Base<3):
        Base = int(input("ERROR. Ingrese base: "))
    figura(Base)
main()
'''
'''
def figura(Altura):
    for fila in range(Altura):
        for columna in range(Altura):
            if (columna<=Altura//2 and fila+columna<=Altura-1 and fila-columna>=0):
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def main():
    Altura = int(input("Ingrese altura: "))
    while(Altura%2 == 0 or Altura<5):
        Altura = int(input("ERROR. Ingrese altura: "))
    figura(Altura)
main()
'''

def figura(Diagonal):
    for fila in range(Diagonal):
        for columna in range(Diagonal):
            if (columna<=Diagonal//2 and fila+columna>=Diagonal//2 and fila-columna<=Diagonal//2) or (columna>=Diagonal//2 and columna-fila<=Diagonal//2 and fila-columna<Diagonal//2):
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def main():
    Diagonal = int(input("Ingrese Diagonal: "))
    while(Diagonal%2 == 0 or Diagonal<5):
        Diagonal = int(input("ERROR. Ingrese Diagonal: "))
    figura(Diagonal)
main()