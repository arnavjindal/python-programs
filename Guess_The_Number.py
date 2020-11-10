guess_count= 0
n = 50
guess_left = 9
while guess_count < 9:
    inpu =int(input("enter your number: "))
    guess_count += 1
    guess_left -= 1
    if inpu == n:
        print("congo ,you gueesed it right, in " ,guess_count, "chances" )
        break
    elif guess_left == 0 :
        print("sorry bruh you lost the game, Ans is",n )
        print("indeed, game is over! \nthanks for playing")
    elif inpu >n:
        print("enter smaller number ")
        print("guesses left: " , guess_left)
    elif inpu<n:
        print("enter greater number")
        print("guesses left: " , guess_left)

