with open('../input/25.txt') as f:
    lines = f.readlines()

snafu_digits = {'0' : 0, '1' : 1, '2' : 2, '=' : -2 , '-' : -1}
reverse_snafu = {0 : '0',1 : '1',2 : '2', -1 : '-', -2 : '='}
decimal_sum = 0
for line in lines:
    places = len(line.strip())
    for i in range(places):
        decimal_sum += (5 ** (places - i - 1) * snafu_digits[line[i]])

snafu_sum = ''
while decimal_sum >= 2:
    factor = round(decimal_sum/ 5)
    remainder = decimal_sum % 5
    decimal_sum = factor
    if remainder < 3:
        snafu_sum = reverse_snafu[remainder] + snafu_sum
    else:
        snafu_sum = reverse_snafu[remainder - 5] + snafu_sum

print("Part 1 : ",snafu_sum)