#3.1

def liquidar():

    ArchivoVentaTarjetas = open("ventaTarjetas.txt","r")
    ListaVentaTarjetas = ArchivoVentaTarjetas.readlines()
    for i in range(len(ListaVentaTarjetas)):
        ListaVentaTarjetas[i] = ListaVentaTarjetas[i][:-1].split(",")

    ArchivoVendedores = open("vendedores.txt","r")
    ListaVendedores = ArchivoVendedores.readlines()
    for i in range(len(ListaVendedores)):
        ListaVendedores[i] = ListaVendedores[i][:-1].split(",")

    ArchivoLiquidacionDeComisiones = open("liquidacionComisiones.txt","w")

    Lista = []

    for i in range(len(ListaVendedores)):

        CodigoVendedor = ListaVendedores[i][0]
        ObjetivoTarjetasAnual = int(ListaVendedores[i][2])
        SueldoAnual = float(ListaVendedores[i][3])
        CantidadTarjetas = 0
        Sublista = []
        for j in range(len(ListaVentaTarjetas)):
            
            if(CodigoVendedor == ListaVentaTarjetas[j][0]):
                CantidadTarjetas += int(ListaVentaTarjetas[j][2])
        
        if(CantidadTarjetas < ObjetivoTarjetasAnual*0.8):
            Comision = 0

        if(CantidadTarjetas >= ObjetivoTarjetasAnual*0.8 and CantidadTarjetas < ObjetivoTarjetasAnual):
            Comision = SueldoAnual*0.03
    
        if(CantidadTarjetas>ObjetivoTarjetasAnual):
            Comision = SueldoAnual*0.1


        ArchivoLiquidacionDeComisiones.write(CodigoVendedor + "," + str(Comision) + "\n")

    ArchivoVentaTarjetas.close()
    ArchivoVendedores.close()
    ArchivoLiquidacionDeComisiones.close()


def main():
    liquidar()
main()

def topCinco():

    ArchivoLiquidacionComisiones = open("liquidacionComisiones.txt","r")
    ListaArchivoLiquidacionComisiones = ArchivoLiquidacionComisiones.readlines()
    for i in range(len(ListaArchivoLiquidacionComisiones)):
        ListaArchivoLiquidacionComisiones[i] = ListaArchivoLiquidacionComisiones[i][:-1].split(",")
    
    ArchivoVendedores = open("vendedores.txt","r")
    ListaArchivoVendedores = ArchivoVendedores.readlines()
    for i in range(len(ListaArchivoVendedores)):
        ListaArchivoVendedores[i] = ListaArchivoVendedores[i][:-1].split(",")
    
    for i in range(len(ListaArchivoLiquidacionComisiones)):
        for j in range(len(ListaArchivoLiquidacionComisiones)):
            if(float(ListaArchivoLiquidacionComisiones[j][1]) < float(ListaArchivoLiquidacionComisiones[i][1])):
                (ListaArchivoLiquidacionComisiones[i],ListaArchivoLiquidacionComisiones[j]) = (ListaArchivoLiquidacionComisiones[j],ListaArchivoLiquidacionComisiones[i])
    
    for i in range(len(ListaArchivoLiquidacionComisiones)):
        CodigoVendedor = ListaArchivoLiquidacionComisiones[i][0]
        Comision = ListaArchivoLiquidacionComisiones[i][1]

        for j in range(len(ListaArchivoVendedores)):
            if(CodigoVendedor == ListaArchivoVendedores[j][0]):
                Nombre = ListaArchivoVendedores[j][1]

        print("Codigo vendedor: {}. Nombre vendedor: {}. Comision: {}\n".format(CodigoVendedor,Nombre,Comision))                

def main():
    topCinco()
main()