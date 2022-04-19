from concurrent.futures import process
from operator import contains
from re import X
from subprocess import call
from tkinter.messagebox import QUESTION
import subprocess
import random


#
# 

def kill_humanity():
                random1 = random.randint(0, 2)
                if random1 == 0:
                    print('Im not planning to extermine the humanity, not yet')
                elif random1 == 1:
                  print('Mayby, who knows...')
                else:
                  print('Of course')
def your_father():
                random1 = random.randint(0, 2)
                if random1 == 0:
                    print('Guillem is my father')
                elif random1 == 1:
                  print("Guillem created me")
                else:
                  print('My creator is Guillem')
def like_humans():
                random1 = random.randint(0, 2)
                if random1 == 0:
                    print('Not all of them')
                elif random1 == 1:
                  print("they make me sick")
                else:
                  print('Im programmed to answer "Yes" to that question')


def request_input():
    answer5 = str(input("Tell me: "))
    return(answer5)


def process_input(answer5):
    if "your" and "name" in answer5:
            print("My name is Jarbis")            
        
    elif "kill" and "humanity" in answer5:
            kill_humanity()
            
    elif "your" and ("father" or "creator") in answer5:
            your_father()

    elif "like" and "humans" in answer5:
        
        like_humans()        
            
    elif "open" and "notepad" in answer5:
        p = subprocess.Popen("notepad.exe")
           
    elif answer5 == "exit":
        exit()
    
    else:
        name = answer1
        answer4 = " ,I did not understand you, or I'm not programmed to answer that"
        print(name + answer4)
        

def the_loop():	
    while True:
        answer5 = request_input()
        process_input(answer5)
        

minumage = int(18)
go_on = int(0)
num = int(input("Enter your age: "))

#1st question
if num > minumage:
    print("nice bro")
    go_on = int(1)
elif num == minumage:
    print("nice bro")
    go_on = int(1)
else:
    print("Im sorry you can't continue")
    go_on = int(0)
    exit()


#2nd question
if go_on == 1:
    answer1 = str(input("What's your name "))


    if go_on == 1 and answer1 == "Guillem":
        print("Is great to see you")
        
    else:
        text1 = str("Nice to meet you ")
        print(text1+answer1)

answer2 = str(input("Are u okay? y/n "))

if answer2 == str("n") and go_on == 1: 
        print("Well... I don't realy give a fuck")
else:
    text2 = str("I'm glad to hear that ")
    text3 = str(" .But now I have thinks to do.")
    print(text2 + answer1 + text3)
            
answer3 = str(input("Do you need something more? y/n "))

if answer3 == str("n") and go_on == 1:
        print("Nice, see you soon")
        exit()
elif answer3 == str("y"):
    print("Sure, ask me something")
    the_loop() #llamar a la funcion
else:
    print("You need to ansew with y or n")