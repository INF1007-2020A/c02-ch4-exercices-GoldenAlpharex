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
	return f"Aujourd'Hui, j'ai vu un {animal} s'emparer d'un panier {adjective} plein de {fruit}."


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
