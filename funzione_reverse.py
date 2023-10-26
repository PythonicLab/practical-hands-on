
def reverse(parola):
    nuova_parola = ""
    indice = (len(parola) -1)
    while indice >= 0:
        nuova_parola += parola[indice]
        indice -= 1
    return nuova_parola



        