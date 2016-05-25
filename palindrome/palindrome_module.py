def palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    return False


def main():
    user_input = input("Please type in a string! ")
    if palindrome(user_input):
        print("Yeah, this is a palindrome!")
    else:
        print("Sorry buddy, it's not a palindrome!")


if __name__ == '__main__':
    main()
