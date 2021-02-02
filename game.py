win=50
guess=1
number=int(input("enter number between 1 to 100 "))
game_over=False


while not game_over:
    if number==win:
        print(f"you win, and in try of {guess} times")
        game_over= True

    else:
        if number>win:
            print("too high")
            guess += 1
            number=int(input("....guess again"))

        else:
            print("too low")
            guess += 1
            number=int(input(".....guess again"))


