#Pizza Crust
#https://open.kattis.com/problems/pizza2

#from math import pi
#pizza_area = pi*r**2
#crust_area = pi*(r-c)**2
#result = 100*(crust_area/pizza_area)

input_data = input()
r = int(input_data[:input_data.find(' ')])
c = int(input_data[input_data.find(' ')+1:])

result = 100*((r-c)/r)**2
formatted = "{:.6f}".format(result)
print(formatted)
