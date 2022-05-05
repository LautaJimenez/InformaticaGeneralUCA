# ESPRIMO
'''
def esPrimo(Num):

    EsPrimo = True
    for i in range(2,Num):
        if(Num%i == 0):
            EsPrimo = False
    
    print(EsPrimo) 
esPrimo(20)

def esPrimo(Num):
    EsPrimo = True
    i = 2
    while(i<Num):
        if(Num%i == 0):
            EsPrimo = False
        i+=1
    return EsPrimo

def Funcion1(cantidad):
    ContadorColumnas = 0
    for i in range(2,cantidad):
        if(esPrimo(i)):
            if(ContadorColumnas<9):
                print("{:4}".format(i),end="")
                ContadorColumnas += 1
            else:
                print("{:>4}".format(i))
                ContadorColumnas = 0

def Funcion2(cantidad):
    Contador = 0
    Numero = 2
    CantidadColumnas = 0
    while(Contador<cantidad):
        if(esPrimo(Numero)):
            Contador += 1
            if(CantidadColumnas<9):
                print("{:4}".format(Numero),end="")
                CantidadColumnas+=1
            else:
                print("{:4}".format(Numero))
                CantidadColumnas=0
        Numero += 1

def main():
    cantidad = 57
    #Funcion1(cantidad)
    Funcion2(cantidad)
main()

'''
'''
#ORDENAR LISTA

def OrdenarLista(Lista):

    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i]>Lista[j]):
                # Aux = Lista[i]
                # Lista[i] = Lista[j]
                # Lista[j] = Aux
                (Lista[i],Lista[j]) = (Lista[j],Lista[i])
    return Lista

def main():
    Lista = [99,11,33,77,22,66,88,44,55]
    print(OrdenarLista(Lista))
main()

'''
'''
#Figura de rombo

def Figura(Base):

    for fila in range(Base):
        for columna in range(Base):
            if (fila+columna >= Base-1-Base//2) and (fila>=columna-Base//2) and (fila+columna <= Base-1+Base//2) and (fila <= columna+Base//2):
                print("* ",end="")
            else:
                print("- ",end="")
        print("")

def main():
    Base = 9
    Figura(Base)
main()

'''
'''
#Numero decimal a binario

def DecimalABinario(Numero):
    Resto = 0
    i = 1
    Binario = 0
    while(Numero>0):
        Resto = Numero%2
        Numero = Numero//2
        Binario = Binario +(Resto*i)
        i = i*10
    return Binario

def main():
    Decimal = 123
    print(DecimalABinario(Decimal))
main()

#Para pasar a octal, etc, únicamente se cambia el //2 y el %8

'''
