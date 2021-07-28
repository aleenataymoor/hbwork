"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight


def print_all_melons(melon_names, melon_seedlessness, 
                        melon_prices, flesh_color,      
                        rind_color, average_weight):
    """Print each melon with corresponding attribute information."""

    for key, melon_name in melon_names.items():
        print(melon_name.upper())
        print(f'price: {melon_prices.get(key, None)}')
        print(f'Seedlessness: {melon_seedlessness.get(key, None)}')
        print(f'Flesh_Color: {flesh_color.get(key, None)}')
        print(f'Rind_Color: {rind_color.get(key, None)}')
        print(f'weight:{average_weight.get(key,None)}')
            
        print('*-*-*-*-*=======*-*-*-*-*-*')

print_all_melons(melon_names, melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight)
