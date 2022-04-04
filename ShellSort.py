#sortowanie shella
import datetime

lista = list(range(0,1000001))
n = len(lista)
def sortowanie_shella(lista, n):
    krok = n//2
    while krok > 0:
        for i in range(krok, n):
            tmp = lista[i]
            j = i
            while j >= krok and lista[j - krok] > tmp:
                lista[j] = lista[j - krok]
                j -= krok
            lista[j] = tmp
        krok //= 2
    return lista

czas1 = datetime.datetime.utcnow().timestamp()
sortowanie_shella(lista,n)
czas2 = datetime.datetime.utcnow().timestamp()
print(sortowanie_shella(lista,n))
print((czas2-czas1), 'seconds')
