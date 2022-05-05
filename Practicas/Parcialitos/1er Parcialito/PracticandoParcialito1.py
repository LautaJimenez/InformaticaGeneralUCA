import math
'''
#1

def areaCua(c):
    Area = c*c
    return Area

def areaCir(r):
    Area = math.pi*math.pow(r,2)
    return Area

def areaNegra(c):
    Area = areaCua(c) + areaCir(c/4) - areaCir(c/2)
    return Area

def main():
    Lado = int(input("Ingrese el lado: "))
    print("La superficie gris es: {:.2f}".format(areaNegra(Lado)))
main()
'''
'''
#2

def areaRec(b):
    Area = b * (2*b)
    return Area

def areaCir(r):
    Area = math.pi * math.pow(r,2)
    return Area

def areaTri(b):
    Area = (b * ((2*b)/2)) / 2
    return Area

def areaNegra(b):
    Area = areaRec(b) - areaCir(b/2) - areaTri(b)
    return Area

def main():
    Lado = int(input("Ingrese la base: "))
    print("La superficie negra es: {:.2f}".format(areaNegra(Lado)))
main()
'''
'''
#3

def areaCuad(Lado):
    Area = Lado*Lado
    return Area

def areaCirc(Radio):
    Area = math.pi * math.pow(Radio,2)
    return Area

def areaTriag(Base,Altura):
    Area = (Base*Altura)/2
    return Area

def areaNegra(x):
    Area = (areaCuad(x/2))*2 + (areaCirc(x/2))/2 + (areaTriag(x/2,x/2))
    return Area 

def areaBlanca(x):
    Area = (areaCirc(x/2))/2 + (areaTriag(x/2,x/2))
    return Area

def main():
    x = int(input("Ingrese un valor: "))
    AreaNegra = areaNegra(x)
    AreaBlanca = areaBlanca(x)
    print(areaNegra)
    print(areaBlanca)
    areaTotal = AreaNegra + AreaBlanca
    print(areaTotal)
    #print("El area negra es {:.2f} y representa el {:.2f}%, el area blanca es {:.2f} y representa el {:.2f}%, y el area total es {:.2f}".format(areaNegra(x),((areaNegra(x)/areaTotal(x))*100),areaBlanca(x),((areaBlanca(x)/areaTotal(x))*100),areaTotal(x)))
main()

#Printea cualquier cosa

'''
'''
#4

def areaCirc(Radio):
    Area = math.pi * math.pow(Radio,2)
    return Area

def areaCuad(Lado):
    Area = Lado * Lado
    return Area

def areaNegra(x):
    Area = areaCirc(x/2) / 2 + areaCirc((x/4)/2)/2 - areaCuad(x/4)
    return Area

def main():
    x = int(input("Ingrese un valor x: "))
    print("El area negra es: {:.2f}".format(areaNegra(x)))
main()
'''
'''
#5
def areaCuad(Lado):
    Area = Lado * Lado
    return Area

def areaCirc(Radio):
    Area = math.pi * math.pow(Radio,2)
    return Area

def areaTriag(Base,Altura):
    Area = (Base*Altura)/2
    return Area

def areaNegra(x):
    Area = areaCirc(x/2)/2 + areaCuad(x/4)
    return Area

def areaBlanca(x):
    Area = areaTriag(x/2,x/2) - areaCuad(x/4) + areaCirc(x/2)/2 - areaTriag(x/2,x/2)
    return Area

def main():
    x = int(input("Ingrese valor X: "))
    AreaNegra = areaNegra(x)
    AreaBlanca = areaBlanca(x)
    areaTotal = AreaNegra + AreaBlanca

    print("\nEl AN es: {:.2f} | Porc. AN: {:.2f}%".format(AreaNegra,(AreaNegra/areaTotal)*100))
    print("El AN es: {:.2f} | Porc. AN: {:.2f}%".format(AreaBlanca,(AreaBlanca/areaTotal)*100))
    print("\nEl area TOTAL es: {:.2f}".format(areaTotal))
main()
'''
'''
#6

def areaCuad(Lado):
    Area = Lado * Lado
    return Area

def areaCirc(Radio):
    Area = math.pi * math.pow(Radio,2)
    return Area

def areaTriag(Base,Altura):
    Area = (Base*Altura)/2
    return Area

def areaNegra(x):
    Area = areaCuad(x) + areaCuad(x/2) - areaTriag(x/2,x/2) - ((areaCirc((x/4)))/2)*3
    return Area

def areaBlanca(x):
    Area = areaTriag(x/2,x/2) + (areaCirc((x/4)))*3
    return Area

def main():
    x = int(input("Ingrese valor X: "))
    AreaNegra = areaNegra(x)
    AreaBlanca = areaBlanca(x)
    AreaTotal = AreaNegra + AreaBlanca
    print("\nEl AN es {:.2f} y su Porc. es AN: {:.2f}%".format(AreaNegra,(AreaNegra/AreaTotal)*100))
    print("El AB es {:.2f} y su Porc. es AB: {:.2f}%".format(AreaBlanca,(AreaBlanca/AreaTotal)*100))
main()
'''

def DescomponerNumero(Numero):
    Largo = len(str(Numero))
    PrimeraCifra = Numero//(10**(Largo-1))
    UltimaCifra = Numero%10
    NumeroNuevo = (Numero - PrimeraCifra*(10**(Largo-1)))//10
    return NumeroNuevo

def main():
    Numero = int(input("Ingrese número: "))
    print("El numero es: {:d}, y sin su primera ni ultima cifra es: {:d}".format(Numero,DescomponerNumero(Numero)))
main()