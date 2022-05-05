import math
import random

'''
#Ejercicio1

def AreaTriangulo(Lado1,Lado2,Lado3):
    p = (Lado1+Lado2+Lado2)/2
    Area = math.sqrt(p*(p-Lado1)*(p-Lado2)*(p-Lado3))
    return Area

def main():
    Lado1 = int(input("Ingrese lado 1: "))
    Lado2 = int(input("Ingrese lado 2: "))
    Lado3 = int(input("Ingrese lado 3: "))
    print("El area del triangulo es = {:.2f}".format(AreaTriangulo(Lado1,Lado2,Lado3)))
main()
'''
'''
#Ejercicio2

def Raiz(Indice,Radicando):
    Resultado = math.pow(Radicando,1/Indice)
    return Resultado

def main():
    Radicando = float(input("Ingrese el radicando (Numero real): "))
    Indice = int(input("Ingrese el índice (Número natural): "))
    print("La raiz de {:d} de {:.0f} es = {:.6f}".format(Indice,Radicando,Raiz(Indice,Radicando)))
main()
'''
'''
#Ejercicio 3

def paridad(Numero):

    Numero1 = Numero%10
    Numero2 = (Numero//10)%10
    Numero3 = (Numero//100)%10
    Numero4 = (Numero//1000)%10
    Numero5 = (Numero//10000)%10
    Numero6 = (Numero//100000)%10
    Numero7 = (Numero//1000000)%10
    Numero8 = (Numero//10000000)%10

    Suma = (Numero1+Numero2+Numero3+Numero4+Numero5+Numero6+Numero7+Numero8)
    Resultado = Suma%2
    return Resultado

def main():
    Numero = int(input("Ingrese un numero de binario de hasta 8 bits: "))
    print("Bit de paridad generado: {:d}".format(paridad(Numero)))
main()
'''
'''
#Ejercicio 4

def AreaCirc(Diametro):
    Radio = Diametro/2
    Area = (math.pi)*(math.pow(Radio,2))
    return Area

def AreaCuad(Lado):
    Area = Lado*Lado
    return Area

def AreaNegra(Lado):
    Area = AreaCuad(Lado) - AreaCirc(Lado/3)*2 - AreaCirc(Lado*(2/3))
    return Area

def main():
    Lado = int(input("Ingrese lado: "))
    print("El area negra es de {:.2f} y es un {:.2f}% del area total del cuadrado".format(AreaNegra(Lado),(AreaNegra(Lado)/AreaCuad(Lado)*100)))
main()
'''
'''
#Ejercicio 5

def Aleatorio(Numero1,Numero2):
    Resultado = random.randint(Numero1,Numero2)
    return Resultado

def main():
    Numero1 = int(input("Ingrese el limite inferior: "))
    Numero2 = int(input("Ingrese el limite superior: "))
    Aleatorio1 = Aleatorio(Numero1,Numero2)
    Aleatorio2 = Aleatorio(Aleatorio1,Numero2)
    Aleatorio3 = Aleatorio(Aleatorio1,Aleatorio2)
    print("\n1- Limite inferior {:d}, límite superior {:d}. Numero generado: {:d}".format(Numero1,Numero2,Aleatorio1))
    print("2- Limite inferior {:d}, límite superior {:d}. Numero generado: {:d}".format(Aleatorio1,Numero2,Aleatorio2))
    print("3- Limite inferior {:d}, límite superior {:d}. Numero generado: {:d}".format(Aleatorio1,Aleatorio2,Aleatorio3))
main()
'''
'''
#Ejercicio 6

def Aleatorio(Opcion1,Opcion2):
    Azar = random.choice([Opcion1,Opcion2])
    return Azar
def main():
    Vestimenta1 = input("Ingrese alternativa 1 para vestimenta: ")
    Vestimenta2 = input("Ingrese alternativa 2 para vestimenta: ")
    Plato1 = input("Ingrese alternativa 1 para plato: ")
    Plato2 = input("Ingrese alternativa 2 para plato: ")
    Bebida1 = input("Ingrese alternativa 1 para bebida: ")
    Bebida2 = input("Ingrese alternativa 2 para bebida: ")

    Vestimenta = Aleatorio(Vestimenta1,Vestimenta2)
    Plato = Aleatorio(Plato1,Plato2)
    Bebida = Aleatorio(Bebida1,Bebida2)

    print("\nCena al azar: {}, {} y {} ".format(Vestimenta,Plato,Bebida))

main()
'''
'''
#Ejercicio 7

def Justificado(Frase,Ancho):
    Resultado = "'"+(Ancho-2-len(Frase))*" "+Frase+"'"
    return Resultado

def main():
    Frase = input("Ingrese frase: ")
    Ancho = int(input("Ingrese el ancho total a ser usado: "))
    print(Justificado(Frase,Ancho))
main()
'''
'''
#Ejercicio 8

def crearFila(Ancho):
    Resultado = "*"*Ancho + '\n'
    return Resultado

def crearRectangulo(Ancho,Alto):
    Resultado = crearFila(Ancho)*Alto
    return Resultado

def main():
    Ancho = int(input("Ingrese ancho: "))
    Alto = int(input("Ingrese alto: "))
    print(crearRectangulo(Ancho,Alto))
main()
'''