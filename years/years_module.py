from datetime import date

def years(age):
    years_till_100 = 100 - age
    return date.today().year + years_till_100


def main():
    name = input("What is your name?: ")
    age = int(input("How old are you? "))
    message = "So, {}, you're going to be 100 years old in {}!".format(name, years(age))
    print(message)


if __name__ == '__main__':
    main()
