"""Print out all the melons in our inventory."""

from melons import melons

def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for melon, attributes in melons.items():
        print(melon.upper())
        for name, value in attributes.items():
            print(f'     {name}: {value}')

print_melon(melons)
