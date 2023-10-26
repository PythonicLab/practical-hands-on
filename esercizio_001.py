numero_1 = input("Inserisci il primo numero: ")
numero_2 = input("Inserisci il secondo numero: ")
if numero_1 > numero_2:
    print(numero_1)
elif numero_1 < numero_2:
    print(numero_2)
else:
    print("Hai inserito due numeri uguali")



def numero_alto(a, b):
    numero_1 = input("Inserisci il primo numero: ")
    numero_2 = input("Inserisci il secondo numero: ")
    if numero_1 > numero_2:
        print(numero_1)
    elif numero_1 < numero_2:
        print(numero_2)
    else:
        print("Hai inserito due numeri uguali")
        
        
numero_alto(8, 7)



# Soluzione 

a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")

if a == b:
    print("I numeri sono identici")
elif a > b:
    print("Il numero più grande tra i due è " + str(a))
else:
    print("Il numero più grande tra i due è " + str(b))

