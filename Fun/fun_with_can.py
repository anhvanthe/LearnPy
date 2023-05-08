"""
Created on Fri Apr  1 22:44:35 2016
Amplitude analisys of Bode Diagram
@author: Thiago dos Santos Fontes
"""
import matplotlib.pyplot as plt
import numpy as np
import math


# acumular coeficientes +20, -20 db/déc em valores de w
def plot_amp(matrix):
    n = len(matrix[:])

    for i in range(n):
        matrix[i][0] = math.sqrt(matrix[i][0] ** 2)

    matrix = sorted(matrix)
    x = [0] * (n + 1)  # Adiciona 2 devido a folga de uma década no inicio e outra no final
    y = [0] * (n + 1)
    a = [0] * (n + 1)  # Vetor de inclinações guarda graus para cada ponto de x
    size = 0

    minX, minY, minE = min(matrix)

    segundo_menor = matrix[n - 1][0]
    for i, j, k in matrix:
        if ((i < segundo_menor) and (i > 0)):
            segundo_menor = i

    # Como 1 zero foi adiconado antes os indices estão sempre adiantados em 1
    # Para os vetores X e Y
    x[0] = matrix[0][0]
    for i in range(n):

        aux = x[size]
        if (aux != matrix[i][0]):  # Verifica se há mais de um polo/zero no mesmo ponto
            size = size + 1
            a[size] = a[size - 1]

        if ((minX == 0) and (size == 0)):
            x[0] = segundo_menor * pow(10, -1)
            a[size] = a[size] + matrix[i][1]
            y[0] = -a[size] * 20 * int(math.log(10, 10))  # já é a razão entre os dois

        else:
            x[size] = matrix[i][0]
            # Deve se somar os valores de "a" pois não há garantias de que haverá somente 1 polo ou zero no ponto x
            a[size] = a[size] + matrix[i][1]

    if (minX != 0):
        y[1] = -20 * a[0] * math.log(x[0] / x[1], 10)

    for i in range(size - 1):
        j = i + 1
        if (a[j] == 0):
            y[j + 1] = y[j]
        else:
            y[j + 1] = y[j] + 20 * a[j] * math.log(x[j + 1] / x[j], 10)

    # Continuação do diagrama na decada adicionada para folga com objetivo de melhorar a visualizção
    x[size + 1] = x[size] * 10
    y[size + 1] = y[j + 1] + 20 * a[j + 1] * math.log(10, 10)

    vetx = [0] * (size + 2)
    vety = [0] * (size + 2)
    for i in range(size + 2):
        vetx[i] = float(x[i])
        vety[i] = y[i]

    print(vetx)
    print(vety)
    print(a)
    print(matrix)
    # Configurações de desenho do gráfico
    fig, ax0 = plt.subplots()
    ax0.spines['right'].set_visible(False)
    ax0.spines['top'].set_visible(False)
    plt.plot(vetx, vety, lw=2)
    plt.tight_layout()
    plt.autoscale()
    plt.semilogx()
    # Plota linhas a cada 20 Db
    miny = min(vety)
    miny = 20 - (miny % 20) + miny

    plt.yticks(np.arange(miny - 40, max(vety) + 40, 20))

    plt.grid(True)
    plt.show()

    plt.plot(vetx, vety, lw=2)
    plt.tight_layout()
    plt.autoscale()
    plt.semilogx()
    plt.yticks(vety)
    plt.xticks(vetx)
    plt.grid(True)
    plt.show()


# bode plot ((s+100)^2(s+1000)^2)/((s^2)(s+10)(s+100000))
plot_amp([[0, -2, 0], [10, -1, 0], [100, 2, 0], [1000, 2, 0], [100000, -1, 0]])

# bode plot ((s+0,1)^2(s+1000)^2(s+10000))/((s+10)^2(s+100)^2)
plot_amp([[0.1, 2, 0], [10, -2, 0], [-20, -2, 0], [1000, 2, 0], [10000, 1, 0]])

# bode plot ((s+100)*s)/(s+10)^2
plot_amp([[0, 1, 0], [10, -2, 0], [100, 1, 0]])