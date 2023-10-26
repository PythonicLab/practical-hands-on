# Non ho trovato la soluzione
def numero_massimo(lista):
    massimo = 0
    #for n in range(len(lista)):
    for n in lista:       
        if massimo >= n:
            pass
        else:
            massimo = n
    return massimo



def leggi_numeri():
    numero_int_lista = []
    while True:
        numero = input('Inserisci un numero? ')
        if numero == "":
            break
        else:
            numero_int = int(numero)
            numero_int_lista.append(numero_int)

    return numero_int_lista

numero_int = leggi_numeri()
massimo = numero_massimo(numero_int)

print(massimo)

# Soluzione

#lista_numeri = [42, 9, 23, 11, 17, 56, 3]
#numero_maggiore = lista_numeri[0]
#for numero in lista_numeri:
#    if numero > numero_maggiore:
#        numero_maggiore = numero
#print("Il numero maggiore tra tutti è:", numero_maggiore)



            
            





