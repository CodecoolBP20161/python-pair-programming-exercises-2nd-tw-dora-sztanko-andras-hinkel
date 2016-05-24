import random


def listoverlap(list1, list2):
    return list(set(list1) & set(list2))


def main():
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    a = [random.randint(1, 50) for x in range(1, random.randint(10, 20))]
    print(sorted(a))
    b = [random.randint(1, 50) for x in range(1, random.randint(10, 20))]
    print(sorted(b))

    print(listoverlap(a, b))


if __name__ == '__main__':
    main()
