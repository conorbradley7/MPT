n = int(input())
p = int(input())
d = list(input().split())
c = int(input())
e = list(input().split())

leaderboard = []
for i in e:
    score = 0
    for x in d:
        if i >= x:
            score += 1
    leaderboard.append(score)

leaderboard.sort()

x = (len(leaderboard)-int(n))
leaderboard.pop(x)

for i in leaderboard:
    if i == i + 1:
        print('no')
        break

    else:
        print('yes')
        break

