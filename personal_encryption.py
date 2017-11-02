#### PERSONAL NOTES ####
# 1) Create dictionary of alphabet -- DONE
# 2) Create list of the letters in the alphabet to get index for encryption -- DONE
# 3) Create loop to check each letter of the string and add corresponding encrypted digit to output string -- DONE

from numpy import binary_repr

# List is used to check index location of the specified letter
alpha_list = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

# Dictionary used to keep count, which is used in the encryption process
alpha_dict = {
'a': 0,
'b': 0,
'c': 0,
'd': 0,
'e': 0,
'f': 0,
'g': 0,
'h': 0,
'i': 0,
'j': 0,
'k': 0,
'l': 0,
'm': 0,
'n': 0,
'o': 0,
'p': 0,
'q': 0,
'r': 0,
's': 0,
't': 0,
'u': 0,
'v': 0,
'w': 0,
'x': 0,
'y': 0,
'z': 0,
}

# Prompt for user input (make lowercase for ease)
string = str.lower(input("Please enter your string to be encrypted (without spaces): "))

# Empty string to build output
cipher = ''

# Iterate through the string, incrementing the counts for each letter 
# occurred, and adding the count and the letter's index, corresponding 
# to the alphabet, to the output
for char in string:
	alpha_dict[char] += 1
	cipher += str(alpha_dict[char] + alpha_list.index(char))
	
# Convert the cipher into binary, and print	
print(binary_repr(int(cipher)))


