def even(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even(L))
