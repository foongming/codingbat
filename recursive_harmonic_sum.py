#calculate harmonic sum of n-1 

def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return harmonic_sum(n-1) + (1/n)


print(harmonic_sum(2))
print(harmonic_sum(4))
print(harmonic_sum(7))