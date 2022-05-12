import time
import random


def mountain():
    print_pause("You are in the Mountains!")


def ocean():
    print_pause("You are in the Oceans!")


def sky():
    print_pause("You are in the Sky!")


def mine():
    print_pause("You are in the Mine!")


def print_pause(s: str, secs: int = 1):
    print(s)
    time.sleep(secs)


def string_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            print("Option selected: " + option)
            return option
        print(f'Option {option} is invalid. Try again!')


def play_again():
    while True:
        print_pause("Do you want to play the game again?(y/n)")
        s = str(input())
        options = ['y', 'n']
        choice = string_input(s, options)
        if choice == 'y':
            print_pause("You chose to play the game again!")
            main()

        elif choice == 'n':
            print_pause("Thank you for playing the adventure game today!")
            break
            return(0)


def story():
    print_pause("Hi there!!!")

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
    print_pause(s)


def numeric_input(prompt, minimum, maximum):
    while True:
        try:
            option = (input(prompt)).lower()
            if option.isnumeric():
                option = int(option)

                if option >= minimum and option <= maximum:
                    return option
                else:
                    print_pause(
                        f'Option must be between {minimum} and {maximum}! Try again!')
                    print_pause(
                        "Please enter your choice: 1 for Mountain, 2 for Ocean, 3 for Sky, 4 for Mine")
                    s = str(input())
                    numeric_input(s, 1, 4)

        except ValueError:
            print(f'{n} is not a valid input. Try again!')


def adventure_game_choice():
    s = ""
    s += "You can visit 1.Mountain\n 2.Ocean\n 3.Sky\n 4.Mine\n."
    s += "Press 1 , 2 , 3 or 4: \n Your choice: \n"
    print_pause(s)
    n = int(input())
    adventure_choice = numeric_input(n, 1, 4)
    if adventure_choice == 1:
        print_pause("You chose the Mountains!")
        mountain()

        play_again()
    elif adventure_choice == 2:
        print_pause("You chose the Oceans!")
        ocean()

        play_again()
    elif adventure_choice == 3:
        print_pause("You chose the Sky!")
        sky()

        play_again()
    elif adventure_choice == 4:
        print_pause("You chose the Mine!")
        mine()

        play_again()
    else:
        print_pause("You chose the wrong option! Try again!")
        adventure_game_choice()


def main():

    print_pause("********************************")
    print_pause("Welcome to the Adventure Game")
    print_pause("********************************")
    story()
    adventure_game_choice()

    play_again()


if __name__ == "__main__":
    main()
