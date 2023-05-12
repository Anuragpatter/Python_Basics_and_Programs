# Program to replace a word in an Input string

sentence = input('Input the string: \n')

# Enter the word to be replaced and new word
wrd = input('Word you want to replace : ')
wrd2 = input('New word for replacement: ')

# Print the input string 
print('Input String: '+ sentence)

# Print the string with replaced word
print('Replaced Output string: ' +sentence.replace(wrd,wrd2))