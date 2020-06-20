import matplotlib.pyplot as plt
import numpy as np
import random as rdm

plt.rcParams['image.cmap'] = 'gray'


# size = (40, 40)
#
noisysquare = np.zeros((40, 40))
noisysquare[10:-10, 10:-10] = 1


#
# np.random.seed(2)
# x, y = (40 * np.random.random((2, 20))).astype(np.int)
# noisysquare[x, y] = 1
# plt.imshow(noisysquare)
#
# for x in range(0, 39):
#
#     for y in range(0, 39):
#         esd = False
#         esi = False
#         eid = False
#         eii = False
#         cont = 0
#         if 1 <= x <= 38 and 1 <= y <= 38:
#
#             if noisysquare[x - 1, y] == 1:
#                 cont += 1
#             if noisysquare[x, y - 1] == 1:
#                 cont += 1
#             if noisysquare[x - 1, y - 1] == 1:
#                 cont += 1
#             if noisysquare[x + 1, y] == 1:
#                 cont += 1
#             if noisysquare[x, y + 1] == 1:
#                 cont += 1
#             if noisysquare[x + 1, y + 1] == 1:
#                 cont += 1
#             if noisysquare[x + 1, y - 1] == 1:
#                 cont += 1
#             if noisysquare[x - 1, y + 1] == 1:
#                 cont += 1
#             if noisysquare[x, y] == 1:
#                 cont += 1
#             if noisysquare[x - 1, y] == noisysquare[x, y - 1] == noisysquare[x - 1, y - 1] == noisysquare[x, y]:
#                 esi = True
#                 # print('esi', x, y)
#             if noisysquare[x, y - 1] == noisysquare[x + 1, y] == noisysquare[x + 1, y - 1] == noisysquare[x, y]:
#                 esd = True
#                 # print('esd', x, y)
#             if noisysquare[x - 1, y] == noisysquare[x, y + 1] == noisysquare[x - 1, y + 1] == noisysquare[x, y]:
#                 eii = True
#                 # print('eii', x, y)
#             if noisysquare[x + 1, y] == noisysquare[x, y + 1] == noisysquare[x + 1, y + 1] == noisysquare[x, y]:
#                 eid = True
#                 # print('eid', x, y)
#             if esi | esd | eii | eid:
#                 noisysquare[x, y] = noisysquare[x, y]
#             elif cont >= 5:
#                 noisysquare[x, y] = 1
#             else:
#                 noisysquare[x, y] = 0
#
# plt.figure()
# plt.imshow(noisysquare)


def crearMatrizRandom(m, n):
    matriz = np.zeros((m, n))
    for x in range(0, m):
        for y in range(0, n):
            matriz[x, y] = rdm.randrange(0, 100, 10)
    return matriz


def resultadoDiv(sumatoria, div):
    residuo = (sumatoria // div) % 10
    if residuo == 0:
        return sumatoria // div
    elif residuo > 5:
        res = (sumatoria // div) + (10 - residuo)
        return res
    else:
        return (sumatoria // div) - residuo


def quitarRuido(img):
    for m in range(0, len(img)):
        for n in range(0, len(img)):
            if 1 <= m <= len(img) - 2 and 1 <= n <= len(img) - 2:
                img[m, n] = resultadoDiv(
                    (img[m - 1, n] + img[m, n - 1] + img[m - 1, n - 1] + img[m + 1, n] + img[m, n + 1] + img[
                        m + 1, n + 1] + img[m + 1, n - 1] + img[m - 1, n + 1] + img[m, n]), 9)

            if m == 0 and 1 <= n <= len(img) - 2:
                img[m, n] = resultadoDiv((img[m, n - 1] + img[m + 1, n] + img[m, n + 1] + img[
                    m + 1, n + 1] + img[m + 1, n - 1] + img[m, n]), 6)

            if n == 0 and 1 <= m <= len(img) - 2:
                img[m, n] = resultadoDiv((img[m - 1, n] + img[m + 1, n] + img[m, n + 1] + img[
                    m + 1, n + 1] + img[m - 1, n + 1] + img[m, n]), 6)

            if n == 0 and m == 0:
                img[m, n] = resultadoDiv((img[m + 1, n] + img[m, n + 1] + img[
                    m + 1, n + 1] + img[m, n]), 4)

            if m == len(img) - 1 and n == 0:
                img[m, n] = resultadoDiv((img[m - 1, n] + img[m, n + 1] + img[m - 1, n + 1] + img[m, n]), 4)

            if n == len(img) - 1 and m == 0:
                img[m, n] = resultadoDiv((img[m, n - 1] + img[m + 1, n] + img[m + 1, n - 1] + img[m, n]), 4)

            if m == len(img) - 1 and n == len(img) - 1:
                img[m, n] = resultadoDiv((img[m - 1, n] + img[m, n - 1] + img[m - 1, n - 1] + img[m, n]), 4)

            if n == len(img) - 1 and 1 <= m <= len(img) - 2:
                img[m, n] = resultadoDiv(
                    (img[m - 1, n] + img[m, n - 1] + img[m - 1, n - 1] + img[m + 1, n] + img[m + 1, n - 1] +
                     img[m, n]), 6)

            if m == len(img) - 1 and 1 <= n <= len(img) - 2:
                img[m, n] = resultadoDiv(
                    (img[m - 1, n] + img[m, n - 1] + img[m - 1, n - 1] + img[m, n + 1] + img[m - 1, n + 1] +
                     img[m, n]), 6)
    return img


imagen = crearMatrizRandom(30, 30)
imagen[10:-10, 10:-10] = 1
print(imagen)

plt.imshow(imagen)

imagen = quitarRuido(imagen)
print(imagen)
plt.figure()
plt.imshow(imagen)
