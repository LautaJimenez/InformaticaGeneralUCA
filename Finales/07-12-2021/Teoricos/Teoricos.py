'''
#Teorico 1

def fun(t,a):
    i = 0
    while i<len(t) and t[i] < a:
        i+=1                    #LLEGA HASTA i =2
    
    return t[:i] + (a,) + t[i:] #Las tuplas son como listas que no se pueden modificar, pero si sumar, restar, etc...

def main():
    x = (10,20,30,40,50)
    x = fun(x,26)
    print(x)
main()

# (10,20,26,30,40,50)

'''
'''
#Teorico 2

def fun(di,nom,parcial,valor):
    if di.get(nom)!=None: #Si no encuentra a Juan en el diccionario (Si lo encuentra)
        i = di.get(nom)[1] #Es 0
        if(di[nom][i]["a"].get(parcial) == None): #Si no esta pp3 en el diciconario de "a"
            di[nom][i]["a"][parcial] = valor #Agrega "pp3" : "A"

def main():
    x = {"Juan":[{"a":{"pp1":"A","pp2":"D"}},0], 
    "Lola":[{"p1":{"pp2":"A","pp3":"A-"}},1],
    "Charly":[{746:{"pp1":"A","pp3":"A-"}},2]}
    fun(x,"Juan","pp3","A")
    print(x["Juan"])
main()

# [{"a":{"pp1":"A","pp2":"D","pp3":"A"}},0]

'''
'''
#Teorico 3

def fun(var):
    aux = -10
    var = [] #Variable local
    for i in range(0,len(var)-1): #No entra al for (No se por que)
        for j in range(i+1,len(var)):
            if(var[i]>var[j]):
                aux = var[j]
                var[j] = var[i]
                var[i] = aux
    
def main():
    miVar = [23,45,10]
    fun(miVar)
    print(miVar)
main()

#Imprime [23,45,10]

'''
'''
#Teorico 4

def figura(Base):
    for fila in range(Base):
        for col in range(Base):
            if(fila == Base//2 or (fila<=col and fila+col >= Base-1)):
                print("* ",end="")
            else:
                print("- ",end="")
        print()

figura(9)
'''
'''
#Teorico 5

def fun(lst,di):
    di = {} #Se declara una variable local
    i = 0
    while(i<len(lst)):
        clave = lst[i]
        di[clave] = i
        i = i+1
    #return di

def main():
    di = {"x":10}
    lst = ["a","b"]
    #di = fun(lst,di)
    print(di)
main()

'''