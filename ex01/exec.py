# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: absalhi <absalhi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/01 13:33:49 by absalhi           #+#    #+#              #
#    Updated: 2022/12/01 13:51:11 by absalhi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

if __name__ == "__main__":
	if len(argv) > 1:
		print(" ".join(argv[1:])[::-1].swapcase())
		exit(0)
	print("Usage: python3 exec.py 'Hello World!'")
	exit(0)
