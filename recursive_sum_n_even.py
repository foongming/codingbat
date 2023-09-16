"""Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)"""
def sum_series(n):
    if n == 0:
        return 0 
    else: 
        return sum_series(n-2) + n

print(sum_series(6)) #12
print(sum_series(10)) #30