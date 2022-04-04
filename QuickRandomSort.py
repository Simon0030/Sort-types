#sortowanie szybkie losowe
import datetime
import random

lista = list(range(0,1000001))
def sortowanie_szybkie(lista):
    less = []
    greater = []
    if len(lista) > 1:
        pivot = lista[random.randint(0,len(lista)-1)]
        for x in lista:
            if x <= pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
        return sortowanie_szybkie(less)+sortowanie_szybkie(greater)
    else:
        return lista
    return lista

czas1 = datetime.datetime.utcnow().timestamp()
sortowanie_szybkie(lista)
czas2 = datetime.datetime.utcnow().timestamp()
print(sortowanie_szybkie(lista))
print((czas2-czas1), 'seconds')
