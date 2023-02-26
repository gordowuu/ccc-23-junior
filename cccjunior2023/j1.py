P = int(input())
C = int(input())
points = 0
points += 50 * P
points -= 10 * C
if P > C:
    points += 500
print(points)