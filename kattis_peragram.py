#peragrams
#https://open.kattis.com/problems/peragrams

input_data = input()
characters = []

for i in input_data:
    if i in characters:
        characters.remove(i)
    else:
        characters.append(i)
        #characters.append(input_data[0])
        #input_data = input_data[1:]
result = max(len(characters)-1,0)
print(result)

#github answer 
from collections import Counter
print(Counter(input()).values())
print(max(sum(x % 2 for x in Counter(input()).values()) - 1, 0))


#chatgpt answer 
from collections import Counter

input_data = input()
character_counts = Counter(input_data)

odd_count = sum(count % 2 == 1 for count in character_counts.values())
min_chars_to_remove = max(0, odd_count - 1)

print(min_chars_to_remove)
