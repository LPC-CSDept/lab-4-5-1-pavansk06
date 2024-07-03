import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i = 0
    numbers = []
    while i < 5:
        i = i + 1
        num = random.randrange(0, 100)
        numbers.append(num)
    
    total = sum(numbers)
        
   

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers#, total


if __name__ == '__main__':
    main()
