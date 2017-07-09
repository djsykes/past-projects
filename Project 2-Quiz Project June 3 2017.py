
#The variables below are the quiz and answers to quizzes for the various difficulty levels. The lists are in answer form.
eanswers =[["___1___","INTEGER"],["___2___","STRING"],["___3___","FLOAT"],["___4___","LIST"]]
equiz="5 is a ___1___. '5' is a ___2___. 5.0 is a ___3___. A [5,5] is a ___4___."

manswers =[["___1___","FOR"],["___2___","WHILE"],["___1___","WHILE"],["___2___","FOR"],["___3___","FOR"],["___4___","WHILE"]]
mquiz="___1___ and ___2___ are two terms used for loop statements. ___3___ loops are good for when you know how many times a loop will run. ___4___ loops required a conditional statement"


hanswers =[["___1___","RANDINT"],["___2___","IMPORT"],["___3___","FROM"],["___4___","BEFORE"]]
hquiz="If you were to use ___1___, a random number generator, you would need to ___2___ it first. To use import, you need to use the term ___3___ first and you need to do this ___4___ you try to use the module."

#These are the functions used in the game.

def welcome():
    """ This function welcomes the player, finds out the players name and provides the player with basic instructions
        Args:
            None
        Returns:
            name: This is the players name. Example, if the player answered "Joe" his name would be "Joe."
    """          
    print("Welcome to my Quiz!")
    name=input("\nWhat is your name?")
    print("\nWelcome "+name+"!")
    print("\nThis is a quiz on python terms! You will be able to determine your own difficulty. There will be four blanks to fill in for each difficulty level . Good luck!")
    return name

def difficulty():
    """ This function enables the player to set their own difficulty, either Easy, Medium or Hard.
        Args:
            None
        Returns:
            difficulty_level: This is the difficulty level. There are three options, Easy, Medium and Hard. If the player answers "Easy", then the level is "Easy."
    """ 
    while True:
        difficulty_level = input("\nWhat difficulty level would you like? Easy, Medium or Hard?")
        if difficulty_level == "Easy" or difficulty_level == "Medium" or difficulty_level == "Hard":
            print("\nYou choose the "+difficulty_level+" difficulty level!")
            return difficulty_level
        else:
            print("\nChoose a valid difficulty level...")


def wrong_choices():
    """ This function enables the player to set how many wrong answers that they are able to have. It also checks to see if the user entered a valid integer.
        Args:
            None
        Returns:
            num_wrong_choices: This is an integer of how many wrong answers that a player selected. If a player select 4, then it would be 4.
    """
    while True:
        try:
            num_wrong_choices = int(input("\nHow many errors would you like to make? Please enter a valid number:"))
            return num_wrong_choices
        except:
            print("\nThat is not a valid number. Try again...")

def blank_convert(blank):
    """ This function converts the blank response in the play_game() function that the player provided for which blank they wanted to answer and it adds applicable underscores.
        Args:
            blank: This is the response the player provided. It will be an integer from 1 to 4.
        Returns:
            blank: This returns the cleaned up version of the response so that it can find the matching response in the answers. If the player input 1. It would output "___1___."
            if the user does not answer with an integer 1-4, then the response will be wrong so we do not add underscores for anything greater than 4.
    """
    if blank == "1":
        return "___1___"
    elif blank =="2":
        return "___2___"
    elif blank =="3":
        return "___3___"
    elif blank =="4":
        return "___4___"
    else:
        return blank

def answer_check(answers,blank,answer):
    """ This function checks if the users response is correct or not by pairing it up against each item in the answers list for the quiz.
        The blank and the answer are combined into a list to check to see if that combo matches the combos in the answer list.
        Args:
            answers:This is the answers list for the quiz for the difficulty level selected.
            blank: This is the blank the user selected that the user wished to answer for.
            answer: This is the word that the user wished to guess for the blank they selected.
        Returns:
            fill:This is a binary variable that will either be 1 or 0. If it is 1, then the answer provided was correct 
            and the answer should be replaced in the quiz string. If it is wrong, the output is a 0 and the quiz string
            will not be changed. User enters "___1___" and "INTEGER" for the easy quiz. The items are pairs up in a list 
            and matched with the list item ["___1___","INTEGER"] and this would return fill=1.
    """
    check=0
    answer=answer.upper()
    alist=[blank,answer]
    fill=0    
    while True:
        if alist == answers[check]:
            fill=1
            return fill
        else:
            check=check+1
            if check >= len(answers):
                return fill
                
def play_game(player,quiz,remaining,wchoices,answers):
    """ This function is the main game coding. It provides the user the quiz 
        and applicable game parts. If the user fills in the blanks correctly, 
        the user wins, if not the user loses.
        Args:
            player: This is the players name that comes form the welcome() function.
            quiz: This is the quiz that user selected.
            wchoices: This is the number of wrong choices the user selected.
            answers: This is the answers for the the quiz level selected.
            remaning: This is the number of blanks remaining to be answered in the question.
        Returns:
            It only returns if the player won or lost.
    """
    while remaining !=0:
        blank = input("\nWhich blank will you guess for? Input a number.")
        blank = blank_convert(blank)
        answer = input("\nWhat is your guess?")
        replace=answer_check(answers,blank,answer)
        if replace == 1:
            quiz=quiz.replace(blank,answer)
            print(quiz)
            remaining = remaining-1
        else:
            wchoices=wchoices-1
            print("\n",player," you have", wchoices, "incorrect choices left.")
            if wchoices == 0:
                break
    if wchoices == 0:
        print("\nYou lose! Try again!")
    else:
        print("\nCongrats, you won!")

# This is the coding for the game.

player=welcome()
dlevel=difficulty()
wchoices=wrong_choices()
remaining=4

if dlevel=="Easy":
    quiz=equiz
    answers=eanswers
    print(quiz)
    play_game(player,quiz,remaining,wchoices,answers)
elif dlevel=="Medium":
    quiz=mquiz
    answers=manswers
    print(quiz)
    play_game(player,quiz,remaining,wchoices,answers)
elif dlevel=="Hard":
    quiz=mquiz
    answers=manswers
    print(quiz)
    play_game(player,quiz,remaining,wchoices,answers)

input("\nThanks for playing the game. Press ENTER to leave.")
