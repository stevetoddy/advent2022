li = []
total = 0

f = open("data2.txt")
lines = f.readlines()
for line in lines:
    new_data = line.rstrip()
    for letter in new_data:
        if len(li) < 3:
            li.append(letter)
            if len(li) == 3:
                if li[0] == 'A' and li[2] == 'X':
                    total = total + 4
                    li = []
                    continue
                if li[0] == 'A' and li[2] == 'Y':
                    total = total + 8
                    li = []                       
                    continue
                if li[0] == 'A' and li[2] == 'Z':
                    total = total + 3
                    li = []        
                    continue
                if li[0] == 'B' and li[2] == 'X':
                    total = total + 1
                    li = []
                    continue
                if li[0] == 'B' and li[2] == 'Y':
                    total = total + 5
                    li = []
                    continue
                if li[0] == 'B' and li[2] == 'Z':
                    total = total + 9
                    li = []
                    continue
                if li[0] == 'C' and li[2] == 'X':
                    total = total + 7
                    li = []
                    continue
                if li[0] == 'C' and li[2] == 'Y':
                    total = total + 2
                    li = []
                    continue
                if li[0] == 'C' and li[2] == 'Z':
                    total = total + 6
                    li = []
print(f"First total = {total}")

# total = 0

# f = open("data.txt")
# lines = f.readlines()
# for line in lines:
#     new_data = line.rstrip()
#     # print(new_data)
#     for letter in new_data:
#         if len(li) < 3:
#             li.append(letter)
#             if len(li) == 3:
#                 if li[0] == 'A' and li[2] == 'X':
#                     total = total + 3
#                     li = []
#                     continue
#                 if li[0] == 'A' and li[2] == 'Y':
#                     total = total + 4
#                     li = []                       
#                     continue
#                 if li[0] == 'A' and li[2] == 'Z':
#                     total = total + 8
#                     li = []        
#                     continue
#                 if li[0] == 'B' and li[2] == 'X':
#                     total = total + 1
#                     li = []
#                     continue
#                 if li[0] == 'B' and li[2] == 'Y':
#                     total = total + 5
#                     li = []
#                     continue
#                 if li[0] == 'B' and li[2] == 'Z':
#                     total = total + 9
#                     li = []
#                     continue
#                 if li[0] == 'C' and li[2] == 'X':
#                     total = total + 2
#                     li = []
#                     continue
#                 if li[0] == 'C' and li[2] == 'Y':
#                     total = total + 6
#                     li = []
#                     continue
#                 if li[0] == 'C' and li[2] == 'Z':
#                     total = total + 7
#                     li = []

# print(f"Second total = {total}")


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

