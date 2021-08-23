# relative primes
# any two successive integers are co-primes
def coprimes(l,r):
    if (r-l+1) % 2 !=0:
        return 0
    i = l
    j = l+1
    while j <= r:
        print(i,j)
        i += 2
        j += 2
    
coprimes(1,8)
