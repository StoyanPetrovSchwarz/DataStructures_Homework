# Couldn't find the file with the list 'test_list' that I need to use,
# that's why I will use the one from the presentation

# 1st way
def find_kth_max(k):
    kth_max = 0
    test_list = [40, 35, 82, 14, 22, 66, 53]

    reworked_list = sorted(test_list)[::-1]

    kth_max = reworked_list[-k]

    return kth_max

    # try:
    #     return reworked_list[-k]
    # except IndexError:
    #     return 'Index out of range'


# 2nd way
def find_kth_max2(k):
    test_list = [40, 35, 82, 14, 22, 66, 53]
    sorted_list = sorted(test_list)
    kth_max = [sorted_list[i] for i in range(len(sorted_list)) if i == k - 1][0]
    return kth_max


if __name__ == '__main__':
    print(find_kth_max(2))
    print(find_kth_max(6))
    print(find_kth_max2(7))
