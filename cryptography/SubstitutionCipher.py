text = "A JBSJKZKBKZYY"

# Find out what the most common letters are, substitute them for common letters in english

count = {} # Empty dictionary

for char in text:
    if char in count: # If the character is already in count
        count[char] += 1
    else:
        count[char] = 1

for i in count:
    print (i, count[i])

decrypt = {
    'J' : 'S',
    'Z' : 'I',
    'B' : 'U',
    'S' : 'B',
    'K' : 'T',
    'Y' : 'N',
}

newStr = ""

# Fill new string with substituted characters
for char in text:
    if char in decrypt:
        newStr += decrypt[char]
    else:
        newStr += char

print(newStr)