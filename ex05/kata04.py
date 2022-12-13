# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: absalhi <absalhi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/01 20:04:07 by absalhi           #+#    #+#              #
#    Updated: 2022/12/01 20:14:06 by absalhi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    kata = (0, 4, 132.42222, 10000, 12345.67)

    print(f"module_{kata[0]:02}, ex_{kata[1]:02} : {kata[2]:.2f}, {kata[3]:#.2e}, {kata[4]:#.2e}")

"""
[‘e’] Scientific notation.
For a given precision p, formats the number in scientific notation with
the letter ‘e’ separating the coefficient from the exponent. The coefficient
has one digit before and p digits after the decimal point, for a total of
p + 1 significant digits. With no precision given, uses a precision of 6 digits
after the decimal point for float, and shows all coefficient digits for Decimal.
If no digits follow the decimal point, the decimal point is also removed unless the # option is used.
"""