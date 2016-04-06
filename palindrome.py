# import the re module
import re
# first we are going to ask the user to input a string of word(s)

def reverse_string(text):
    if len(text) == 0:
         return ''
    return reverse_string(text[1:]) + text[0]

def is_palindrome(user_palindrome_input):
    if user_palindrome_input == reverse_string(user_palindrome_input):
        return True
    else:
        return False

def main():
    user_palindrome_input = input("Hello, please give me a word, sentence or group of sentences and I can tell you if it is a palindrome or not. It must be longer than (2) characters. ")

    user_inputs_a_palindrome = is_palindrome(user_palindrome_input)
    if user_inputs_a_palindrome:
        print("Wow, that's a palindrome!")

    else:
        print("Sorry, that isn't a palindrome.")

if __name__ == '__main__':
    main()
