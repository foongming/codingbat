#A Different Problem
#https://open.kattis.com/problems/different
#difficulty = 2.6

while True:
    try:
        a, b = map(int, input().split())
        print(abs(a - b))
    except EOFError:
        break


#chatgpt explanation 

'''
The while True: loop is used to continuously read and process input lines until an EOFError occurs, which happens when there is no more input to read.

Inside the loop, you use try and except EOFError: to catch the end of the input. When there's no more input to read, the EOFError exception is raised, and the loop is terminated using the break statement.
'''