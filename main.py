from typing import Tuple


def functia_mea(param_1: int, param_2: int, param_3: int) -> Tuple:
    """
    Aduna si inmulteste niste numere.
    :param param_1: primul numar
    :param param_2: al doilea numar
    :param param_3: al treilea numar
    :return: valoarea expresiei param_1 + param_2 * param_3
    """
    # var = None
    if param_1:
        var = 7
    # print(var) # have it if the if statement body gets executed
    return param_1 + param_2 * param_3, 17


def functie_none(x, y):
    if x % 2 == 0:
        return y
    return None


x, y = functia_mea(1, 2, 3)
#p, q = functia_mea('ana', 'are', 'mere')
print(x, y)
#print(p, q)
print(functie_none(3, 4))
