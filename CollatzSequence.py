def collatz(number):
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        elif number % 2 == 1:
            print(3 * number + 1)
            return 3 * number + 1 

while True: 
    try:
        number = int(input('Enter number: '))
        while number != 1:
            number = collatz(number)
    except ValueError:
        print('Must enter an integer')

