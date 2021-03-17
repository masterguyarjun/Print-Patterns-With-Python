# # To Print Inverted Pyramid Pattern With * Symbols
n = int (input ('Enter number of rows: '))

for i in range(n):
    print(' ' * i + '* ' * (n-i))
