# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: absalhi <absalhi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/01 13:59:38 by absalhi           #+#    #+#              #
#    Updated: 2022/12/01 14:04:23 by absalhi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

if __name__ == "__main__":
	if len(argv) < 3:
		print("Usage: python3 operations.py <number1> <number2>")
		exit(0)
	if len(argv) > 3:
		print("AssertionError: too many arguments")
		exit(1)
	try:
		(n1, n2) = int(argv[1]), int(argv[2])
	except ValueError:
		print("AssertionError: only integers")
		exit(1)
	print(f"Sum:        {n1 + n2}")
	print(f"Difference: {n1 - n2}")
	print(f"Product:    {n1 * n2}")
	print(f"Quotient:   {'ERROR (division by zero)' if n2 == 0 else n1 / n2}")
	print(f"Remainder:  {'ERROR (modulo by zero)' if n2 == 0 else n1 % n2}")
