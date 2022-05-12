import time
import random

points=0


def print_pause(s:str):
    print(s)
    time.sleep(2)

def story():
    print_pause("This is the story!")
    s="You are going on a morning walk!\n"
    s+="You stepped on a magic stone!\n"
    s+="Suddenly,you see a MOUNTAIN in front of you!\n"
    s+="An OCEAN behind you!\n"
    print_pause(s)
    s=""
    s+="A SKY above you!\n"
    s+="A GOLD MINE below you!\n"
    s+="The magic stone is transparent!\n"
    s+="You need to climb down the staircase of the mine to get the key \n that will change everything back to normal."
    print_pause(s)
    s=""
    s+="And bring you back to the normal world near your home!\n"
    s+="You need to find the key to get back to the normal world!"
    s+="What do you want to do?"
    print_pause(s)
    return(0)

def choice(i:int):
    return(i)

def points(num:int):
    points+=num
    return(points)

def rules():
    
    s="First attempt:15 points\n"
    s+="Second attempt:10 points\n"
    s+="Third attempt:05 points"
    print_pause(s)    

def guessit():
    print("")


def main():
    story()
    #rules()

if __name__=="__main__":
    main()            



    