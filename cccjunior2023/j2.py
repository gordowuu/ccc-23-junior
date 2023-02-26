shu = 0
dict = {"Poblano":1500, "Mirasol":6000, "Serrano":15500,"Cayenne":40000,"Thai":75000,"Habanero":125000}

n = int(input())
for i in range(n):
    pepper = str(input())
    shu += dict[pepper]

print(shu)