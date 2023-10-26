carattere = input("Inserisci un carattere dell'alfabeto: ")
vocali = ["a", "e", "i", "o", "u"]

if carattere in vocali:
    print("Il carattere " + carattere + " è una vocale")
else:
    print("Il carattere " + carattere + " non è una vocale")
    
    
    
# Soluzione

carattere = input("Inserisci un carattere: ")
vocali = "aeiou"
if carattere in vocali:
    print(f"Il carattere {carattere} è una vocale")
else:
    print(f"Il carattere {carattere} non è una vocale")
    
    