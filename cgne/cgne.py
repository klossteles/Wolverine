# Implementar um servidor para reconstrução de imagens:
#
# 1.    Receber os dados para reconstrução;
# 2.    Carregar o modelo de reconstrução de acordo com os parâmetros recebidos;
# 3.    Executar o algoritmo de reconstrução;
# 4.    Executar até que a norma L2 do resíduo (r) seja menor do que 1e10-4 .
# 5.    Salvar o resultado.
#
# Imagem A, 60x60 pixels, H(50816x3600), g(50816x1):

import numpy as np


def main():
#    g = np.random.uniform(low=0.0, high=100000, size=(20, 1))
#    g = np.memmap('./g-1.txt', mode='r+', dtype=np.float64, shape=(50816, 1))
    g = np.loadtxt(open('./g-test.txt', 'r'), delimiter=',')

#    H = np.random.uniform(low=0.0, high=100000, size=(20, 3))
#    H = np.memmap('./H-1.txt', mode='r+', dtype=np.float64, shape=(50816, 3600))
    H = np.loadtxt(open('./H-test.txt', 'r'), delimiter=',')

    r = g
    p = np.matmul(np.transpose(H), r)
    print(H)
    print(g)
#    print(p)

    alpha0 = np.matmul(np.transpose(r), r)
    alpha1 = np.matmul(np.transpose(p), p)
    print(alpha0)
    print(alpha1)

    alpha = np.divide(alpha0, alpha1)
    print(alpha)

main()
