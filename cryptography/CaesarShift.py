# Brute force...
# Print every possible caesar shift of a given string

string = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

for i in range(0, 26): # 26 letters in alphabet
    dec = "" # Decoded string
    for char in string: # Iterate through characters
        if ord(char) >= ord('a') and ord(char) <= ord('z'): # If the current character is lower case
            dec += chr((((ord(char) - ord('a')) + i) % 26) + ord('a')) # Modulo used to wrap around to the beginning
        elif ord(char) >= ord('A') and ord(char) <= ord('Z'): # If the character is capitalized
            dec += chr(((ord(char) - ord('A') + 1) % 26) + ord('A'))
        else:
            dec += char # If the character is not a letter
    print(dec)