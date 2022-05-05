#Ejercicio1

'''
def estaEnListaConIn(num,lst):

    if num in lst:
        return True
    else:
        return False
    
def estaEnListaConFor(num,lst):
    for i in range(len(lst)):
        if(lst[i] == num):
            return True
    return False

def estaEnListaConWhile(num,lst):
    
    i = 0
    while(i<len(lst)):
        if(lst[i] == num):
            return True
        i+=1
    return False

def main():
    Lista = [2,3,4,5,6,7,8]
    Numero = 23
    print(estaEnListaConIn(Numero,Lista))
    print(estaEnListaConFor(Numero,Lista))
    print(estaEnListaConWhile(Numero,Lista))
main()

'''
'''
#Ejercicio 2

def CargarLista():
    Lista = []
    Numero = int(input("Ingresar números o cero para terminar: "))
    while(Numero<0):
        Numero =  int(input("Error, número NO positivo."))
    
    while(Numero!=0):
        Lista.append(Numero)
        Numero = int(input("Ingresar números o cero para terminar: "))
        while(Numero<0):
            Numero =  int(input("Error, número NO positivo: "))
        while(Numero in Lista):
            Numero =  int(input("Error, número repetido: "))

    return Lista

def main():
    print("La lista contiene {}".format(CargarLista()))
main()

'''
'''
#Ejercicio 3

def CargarLista(Lista):
    
    Numero = int(input("Ingrese número o cero para terminar: "))
    while(Numero<0):
        Numero = int(input("Error. Ingresar número positivo."))

    while(Numero!=0):
        Lista.append(Numero)
        Numero = int(input("Ingrese número o cero para terminar: "))
        while(Numero<0):
            Numero = int(input("Error. Ingresar número positivo: "))
        while(Numero in Lista):
            Numero = int(input("Error. Numero repetido en la lista: "))
            while(Numero<0):
                Numero = int(input("Error. Ingresar número positivo: "))

def CargarConjuntos(Lista1,Lista2):
    print("\nCarga la primera lista: \n")
    Lista1 = CargarLista(Lista1)
    print("\nCarga la segunda lista: \n")
    Lista2 = CargarLista(Lista2)

def Union(Lista1,Lista2):
    ListaNueva = []
    
    for i in range(len(Lista1)):
        ListaNueva.append(Lista1[i])

    for i in range(len(Lista2)):
        if(Lista2[i] not in ListaNueva):
            ListaNueva.append(Lista2[i])
    
    return ListaNueva

def Interseccion(Lista1,Lista2):
    ListaNueva = []
    for i in range(len(Lista1)):
        if(Lista1[i] in Lista2):
            ListaNueva.append(Lista1[i])
    
    return ListaNueva

def Diferencia(Lista1,Lista2):
    
    ListaNueva = []

    for i in range(len(Lista1)):
        ListaNueva.append(Lista1[i])
    
    for i in range(len(Lista2)):
        if(Lista2[i] in ListaNueva):
            ListaNueva.remove(Lista2[i])

    return ListaNueva

def DiferenciaSimetrica(Lista1,Lista2):

    ListaNueva = []
 
    for i in range(len(Lista1)):
        ListaNueva.append(Lista1[i])
    
    for i in range(len(Lista2)):
        ListaNueva.append(Lista2[i])
    
    for i in range(len(Lista1)):
        if(Lista1[i] in Lista2):
            ListaNueva.remove(Lista1[i])

    for i in range(len(Lista2)):
        if(Lista2[i] in Lista1):
            ListaNueva.remove(Lista2[i])
    
    return ListaNueva

def main():
    Lista1 = [] ; Lista2 = []
    print("1. CARGAR CONJUNTOS\n2. UNION\n3. INTERSECCION\n4. DIFERENCIA (A-B)\n5. DIFERENCIA SIMETRICA\n6. SALIR\n")
    Valor = int(input("Ingrese el valor de la opción: "))
    while(Valor!=6):
        
        if(Valor == 1):
            CargarConjuntos(Lista1,Lista2)
        
        if(Valor == 2):
            print("\nLa unión de las listas son {}".format(Union(Lista1,Lista2)))
        
        if(Valor == 3):
            print("\nLa intersección de las listas son {}".format(Interseccion(Lista1,Lista2)))

        if(Valor == 4):
            print("\nLa diferencia de las listas es: {}".format(Diferencia(Lista1,Lista2)))
        
        if(Valor == 5):
            print("\nLa diferencia simétrica de las listas es: {}".format(DiferenciaSimetrica(Lista1,Lista2)))
        
        print("\n1. CARGAR CONJUNTOS\n2. UNION\n3. INTERSECCION\n4. DIFERENCIA (A-B)\n5. DIFERENCIA SIMETRICA\n6. SALIR\n")
        Valor = int(input("Ingrese el valor de la opción: "))
    
main()

'''

