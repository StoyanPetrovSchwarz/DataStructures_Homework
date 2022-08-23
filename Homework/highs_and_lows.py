def count_low_high(num_list):
    if not num_list:
        return None

    lows = [x for x in num_list if (x <= 50 and x % 3 != 0)]
    highs = [x for x in num_list if (x > 50 or x % 3 == 0)]

    result = [len(lows), len(highs)]

    return result


num_list = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high(num_list))
print(count_low_high([]))
