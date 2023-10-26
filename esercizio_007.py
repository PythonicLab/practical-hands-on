e = "i"
lista_e = ["a", "o", "v", "d", "g"]
                
if e in lista_e:
    print(lista_e.index(e))
else:
    print(f"L'elemento {e} non è presente nella lista")
        
        
        
# Soluzione

lista = ['Marco', 'Luigi', 'Paolo', 'Giuseppe', 'Maria']
el = input("Inserisci un nome da cercare: ")
trovato = False
for nome in lista:
    if nome == el:
        trovato = True
        break
if trovato:
    print(f"{el} è presente nella lista all'indice {lista.index(el)}")
else:
    print(f"{el} non è presente nella lista.")       