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
    print('Getting g')
    g = np.memmap('./g-1.txt', mode='r+', dtype='float', shape=(1, 50816))
    # print(g)
    print('Getting H')

    H = np.memmap('./H-1.txt', mode='r+', dtype='float', shape=(50816, 3600))
    print(H)

    r = g
    trs = np.transpose(H)
    p = np.multiply(trs, r)
    print(p)


main()
