# Task 4:
# Question1:
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
evenlist = [i for i in numbers if i % 2 == 0]
oddlist = [i for i in numbers if i % 2 != 0]
print(evenlist)
print(oddlist)

Question2:
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
Value = [n for n in numbers if all(n % i != 0 for i in range(2, n))]
print(Value)

Question3:
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

for i in numbers:
    NewNum = i
    for _ in range(50):  # checking for sum of squared digits value for 50 times
        NewValue = 0
        for digit in str(NewNum):  # converting integer into string value so that each digit can be taken
            NewValue += int(digit) ** 2  # stroing the squared value in new variable
        NewNum = NewValue
        if NewNum == 1:
            break
    if NewNum == 1:
        print(f"{i} is happy number")

Question4:
Value = input("please enter the number" + "\n")
Sumvalue = int(Value[0]) + int(Value[-1])
print(Sumvalue)

Question5:
x = [1, 2, 5, 10]
MV = [(a, b) for a in x for b in x if a * b == 10]
for a, b in MV:
    print(f"{a}, {b}")

Question6:

Cars = ["Ford", "TATA", "Mahindra", "Hyundai", "KIA", "BMW"]
Courses = ['MBA', 'B.Sc', "Hyundai", "ME", "BMW", "B.com"]
Mobiles = ["Motorola", 'Hyundai', 'iphone', 'Nokia', "B.com", "KIA"]
DuplicateValue = []
for a in Cars:
    if a in Courses or a in Mobiles:
        DuplicateValue.append(a)
for b in Courses:
    if b in Mobiles or b in Cars:
        if b in DuplicateValue:
            continue
        DuplicateValue.append(b)
print(DuplicateValue)

Question7:
from collections import Counter

numbers = [2, 4, 37, 49, 532, 95, 5, 10, 20, 2, 49, 10, 532, 95, 37]
nv = Counter(numbers)
for x in numbers:
    if nv[x] == 1:
        print(x)
        break

Question8:
numbers = [4, 37, 49, 532, 95, 5, 10, 20, 2]
numbers.sort()
MinimumNum = numbers[0]
MaximumNum = numbers[-1]
print(f"Minimum number is {MinimumNum}")
print(f"Maximum number is {MaximumNum}")

question9:
from itertools import combinations

Numbers = [10, 20, 30, 9]
RequiredNumber = 59
for i in combinations(Numbers, 3):
    if sum(i) == RequiredNumber:
        print(f"Triplet numbers are {i}")

Question10:

from itertools import combinations

Numbers = [4, 2, -3, 1, 6]
RequiredNumber = 3
NewValue = 0
for i in combinations(Numbers, 2):
    if sum(i) == RequiredNumber:
        NewValue = sum(i) + Numbers[2]
        if NewValue == 0:
            sublist = list(i)
            print(f"Sublist is {sublist}")




