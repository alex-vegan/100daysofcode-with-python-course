def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 0
    except Exception as x:
        raise x
    if result < 0:
        raise ValueError
    return result
        