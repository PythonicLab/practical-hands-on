Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.


lista = [2, 67, 88, 76, 5, 4]
risultato = 1

for numero in lista:
    risultato *= numero

print(risultato)



# Soluzione

lista = [7, 66, 100, 457, 472]
risultato = 1
for numero in lista:
    if numero != 0:
        risultato *= numero
print("Il risultato della moltiplicazione tra tutti gli elementi della lista è... " + str(risultato))