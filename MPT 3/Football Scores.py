'''
given number of players on each team
given number of goals in match
given players who scored
return who won
'''

def footballScores():
    A , N , G = map(int, input().split())
    teamA = map(input().split())
    teamB = map(input().split())
    
