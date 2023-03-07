#  Brittney Bui

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(encoded_num):
    num_input = ""

    for i in encoded_num:
        num_input += str((int(i) + 3) % 10)
    return num_input


def main():
    while True:
        menu()
        option = input("Please enter an option: ")
        if option == "3":
            break

        elif option == "1":
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!")


if __name__ == "__main__":
    main()
