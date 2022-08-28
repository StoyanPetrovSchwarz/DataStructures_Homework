def intersect_sorted_array(A, B):
    intersection = []
    for i in A:
        if i in B:
            if i not in intersection:
                intersection.append(i)

    return intersection


if __name__ == '__main__':
    A = [2, 3, 3, 5, 7, 11]
    B = [3, 3, 7, 15, 31]

    print(intersect_sorted_array(A, B))
