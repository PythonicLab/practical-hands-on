# Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while
#e li stampi con la funzione print senza andare a capo. Il ciclo while si deve interrompere quando l'utente preme INVIO 


def senza_andare_a_capo():
    parole = ""
    while True:
        azione_1 = input("Inserisci qualcosa: ")
        parole += azione_1
        print(parole)
        if azione_1 == "":
            print("Sto chiudendo il programma")
            break

senza_andare_a_capo() 


#Soluzione 

def print_senza_andare_a_capo():
    input_utente = input("Inserisci una stringa: ")
    while input_utente != "":
        print(input_utente, end=" ")
        input_utente = input("Inserisci una stringa: ")

print_senza_andare_a_capo()     