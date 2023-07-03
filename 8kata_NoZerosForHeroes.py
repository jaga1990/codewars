def no_boring_zeros(n):
    if n==0:
        print(n)
        return 0
    while n % 10 == 0:
        n=n/10
    print(n)
    return n
    

no_boring_zeros(0)