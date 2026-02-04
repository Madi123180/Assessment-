"""Task 5
Question 1
NameAge = {"Name1": {"Name": "Malathi", "Age": 31},
           "Name2": {"Name": "Pranav", "Age": 5},
           "Name3": {"Name": "Madhu", "Age": 37},
           "Name4": {"Name": "Yazhini", "Age": 13}}  #Nested Dictionary
AgeBelow18=filter(lambda age: (NameAge[age]["Age"]) < 18, NameAge)
print(list(AgeBelow18)) #Validating Age using Lambda and Filter, Filter is used to here to return the Name list
AgeAbove18=list(map(lambda age: (NameAge[age]["Age"]) > 18, NameAge))
print((AgeAbove18))

Question 2:
from functools import reduce
numbers = [5,10,5,20,5,30,5]
total = reduce(lambda a, b: a + b, numbers) #adding all the numbers and finding total
print(total)

Question 3:
numbers = [2,3,4,5,6,7,8,9,10]
findeven = filter(lambda num: num % 2 ==0, numbers) #finding even numbers
evennumbers = map (lambda num: num * num, findeven) #using map here to square each number from the even number list
print(list(evennumbers))

Question 4:
user=input(str("Enter text" + "\n")) # defining function and passing parameter x
Validation = lambda value: value.isdigit(), user
print(Validation(user))

# I am trying to execute this code by getting text from User but it is not working, and i am not able understand the mistake.

Question 5:
from datetime import datetime
YMD = lambda: datetime.now()
print(YMD())

Question 6:
def fibonacci(n):
    a, b = 5, 10
    fib = lambda c, d : (d, c + d)
    for _ in range(n):
        print(a, "")
        a, b = fib(a, b)
fibonacci(10)

#With the help of AI I have learnt this code and written.
"""
