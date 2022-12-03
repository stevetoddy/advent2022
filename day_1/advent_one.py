temp_var = 0
li = []

f = open("data.txt")
lines = f.readlines()
for line in lines:
    if line.rstrip():
        temp_var = int(line.rstrip()) + temp_var  
    else:
        li.append(temp_var)
        temp_var = 0

# Biggest temp_var
print(max(li))

li.sort()
total = sum(li[-3:])

# # Top three biggest elves combined
print(total)
