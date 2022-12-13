# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: absalhi <absalhi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/01 13:47:34 by absalhi           #+#    #+#              #
#    Updated: 2022/12/01 13:51:38 by absalhi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

if __name__ == "__main__":
	if len(argv) > 1:
		if len(argv) == 2:
			try:
				n = int(argv[1])
				if n == 0:
					print("I'm Zero.")
				elif n % 2 == 0:
					print("I'm Even.")
				else:
					print("I'm Odd.")
			except ValueError:
				print("AssertionError: argument is not an integer")
				exit(1)
		else:
			print("AssertionError: more than one argument are provided")
			exit(1)
	else:
		print("Usage: python3 whois.py 42")
		exit(0)
