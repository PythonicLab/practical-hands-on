numero_1 = input("Inserisci il primo numero: ")
numero_2 = input("Inserisci il secondo numero: ")
numero_3 = input("Inserisci il terzo numero: ")

print(max(numero_1, numero_2, numero_3))



def numero_alto(a, b, c):
    return a, b, c

print(max(numero_alto(500, 850, 745)))



# Soluzione

a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")
c = input("Inserisci il terzo numero: ")

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)