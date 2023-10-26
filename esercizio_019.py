#Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. 
# Il programma deve poi chiedere all'utente di inserire una lettera
#e mostrare in output solo i colori nella lista che iniziano con quella lettera.

# Suggerimento: potresti usare la funzione range e il metodo startswith().


def colore_lista():
    contatore = 0
    colori = []
    while contatore < 10:
        colore = input("Inserisci dieci nomi di colori uno alla volta:  ")
        contatore += 1
        colori.append(colore)
    lettera_iniziale = input("Inserisci una lettera: ")
    for colore_corrente in colori:
        if colore_corrente.startswith(lettera_iniziale):
            print(colore_corrente)
                
    return colori

colore_lista()

        


def colore_lista_1():
    colori = []
    for _ in range(11):
        colore = input("Inserisci un colore alla volta: ")
        colori.append(colore)
    lettera_iniziale = input("Inserisci una lettera: ")
    for _ in colori:
        if _.startswith(lettera_iniziale):
            print(_)
    
        

colore_lista_1()
    