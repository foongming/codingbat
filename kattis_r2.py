input_data = input()
space_at = input_data.find(' ')
#print(space_at)
#print(input_data[0:space_at])
r1 = int(input_data[0:space_at])
#print(r1)
s = int(input_data[space_at:])
#print(s)
r2 = s*2 - r1
print(r2)