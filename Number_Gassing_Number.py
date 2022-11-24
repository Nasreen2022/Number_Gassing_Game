winning_number=21
guess=1
number = int(input("Guess the number between 1 to 100 : "))
game_over = False
while not game_over:
    if number==winning_number:
        print("you win!!!!!!!!!!!!  \U0001F973 \U0001F973")
        # print("\U0001F973 \t \U0001F973")
        print(f"And you guessed the number {guess} times")
        game_over=True
    elif number>winning_number:
        print("Too High ")
        guess+=1
        number=int(input("Again enter the number : "))
    elif number<winning_number:
        print("Very Low")
        guess+=1
        number=int(input("Again enter the number : "))
    else:
        print("Number is invalid..........")
