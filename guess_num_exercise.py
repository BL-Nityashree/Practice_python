num = 18
count = 0
while (True):
    guessnum= int(input("Guess a number : "))
    count += 1

    if guessnum > num and count<=9:
        print("You have guessed a greater num. ")
        if count<9:
            print("You are left with",9-count,"guess")
        elif count==9:
            print("Game Over!!!!!!!")
            break
        continue
    elif guessnum < num and count<=9:
        print("You have guessed a lesser num. ")
        if count<9:
            print("You are left with", 9 - count, "guess")
        elif count==9:
            print("Game Over!!!!!!!")
            break
        continue
    elif guessnum == num and count<=9:
        print("Congrats! You have guessed correct num.\n""You took ",count, "attempts to guess" )
        break
    # elif count==9:
    #     print("Game Over!!!!!!!")
    #     break