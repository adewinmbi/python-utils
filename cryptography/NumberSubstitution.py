# The list of numbers never exceeds 26, meaning each number could correlate to a letter
numbers = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

result = ""
for n in numbers:
    if type(n) is int:
        result += chr(n + 64) # Add 64 to turn the normal numbers into utf-8 / ascii
    else:
        result += n

print(result)