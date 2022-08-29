# Assuming that every worker gets 2 jobs at a time,
# that's why there is no check for lists with odd number of elements
def optimal_task_assignment(llist):
    sorted_list = sorted(llist)
    hours = 0
    for i in range(int(len(llist) / 2)):
        pair_hours = sorted_list[i] + sorted_list[- (i + 1)]
        if pair_hours > hours:
            hours = pair_hours

    return hours


# Didn't understand if the number of workers should be passed as parameter, so I did it both ways
# Also in the second function I return hours for each worker
def optimal_task_assignment2(number_workers, llist):
    sorted_list = sorted(llist)
    hours = []
    for i in range(number_workers):
        pair_hours = sorted_list[i] + sorted_list[- (i + 1)]
        hours.append(pair_hours)

    return hours


if __name__ == '__main__':
    workers = 3
    test_list = [6, 3, 2, 7, 5, 5]

    print(optimal_task_assignment(test_list))
    # Output: 10

    print(optimal_task_assignment2(workers, test_list))
    # Output: [9, 9, 10]
