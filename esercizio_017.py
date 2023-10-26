#Scrivi una funzione che, dato un carattere in ingresso, restituisca in output 
# il codice ASCII associato al carattere passato.

# Anche in questo caso, usare una libreria potrebbe facilitare la risoluzione 
# dell'esercizio!


def carattere_is_ascii(c):
    c_ascii = ord(c)
    return c_ascii  

print(carattere_is_ascii("a"))

# Soluzione

def trova_ascii():
    carattere = input("Inserisci il carattere che ti interessa convertire: ")
    valore = ord(carattere)
    output = f"Il valore ASCII associato a '{carattere}' è {valore}"
    return output   