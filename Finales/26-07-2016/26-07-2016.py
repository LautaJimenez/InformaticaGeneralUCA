#3.1

def cantHabitantes(nombreLocalidad,hijos):
    
    ArchivoHabitantes = open("habitantes.txt","r")
    ListaHabitantes = ArchivoHabitantes.readlines()
    for i in range(len(ListaHabitantes)):
        ListaHabitantes[i] = ListaHabitantes[i][:-1].split(",")

    ArchivoLocalidades = open("localidades.txt","r")
    ListaLocalidades = ArchivoLocalidades.readlines()
    for i in range(len(ListaLocalidades)):
        ListaLocalidades[i] = ListaLocalidades[i][:-1].split(",")

    ArchivoHabitantesPorLocalidad = open("habitantesXlocalidad.txt","r")
    ListaHabitantesPorLocalidad = ArchivoHabitantesPorLocalidad.readlines()
    for i in range(len(ListaHabitantesPorLocalidad)):
        ListaHabitantesPorLocalidad[i] = ListaHabitantesPorLocalidad[i][:-1].split(",")

    Lista = []

    for i in range(len(ListaLocalidades)):
        if(nombreLocalidad == ListaLocalidades[i][1]):
            IDLocalidad = ListaLocalidades[i][0]

            for j in range(len(ListaHabitantesPorLocalidad)):
                if(IDLocalidad == ListaHabitantesPorLocalidad[j][0]):
                    IDHabitante = ListaHabitantesPorLocalidad[j][1]
            
                    for k in range(len(ListaHabitantes)):
                        Sublista = []
                        if(IDHabitante == ListaHabitantes[k][0] and hijos == int(ListaHabitantes[k][2])):
                                Nombre = ListaHabitantes[k][1]
                                Sublista.append(IDHabitante)
                                Sublista.append(Nombre)
                                Lista.append(Sublista)          

    print(Lista)

def main():

    NombreLocalidad = input("Ingrese nombre de la localidad: ")
    Hijos = int(input("Ingrese la cantidad de hijos: "))
    cantHabitantes(NombreLocalidad,Hijos)

main()

#3.2

def EliminarElementosRepetidos(Lista):
    ListaAux = []
    
    for i in range(len(Lista)):
        if(Lista[i] not in ListaAux):
            ListaAux.append(Lista[i])
    
    return ListaAux

def EliminarElementosNoCosiderados(Lista):
    for i in range(len(Lista)):
        if(len(Lista[i])>2):
            del Lista[i][0:2]

def OrdenarLista(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i][0]<Lista[j][0]):
                (Lista[i],Lista[j]) = (Lista[j],Lista[i])
                
def edadXlocalidad():

    ArchivoHabitantes = open("habitantes.txt","r")
    ListaHabitantes = ArchivoHabitantes.readlines()
    for i in range(len(ListaHabitantes)):
        ListaHabitantes[i] = ListaHabitantes[i][:-1].split(",")

    ArchivoLocalidades = open("localidades.txt","r")
    ListaLocalidades = ArchivoLocalidades.readlines()
    for i in range(len(ListaLocalidades)):
        ListaLocalidades[i] = ListaLocalidades[i][:-1].split(",")

    ArchivoHabitantesPorLocalidad = open("habitantesXlocalidad.txt","r")
    ListaHabitantesPorLocalidad = ArchivoHabitantesPorLocalidad.readlines()
    for i in range(len(ListaHabitantesPorLocalidad)):
        ListaHabitantesPorLocalidad[i] = ListaHabitantesPorLocalidad[i][:-1].split(",")

    Lista = []

    for i in range(len(ListaLocalidades)):
        IDLocalidad = ListaLocalidades[i][0]
        Contador = 0
        Edad = 0
        Sublista = []

        for j in range(len(ListaHabitantesPorLocalidad)):
            if(IDLocalidad == ListaHabitantesPorLocalidad[j][0]):
                IDHabitante = ListaHabitantesPorLocalidad[j][1]
                
                for k in range(len(ListaHabitantes)):
                    if(IDHabitante == ListaHabitantes[k][0]):
                        Edad += int(ListaHabitantes[k][3])
                        Contador += 1
        
                        if(Contador!=0):
                            Promedio = Edad / Contador       
                        
                        Sublista.append(IDLocalidad)
                        Sublista.append(Promedio)
                        Lista.append(Sublista)
    
    Lista = EliminarElementosRepetidos(Lista)
    EliminarElementosNoCosiderados(Lista)
    OrdenarLista(Lista)

    print("\n\n{} {:>20}".format("ID Localidad","Promedio edad"))
    for i in range(len(Lista)):
        print("{:>5} {:>20}".format(Lista[i][0],Lista[i][1]))

def main():
    edadXlocalidad()
main()