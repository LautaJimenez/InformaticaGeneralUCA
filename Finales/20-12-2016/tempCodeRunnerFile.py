    MinutosTotales = 0
    for i in range(len(ListaConexiones)):
        if(ID_Abonado == ListaConexiones[i][0]):
            MinutosTotales += int(ListaConexiones[i][1])
    
    for i in range(len(ListaCategorias)):
        if(IDCategoria == ListaCategorias[i][0]):
            Abono = int(ListaCategorias[i][1])
            ImportePorMinuto = int(ListaCategorias[i][2])
    
    Importe = MinutosTotales * ImportePorMinuto
    Total = Importe + Abono

    print("Nombre: {}\nDomicilio: {}\nAbono: {}\nImporte: {}\nTotal: {}".format(NombreYApellido,Domicilio,Abono,Importe,Total))
