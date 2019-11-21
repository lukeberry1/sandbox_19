from random import randint


# def random_number(n):
#     numbers = []
#     for number in range(n):
#         numbers.append(randint(1, 10 * n))
#     print(numbers)

def random_number(n):
    numbers = [randint(1, 10 * n) for number in range(n)]
    print(numbers)


random_number(4)
