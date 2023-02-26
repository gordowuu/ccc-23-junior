W = str(input())
R = int(input())
C = int(input())
word = list(W)
word2 = list(W)
word2.reverse()
grid = []

count = 0
for i in range(R):
    grid.append(list(input().split()))

for r in range(R):
    for c in range(C):
        combo = []
        if c <= C-len(W):
            for x in range(c,len(W)+c,1):
                combo.append(grid[r][x])
            if combo == word or combo == word2:
                count+=1

for c in range(C):
    for r in range(R):
        combo = []
        if r <= R-len(W):
            for x in range(r,len(W)+r,1):
                combo.append(grid[x][c])
            if combo == word or combo == word2:
                count+=1


print(count)
