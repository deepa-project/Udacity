import time
import random

def print_pause(s:str):
    print(s)
    time.sleep(2)
def yesOrNo():
    print_pause("Press y for yes and n for no")
    if s=='y':
        return(1)
    elif s=='n':
        return(0)
    else:
        print_pause("Invalid input!")
        print_pause("Press only y or n!")
        s=input("Enter your choice:")
        yesOrNo(s)
def story():
    s="You are going on a morning walk!\n"
    s+="You stepped on a magic stone!\n"
    s+="Suddenly,you see a mountain in front of you!\n"
    s+="An ocean behind you!\n"
    print_pause(s)
    s=""
    s+="A sky above you!\n"
    s+="A mine below you!\n"
    s+="The magic stone is transparent!\n"
    s+="You need to climb down the staircase of the mine to get the key \n that will change everything back to normal."
    print_pause(s)
    s=""
    s+="And bring you back to the normal world near your home!\n"
    s+="You need to find the key to get back to the normal world!"
    s+="What do you want to do?"
    print_pause(s)
    s=""
    choice(s)

def mountains(key:int):
    print_pause("Welcome to my humble abode!")
    evaluate_key(key)
        

    return(key)


def oceans(key:int):
    return(key)

def skies(key:int):
    return(key)

def mines(key:int):
    return(key)       
  


def key():
    if key==1:
        print_pause("Congratulations!You found the key!")
    elif key==0:
        key=0
    return(key)

def guessit():
    x=[]
    x=range(1,10)
    y=random.choice(x)

    my_number=y
    print("Guess the number between 1 and 10")
    guess=int(input("Enter your guess:"))
    if guess==y:
        print("Congratulations!You guessed the number!")
        key=1
        oceans(key)
    else:
        print("Sorry!You did not guess the number!")
        print("The number was "+str(y))
        print("Do you want to quit?")
        s=yesOrNo()
        if s==1:
            main()
        if s==0:
            print_pause("Thank you for playing this game!")
            exit()    



def evaluate_key(key:int,a=""):
    if key==1:
        print_pause("You found the key!")
        print_pause("Please continue yout journey!")
        if a=="mountains":
            oceans(key)
        elif a=="oceans":
            mines(key)
        elif a=="mines":
            skies(key)
    
            
                           
    elif key==0:
        print_pause("You did not find the key!")
        print_pause("Do you want to quit?")
        s=yesOrNo()
        if s==1:
            choice('1')
        if s==0:
            print_pause("Thank you for playing this game!")
            exit()

    
        return(0) 
def oceans(key:int):
    return(0)

def mines(key:int):
    return(0)

def skies(key:int):
    return(0)
    
                            


def choice(s:chr):
    if s=="":
        pass
    
    print("1.Mountains ")
    print("2.Oceans ")
    print("3.Skies ")
    print("4. Mines")
    print("Make a choice")
    if s=='1':
      key=mountains(key)
    elif s=='2':
      key=oceans(key)
    elif s=='3':
        key=skies(key)
    elif s=='4':
        key=mines(key)
    else:
        print("Invalid input!")
        print("Press only 1, 2, 3 or 4!")
        s=input("Enter your choice:")
        choice(s)

         




    
def main():
    print("Welcome to Adventure Island!")
    story()
    key=key()


if __name__=="__main__":
    main()        