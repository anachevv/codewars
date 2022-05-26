user_input = input()
total_sum = 0
word_length = len(user_input)

for x in range(word_length):
    if user_input[x] == "a" or user_input[x] == "A":
        total_sum += 1
    if user_input[x] == "e" or user_input[x] == "E":
        total_sum += 1
    if user_input[x] == "i" or user_input[x] == "I":
        total_sum += 1
    if user_input[x] == "o" or user_input[x] == "O":
        total_sum += 1
    if user_input[x] == "u" or user_input[x] == "U":
        total_sum += 1

print(f"Vowels in '{user_input}': {total_sum}")
