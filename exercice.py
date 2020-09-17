#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0


def get_num_char(string, char):
	num_char = 0
	for character in string:
		num_char += 1 if character == char else 0
	return num_char


def get_first_part_of_name(name):
	first_name = name.split("-")[0]
	capitalized = first_name[0].upper() + first_name[1:].lower()
	return f"Bonjour, {capitalized}"


def get_random_sentence(animals, adjectives, fruits):
	animal = animals[random.randrange(0,len(animals))]
	adjective = adjectives[random.randrange(0,len(adjectives))]
	fruit = fruits[random.randrange(0,len(fruits))]
	return f"Aujourd'hui, j'ai vu un {animal} s'emparer d'un panier {adjective} plein de {fruit}."

# def alt_get_random_sentence(animals, adjectives, fruits):
# 	basic_sentence = "Aujourd'hui, j'ai vu un %s s'emparer d'un panier %s plein de %s."
# 	words = []
# 	for word_set in (animals, adjectives, fruits):
# 		words += [word_set[random.randrange(0, len(word_set))]]
# 	return basic_sentence % tuple(words)

# def alt_alt_get_random_sentence(animals, adjectives, fruits):
# 	basic_sentence = "Aujourd'hui, j'ai vu un %s s'emparer d'un panier %s plein de %s."
# 	words = [word_set[random.randrange(0, len(word_set))] for word_set in (animals, adjectives, fruits)]
# 	return basic_sentence % tuple(words)


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
	# print(alt_get_random_sentence(animals, adjectives, fruits))
	# print(alt_alt_get_random_sentence(animals, adjectives, fruits))
