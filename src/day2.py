with open('../input/day2.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    plays = line.split(" ")
    player_1 = ord(plays[0].strip())-64
    player_2 = ord(plays[1].strip())-87
    if player_1 == player_2:
        score += 3 + player_2
    elif player_2 > player_1:
        if player_2 == 3 and player_1 == 1:
            score += player_2
        else:
            score += 6 + player_2
    else:
        if player_1 == 3 and player_2 == 1:
            score += 6 + player_2
        else:
            score += player_2

print(score)
            
