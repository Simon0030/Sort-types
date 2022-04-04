#sortowanie szybkie prawe
import datetime
import sys

sys.setrecursionlimit(1000000000)
lista = list(range(100000,0,-1))
def sortowanie_szybkie(lista):
    male = []
    rowne = []
    wieksze = []
    if len(lista) > 1:
        pivot = lista[-1]
        for x in lista:
            if x < pivot:
                male.append(x)
            elif x == pivot:
                rowne.append(x)
            elif x > pivot:
                wieksze.append(x)
        return sortowanie_szybkie(male)+rowne+sortowanie_szybkie(wieksze)
    else:
        return lista
    return lista

czas1 = datetime.datetime.utcnow().timestamp()
sortowanie_szybkie(lista)
czas2 = datetime.datetime.utcnow().timestamp()
print(sortowanie_szybkie(lista))
print((czas2-czas1), 'seconds')

