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
    # g = np.random.uniform(low=0.0, high=100000, size=(20, 1))
    # g = np.memmap('./g-1.txt', mode='r+', dtype=np.float64, shape=(50816, 1))
    g = np.loadtxt(open('./cgne/g-test.txt', 'r'), delimiter=',')

#    H = np.random.uniform(low=0.0, high=100000, size=(20, 3))
#    H = np.memmap('./H-1.txt', mode='r+', dtype=np.float64, shape=(50816, 3600))
    H = np.loadtxt(open('./cgne/H-test.txt', 'r'), delimiter=',')

    # print(H.shape)
    # print(g.shape)
    tst = np.multiply(H, 0)
    r = np.subtract(g, np.transpose(tst))
    p = np.matmul(H, r)
    # print(p)

    alpha = get_alpha(p, r)

    f = np.multiply(alpha, p)
    # print(f)

    i = 0
    # 4.    Executar até que a norma L2 do resíduo (r) seja menor do que 1e10-4 .
    # while r < 0.0001:
    for i in range(0, 10000):
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
        print("STILL RUNNING")

    print("END")
    print(r)


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
