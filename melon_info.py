"""Print out all the melons in our inventory."""


from melons import all_melons


def print_melon(all_melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in all_melons.items():
        print(f'The {melon_name} has the following attributes:')
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

    
            

print_melon(all_melons)
