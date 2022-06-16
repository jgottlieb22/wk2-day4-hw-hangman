from operator import index
import random
# from IPython.display import clear_output

word_list = ['storybook', 'excellence', 'meteor', 'mississippi', 'tabletop', 'vacuum', 'galactic', 'superstar', 'emphatic', 'puppy', 'romanticism']


def select_letter():

    # Select random word from list of words
    hidden_word = random.choice(word_list)
    print(f"""
    {hidden_word}
    """)
    incorrect_guesses_remaining = 7
    progress = []
    guessed_letters = []

    # Add blanks in the running progress list for each letter in hidden word
    for each in hidden_word:
        progress.append('_ ')

    print(f"""
    {progress}
    """)

    # Add while loop to continue running until user wins or loses.
    finished = False
    while finished == False:

        # User selects letter
        selection = input("Guess a letter: ").lower()
        for num in range(len(hidden_word)):
            
            # If guess is correct, add it to progress and list of guessed letters
            if selection == hidden_word[num]:
                progress[num] = selection
                if selection not in guessed_letters:
                    guessed_letters.append(selection)
                
        print(f"""
        {progress}
        """)
        # If guess is correct, congratulate user
        if selection in hidden_word:
            print("""
Nice work! That was a good guess.
            """)
       
        # If guess incorrect, subtract 1 from remaining guesses and add letter to guessed letters list     
        if selection not in hidden_word:
            incorrect_guesses_remaining -= 1
            guessed_letters.append(selection)
            print(f"""
That is not correct. You have {incorrect_guesses_remaining} incorrect guesses remaining.
            """)
            print(f"""Guessed letters: {guessed_letters}
            """)

        # If out of guesses, end game and ask if user wants to play again
        if incorrect_guesses_remaining == 0:
            finished = True
            print(f"""
Sorry.  You lose.  The correct word was {hidden_word}. Better luck next time.
            """)
            again = input("Play again? y/n: ").lower()
            if again == 'y':
                setup()
                select_letter()
            else:
                finished = True
                print("See ya!")

        # If user completes word, congratulate and ask if user wants to play again    
        if '_ ' not in progress:
            finished = True
            print("""
Congratulations!  You won!!!
            """)
            again = input("Play again? y/n: ").lower()
            if again == 'y':
                select_letter()
            else:
                finished = True
                print("See ya!")



select_letter()