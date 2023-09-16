#Write a Python program to calculate the sum of a list of numbers

def sum_r(ls):
    if not ls:
        return 0
    else: 
        return sum_r(ls[1:]) + ls[0]

print(sum_r([1,2,3]))
print(sum_r([2, 4, 5, 6, 7]))