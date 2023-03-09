# Christian Mora


# encode() will take in a string of 8 numbers and return the encoded string where each digit equals itself plus 3.
def encode(password):

    # creating an empty string as a placeholder for the encoded password.
    encoded_password = ''

    # The for loop iterates for each digit in the inputted password.
    for digit in password:

        # encoded_digit converts each string digit into an int so 3 can be added,
        # modulus 10 ensures that the newly encoded digit still falls between 0-9,
        # then the digit is converted back to a string.
        encoded_digit = str((int(digit) + 3) % 10)

        # each encoded digit is added to the encoded_password string
        encoded_password += encoded_digit

    # returns the new encoded password
    return encoded_password


def decode(password):  # based on given encoded 8 eight password, decodes to original by subtracting 3 for each digit
    decoded_password = ""
    decoded_char_value = ""

    # for each, checks if there's a remainder less than 0, if so subtracts reminder from 10 to loop back
    # if no remainder less than 0, subtracts 3 from the digit
    for i in password:
        if (int(i) - 3) < 0:
            decoded_char_value = str(10 + (int(i) - 3))
        else:
            decoded_char_value = str((int(i) - 3))
        decoded_password = decoded_password + decoded_char_value
    return decoded_password


while __name__ == '__main__':
    # quit_menu will equal 1 when the user wants to quit the program.
    quit_menu = 0

    # The program will loop until the user wants to quit.
    while quit_menu != 1:

        # Printing the encoder menu.
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        # Prompts the user to select a menu option.
        menu_input = int(input('Please enter an option: '))

        # This if loop runs if the user selects the menu option 1. Encode.
        if menu_input == 1:

            # Prompts the user to enter a password to encode.
            pass_to_encode = input('Please enter your password to encode: ')

            # If the password is not 8 digits, an error message is printed.
            if len(pass_to_encode) != 8:
                print('Error, your password should be 8 digits.')
                continue

            # encoded_pass stores the newly encoded password.
            encoded_pass = encode(pass_to_encode)

            # Prints a statement to let the user know the password was encoded.
            print('Your password has been encoded and stored!\n')

        # This elif will run if the user selects the menu option 2. Decode.
        elif menu_input == 2:
            pass_to_encode = decode(encoded_pass)
            # Prints the encoded password and the decoded password, which is identical to the original password.
            print('The encoded password is ', encoded_pass, ', and the original password is ', pass_to_encode, '.\n', sep='')

        # This elif will cause the program to end if the user selects menu option 3.
        elif menu_input == 3:
            quit_menu = 1
            break

    break





