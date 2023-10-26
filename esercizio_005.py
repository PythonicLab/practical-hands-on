# Non ho trovato la soluzione

# Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.

# Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

def somma_tra_numeri(lista):
    somma = 0   
    for n in lista:
        somma += n
    return somma

lista_numeri = [3, 8, 10, 95]        

print(somma_tra_numeri(lista_numeri))
