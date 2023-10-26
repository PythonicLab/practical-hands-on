#Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.

#Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria! ;)

import os

def sistema_operativo():
    sys = (os.uname().sysname), (os.uname().release), (os.uname().version), (os.uname().machine)
    return sys

print(sistema_operativo())


# Soluzione

import platform

def sys_info():
    print("Il Sistema attualmente in uso è: " + platform.system())
    print("Info Release: " + platform.release())

sys_info()