with open('../input/day2.txt') as f:
    lines = f.readlines()

score = 0
score_p2 = 0
for line in lines:
    plays = line.split(" ")
    player_1 = ord(plays[0].strip())-64
    player_2 = ord(plays[1].strip())-87
    play_diff = player_2 - player_1
    if play_diff == 0:
        score += 3 + player_2
    elif play_diff == 1 or play_diff == -2:
        score += 6 + player_2
    else:
        score += player_2

    if player_2 == 1:
        score_p2 += (player_1 - 1) if player_1 != 1 else 3
    elif player_2 == 2:
        score_p2 += player_1 + 3
    else:
        score_p2 += (player_1 + 1) if player_1 != 3 else 1
        score_p2 += 6

print("Part 1 : ",score)     
print("Part 2 : ",score_p2)
