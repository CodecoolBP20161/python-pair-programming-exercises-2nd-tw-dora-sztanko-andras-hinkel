from datetime import date


def years(age):
    years_till_100 = 100 - age
    return date.today().year + years_till_100


def main():
    age = None
    number = None
    name = input("What is your name?: ")
    while age is None:
        try:
            age = int(input("How old are you? "))
        except ValueError:
            print("Please insert a number for your age!")
    while number is None:
        try:
            number = int(input("How many times should I print this stuff? "))
        except ValueError:
            print("Please insert a number!")
    message = "So, {}, you're going to be 100 years old in {}!".format(name, years(age))
    for i in range(number):
        print(message)

if __name__ == '__main__':
    main()
