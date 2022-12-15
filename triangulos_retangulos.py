import math


def get_triangulos_retangulos(limit=100):
    ans = []
    for i in range(1, 100):
        for j in range(1, 100):
            hipotenuse = math.sqrt(i**2 + j**2)
            is_whole = hipotenuse - int(hipotenuse) == 0
            if is_whole and hipotenuse <= 100 and i < j:
                ans.append((i, j, int(hipotenuse)))
    return ans



for i, j, k in get_triangulos_retangulos():
    print(i, j, k)
