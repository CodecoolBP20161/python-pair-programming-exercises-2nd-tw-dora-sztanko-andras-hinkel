import random


def random_number():
    return chr(random.randint(48, 57))


def random_upper_case():
    return chr(random.randint(65, 90))


def random_lower_case():
    return chr(random.randint(97, 122))


def random_symbol():
    x = list(range(33, 47))
    x.extend(list(range(58, 64)))
    x.extend(list(range(91, 96)))
    x.extend(list(range(123, 126)))

    return chr(random.choice(x))

def passwordgen(weak=False):
    password = []
    weak_passwords = ['cat', 'password', '0000', '1234']

    if weak is False:
        for i in range(0, random.randint(8, 16)):
            random_choice = random.randint(1, 4)

            if random_choice == 1:
                password.append(random_number())
                number = True
            elif random_choice == 2:
                password.append(random_upper_case())
                upper_case = True
            elif random_choice == 3:
                password.append(random_lower_case())
                lower_case = True
            elif random_choice == 4:
                password.append(random_symbol())
                symbol = True

            if not number:
                password.append(random_number())
            if not upper_case:
                password.append(random_upper_case())
            if not lower_case:
                password.append(random_lower_case())
        return "".join(password)
    else:
        return weak_passwords[random.randint(0, len(weak_passwords)-1)]


def main():
    answer = input("Would you like to create a strong password? Y/n ")
    if answer != "n":
        password = passwordgen(False)
    else:
        password = passwordgen(True)
    print("Your new password is: '{}'".format(password))
    print("Thank you for using us! Have a nice day!")


if __name__ == '__main__':
    main()
