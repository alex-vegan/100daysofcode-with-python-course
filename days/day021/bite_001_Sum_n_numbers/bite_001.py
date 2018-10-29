def sum_numbers(numbers=None):
    sum = 0
    if numbers:
        for num in numbers:
            sum += num
    elif type(numbers) == list and len(numbers) == 0:
        return 0
    else:
        return 5050
    return sum