from get_perfect_number import is_perfect_number

def get_number_of_perfect_numbers(input_num):
    return sum(1 for num in range(1, input_num + 1) if is_perfect_number(num))
