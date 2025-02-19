import random


def gen_ran_number(n):
    return random.randint(1, n)


def gus_num():
    print("-----------GAME STARTED------------\n")
    ans = gen_ran_number(100)
    print(ans)  # ans

    option = []
    for i in range(1, 6):
        option.append(gen_ran_number(100))
    option.append(ans)
    option = set(option)

    for i in option:
        print(f"Option {i}")

    print()
    print("You have 3 chance to win the game")
    print("===================================\n")
    print(f"Chance Left {3}")
    for i in range(1, 4):
        choice = int(input("Enter any option: "))
        if choice == ans:
            print(f"Chance Left: {3-i}")
            print("You Won the Game")
            break
        else:
            print(f"Chance Left: {3-i}")
            print("Try once again!!")

        if i == 3:
            print(f"Chance Left: {3-i}")
            print(f"You Loss the Game \nCorrect guess is {ans}")

    print("------------------Game End---------------\n\n")


# 1. Rock
# 2. Paper
# 3. Scissor
# 1 or 2 = 2
# 1 or 3 = 1
# 2 or 3 = 3
def rock_paper_scissor():
    print("-----------GAME STARTED------------\n")
    computer = gen_ran_number(3)
    print("Computer Choice ", computer)
    print("1. Rock \n2. Paper\n3.Scissor\n")
    choice = int(input("Enter Your Choice: "))
    match (choice):
        case 1:
            if computer==1:
                print("Game Draw\nBoth Selected Rock\n")
            if computer==2:
                print("You Loss The Game\nComputer Selected Paper and You Selected Rock\n")
            if computer==3:
                print("You Won The Game\nComputer Selected Scissor and You Selected Rock\n")
            
        case 2:
            if computer==1:
                print("You Won The Game\nComputer Selected Rock and You Selected Paper\n")
            if computer==2:
                print("Game Draw\nBoth Selected Paper\n")
            if computer==3:
                print("Computer Won The Game\nComputer Selected Scissor and You Selected Paper\n")
            
        case 3:
            if computer==1:
                print("Computer Won The Game\nComputer Selected Rock and You Selected Scissor\n")
            if computer==2:
                print("You Won The Game\nComputer Selected Paper and You Selected Scissor\n")
            if computer==3:
                print("Game Draw\nBoth Selected Paper\n")
            
        case default:
            print(f"Option {choice} is not found")
    print("------------------Game End---------------\n\n")


while True:
    print("\n1. Guess the Number Game \n2. Rock Paper Scissor\n9. Exit\n")

    choice = int(input("Choice any Option: "))
    exit = 0
    match (choice):
        case 1:
            print("\nGuess the Number Game")
            gus_num()
            continue

        case 2:
            print("\nRock Paper Scissor")
            rock_paper_scissor()
            continue

        case 9:
            print("\nExit")
            break

        case default:
            print(f"Option {choice} is not found")
