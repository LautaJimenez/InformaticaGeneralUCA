#Ejercicio 1

'''
#Ejercicio 01

def OrdenarListaPorGeneracion(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(int(Lista[i][3]) > int(Lista[j][3])):
                (Lista[i],Lista[j]) = (Lista[j],Lista[i])

    return Lista

def OrdenarListaPorFecha(Lista):
    for i in range(len(Lista)):
        for j in range(len(Lista)):
            if(Lista[i][4] > Lista[j][4]):
                (Lista[i],Lista[j]) = (Lista[j],Lista[i])

    return Lista

def maximo(lsArch,n):

    for i in range(len(lsArch)):
        lsArch[i] = lsArch[i][:-1].split(",")
    
    lsArch = lsArch[1:]
    lstArch = OrdenarListaPorGeneracion(lsArch)
    lstArch = lstArch[0:n]
    lstArch = OrdenarListaPorFecha(lstArch)
    
    print("{:20}{:20}{:20}".format("central","generacion","anio_mes"))
    for i in range(len(lstArch)):
        print("{:20}{:20}{:20}".format(lstArch[i][0],lstArch[i][3],lstArch[i][4]))


def main():
    lsArch = ["central,region,fuente,generacion,anio_mes\n", "CAPE,COMAHUE,Termica,21868984,2020-01\n",
    "AESP,BUENOS AIRES,Termica,193938412,2012-01\n","CAPE,COMAHUE,Termina,20009911,2017-03\n",
    "ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n","AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n",
    "ANAT,NOROESTE,Termica,7670154,2018-07\n","APAR,BUENOS AIRES,Termica,1077474,2015-09\n",
    "ARAUEO,NOROESTE,Renovable,844759,2017-02\n","ARROHI,COMAHUE,Hidraulica,2961,2021-01\n",
    "ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n","ULNIFV,CUYO,Renovable,5779081,2020-03\n",
    "APAR,BUENOS AIRES,Termica,43969,2020-02\n","VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n"]
    
    n = 5
    print("Para n =",n)
    maximo(lsArch,n)
main()

'''

#Ejercicio 02

def filtrar(lsArch,lsCol,diFiltro):

    for i in range(len(lsArch)):
        lsArch[i] = lsArch[i][:-1].split(",")
    lsArch = lsArch[1:]
    
    ListaCentrales = [] ; ListaRegiones = [] ; ListaFuentes = [] ; ListaGeneraciones = [] ; ListaFecha = []

    for i in range(len(lsArch)):
        ListaCentrales.append(lsArch[i][0])
        ListaRegiones.append(lsArch[i][1])
        ListaFuentes.append(lsArch[i][2])
        ListaGeneraciones.append(lsArch[i][3])
        ListaFecha.append(lsArch[i][4])

    Clave = ""
    Indice = ""

    if(diFiltro!={}):
        Clave = (list(diFiltro.keys()))
        Clave = Clave[0]
        Respuesta = diFiltro.get(Clave)
    
    for i in range(len(lsCol)):
        print("{:10}".format(lsCol[i]),end="")
    
    print("\n")
    
    for i in range(len(lsArch)):
        for j in range(len(lsCol)):
            if(lsCol[j] == Clave):
                Indice = 
                print("{:10}".format(lsArch[i][0]),end="")
            
            if(lsCol[j] == "anio_mes"):
                print("{:10}".format(lsArch[i][4]))

def main():
    lsArch = ["central,region,fuente,generacion,anio_mes\n", "CAPE,COMAHUE,Termica,21868984,2020-01\n",
    "AESP,BUENOS AIRES,Termica,193938412,2012-01\n","CAPE,COMAHUE,Termina,20009911,2017-03\n",
    "ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n","AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n",
    "ANAT,NOROESTE,Termica,7670154,2018-07\n","APAR,BUENOS AIRES,Termica,1077474,2015-09\n",
    "ARAUEO,NOROESTE,Renovable,844759,2017-02\n","ARROHI,COMAHUE,Hidraulica,2961,2021-01\n",
    "ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n","ULNIFV,CUYO,Renovable,5779081,2020-03\n",
    "APAR,BUENOS AIRES,Termica,43969,2020-02\n","VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n"]
    
    lsCol = ["central","anio_mes"]
    diFiltro = {"anio_mes":"2020-01"}
    
    filtrar(lsArch,lsCol,diFiltro)
main()