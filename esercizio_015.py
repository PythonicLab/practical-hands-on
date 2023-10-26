
#Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless 
#(es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.

#Un esempio di MAC è 02:FF:A5:F2:55:12.

#Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.
#11111111 
#FF
#255

import random

def genera_mac_address():
    val_elaborato = ""
    for carattere in range(7):
        val = random.randint(0, 255)
        val_elaborato += f"{val:02x}"
        if carattere < 6:
            val_elaborato += ":"
    return val_elaborato

    
print(genera_mac_address())


# Soluzione

# import random

def genera_mac():
    char_set = "ABCDEF0123456789"
    mac_addr = ""
    due_punti = 0

    for _ in range(6):
        for _ in range(2):
            mac_addr += random.choice(char_set)
        if due_punti < 5:
            mac_addr += ":"
            due_punti += 1

    return mac_addr

