import math

'''
# Ejercicio 1

print(".............................")
print(".           pppppppp        .")
print(".        ppp        ppp     .")
print(".      pp              pp   .")
print(".    pp                  pp .")
print(".    pp    pp      pp    pp .")
print(".    pp                  pp .")
print(".     pp                pp  .")
print(".      pp  ppppppppp   pp   .")
print(".       pp            pp    .")
print(".         pp        pp      .")
print(".            pppppp         .")
print(".............................")

# Ejercicio 2

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
print("Hola",Nombre,Apellido,"!")

#Ejercicio 3

Lado1 = int(input("Ingrese lado 1: "))
Lado2 = int(input("Ingrese lado 2: "))
print("Perimetro: ",Lado1+Lado1+Lado2+Lado2)
print("Area: ",Lado1*Lado2)

#Ejercicio 4

Numero = float(input("Ingrese Numero: "))
print("Parte entera: ",int(Numero))
print("Parte fraccionaria: ",Numero-int(Numero))


#Ejercicio 5

Numero = input("Ingrese número: ")
print("Separación en dígitos:",int(Numero[0])**2,"-",int(Numero[1])**2,"-",int(Numero[2])**2,"-",int(Numero[3])**2,"-",int(Numero[4])**2)



#Ejercicio 6

Base = int(input("Ingrese base: "))
Altura = int(input("Ingrese altura: "))
Area = (Base*Altura)/2
Perimetro = Base + (math.sqrt((pow(Base/2,2))+(pow(Altura,2))))*2
print("Cálculos para un triangulo con base {:d} y altura {:d}:".format(Base,Altura))
print("<<< Area = {:.2f}>>> <<< Perimetro = {:.2f} >>>".format(Area,Perimetro))



# Ejercicio 7

Numero1 = int(input("Ingrese el primer numero: "))
Numero2 = int(input("Ingrese el segundo numero: "))

UnidadesDelPrimerNumero = Numero1%10
DecenasDelSegundoNumero = (Numero2//10)%10

print("El número resultante es: {:d}{:d}".format(DecenasDelSegundoNumero,UnidadesDelPrimerNumero))



#Ejercicio 8

Tiempo = int(input("Ingrese el tiempo en segundos: "))
Dia = Tiempo//86400
Hora = (Tiempo-Dia*86400)//3600
Minutos = (Tiempo - Dia*86400 - Hora*3600)//60
Segundos = (Tiempo - Dia*86400 - Hora*3600 - Minutos*60)
print("{:d} día(s), {:d} hora(s), {:d} minuto(s), {:d} segundo(s).".format((Dia),Hora,Minutos,Segundos))



#Ejercicio 9

Numero = int(input("Ingrese un numero de cantidad impar de cifras (al menos 3 cifras): "))
Largo = len(str(Numero))
print("El numero ingresado tiene {:d} cifras.".format(Largo))
PrimeraCifra = Numero//(pow(10,Largo-1))
UltimaCifra = Numero%10
CifraCentral = (Numero//(pow(10,Largo//2)))%10

print("La primera cifra es {:d}, la ultima es {:d} y la central es {:d}.".format(PrimeraCifra,UltimaCifra,CifraCentral))

'''
'''
#Ejercicio 10 

Binario = int(input("Ingrese numero en binario: "))
Resto1 = (Binario%10)*2 ** 0
Resto2 = ((Binario//10)%10)*2 **1
Resto3 = ((Binario//100)%10)*2 **2
Resto4 = ((Binario//1000)%10)*2 **3
Resto5 = ((Binario//10000)%10)*2 **4
Decimal = Resto1 + Resto2 + Resto3 + Resto4 + Resto5
print("Numero en decimal: {:d}".format(Decimal))
'''
'''
#Ejercicio 11

Decimal = int(input("Ingrese un número decimal: "))

Resto1 = (Decimal%8)
Decimal1 = (Decimal//8)
Resto2 = (Decimal1%8)
Decimal2 = (Decimal1//8)
Resto3 = (Decimal2%8)
Decimal3 = (Decimal2//8)
Resto4 = (Decimal3%8)

Octal = (str(Resto4)+str(Resto3)+str(Resto2)+str(Resto1))
print("El numero en octal es {:s}".format(Octal))
'''
'''
#Ejercicio 12

Numero1 = int(input("Ingrese el primer número: "))
Numero2 = int(input("Ingrese el segundo número: "))
Numero3 = int(input("Ingrese el tercer número: "))

Suma = Numero1+Numero2+Numero3

print("{:=10d}".format(Numero1))
print("{:=10d}".format(Numero2))
print("{:=10d}".format(Numero3))
print("-"*10)
print("{:>10d}".format(Suma))
'''
'''
#Ejercicio 13

Numero1 = int(input("Ingrese el multiplicando: "))
Numero2 = int(input("Ingrese el multiplicador: "))

Multiplicacion = Numero1 * Numero2
Multiplicacion1 = (Numero2 % 10) * Numero1
Multiplicacion2 = ((Numero2 // 10)%10 * Numero1) 
Multiplicacion3 = ((Numero2 // 100)%10 * Numero1)


print("{:>10}".format(Numero1))
print("x {:>8}".format(Numero2))
print("-" * 10)
print("{:>10}".format(Multiplicacion1))
print("+ {:>7}-".format(Multiplicacion2))
print("{:>8}--".format(Multiplicacion3))
print("-" * 10)
print("{:>10}".format(Multiplicacion))
'''