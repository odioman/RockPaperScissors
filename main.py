from random import randint

player = input('rock(r), paper (p) or scissor (s)?')

print(player, 'vs', end='')

chosen = randint(1, 3)
#print(chosen)

if chosen == 1:
    computer = 'r'
    print('O')

elif chosen == 2:
    computer = 'p'
    print('___')
else:
    computer = 's'
    print('>8')

print(computer)
