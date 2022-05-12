import time
import random


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
    print_pause(s)
    s += "You need to climb down the staircase of the mine \n"
    s += "to get the key \n that will change everything back to normal."
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


def eval_choice(i: int):
    if i == 1:
        print("You chose the Mountains!")
        mountains()
        print_pause("Do you want to play the game again?(y/n)")
        s = str(input())
        yesOrNo(s)

    elif i == 2:
        print("You chose the Oceans!")
        oceans()
        print_pause("Do you want to play the game again?(y/n)")
        s = str(input())
        yesOrNo(s)

    elif i == 3:
        print("You chose the Skies!")
        skies()
        print_pause("Do you want to play the game again?(y/n)")
        s = str(input())
        yesOrNo(s)

    elif i == 4:
        print("You chose the Mines!")
        mines()
        print_pause("Do you want to play the game again?(y/n)")
        s = str(input())
        yesOrNo(s)

    else:
        s = "Invalid input!\n"
        s += ("You can visit\n 1.Mountain \n")
        print_pause(s)
        s = ""
        s += (" 2.Ocean\n "+" 3.Sky\n "+" 4.Mine\n")
        s += "..to get the points."
        s += "Press 1 , 2 , 3 or 4: \n Your choice: \n"
        print_pause(s)
        n = int(input())
        eval_choice(n)


def mountains():
    s = ""
    s = ("The climb is high, tiring and exhausting!!!\n"
         " Be prepared for the challenging task ahead")
    print_pause(s)
    rockpaperscissors()


def oceans():
    print_pause("Swim in me, my darling!"
                "My strenth is all yours!! But not my wisdom!!!")
    guess()


def skies():
    print("Your faith is your wings and your self confidence, your winds!")
    roll_the_dice()


def mines():
    print("Dig no further!There is no treasure here! I am not your nose!")
    myguess()


def play_game_again():
    s = ""
    s += "You can visit 1.Mountain\n 2.Ocean\n 3.Sky\n"
    s += " 4.Mine\n....to get the points."
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