#Ejercicio 5
'''


import random

def CargarLista():
    Lista = []
    Numero = int(input("Ingrese numero positivo o cero para terminar: "))
    
    while(Numero<0):
        Numero = int(input("Error.Ingrese numero positivo: "))
    
    while(Numero!=0):
        Lista.append(Numero)
        Numero = int(input("Ingrese numero positivo o cero para terminar: "))
        while(Numero<0):
            Numero = int(input("Error. Ingrese numero positivo: "))
        while(Numero in Lista):
            Numero = int(input("Error. El número esta repetido: "))
            while(Numero<0):
                Numero = int(input("Error. Ingresar número positivo: "))

    return Lista

def CambiaLista(Lista,a,b):
    
    for i in range(len(Lista)):
        if(Lista[i]<a or Lista[i]>b):
            Lista[i] = random.randint(a,b)
    
def main():
    Lista = CargarLista()
    print("Lista generada: {}".format(Lista))
    A = int(input("\nIngrese límite a del rango: "))
    B = int(input("Ingrese límite b del rango: "))
    CambiaLista(Lista,A,B)
    print("\nLa lista modificada es: {}".format(Lista))
main()

'''

#Ejercicio 6
'''
def CargarLista():
    Lista = []
    Numero = int(input("Ingrese numero positivo o cero para terminar: "))
    
    while(Numero<0):
        Numero = int(input("Error.Ingrese numero positivo: "))
    
    while(Numero!=0):
        Lista.append(Numero)
        Numero = int(input("Ingrese numero positivo o cero para terminar: "))
        while(Numero<0):
            Numero = int(input("Error. Ingrese numero positivo: "))
        while(Numero in Lista):
            Numero = int(input("Error. El número esta repetido: "))
            while(Numero<0):
                Numero = int(input("Error. Ingresar número positivo: "))

    return Lista

def OrdenarLista(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i]<Lista[j]):
                Aux = Lista[i]
                Lista[i] = Lista[j]
                Lista[j] = Aux
    
    return Lista

def main():
    Lista = CargarLista()
    print("\nLista generada: {}".format(Lista))
    print("\nLa lista ordenada es {}".format(OrdenarLista(Lista)))
main()
'''

#Ejercicio 7
'''


def CargarLista():
    Lista = []
    Numero = int(input("Ingrese número positivo o cero para terminar: "))
    
    while(Numero<0):
        Numero = int(input("Error. Ingrese número positivo: "))
    
    while(Numero!=0):
        
        Lista.append(Numero)
        Numero = int(input("Ingrese número positivo o cero para terminar: "))

        while(Numero<0):
            Numero = int(input("Error. Ingrese número positivo: "))

        while(Numero in Lista):
            Numero = int(input("Error. Ingrese número repetido: "))
            while(Numero<0):
                Numero = int(input("Error. Ingrese número positivo: "))
    return Lista

def OrdenarLista(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i]<Lista[j]):
                Aux = Lista[i]
                Lista[i] = Lista[j]
                Lista[j] = Aux
    return Lista

def inserOrd(Lista,Valor):
    Contador = 0
    
    for i in range(len(Lista)):
        if(Lista[i]>Valor):
            if(Contador == 0): 
                Lista.insert(i,Valor)
                Contador = 1
    
    return Lista

def main():
    Lista = CargarLista()
    Lista = OrdenarLista(Lista)
    print("\nLista generada: {}".format(Lista))
    Valor = int(input("\nIngrese valor a insertar: "))
    print("\nLa lista con inserción ordenada es: {}".format(inserOrd(Lista,Valor)))
main()

'''
#Ejercicio 8
'''
def inserOrd(Lista,Numero):
    Contador = 0
    for i in range(len(Lista)):
        if(Lista[i]>Numero):
            if(Contador==0):
                Lista.remove(Numero)
                Lista.insert(i,Numero)
                Contador = 1

def CargarLista():
    Lista = []
    Numero = int(input("Ingrese número positivo o cero para terminar: "))
    
    while(Numero<0):
        Numero = int(input("Error. Ingrese número positivo o cero para terminar: "))
    
    while(Numero!=0):
        Lista.append(Numero)
        inserOrd(Lista,Numero)
        Numero = int(input("Ingrese número positivo o cero para terminar: "))
        while(Numero<0):
            Numero = int(input("Error. Ingrese número positivo o cero para terminar: "))
        while(Numero in Lista):
            Numero = int(input("Error. Número repetido: "))
            while(Numero<0):
                Numero = int(input("Error. Ingrese número positivo o cero para terminar: "))

    return Lista

def main():
    print("La lista ordenada es: {}".format(CargarLista()))
main()

'''

