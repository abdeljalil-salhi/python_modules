# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: absalhi <absalhi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 16:07:40 by absalhi           #+#    #+#              #
#    Updated: 2022/12/05 16:52:42 by absalhi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from contextlib import suppress

cookbook = {
	"sandwich": {
		"ingredients": ["ham", "bread", "cheese", "tomatoes"],
		"meal": "lunch",
		"prep_time": 10
	},
	"cake": {
		"ingredients": ["flour", "sugar", "eggs"],
		"meal": "dessert",
		"prep_time": 60
	},
	"salad": {
		"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
		"meal": "lunch",
		"prep_time": 15
	}
}

def print_recipes():
	with suppress(Exception):
		for key in cookbook: print(key)

def print_recipe_details(name):
	with suppress(Exception):
		for key in cookbook[name]: print(f"{key}: {cookbook[name][key]}" if key != "ingredients" else f"{key}: {', '.join(cookbook[name][key])}")

def delete_recipe(name):
	with suppress(KeyError): del cookbook[name]

def add_recipe():
	try:
		print("Enter a name:")
		name = input()
		ingredients = []
		print("Enter ingredients:")
		tmp = input()
		while tmp != "":
			ingredients.append(tmp)
			tmp = input()
		print("Enter a meal type:")
		meal = input()
		print("Enter a preparation time:")
		prep_time = input()
		cookbook[name] = {
			"ingredients": ingredients,
			"meal": meal,
			"prep_time": prep_time
		}
	except:
		print("Error.")
