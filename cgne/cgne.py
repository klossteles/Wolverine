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
import csv


def main():
    g = read_matrix_from_file('./cgne/g-1.txt')
    print('G loaded')

    H = read_matrix_from_file('./cgne/H-1.txt')
    H = np.transpose(H)
    print('H loaded')

    tst = np.multiply(H, 0)
    print('#1')
    r = np.subtract(g, np.transpose(tst))
    print('#2')
    p = np.matmul(H, r)
    print('#3')

    alpha = get_alpha(p, r)
    print('#4')

    f = np.multiply(alpha, p)
    print('#5')

    i = 0
    # 4.    Executar até que a norma L2 do resíduo (r) seja menor do que 1e10-4 .
    # while r < 0.0001:
    for i in range(0, 1):
        # GET alpha i
        alpha = get_alpha(p, r)

        # GET fi+1
        f_next = np.add(f, np.matmul(alpha, p))

        # GET ri+1
        aux1 = np.matmul(np.transpose(H), p)
        aux = np.matmul(alpha, np.transpose(aux1))
        r_next = np.subtract(r, np.transpose(aux))

        # GET beta i
        beta = get_beta(r_next, r)

        # GET pi+1
        # transp = np.transpose(H)
        aux1 = np.matmul(H, r_next)
        aux = np.matmul(beta, p)
        p_next = np.add(aux1, aux)

        # Atualizar valores antigos
        r = r_next
        p = p_next
        f = f_next
        # i += 1

        mark = '|' if i % 2 == 0 else '-'
        print("STILL RUNNING [{}]".format(mark))

    print("END")
    print(r)


def read_matrix_from_file(filename):
    with open(filename, 'r') as source:
        data = csv.reader(source, delimiter=',', quotechar='"')
        return np.asarray([row for row in data], dtype=np.float)


def get_alpha(p, r):
    alpha0 = np.matmul(np.transpose(r), r)
    alpha1 = np.matmul(np.transpose(p), p)
    alpha = np.nan_to_num(np.divide(alpha0, alpha1))
    return alpha


def get_beta(r_next, r):
    beta0 = np.matmul(np.transpose(r_next), r_next)
    beta1 = np.matmul(np.transpose(r), r)
    beta = np.nan_to_num(np.divide(beta0, beta1))
    return beta


main()
