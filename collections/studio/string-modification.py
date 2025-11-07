my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
piglatin = my_string[0:3]
modified_string = my_string[3:] + piglatin
print(my_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"Original word: {my_string}, Modified word: {modified_string}")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
their_string = input("Enter a word: ")
their_number = int(input("Please enter a number: "))
piglatin = their_string[0:their_number]
their_string = their_string[their_number: ] + piglatin
print(their_string)
# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
their_string = input("Enter a word: ")
their_number = int(input("Please enter a number: "))
original_word = their_string
if their_number > len(their_string):
    print(f"Oops! {their_number} is larger than the word. Defaulting to 3.")
    num_to_move = 3
    error_message = f" (Note: {their_number} was too large, defaulted to 3)"
else:
    num_to_move = their_number
piglatin = their_string[0:num_to_move]
modified_word = their_string[num_to_move:] + piglatin