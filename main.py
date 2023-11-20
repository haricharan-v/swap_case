first_time = True
try_again_inp = True

def swap_case(s):
    global first_time
    # Define new string
    new_str = ""
    # Make a for loop to iterate through every character in the given string
    for char in s:
        # Check if the character is lowercase
        if char.islower():
            # Convert the string to uppercase
            # Add uppercase character to the new_str
            new_str += char.upper()
        # Check if the character is uppercase
        elif char.isupper():
            # Convert the string to lowercase
            # Add lowercase character to the new_str
            new_str += char.lower()
        # Check if the character is not an alphabet
        else:
            # Add character to new_str as is
            new_str += char
    first_time = False
    # Return new_str
    return new_str

def try_again():
    global try_again_inp
    user_response_original = input("If you want to try again, enter y for Yes and n fo No: ")
    user_response = user_response_original.lower()
    if type(user_response) == str:
        if user_response == "y":
            # Take user input
            new_use_input = input("Enter the string you want to swap cases: ")
            # Call the swap_case function with argument as user_input and store it in variable
            swap_func = swap_case(new_use_input)
            # Print the result
            print(swap_func)
        elif user_response == "n":
            try_again_inp = False
            print("Hope you try again next time!")
        else:
            print("That isn't a valid input. Please enter y or n.")

    else:
        print("That isn't a valid input")

while try_again_inp:
    if first_time:
        # Take user input
        user_input = input("Enter the string you want to swap cases: ")
        # Call the swap_case function with argument as user_input and store it in variable
        swap_case_function = swap_case(user_input)
        # Print the result
        print(swap_case_function)
    elif not first_time:
        try_again()
