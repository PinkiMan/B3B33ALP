import sys

FileName = sys.argv[1]
# FileName='slovnik.txt'

Postfix = sys.argv[2]
# Postfix='ER'

File = open(FileName, 'r')

count = 0
shortest_word = None
for line in File:
    line = line.replace('\n', '')
    # xd=line.endswith(Postfix)
    if line.endswith(Postfix):
        count += 1
        if shortest_word == None:
            shortest_word = line
        elif len(line) < len(shortest_word):
            shortest_word = line

print(count)
print(shortest_word)