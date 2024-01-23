#Where's My Internet??
#https://open.kattis.com/problems/wheresmyinternet 
#difficulty = 2.9 

n,m = map(int, input().split())
values = []
i = 1 
house_numbers = []
while i <=m:
    a, b = map(int, input().split())
    if a < b:
        values.append((a,b))
    else:
        values.append((b,a))
    i+=1 
    if a not in house_numbers:
        house_numbers.append(a)
    if b not in house_numbers:
        house_numbers.append(b)
    
d = {}

print(d)

values.sort()
house_numbers.sort()


if len(house_numbers) != n:
    print("houses checked not equal to number of houses given")
print(values)

