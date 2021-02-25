import random
from wonderwords import RandomWord

SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'

#THIS SECTION IS TO GENERATE A RANDOM WORD
r = RandomWord()
snowman_word = r.word(
    word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
    word_max_length=SNOWMAN_MAX_WORD_LENGTH)
print(snowman_word)

def snowman(snowman_word):
    """Complete the snowman function
    It should print 'Congratuations, you win!'
    If the player wins and, 'Sorry, you lose!  The word was {snowman_word}' if the player loses
    """
    wrong_guesses_list = []
    correct_guesses_list = []
    all_guessed_flag = False
    user_word_list = build_word_list(snowman_word)

    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES and not all_guessed_flag: 
       
        #Print how many letters have been guessed in the word. 
        #In case a letter has not been guessed, print a '_'
        print_word_list(user_word_list)
        
        #Ask the user for a letter and store it in the corresponding list 
        #as correct or incorrect
        guessed_letter = get_letter_from_user(wrong_guesses_list, correct_guesses_list)
        if guessed_letter in snowman_word:
            print("You guessed a letter that is in the word. Keep trying!")
            correct_guesses_list.append(guessed_letter)
        else:
            print(f"Letter {guessed_letter} is not in the word. Try again!")
            wrong_guesses_list.append(guessed_letter)
        
        #Update the user_word_list. If the guessed letter is in the snowman word, 
        #then it is activated in the user word list to print it in next iteration
        all_guessed_flag = update_and_check_word_list(user_word_list,guessed_letter)
        
        #Print snowman progress according to the user's wrong guesses
        print_snowman_graphic(len(wrong_guesses_list))
    
    if not all_guessed_flag:
        #len(wrong_guesses_list) == SNOWMAN_MAX_WRONG_GUESSES:
        print(f"Sorry, you lose!  The word was {snowman_word}")
    elif all_guessed_flag: # and len(correct_guesses_list) == len(snowman_word):
        print("Congratulations, you win!")


def print_snowman_graphic(num_wrong_guesses):
    """This function prints a portion of the 
    snowman depending on the number of 
    wrong guesses
    """
    for i in range(1, num_wrong_guesses + 1):
        if(i == 1):
            print(SNOWMAN_1)
        if(i == 2):
            print(SNOWMAN_2)
        if(i == 3):
            print(SNOWMAN_3)
        if(i == 4):
            print(SNOWMAN_4)
        if(i == 5):
            print(SNOWMAN_5)
        if(i == 6):
            print(SNOWMAN_6)
        if(i == 7):
            print(SNOWMAN_7)

def build_word_list(word):
    """This function builds a list of dictionaries
    With each letter and "guessed": False
    Example: [ { 'letter': 'a', 'guessed': False }, 'letter': 'b', 'guessed': False }, ]
    """
    word_list = []
    for letter in word:
        letter_dict = {"letter": letter, "guessed": False}
        word_list.append(letter_dict)
    return word_list

def print_word_list(word_list):
    """This function prints the letters of the word
    based on if that letter has been guessed or not
    """
    output_string = ""
    for elem in word_list:
        if elem["guessed"]:
            output_string += elem["letter"]
        else:
            output_string += "_"
        output_string += " "
    print(output_string)


def get_letter_from_user(wrong_list, correct_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in wrong_list or user_input_string in correct_guesses_list:
            print(f"You have already guessed letter {user_input_string}")
        else:
            valid_input = True
    return user_input_string

#RETURN TRUE IF ALL LETTERS HAVE BEEN GUESSED AND FALSE IF ONE OR MORE ARE MISSING
def update_and_check_word_list(list_of_letters, guessed_letter):
    all_letters_guessed = True
    for letter_dict in list_of_letters:
        if (guessed_letter == letter_dict["letter"]):
            letter_dict["guessed"] = True
        elif (not letter_dict["guessed"]):
            all_letters_guessed = False
    
    return all_letters_guessed





snowman(snowman_word)
