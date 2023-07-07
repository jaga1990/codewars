def sum_mul(n, m):
    sum_partial = 0;
    sum = 0;
    if (n == 0 and m != 0) or (n!=0 and m==0) or (n<0 and m>0) or (n>0 and m<0):
        print('Invalid')
        return 'INVALID'
    elif n == m or n>m:
        print(0)
        return 0
    while sum_partial + n < m:
        sum_partial = sum_partial + n
        sum = sum + sum_partial
        print(sum_partial)
    print(sum)
    return sum
sum_mul(0,0)