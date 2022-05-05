#3.1

def factura(ID_Abonado):

    ArchivoAbonados = open("abonados.txt","r")
    ListaAbonados = ArchivoAbonados.readlines()
    for i in range(len(ListaAbonados)):
        ListaAbonados[i] = ListaAbonados[i][:-1].split(",")
    
    ArchivoCategorias = open("categorias.txt","r")
    ListaCategorias = ArchivoCategorias.readlines()
    for i in range(len(ListaCategorias)):
        ListaCategorias[i] = ListaCategorias[i][:-1].split(",")
        
    ArchivoConexiones = open("conexiones.txt","r")
    ListaConexiones = ArchivoConexiones.readlines()
    for i in range(len(ListaConexiones)):
        ListaConexiones[i] = ListaConexiones[i][:-1].split(",")

    for i in range(len(ListaAbonados)):
        if(ID_Abonado == int(ListaAbonados[i][0])):
            NombreYApellido = ListaAbonados[i][1]
            Domicilio = ListaAbonados[i][2]
            IDCategoria = ListaAbonados[i][3]
    
    MinutosTotales = 0
    for i in range(len(ListaConexiones)):
        if(ID_Abonado == int(ListaConexiones[i][0])):
            MinutosTotales += float(ListaConexiones[i][1])
    
    for i in range(len(ListaCategorias)):
        if(IDCategoria == ListaCategorias[i][0]):
            Abono = float(ListaCategorias[i][1])
            ImportePorMinuto = float(ListaCategorias[i][2])
    
    Importe = MinutosTotales * ImportePorMinuto
    Total = Importe + Abono

    print("\nNombre: {}\nDomicilio: {}\nAbono: {:.2f}\nImporte: {:.2f}\nTotal: {:.2f}".format(NombreYApellido,Domicilio,Abono,Importe,Total))

def main():
    IDAbonado = int(input("Ingrese ID del abonado: "))
    factura(IDAbonado)
main()

#3.2

def DuracionMaxima():

    ArchivoAbonados = open("abonados.txt","r")
    ListaAbonados = ArchivoAbonados.readlines()
    for i in range(len(ListaAbonados)):
        ListaAbonados[i] = ListaAbonados[i][:-1].split(",")

    ArchivoCategorias = open("categorias.txt","r")
    ListaCategorias = ArchivoCategorias.readlines()
    for i in range(len(ListaCategorias)):
        ListaCategorias[i] = ListaCategorias[i][:-1].split(",")
        
    ArchivoConexiones = open("conexiones.txt","r")
    ListaConexiones = ArchivoConexiones.readlines()
    for i in range(len(ListaConexiones)):
        ListaConexiones[i] = ListaConexiones[i][:-1].split(",")

    MinutosMaximos = 0

    for i in range(len(ListaAbonados)):
        IDAbonado = ListaAbonados[i][0]
        Minutos = 0
        for j in range(len(ListaConexiones)):
            if(IDAbonado == ListaConexiones[j][0]):
                Minutos += int(ListaConexiones[j][1])
        if(Minutos>MinutosMaximos):
            MinutosMaximos = Minutos
            IDAbonadoAGuardar = ListaAbonados[i][0]
            Nombre = ListaAbonados[i][1]
            Categoria = ListaAbonados[i][3]

    print("\n\nID_Abonado: {}\nNombre: {}\nCategoria: {}\nDuracion total en minutos: {}".format(IDAbonadoAGuardar,Nombre,Categoria,MinutosMaximos))

def main():
    DuracionMaxima()
main()