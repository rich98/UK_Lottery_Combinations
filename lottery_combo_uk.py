import math


def calculate_combinations(total_numbers, numbers_to_choose):

    combinations = math.comb(total_numbers, numbers_to_choose)

    return combinations


total_numbers = 59


numbers_to_choose = 6


combinations = calculate_combinations(total_numbers, numbers_to_choose)

print(f"The total number of combinations is: {combinations} to 1")

