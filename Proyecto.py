import random
import matplotlib.pyplot as plt
import numpy as np

x = random.randrange(80,100)
vectores =[[random.randrange(80,100) for _ in range(40)] for _ in range(4)]
print(f"x: {vectores}")


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

# for x in vectores:
#     print(f"El Vecto es: {determinarTipo(x)}")
#     y = np.array(x)
#     x = np.array([i for i in range(40)])
#     showGraph(x, y)

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

print(determinarTipoABC(vectores[0]))
for x in vectores:
    x = np.array(x)
    print(x*5000)
    pieGraph(determinarTipoABC(x*5000))