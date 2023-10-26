def len_str_list(a):
    print(len(a))


len_str_list("safsgasgsggssgssgsagsgfafgagassdgagassgasga")
len_str_list(["alfabeto", "vocale", "morale"])



# Soluzione

def my_len(lst_or_str):
    length = 0
    for unit in lst_or_str:
        length += 1
    return length

