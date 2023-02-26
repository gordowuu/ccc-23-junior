n = int(input())
row1 = list(input().split())
row2 = list(input().split())
x = 0
y = 0
tape1 = 0
count = 0

while x != n:
    if row1[x] == "1":
        count += 1
        x += 1
    elif row1[x] == "0":
        if count > 0:
            tape1 += 3 + (count-1)
        count = 0
        x += 1
if count > 0:
    tape1 += 3 + (count-1)
y = 0
tape2 = 0
count = 0
while y != n:
    if row2[y] == "1":
        count += 1
        y += 1
    elif row2[y] == "0":
        if count > 0:
            tape2 += 3 + (count-1)
        count = 0
        y += 1
if count > 0:
    tape2 += 3 + (count-1)

total = tape1 + tape2
lst = []
for i in range(n):
    lst.append(int(row1[i]) + int(row2[i]))
new_lst = []
for i in range(0,n,2):
    new_lst.append(lst[i])
yo = new_lst.count(2)

print(total- 2*yo)
