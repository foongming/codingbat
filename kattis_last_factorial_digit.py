#Last Factorial Digit
#https://open.kattis.com/problems/lastfactorialdigit 
import math

number_of_lines = int(input())
i = 1
#result = []

while i <= number_of_lines:
    #print(i)
    x = int(input())
    compute = math.factorial(x)
    #print((str(compute))[-1])
    r = (str(compute))[-1]
    #result.append(r)
    print(r)
    #print(input_number)
    i += 1
    