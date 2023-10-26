def funzione(lista):
    for e in lista:
        print(int(len(e)))

lista_b = ["apice", "ercole", "giove", "nessuno"]

funzione(lista_b)

# Due possibili soluzioni 

def char_counter(lista_a):
    lista_b = []
    for parola in lista_a:
        lista_b.append(len(parola))
    return lista_b

def char_counter_pro(lista_a):
    return [len(parola) for parola in lista_a]