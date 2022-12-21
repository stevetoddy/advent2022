f = open("data.txt")

l = []
count = 0

for lines in f:
    line = lines.split()
    pairs = line[0].split(",")
    pair1 = pairs[0].split("-")
    pair2 = pairs[1].split("-")
    num1 = [eval(i) for i in pair1]
    num2 = [eval(i) for i in pair2]
    
    # TASK ONE
    if num1[0] == num2[0] and num1[1] == num2[1]:
        count += 1
        continue
    if num2[1] >= num1[1] and num2[0] <= num1[0]:
        count += 1
    if num1[1] >= num2[1] and num1[0] <= num2[0]:
        count += 1
        
    # TASK TWO
    # if num1[0] >= num2[0] and num1[0] <= num2[1]:
    #     count += 1
    #     continue
    # if num2[0] >= num1[0] and num2[0] <= num1[1]:
    #     count += 1

print(count)