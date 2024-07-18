try:
    my_lista = [1, 2, 3]
    print(my_lista[5])
except IndexError as ie:
    print(f"Error: {ie}")
