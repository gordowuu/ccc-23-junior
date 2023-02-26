n = int(input())
row1 = list(input().split())
row2 = list(input().split())
i = 0
tape = 0
count = 0

while i != n:
    if row1[i] == "1":
        count += 1
        i += 1
    elif row1[i] == "0":
        if count > 0:
            tape += 3 + (count-1)
        count = 0
        i += 1
if count > 0:
    tape += 3 + (count-1)
print(tape)
