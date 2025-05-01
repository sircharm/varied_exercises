# Accepted (100) - 0.04 s
#I'm sure there are way better ways of solving this, but I'm tired

def check_victory(chars):
    johan = 0
    abdullah = 0
    
    for char in chars:
        if char == 'X':
            johan += 1
        elif char == 'O':
            abdullah += 1
    
    if johan == 3:
        print("Johan har vunnit")
        return True
    if abdullah == 3:
        print("Abdullah har vunnit")
        return True
    return False
    

game = []
victory = False

for i in range(3):
    game.append(input().replace(' ',''))

for line in game:
    if check_victory(line):
        victory = True

if not victory:
    for i in range(3):
        if check_victory(game[0][i]+game[1][i]+game[2][i]):
            victory = True

if not victory:
    if check_victory(game[0][0]+game[1][1]+game[2][2]):
        victory = True
    if check_victory(game[0][2]+game[1][1]+game[2][0]):
        victory = True
    
if not victory:
    print("ingen har vunnit")
