#a = lambda b: b + 15
#b = lambda x,y: x*y
#print(a(7))
#print(b(3,4))

#Multiply number
#def func_compute(n):
#    return lambda x : x * n
#result = func_compute(2)
#print(result)
#print("Double the number of 15 =", result(15))

#Sort tuples
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#subject_marks.sort(key=lambda a: a[1])
#print(subject_marks)


#models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
#models.sort(key=lambda a: a['make'])
#print(models)

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print("Original list of integers:")
#print(nums)
#print("\nEven numbers from the said list:")
#even = list(filter(lambda a: a%2==0, nums)
#print(even)

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#result = list(map(lambda a: a**2, nums))
#print(result)

#result = lambda a, n: a.startswith(n) == True
#print(result('Aga', 'p'))

#result = lambda a: a.isnumeric()
#print(result("2"))

from functools import reduce

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
result = reduce(lambda a, b: a + b,list(filter(lambda a: a<0, nums)))
print(abs(result))