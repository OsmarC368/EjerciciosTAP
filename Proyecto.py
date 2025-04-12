import random
import matplotlib.pyplot as plt
import numpy as np
import cutie
from math import sqrt

# x = random.randrange(80,100)
# vectores =[[random.randrange(80,100) for _ in range(40)] for _ in range(4)]
# print(f"x: {vectores}")


def determinarTipo(datos):
    n = len(datos)

    d = sum(datos) / n

    s = (sum([x**2 for x in datos]) - (n*(d**2))) / len(datos) - 1

    compVar = (s**2) / (d**2)

    if(compVar < 0.2):
        return "Determinista"
    else:
        return "Probabilistica"


def showGraph(x, y):
    plt.plot(x, y)
    plt.show()



def pieGraph(datos):
    y = [len([x for x in datos if x[1] == 'A']), len([x for x in datos if x[1] == "B"]), len([x for x in datos if x[1] == "C"])]
    labels = ["A", "B", "C"]
    plt.pie(y, labels=labels, autopct="%1.1f%%")
    plt.legend(title = "Tipo ABC")
    plt.show()

def determinarTipoABC(datos):
    #sortedData = sorted(datos, key=lambda items: items[1])[::-1]
    n = 1
    sortedData = sorted(datos)[::-1]
    totalSum = sum(sortedData)
    typeA = totalSum * 0.8
    typeC = totalSum * 0.05
    auxA = 0
    auxC = 0
     
    a = []
    bc = []
    popList = []
    for i, x in enumerate(sortedData):
        if x + auxA < typeA:
            a.append([f"N-{n}", "A", x])
            auxA += x
            popList.append(i)
            n+=1
        else:
            break
    [sortedData.pop(0) for i in popList]

    
    for x in sortedData[::-1]:
        if x + auxC < typeC:
            auxC += x
            bc.append([f"N-{n}", "C", x])
            n+=1
        else:
            bc.append([f"N-{n}", "B", x])
            n+=1


    [a.append(x) for x in bc[::-1]]
    return a





def calcQ(D, k, h):
    return sqrt((2*k*D)/h)

def calcQFaltante(D, k, h, pe):
    return sqrt(((2*k*D)*(h+pe))/(h*pe))

def calcE(D, k, h, pe):
    return sqrt((2*k*D*h) / (h+pe) * pe)

def calcCosto(D, c, Q, h, k):
    return (c*D) + (k * (D/Q)) + ((1/2)*h*Q)

def calcCostoFaltante(D, c, Q, h, k, pe, e):
    return (c*D) + (k * (D/Q)) + (h*(Q-e)**2 / 2*Q) + (pe**2 / 2*Q)
    
def calcD(R, l):
    return R / l




def modeloSimple():
    print("\nIngrese el Tiempo que Desea Utilizar.")
    tiempoLabels = ["Diario", "Semanal", "Mensual", "Anual"]
    tiempo = cutie.select(tiempoLabels)

    c = cutie.get_number("\nIngrese el valor unitario del Producto: ")

    D = cutie.get_number(f"\nIngrese el valor de la Demanda en {tiempoLabels[tiempo]}: ")

    k = cutie.get_number("\nIngrese el costo del Pedido: ")

    h = cutie.get_number("\nIngrese el costo de Almacenar: ")

    l = cutie.get_number(f"\nIngrese el tiempo de Entrega: ")

    Q = calcQ(D, k, h)

    costo = calcCosto(D, c, Q, h, k)

    T = Q / D

    if l < T:
        R = D*l

    else:
        m = 0
        while((l-m*T < 0) or (l - ((m+1)*T) > 0)): m+=1
        R = D * (l-m*T)

    print(f"\n Cantidad a pedir {round(Q, 2)}, la cual tendra un costo de {round(costo, 2)} y se debe pedir cada el inventario disminuya a {round(R,2)} todo calculado en el tiempo {tiempoLabels[tiempo]}")



def modeloFaltante():
    print("\nIngrese el Tiempo que Desea Utilizar.")
    tiempoLabels = ["Diario", "Semanal", "Mensual", "Anual"]
    tiempo = cutie.select(tiempoLabels)


    c = cutie.get_number("\nIngrese el valor unitario del Producto: ")

    D = cutie.get_number(f"\nIngrese el valor de la Demanda en {tiempoLabels[tiempo]}: ")

    k = cutie.get_number("\nIngrese el costo del Pedido: ")

    h = cutie.get_number("\nIngrese el costo de Almacenar: ")

    l = cutie.get_number(f"\nIngrese el tiempo de Entrega: ")

    pe = cutie.get_number("\nIngrese el costo por perdida: ")

    Q = calcQFaltante(D, k, h, pe)
    e = calcE(D, k, h, pe)

    T = Q / D

    costo = calcCostoFaltante(D, c, Q, h, k, e=e, pe=pe)

    if l < T:
        R = D*l

    else:
        m = 0
        while((l-m*T < 0) or (l - ((m+1)*T) > 0)): m+=1
        R = D * (l-m*T)




def ejercicio3():
    print("\nMenu de Opciones")
    options = ["Clasificacion ABC", "Lote Economico Simple", "Lote Economico Descuento", "Lote Economico Faltante"]
    opt = cutie.select(options=options)

    if opt == 0:
        datos = input("Ingrese el Arreglo de Datos: ").strip("[]").split(",")
        datos = [int(i) for i in datos]
        pieGraph(determinarTipoABC(datos))
    elif opt == 1:
        modeloSimple()
    
    


if __name__ == "__main__":
    # #EJERCICIO 1
    # vectores =[[random.randrange(80,100) for _ in range(40)] for _ in range(4)]
    # for x in vectores:
    #     print(f"El Vecto es: {determinarTipo(x)}")
    #     y = np.array(x)
    #     x = np.array([i for i in range(40)])
    #     showGraph(x, y)
    # #EJERCICIO 2
    # newVector = [[random.randrange(5000, 20000) * random.randrange(5,10) for _ in range(40)] for _ in range(4)]
    # for z in newVector:
    #     pieGraph(determinarTipoABC(z))
    
    #EJERCICIO 3
    ejercicio3()