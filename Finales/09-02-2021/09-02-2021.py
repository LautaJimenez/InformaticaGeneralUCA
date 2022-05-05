from typing import List

#01

def Aprobadas(ListaAlumnos,ListaMaterias,ListaCursadas,NombreAlumno):

    for i in range(len(ListaAlumnos)):
        ListaAlumnos[i] = ListaAlumnos[i][:-1].split(",")

    for i in range(len(ListaMaterias)):
        ListaMaterias[i] = ListaMaterias[i][:-1].split(",")

    for i in range(len(ListaCursadas)):
        ListaCursadas[i] = ListaCursadas[i][:-1].split(",")
    
    Lista = []

    for i in range(len(ListaAlumnos)):
        if(NombreAlumno == ListaAlumnos[i][1]):
            IDAlumno = ListaAlumnos[i][0]

            for j in range(len(ListaCursadas)):
                if(IDAlumno == ListaCursadas[j][1]):
                    Nota = float(ListaCursadas[j][2])
                    IDMateria = ListaCursadas[j][0]

                    for k in range(len(ListaMaterias)):
                        if(ListaMaterias[k][0] == IDMateria):
                            NombreMateria = ListaMaterias[k][1]
                            if(Nota>=4):
                                Tupla = (NombreMateria,Nota)
                                Lista.append(Tupla)

    return(Lista)

def main():

    lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n','180372,Vicente Pernia\n']
    lstMaterias = ['132,Informática Gral\n', '127,Álgebra y Geometría\n', '137,Física I\n']
    lstCursadas = ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n' ,'132,152002,2.0\n', '132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']
    print(Aprobadas(lstAlumnos,lstMaterias,lstCursadas,"Ricardo Bochini"))
main()

#02

def segmentos(ListaAlumnos,ListaMaterias,ListaCursadas):

    for i in range(len(ListaAlumnos)):
        ListaAlumnos[i] = ListaAlumnos[i][:-1].split(",")

    for i in range(len(ListaMaterias)):
        ListaMaterias[i] = ListaMaterias[i][:-1].split(",")

    for i in range(len(ListaCursadas)):
        ListaCursadas[i] = ListaCursadas[i][:-1].split(",")
    
    ListaM = []
    ListaR = []
    ListaB = []
    ListaE = []
    Diccionario = {}

    for i in range(len(ListaCursadas)):
        Nota = float(ListaCursadas[i][2])
        IDAlumno = ListaCursadas[i][1]
        IDMateria = ListaCursadas[i][0]
        Sublista = []
        
        for j in range(len(ListaMaterias)):
            if(IDMateria == ListaMaterias[j][0]):
                NombreMateria = ListaMaterias[j][1]
        
        for k in range(len(ListaAlumnos)):
            if(IDAlumno == ListaAlumnos[k][0]):
                NombreAlumno = ListaAlumnos[k][1]

        Sublista.append(NombreMateria)
        Sublista.append(NombreAlumno)
        
        if(Nota<4):
            ListaM.append(Sublista)
        if(Nota>=4 and Nota<7):
            ListaR.append(Sublista)
        if(Nota>=7 and Nota<8):
            ListaB.append(Sublista)
        if(Nota>=8 and Nota<=10):
            ListaE.append(Sublista)
        
    Diccionario["M"] = ListaM
    Diccionario["R"] = ListaR 
    Diccionario["B"] = ListaB
    Diccionario["E"] = ListaE

    return Diccionario           

def main():
    lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n','180372,Vicente Pernia\n']
    lstMaterias = ['132,Informática Gral\n', '127,Álgebra y Geometría\n', '137,Física I\n']
    lstCursadas = ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n' ,'132,152002,2.0\n', '132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']
    print(segmentos(lstAlumnos ,lstMaterias ,lstCursadas))
main()