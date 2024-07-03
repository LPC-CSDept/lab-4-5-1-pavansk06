import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i = 0
    numbers = []
    while i <= 5:
        i = i + 1
        num = int(random.random())
        numbers.append(num)
        
    total = int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]) + int(num[5])

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
