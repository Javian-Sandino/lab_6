

def decoder(number):
    pass


def encoder(number):
    str_number = str(number)
    new_number = ""
    for i in str_number:
        new_number += str(int(i)+3)
    return new_number


def main():
    while True:
        menu = ("Menu\n------------- \n1. Encode\n2. Decode\n3. Quit")
        print(menu)
        option = int(input("Please enter an option:"))

        if option == 1:
            passcode = int(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")
            new_passcode = encoder(passcode)

        elif option == 2:
            decoded_passcode = decoder(new_passcode)
            print(f'The encoded password is {new_passcode}, and the original password is {decoded_passcode}.')


        elif option == 3:
            break


if __name__ == '__main__':
    main()