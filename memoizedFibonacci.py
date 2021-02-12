calculated_fibonacci = {0:0, 1:1}
def fibonacci(n):
    if n in calculated_fibonacci:      
        return(calculated_fibonacci[n])
    else:
        new_finbonacci_result = fibonacci(n - 1) + fibonacci(n - 2)
        calculated_fibonacci[n] = new_finbonacci_result
        return(new_finbonacci_result)

fibonacci(70)