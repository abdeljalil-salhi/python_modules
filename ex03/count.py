# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: absalhi <absalhi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/01 13:53:21 by absalhi           #+#    #+#              #
#    Updated: 2022/12/01 14:04:19 by absalhi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from string import punctuation
from sys import argv

def text_analyzer(*args):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if len(args) == 0 or args[0] == None:
		print("What is the text to analyze?")
		text_analyzer(input())
		return
	if not isinstance(args[0], str):
		print("AssertionError: argument is not a string")
		exit(1)
	(upper, lower, punct, space) = 0, 0, 0, 0
	for c in args[0]:
		if c.isupper():
			upper += 1
		elif c.islower():
			lower += 1
		elif c in punctuation:
			punct += 1
		elif c.isspace():
			space += 1
	print(f"The text contains {len(args[0])} character(s):")
	print(f"- {upper} upper letter(s)")
	print(f"- {lower} lower letter(s)")
	print(f"- {punct} punctuation mark(s)")
	print(f"- {space} space(s)")


if __name__ == "__main__":
	if len(argv) > 1:
		if len(argv) == 2:
			text_analyzer(argv[1])
		else:
			print("AssertionError: more than one argument are provided")
			exit(1)
	else:
		print("AssertionError: no arguments are provided")
		exit(1)
