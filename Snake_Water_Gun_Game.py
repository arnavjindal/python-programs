import random




no_of_games_completed = 0
winn =0

while no_of_games_completed <10:
    no_of_games_completed+=1

    Comp_option=['Snake','Water' ,'Gun']
    Comp_Choose= random.choice(Comp_option)
    person_guess = input('enter s,w,g as per your choice :\n')
    person_guess = person_guess.lower()

    if person_guess == 's' and Comp_Choose == 'Water'   or  person_guess == 'w' and Comp_Choose == 'Gun' or  person_guess == 'g' and Comp_Choose == 'Snake' :
        print('You won From', Comp_Choose+"!!" )
        winn+=1
    else:
        print('you lost from ', Comp_Choose + "!!")

print("Game Over")




winnn= winn
lost= str(10-winn)
winn = str(winn)
if winnn >5:
    print(f'In General, you  Won by {winn}:{lost}' )
elif winn ==5 :
    print(f'In General, The match is draw by {winn}:{lost}')
else:
    print(f'In General, you Lost by  {winn}:{lost}')


"""TODO
code accepts invalid characters.
use numbers instead of s,w,g.
print score with each turn.

upload on github!. 

"""
