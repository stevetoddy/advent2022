import string 

compartment_1 = []
compartment_2 = []
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

# Open data and get line length and half length 
data = open('data.txt')
for line in data:
    length = len(line.rstrip())
    half = len(line.rstrip()) / 2
    
    #Compartment 1
    for letter in line[:(int(half))]:
        compartment_1.append(letter)

    #Compartment 2
    for letter in line[(int(half)):(length)]:
        compartment_2.append(letter)

    for item in compartment_1:
        if item in compartment_2:
            combined.append(item)
            compartment_1 = []
            compartment_2 = []
            break

#Cross reference combined list against letter values and add together
for y in combined:
    score += letter_value[y]
 
print(f"Total value of combined items = {score}")

