def value_predictor(numbers):

    total_sum = sum(numbers)
    total_numbers = len(numbers)

    return total_sum/total_numbers


print(value_predictor([1, 1, 1, 6, 6, 6]))