#Ejercicio 9
'''
def CargarListaAlumnos():
    Lista = []
    Sublista = []
    DNIAlumno = int(input("Ingrese DNI de alumno: "))
    NombreAlumno = input("Ingrese nombre del alumno: ")
    EdadAlumno = int(input("Ingrese edad de alumno: "))
    while(DNIAlumno != 0):
        Sublista.append(DNIAlumno)
        Sublista.append(NombreAlumno)
        Sublista.append(EdadAlumno)
        Lista.append(Sublista)
        print("\n¡Alumno ingresado!\n")
        Sublista = []
        DNIAlumno = int(input("Ingrese DNI de alumno: "))
        if(DNIAlumno!=0):
            NombreAlumno = input("Ingrese nombre del alumno: ")
            EdadAlumno = int(input("Ingrese edad de alumno: "))
    
    return Lista

def OrdenarListaPorDNI(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i][0]>Lista[j][0]):
                Aux = Lista[i]
                Lista[i] = Lista[j]
                Lista[j] = Aux

    return Lista

def main():
    Lista = CargarListaAlumnos()
    print(OrdenarListaPorDNI(Lista))
main()
'''

#Ejercicio 10
'''
import random

def CargarListaAleatoria(A,B,Cantidad):
    Lista = []
    while(len(Lista)<Cantidad):
        Numero = random.randint(A,B)
        Lista.append(Numero)
    return Lista

def AtributoTriple(Lista):
    Contador = 0
    for i in range(len(Lista)-1,-1,-1):
        if(i-2>=0):
            if(Lista[i]==Lista[i-1] and Lista[i] == Lista[i-2]):
                Contador += 1
    
    if(Contador == 0):
        return "NADA"
    if(Contador == 1):
        return "Un triple"
    if(Contador == 2):
        return "Dos triples"
    if(Contador>2):
        return "+ triples"


def main():
    Cantidad = int(input("Ingrese cantidad de numeros a ingresar: "))
    A = int(input("Ingrese el menor valor del intervalo: "))
    B = int(input("Ingrese el mayor valor del intervalo: "))
    Lista = CargarListaAleatoria(A,B,Cantidad)
    print(Lista)
    print("")
    print(AtributoTriple(Lista))
main()

'''
#Ejercicio 11
'''
import random

def Ruleta():
    Cantidad = int(input("Ingrese cantidad de números a ingresar: "))
    Lista = []
    while(len(Lista) < Cantidad):
        Lista.append(random.randint(0,36))
    
    return Lista

def Porcentual(Lista):
    Cantidad = len(Lista)
    Contador = 0
    ListaAuxiliar = []
    for i in range(len(Lista)):
        if(Lista[i] not in ListaAuxiliar):
            for j in range(len(Lista)):
                if(Lista[i]==Lista[j]):
                    Contador += 1
                    ListaAuxiliar.append(Lista[i])
            Porcentaje = int((Contador/Cantidad)*100)
            if(Contador == 1):
                print("El número {} salió {} vez ({}%).".format(Lista[i],Contador,Porcentaje))
            else:
                print("El número {} salió {} veces ({}%).".format(Lista[i],Contador,Porcentaje))
            Contador = 0

def main():
    Lista = Ruleta()
    Porcentual(Lista)
main()
'''
'''

#Ejercicio 12

def Operaciones(A,B):
    Suma = A+B
    Resta = A-B
    Multiplicacion = A*B
    if(B!=0):
        Division = A/B
    else:
        Division = None
    Tupla = (Suma,Resta,Multiplicacion,Division)
    return Tupla


def main():
    A = int(input("Ingresar primer valor: "))
    B = int(input("Ingresar segundo valor: "))
    print(Operaciones(A,B))
main()

'''
'''
def ingresar():
    num = int(input("Ingrese numero: "))
    while (num%2 == 0 or num%3 != 0 or num%7==0):
        print("Error")
        num = int(input("Ingrese numero: "))

    return num
ingresar()
'''

def fun(lst,di):
    di = {}
    i = 0
    while(i<len(lst)):
        clave = lst[i]
        di[clave] = i
        i = i+1
    return di

def main():
    di = {"x":10}
    lst = ["a","b"]
    di = fun(lst,di)
    print(di)
main()