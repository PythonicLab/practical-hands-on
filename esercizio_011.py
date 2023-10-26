#Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere 
#componente la stringa.
#Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}

def frequenza_di_comparsa(stringa):
    dizionario = {}
    for lettera in stringa:
        indice = stringa.index(lettera) + 1
        frequenza = 1
        while indice < len(stringa):
            if stringa[indice] == lettera:
                frequenza += 1
            indice += 1
        dizionario[lettera] = frequenza                
        
    return dizionario

print(frequenza_di_comparsa("barabba"))

# Soluzione

def char_freq(str):
    mappa = {}
    for carattere in str:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    return mappa

