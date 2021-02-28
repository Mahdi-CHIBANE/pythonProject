# -*- coding: utf8 -*-
import random
import json

#read the characters.json file and the quotes.json and convert it to a list
def read_values_from_json(file, key):
    values = []   # Create a new empty list
    with open(file) as f: # open a json file with my objects
      data = json.load(f) # load all the data contained in this file, The load () method transforms a JSON file into a Python object.
      for entry in data:     # add each item in my list
        values.append(entry[key])
    return values  # return my completed list

def message(character, quote):
    c_character = character.capitalize()
    c_quote = quote.capitalize()
    return "{} à dit : {}".format(c_character, c_quote)

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1) #returns a number between 0 and the total length of my list.
    item = my_list[rand_numb] # find the item that matches the randomly determined index.
    return item # returned value
    
def random_quote():
    all_value = read_values_from_json("quotes.json", "quote")
    return get_random_item_in(all_value)

def random_character():
    all_value = read_values_from_json("characters.json", "character")
    return get_random_item_in(all_value)

user_answer = input("Taper sur entrée pour connaitre une autre citation ou B pour quitter le programme.")

while user_answer != "B":
    print(message(random_character(), random_quote()))
    user_answer = input("Taper sur entrée pour connaitre une autre citation ou B pour quitter le programme.")




