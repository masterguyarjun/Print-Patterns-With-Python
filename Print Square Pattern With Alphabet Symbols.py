
# To Print Square Pattern With Alphabet Symbols

n = int(input('Enter number of rows: '))

for i in range (n):
    print((chr(65 + i) + ' ')*n)
