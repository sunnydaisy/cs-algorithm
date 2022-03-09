point = input()
row = int(point[1])
col = 0

if point[1] == 'a':
    col = 1
elif point[1] == 'b':
    col = 2
elif point[1] == 'c':
    col = 3
elif point[1] == 'd':
    col = 4
elif point[1] == 'e':
    col = 5
elif point[1] == 'f':
    col = 6
elif point[1] == 'g':
    col = 7
elif point[1] == 'h':
    col = 8

count = 0
if row - 2 > 0 and col - 1 > 0:
    count += 1
if row - 1 > 0 and col - 2 > 0:
    count += 1
if row - 2 > 0 and col + 1 > 0:
    count += 1
if row - 1 > 0 and col + 2 > 0:
    count += 1
if row + 2 > 0 and col - 1 > 0:
    count += 1
if row + 1 > 0 and col - 2 > 0:
    count += 1
if row + 2 > 0 and col + 1 > 0:
    count += 1
if row + 1 > 0 and col + 2 > 0:
    count += 1
print(count)