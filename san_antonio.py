# -*- coding: utf8 -*-
import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1) #returns a number between 0 and the total length of my list.
    item = my_list[rand_numb] # find the item that matches the randomly determined index.
    return item # returned value

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    c_character = capitalize(character)
    c_quote = capitalize(quote)
    return "{} à dit : {}".format(c_character, c_quote)


user_answer = input("Taper sur entrée pour connaitre une autre citation ou B pour quitter le programme.")

while user_answer != "B":
    print(message(get_random_item_in(characters), get_random_item_in(quotes)))
    user_answer = input("Taper sur entrée pour connaitre une autre citation ou B pour quitter le programme.")




