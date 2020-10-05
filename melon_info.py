"""Print out all the melons in our inventory."""


from melons import (melon_names, melon_seedlessness, melon_prices, 
melon_flesh_color, melon_weight, melon_rind_color)


def print_melon(name, seedless, price, fleshcolor, weight, rindcolor):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')
    print(f"{name}: \n"
            f"seedless: {seedless}\n" 
            f"price: {price}\n"
            f"flesh color: {fleshcolor}\n"
            f"weight: {weight}\n" 
            f"rind color: {rindcolor}\n")


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i],
                melon_flesh_color[i], melon_weight[i], melon_rind_color[i])