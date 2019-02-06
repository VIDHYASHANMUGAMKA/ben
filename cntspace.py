input_string = input()

splitter = input_string.split()

final = []

for i in range(0,len(splitter)):
    for j in range(0,len(splitter[i])):
        if(j==0):
            final.append(splitter[i][j].upper())
        else:
            final.append(splitter[i][j])
    # Assumed that there is one space btw each words
    final.append(' ')
print(''.join(final)) 
