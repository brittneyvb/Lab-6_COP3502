#  Brittney Bui

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def encode(encoded_num):
    num_input = ""

    for i in encoded_num:
        num_input += str((int(i) + 3) % 10)
    return num_input


def decode(decode_num):
    decoded_string = ""
    for i in decode_num:
        decoded_string += str(((int(i) - 3) + 10) % 10)
    return decoded_string


def main():
    while True:
        menu()
        option = input("Please enter an option: ")
        if option == "3":
            break
        elif option == "1":
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")


if __name__ == "__main__":
    main()

# ((i-3)+10)%10
