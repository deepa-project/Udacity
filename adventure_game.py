

import time
import random


def rockpaperscissors():
    me = 0
    you = 0
    turns = 10
    call = ["rock", "paper", "scissors"]
    while turns > 0:
        print("You have", turns, "turns left")
        print("Enter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input()
        if choice == "1":
            choice = "rock"
        elif choice == "2":
            choice = "paper"
        elif choice == "3":
            choice = "scissors"
        else:
            print("Invalid input")
            continue
        print("You chose", choice)
        print("Computer chose", call[random.randint(0, 2)])
        if choice == call[random.randint(0, 2)]:
            print("It's a tie")
        elif choice == "rock" and call[random.randint(0, 2)] == "scissors":
            print("You win")
            me += 1
        elif choice == "rock" and call[random.randint(0, 2)] == "paper":
            print("You lose")
            you += 1
        elif choice == "paper" and call[random.randint(0, 2)] == "rock":
            print("You win")
            me += 1
        elif choice == "paper" and call[random.randint(0, 2)] == "scissors":
            print("You lose")
            you += 1
        elif choice == "scissors" and call[random.randint(0, 2)] == "paper":
            print("You win")
            me += 1
        elif choice == "scissors" and call[random.randint(0, 2)] == "rock":
            print("You lose")
            you += 1
        turns -= 1
    if me > you:
        print("You won the game")
        you += 1
    elif me < you:
        print("You lost the game")
        me += 1
    else:
        print("It's a tie")
    print("You won", me, "times")
    print("You lost", you, "times")
    print("The game is over")


def guess():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")
    print("Try to guess it!")
    print("You have 5 tries")
    tries = 5
    while tries > 0:
        guess = int(input())
        if guess == number:
            print("You guessed it!")
            break
        elif guess > number:
            print("Too high")
        else:
            print("Too low")
        tries -= 1
    if tries == 0:
        print("You lost")
    print("The number was", number)

    return 0


def roll_the_dice():
    tries = 6
    number = 0
    while tries > 0:
        roll = random.randint(1, 6)
        number += roll
        tries -= 1
        print("You rolled a", roll)
    print("Your score: ", number)
    return 0


def evaluate_input(num: int):
    if num == 1 or num == 2 or num == 3:
        return(num)
    else:
        print("Press\n 1 for Higher\n 2 for Lower\n 3 for Correct\n")
        n = int(input())
        n1 = evaluate_input(n)


def myguess():
    print("You think of a number between 1 and 100!")
    print("I will try to guess it in 10 tries!")
    tries = 10
    myguess = 50
    high = 100
    low = 0
    while tries > 0:
        print("The number is in between "+str(high)+" and "+str(low))
        print("My guess is :", myguess)
        tries -= 1
        print("Press\n 1 for Higher\n 2 for Lower\n 3 for Correct\n")
        h_l_c = int(input())
        h_l_c = evaluate_input(h_l_c)
        if h_l_c == 1:

            guess_add = (high-myguess)//2
            if low < myguess:
                low = myguess
            myguess += guess_add

        if h_l_c == 2:
            guess_sub = (myguess-low)//2
            if high > myguess:
                high = myguess
            myguess -= guess_sub
        if h_l_c == 3:
            print("Yay! Thank you for playing this game with me!")
            print("I am only a computer and guess work is not my talent!")
            return(0)
            break
    print("Guess I csn go wrong sometimes too!")
    print("I am a PC but am made by a human and\n"
          " this is my human side of my creators!")
    print("If I dont score, you dont score!!!")
    print("Thanks for playing this game with me today!")
    print("Good day!")
    return(0)


def name():
    name = ""
    name = input("What is your name?\n")
    return(name)


def print_pause(s: str):
    print(s)
    time.sleep(2)


def story():
    print_pause("Hi there!!!")

    print_pause("Hi "+str(name())+",\n")
    print_pause("This is the story!")
    s = "You are going on a morning walk!\n"
    s += "You stepped on a transparent magic stone!\n"
    s += "Suddenly,you see a MOUNTAIN in front of you!\n"
    s += "An OCEAN behind you!\n"
    print_pause(s)
    s = ""
    s += "A SKY above you!\n"
    s += "A GOLD MINE below you!\n"
    s += "You can see the staircase under the trapdoor like mine to get the key!\n"
    print_pause(s)

    s += "You need to climb down the staircase of the mine to get the key \n that will change everything back to normal."
    print_pause(s)
    s = ""
    s += "And bring you back to the normal world near your home!\n"

    s += "You need to be a part of this adventure!!!"

    play_game_again()

    return(0)


def yesOrNo(s: str):

    if s == 'y':
        play_game_again()
    elif s == 'n':
        print_pause("Thank you for playing the adventure game today!")
    else:
        print_pause("Invalid input!")
        print_pause("Do you want to play the game again?(y/n)")
        s = str(input())
        yesOrNo(s)


def mountains():
    print("The climb is high, tiring and exhaustin!!! Be prepared for the challenging task ahead")
    rockpaperscissors()


def oceans():
    print("Swim in me, my darling! My strenth is all yours!! But not my wisdom!!!")
    guess()


def skies():
    print("Your faith is your wings and your self confidence, your winds!")
    roll_the_dice()


def mines():
    print("Dig no further!There is no treasure here! I am not your nose!")
    myguess()


def play_game_again():
    s = ""
    s += "You can visit 1.Mountain\n 2.Ocean\n 3.Sky\n 4.Mine\n....to get the points."
    s += "Press 1 , 2 , 3 or 4: \n Your choice: \n"
    print_pause(s)
    n = int(input())
    eval_choice(n)


def guessit():
    print("")


def main():
    story()


if __name__ == "__main__":
    main()
