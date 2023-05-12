# Program to compare two strings and give the number of replaced alphabets as the output

count = 0       # Initialize a counter with value zero
# Enter Strings 
sequence_1 = 'ThisIsAStringOfCode'      # String 1
sequence_2 = 'HereIsAStringInCode'      # String 2

# For loop to check and compare each alphabet with same postion one at a time in both strings 
for i in range(0,len(sequence_1)):

    if sequence_1[i] != sequence_2[i]:
        count = count + 1
# Print Statement: The value of counter
print(count)