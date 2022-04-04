#sortowanie babelkowe
import datetime
import random
import sys

sys.setrecursionlimit(1000000)

x = list(range(1,1000001))
x1 = []
x2=[]
for i in range(len(x)):
    if (i%2==0):
        x1.append(x[i])
    else:
        x2.append(x[i])
y1 = x2[::-1]
lista = x1+y1

wartosc_maks = max(lista)
def sortowanie_przez_zliczanie(lista, wartosc_maks):
    zasieg = wartosc_maks +1
    zliczanie = [0] * zasieg
    for x in lista:
        zliczanie[x] += 1
    i = 0
    for a in range(zasieg):
        for b in range(zliczanie[a]):
            lista[i] = a
            i += 1

    return lista

czas1 = datetime.datetime.utcnow().timestamp()
sortowanie_przez_zliczanie(lista,wartosc_maks)
czas2 = datetime.datetime.utcnow().timestamp()
print((czas2-czas1), 'seconds')

def zamiana(i, j):
    lista[i], lista[j] = lista[j], lista[i]

def kopiec(ilosc,i):
    lewa=2 * i + 1
    prawa=2 * (i + 1)
    max=i
    if lewa < ilosc and lista[i] < lista[lewa]:
        max = lewa
    if prawa < ilosc and lista[max] < lista[prawa]:
        max = prawa
    if max != i:
        zamiana(i, max)
        kopiec(ilosc, max)

def sortowanie_przez_kopcowanie():
    ilosc = len(lista)
    start = ilosc // 2 - 1
    for i in range(start, -1, -1):
        kopiec(ilosc, i)
    for i in range(ilosc-1, 0, -1):
        zamiana(i, 0)
        kopiec(i, 0)
    return lista


czas1 = datetime.datetime.utcnow().timestamp()
sortowanie_przez_kopcowanie()
czas2 = datetime.datetime.utcnow().timestamp()
print((czas2-czas1), 'seconds')

def sortowanie_przez_scalanie(lista):
    if len(lista)>1:
        srodek = len(lista)//2
        lewa = lista[:srodek]
        prawa = lista[srodek:]
        sortowanie_przez_scalanie(lewa)
        sortowanie_przez_scalanie(prawa)
        i=0
        j=0
        k=0
        while i < len(lewa) and j < len(prawa):
            if lewa[i] <= prawa[j]:
                lista[k]=lewa[i]
                i=i+1
            else:
                lista[k]=prawa[j]
                j=j+1
            k=k+1
        while i < len(lewa):
            lista[k]=lewa[i]
            i=i+1
            k=k+1
        while j < len(prawa):
            lista[k]=prawa[j]
            j=j+1
            k=k+1
    return lista

czas1 = datetime.datetime.utcnow().timestamp()
sortowanie_przez_scalanie(lista)
czas2 = datetime.datetime.utcnow().timestamp()
print((czas2-czas1), 'seconds')

n = len(lista)
def sortowanie_shella(lista, n):
    krok = 3
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
print((czas2-czas1), 'seconds')

def sortowanie_szybkie(lista):
    less = []
    equal = []
    greater = []
    if len(lista) > 1:
        pivot = lista[random.randint(0,len(lista)-1)]
        for x in lista:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sortowanie_szybkie(less)+equal+sortowanie_szybkie(greater)
    else:
        return lista
    return lista

czas1 = datetime.datetime.utcnow().timestamp()
sortowanie_szybkie(lista)
czas2 = datetime.datetime.utcnow().timestamp()
print((czas2-czas1), 'seconds')