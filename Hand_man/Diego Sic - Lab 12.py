#Diego Sic
#This program it's to play hangman with a word
#predetermined "misisipi"

def to_continue():
    '''This function it's to create a friendly
        enviroment for the user using enter
        a stop
        input: " "
        output: None'''
    input("Press Enter to continue...")
    
def convert_word_in_list(word):
    '''This function it's to create a list
        with all the letters of a word, so we
        can interact with the positions
        input: A string
        output: A list with the characters of the string'''
    l_word = []
    for char in word:
        l_word.append(char)
    return l_word

def converting_word_into_underscores(word):
    '''This function it's to create a list
        with "_" with the len of the word wanted
        input: A string
        output: A list with "_" determined by the
        the len of the given string'''
    l_word_coded = []
    for char in word:
        l_word_coded.append("_")
    return l_word_coded
    
def print_word(l_word_coded):
    '''This function it's to print the list
    with the char that the user have guessed
    input: A list with "_"
    output: A list with characters and "_"
    depending of the guesses of the user'''
    for char in l_word_coded:
        print(char, end = " ")
    print(" ", end="")

def checking_user_input(word, user_input, l_word_code):
    '''This function it's to determine of
    the user have guessed a letter correctly
    input: A list with "_"
    output: A list with characters and "_"
    depending of the guesses of the user'''
    for i in range(len(word)):
        if word[i] == user_input:
            l_word_code[i] = user_input
    return l_word_code

def print_dead_man(attempts_allowed):
    '''This function will determine which
    picture draw depending on the number of
    tries the user still have
    input: The quantity of attempts allowed(integer)
    ouput: A ascii art to draw(String)'''
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    print(HANGMANPICS[-(attempts_allowed+1)])

    
def main():
    s_word = "misisipi"
    i_attempts_allowed = 6
    b_show_only_once = True
    
    l_word_to_guess = convert_word_in_list(s_word)
    l_converted_word = converting_word_into_underscores(s_word)
    
    print(f"You have {i_attempts_allowed} left")
    print_dead_man(i_attempts_allowed)
    print_word(l_converted_word)
    
    
    while True:
        user_input_1 = input("Give the letter to try:")
        list_to_print = checking_user_input(s_word, user_input_1, l_converted_word)
                
        if user_input_1 not in l_word_to_guess:
            i_attempts_allowed -= 1

        if i_attempts_allowed == 1 and b_show_only_once:
            print("*******************")
            print("YOU HAVE 1 MORE TRY")
            print("*******************")
            b_show_only_once = False
            to_continue()
            
        if "_" not in list_to_print:
            print_word(list_to_print)
            print("YOU WIN!!")
            break
            
        if i_attempts_allowed == 0:
            print("********")
            print("YOU LOSE")
            print("********")
            print_dead_man(-7)
            break
        
        print(f"You have {i_attempts_allowed} left")
        print_dead_man(i_attempts_allowed)
        print_word(list_to_print)
        
        

if __name__ == "__main__":
    main()
