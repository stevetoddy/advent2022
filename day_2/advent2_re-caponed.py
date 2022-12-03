table = {
    "AX": 4, "AY": 8, "AZ": 3,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 7, "CY": 2, "CZ": 6
}


table_2 = {
    "AX": 3, "AY": 4, "AZ": 8,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 2, "CY": 6, "CZ": 7
}


score = 0
score_2 = 0


f = open("data.txt")
for line in f:
    p = line.split()
    t = p[0] + p[1]
    score += table[t]
print(f"First score = {score}")
    
    
f = open("data.txt")
for line in f:
    p = line.split()
    t = p[0] + p[1]
    score_2 += table_2[t]
print(f"Second score = {score_2}")



#FIRST DAY
# A + X = 4
# A + Y = 8
# A + Z = 3

# B + X = 1
# B + Y = 5
# B + Z = 9

# C + X = 7
# C + Y = 2
# C + Z = 6


# SECOND
# A + X = 0 3
# A + Y = 3 1
# A + Z = 6 2

# B + X = 0 1
# B + Y = 3 2
# B + Z = 6 3

# C + X = 0 2
# C + Y = 3 3
# C + Z = 6 1

# ROCK = A (1) X
# PAPER = B (2) Y
# SCISSORS = C (3) Z

# WIN = 6 Z
# DRAW = 3 Y
# LOSE = 0 X