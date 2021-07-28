"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight


def print_all_melons(melon_names, melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight):
    """Print each melon with corresponding attribute information."""

    for key, melon_name in melon_names.items():
        print(melon_name.upper())
        print(f'price: {melon_prices.get(key, None)}')
        print(f'Seedlessness: {melon_seedlessness.get(key, None)}')
        print(f'Flesh_Color: {flesh_color.get(key, None)}')
        print(f'Rind_Color: {rind_color.get(key, None)}')
        print(f'weight:{average_weight.get(key,None)}')
            
        print('===================================')

print_all_melons(melon_names, melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight)
# from melons import melon_names, melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight

# def melon_info(melon_names,melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight):

#     seedless=None
#     if melon_seedlessness==True:
#         return "true"
#     elif melon_seedlessness==False:
#         return "false"

#     price = melon_prices

#     for i in melon_names:
#         melon_names[i]={}
#         melon_seedlessness[i].add(seedlessness)
#         return melon_names[i]

# melon_info(melon_names,melon_seedlessness, melon_prices, flesh_color, rind_color, average_weight)





# 


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
