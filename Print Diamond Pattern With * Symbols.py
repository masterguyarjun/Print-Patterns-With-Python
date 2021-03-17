#  To Print Diamond Pattern With * Symbols

n = int (input ('Enter number of rows: '))

for i in range(n):
    print(' ' * (n - i - 1)+'* ' *(i + 1))
for i in range(n):
    print(' ' * i + '* ' * (n-i))