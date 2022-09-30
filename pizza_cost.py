#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in September 2022
# A program that finds the cost of a pizza, using user inputted diameter

import constants


def main():
    # Finds the cost of a pizza using diameter sent by the user

    diameter_of_pizza = int(input("Enter the diameter of the pizza (in): "))
    subtotal = (
        constants.LABOUR_COST
        + constants.SHOP_RENT
        + (constants.MATERIALS * diameter_of_pizza)
    )
    total = subtotal + (subtotal * constants.HST)
    print("\nThe cost of this pizza is ${:,.2f}".format(total))

    print("\nDone.")


if __name__ == "__main__":
    main()
