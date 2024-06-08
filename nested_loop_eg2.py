string_list = ["Coder", "Academy", "Champion"]
result = 0

for string in string_list:
    for letter in string:
        if letter in "Cc":
            result += 1

print("Total occurence of c in the list:", result)
