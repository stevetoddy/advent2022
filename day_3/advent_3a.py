import string 

holder = []
combined = []
letter_value = {}
value = 1
score = 0

# Assigning values to letters
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

for x in lowercase:
    letter_value.update({x:value})
    value += 1
for x in uppercase:
    letter_value.update({x:value})
    value += 1

count = 0
# Group lines into 3s
data = open('data.txt')
for line in data:
    if len(holder) < 3:
        holder.append(line.rstrip())

    # Compare between lines once 3 lines in holder list then clear holder
    if len(holder) == 3:
        for item in holder[0]:
            if item in holder[1] and item in holder[2]:
                combined.append(item)
                break
        holder = []


#Cross reference combined list against letter values and add together
for y in combined:
    score += letter_value[y]
 
print(f"Total value of combined items = {score}")

