import random

gameplay_options = ["bat","bowl"]
Player_won_toss = False

def PlayGame(Player_won_toss):
    Player_batting = False
    player_score = 0
    computer_score= 0
    player_finished = False
    computer_finished = False

    if Player_won_toss:
        Player_choose = input("Enter your choice(Bat/Bowl): ").lower()
        while True:
            if Player_choose == "bat":
                Player_batting = True
                break
            elif Player_choose == "bowl":
                Player_batting = False
                break
            else:
                print("enter a valid option.")
    else:
        Computer_choose = random.choice(gameplay_options)
        print(f"Computer chose to {Computer_choose}.")
        Player_batting = (Computer_choose == "bowl")
            
    while True:
        if Player_batting and not player_finished:
            while True:
                try:
                    Player_move = int(input("Enter your move(1-6): "))
                    if 1 <= Player_move <= 6:
                        break
                    else:
                        print("Please enter a number between 1 and 6.")
                except ValueError:
                    print("Please enter a valid number")

            Computer_move = random.randint(1,6)
            print(f"Computer : {Computer_move}")

            if Player_move == Computer_move:
                Player_batting = False
                player_finished = True
                print("You are out")
                print(f"Your final score is {player_score}")
                print("---------------------------------")
            else:
                player_score += Player_move
                print(f"Your score: {player_score}")

                if computer_finished and player_score > computer_score:
                    print("You achieved the target! You win!")
                    return

        elif player_finished and computer_finished:
            print("Match over")
            if player_score > computer_score:
                print(f"Player won the game") 
            elif player_score < computer_score:
                print("Computer Won the game")
            else:
                print("Game Draw")
            break
        else:
            # Computer batting 
            while True:
                try:
                    Player_move = int(input("Enter your move(1-6): "))
                    if 1 <= Player_move <= 6:
                        break
                    else:
                        print("Please enter a number between 1 and 6.")
                except ValueError:
                    print("Please enter a valid number")

            Computer_move = random.randint(1,6)
            print(f"Computer : {Computer_move}")


            if Player_move == Computer_move:
                Player_batting = True
                computer_finished = True
                print(f"Computer is out, score is {computer_score}")
                print("---------------------------------")
            else :
                computer_score+= Computer_move
                print(f"Computer score: {computer_score}")
                if player_finished and computer_score> player_score:
                    print("Computer achieved the target! Computer wins!")
                    return
                
                    

while True:
    Player_option = input("Enter odd/even (q to quit): ").lower()

    if Player_option == "q":
        print("Bye")
        break
    elif Player_option == "odd" or Player_option == "even":
    
        while True:
            try:
                Player_num = int(input("Enter a number(1-6): "))
                if 1 <= Player_num <= 6:
                    break
                else:
                    print("Please Enter a number between 1 and 6.")
            except ValueError:
                print("Enter a valid number.")
        Computer_num = random.randint(1,6)

        is_even = (Player_num + Computer_num) % 2
        if (Player_option == "even" and is_even == 0) or (Player_option == "odd" and is_even != 0):
            Player_won_toss = True
            print("You Won the toss")
        else:
            Player_won_toss = False
            print("Computer Won the toss")
        PlayGame(Player_won_toss)
    else:
        print("Choose a valid option.")