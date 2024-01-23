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