def optimal_task_assignment(llist):
    sorted_list = sorted(llist)
    hours = 0
    for i in range(int(len(sorted_list) / 2)):
        pair_hours = sorted_list[i] + sorted_list[- (i + 1)]
        if pair_hours > hours:
            hours = pair_hours

    return hours


if __name__ == '__main__':
    test_list = [6, 3, 2, 7, 5, 5]

    print(optimal_task_assignment(test_list))
