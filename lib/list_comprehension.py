#!/usr/bin/env python3

def return_evens(num_list):
    even_num = []
    for n in num_list:
        if n % 2 == 0:
            even_num.append(n)
    return even_num


def make_exclamation(sentence_list):

    strings = []
    for n in sentence_list:
        strings.append(f"{n}!") 
    return strings

    
 



