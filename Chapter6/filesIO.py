file = open('casualFile.log', 'a')

print('First line in the file', file=file)
print('This suppose to be a second line', file=file)
print('This is the end, hold your breath and count to ten', file=file)
print('====================================================', file=file)

file.close()

readFile = open('casualFile.log')

for line in readFile:
    print(line, end='')

readFile.close()

open('casualFile.log', 'w').close()
