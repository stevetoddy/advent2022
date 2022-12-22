# Read data from txt file 
f = open("data.txt")
data = f.read()

# Variable and list
signal = []
count = 1
track = 0

# TASK ONE
# for letter in data:
#     if len(signal) == 3:
#         signal.append(letter)
#         if letter == signal[0] or letter == signal[1] or letter == signal[2] or signal[0] == signal[1] or signal[0] == signal[2] or signal[1] == signal[2]:
#             del signal[0]
#             count += 1
#         else:
#             print((count + 4))
#             break
#     else:
#         signal.append(letter)

# TASK TWO
for letter in data:
    track += 1
    if len(signal) == 13:
        signal.append(letter)
        set_signal = set(signal)
        if len(set_signal) == len(signal):
            print(f"Answer: {track}")
        else:
            del signal[0]
    else:
        signal.append(letter)




