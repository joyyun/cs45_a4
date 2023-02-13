#!/usr/bin/env python3

import string
import random

def play_rps():
    # 0 = rock, 1 = paper, 2 = scissors
    selections = ["rock", "paper", "scissors"]
    cont = True
    while cont:
        cont = False
        print("3! 2! 1! Go!")
        user_selection = input("Please enter your selection:")
        # user = list.index(user_selection)
        comp = random.choice([0,1,2])
        comp_selection = selections[comp]

        # decide winner
        if user_selection == comp_selection:
            print("It's a tie -- play again!")
            cont = True
        elif user_selection == "rock":
            if comp_selection == "paper":
                print("I chose paper -- you lose!")
            else:
                print("I chose scissors -- you win!")
        elif user_selection == "paper":
            if comp_selection == "scissors":
                print("I chose scissors -- you lose!")
            else:
                print("I chose rock -- you win!")
        elif user_selection == "scissors":
            if comp_selection == "rock":
                print("I chose rock -- you lose!")
            else:
                print("I chose paper -- you win!")

    
    return


def main():
    print("Welcome! Time to play rock, paper scissors!")
    print("For anyone new to rock, paper, scissors, here are the rules:")
    print("Two players secretly pick one of “rock,” “paper,” or “scissors. Both players reveal their selection to the other player at once; the winner is chosen based on what the selections are.")
    print("Rock beats scissors (by crushing them); scissors beats paper (by cutting it); and paper beats rock (by covering it). If both players select the same one, it is a tie.")
    print()
    print("Time to play! On the count of 3, enter your selection.")
    play_rps()
    print()
    print("That was fun, thanks for playing :)")

if __name__ == '__main__':
    main()
