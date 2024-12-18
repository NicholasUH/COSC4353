from get_number_of_perfect_numbers import get_number_of_perfect_numbers
        
def print_reponse(num):
    print(f'Here are the number of perfect numbers from 1 to {num}:',get_number_of_perfect_numbers(num))

def get_user_input():
    while True:
        try:
            num = int(input("Please enter a number greater than or equal to 1: "))
            return num
        except ValueError:
            pass

if __name__ == "__main__":
    print_reponse(get_user_input())
    