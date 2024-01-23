#input_data = input().splitlines()
#input_data = kattis_quadrant_selection_input.txt.read()

#input_data = sys.stdin.read(kattis_quadrant_selection_input.txt).splitlines()
#x = int(input_data[0])
#y = int(input_data[-1:(find.('/n'))+1])
#a = input_data.find('/n')
#print(a)
#print(input_data[-1:a])

myfile = open('kattis_quadrant_selection_input.txt')     # Mac and Linux
mytxt = myfile.read()
myfile.close()
lines = mytxt.splitlines()

#lines = input().splitlines()

x = int(lines[0])
y = int(lines[1])

if x < 0:
    if y < 0:
        print(3)
        exit()
    else:
        print(2)
        exit() 
if y > 0:
    print(1)
else:
    print(4)

#chatgpt answer 

x, y = map(int, input().split())

if x < 0:
    if y < 0:
        print(3)
    else:
        print(2)
else:
    if y > 0:
        print(1)
    else:
        print(4)

x = int(first_input())
y = int(second_input)


myfile = open('kattis_quadrant_selection_input.txt')     # Mac and Linux
mytxt = myfile.read()
myfile.close()

#print(mytxt.find('\n'))
#x = int(mytxt[:mytxt.find('\n')])
print(mytxt[:mytxt.find('\n')])
print(mytxt[mytxt.find('\n')+1:])

input_data = input()
x = input_data[:input_data.find('\n')]
y = input_data[input_data.find('\n')+1:]

if x < 0:
    if y < 0:
        print(3)
        exit()
    else:
        print(2)
        exit() 
if y > 0:
    print(1)
else:
    print(4)

#solution

x = int(input())
y = int(input())

if x < 0:
    if y < 0:
        print(3)
        exit()
    else:
        print(2)
        exit() 
if y > 0:
    print(1)
else:
    print(4)

#alt solution 

x = int(input())
y = int(input())

if x <0 and y <0:
    print(3)
elif x<0 and y>0:
    print(2)
elif x>0 and y >0:
    print(1)
else:
    print(4)