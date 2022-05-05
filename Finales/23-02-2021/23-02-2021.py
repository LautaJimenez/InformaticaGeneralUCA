#01

from os import read, readlink
from typing import List

def minimos(ArchivoEnergia):

    Energia = open(ArchivoEnergia,"r")
    ListaEnergia = Energia.readlines()
    for i in range(len(ListaEnergia)):
        ListaEnergia[i] = ListaEnergia[i][:-1].split(",")
    
    Minimo = float(ListaEnergia[0][2])

    for i in range(len(ListaEnergia)):
        if(float(ListaEnergia[i][2])<=Minimo):
            AñoMinimo = ListaEnergia[i][0][0:2]
            MesYAñoMinimo = ListaEnergia[i][0][0:4]
            Minimo = float(ListaEnergia[i][2])

    Tupla1 = (AñoMinimo,Minimo)   
    Tupla2 = (MesYAñoMinimo,Minimo)
    Lista = []
    Lista.append(Tupla1)
    Lista.append(Tupla2)

    return Lista

def main():
    print(minimos("energia.txt"))
main()

#02

def OrdenarLista(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i][1] > Lista[j][1]):
                (Lista[i],Lista[j]) = (Lista[j],Lista[i])

def energiaTotal(n,ArchivoEnergia,ArchivoParques):

    Energia = open(ArchivoEnergia,"r")
    ListaEnergia = Energia.readlines()
    for i in range(len(ListaEnergia)):
        ListaEnergia[i] = ListaEnergia[i][:-1].split(",")
    
    Parques = open(ArchivoParques,"r")
    ListaParques = Parques.readlines()
    for i in range(len(ListaParques)):
        ListaParques[i] = ListaParques[i][:-1].split(",")
    
    Lista = []

    for i in range(len(ListaParques)):
        NombreParque = ListaParques[i][1]
        IDParque = int(ListaParques[i][0])
        CantidadMolinos = int(ListaParques[i][2])
        SumaEnergia = 0
        Sublista = []

        for j in range(len(ListaEnergia)):
            if(IDParque == int(ListaEnergia[j][1])):
                SumaEnergia += float(ListaEnergia[j][2])

        Sublista.append(NombreParque)
        Sublista.append(SumaEnergia)
        Sublista.append(SumaEnergia/CantidadMolinos)  
        Lista.append(Sublista)

    OrdenarLista(Lista)
    Lista = Lista[0:n]
    return Lista

def main():
    print(energiaTotal(3,"energia.txt","parques.txt"))
main()