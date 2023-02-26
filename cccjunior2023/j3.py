
n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))

day = []


for j in range(len(grid[i])):
    sum = 0
    for h in range(n):
        if grid[h][j] == "Y":
            sum += 1
        elif grid[h][j] == ".":
            sum += 0
    day.append(sum)
max = max(day)
top = []
for i in range(len(day)):
    if day[i] == max:
        top.append(i+1)
if len(top) > 1:
    for i in range(len(top)):
        if top[i] == top[-1]:
            print(top[i])
        else:
            print(top[i],end=",")
else:
    print(top[0])

