#01

from typing import List

def OrdenarLista(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i][1] > Lista[j][1]):
                (Lista[i],Lista[j]) = (Lista[j],Lista[i])
    
def media_01(n,ArchivoCiudad,ArchivoResiduos):

    Ciudades = open(ArchivoCiudad,"r")
    ListaCiudades = Ciudades.readlines()
    for i in range(len(ListaCiudades)):
        ListaCiudades[i] = ListaCiudades[i][:-1].split(",")
    
    Residuos = open(ArchivoResiduos,"r")
    ListaResiduos = Residuos.readlines()
    for i in range(len(ListaResiduos)):
        ListaResiduos[i] = ListaResiduos[i][:-1].split(",")
    
    Contador = 0
    ResiduosTotales = 0
    for i in range(len(ListaResiduos)):
        ResiduosTotales += int(ListaResiduos[i][0])
        Contador += 1
    
    PromedioTotal = round(ResiduosTotales/Contador,2)

    Lista = []

    for i in range(len(ListaCiudades)):
        IDCiudad = ListaCiudades[i][0]
        Nombre = ListaCiudades[i][1]
        Residuos = 0
        Contador = 0    
        Sublista = []
        
        for j in range(len(ListaResiduos)):
            if(IDCiudad == ListaResiduos[j][1]):
                Residuos += int(ListaResiduos[j][0])
                Contador += 1
        
        if(Contador!=0):
            Sublista.append(Nombre)
            Promedio = round(Residuos/Contador,2)
            Sublista.append(Promedio)
            Lista.append(Sublista)
    
    OrdenarLista(Lista)    
    Lista = Lista[0:n]
    
    Tupla = (PromedioTotal,Lista)
    
    return Tupla

def main():
    print(media_01(3,"ciudad.txt","residuos.txt"))
main()

#02

def media_02(ArchivoResiduos):

    Residuos = open(ArchivoResiduos,"r")
    ListaResiduos = Residuos.readlines()
    for i in range(len(ListaResiduos)):
        ListaResiduos[i] = ListaResiduos[i][:-1].split(",")

    Diccionario = {}

    for i in range(len(ListaResiduos)):
        Mes = ListaResiduos[i][2][2:4]
        Contador = 0
        Suma = 0

        for j in range(len(ListaResiduos)):
            if(Mes == ListaResiduos[j][2][2:4]):
                Suma += int(ListaResiduos[j][0])
                Contador += 1
        
        if(Contador != 0):
            Promedio = Suma/Contador
        
        Diccionario[Mes] = Promedio
    
    print(Diccionario)

def main():
    print(media_02("residuos.txt"))
main()

