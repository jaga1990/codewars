def two_sum(numbers, target):
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if target == numbers[i] + numbers[j]: return (i,j)

two_sum([1234,5678,9012], 14690)