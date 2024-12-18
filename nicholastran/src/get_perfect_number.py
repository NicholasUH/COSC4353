def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def is_perfect_number_two_times(num, sum):
    return sum == 2 * num

def is_perfect_number(num):
    return is_perfect_number_two_times(num, sum(get_factors(num)))
