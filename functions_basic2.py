
# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countDown(num):
    num_list = []
    for x in range(num,-1,-1):
        num_list.append(x)
    return num_list

print(countDown(6))
print(countDown(9))
print(countDown(3))


# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def printAndReturn(xyz):
    if len(xyz)==2:
        print(xyz[0])
        return(xyz[1])
    else:
        return("Two numbers, please.")

a=[3,5]
b=[6,9]
c=[1]
d=[3,4,5]

print(printAndReturn(a))
print(printAndReturn(b))
print(printAndReturn(c))
print(printAndReturn(d))


# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firstPlusLength(xyz):
    if type(xyz[0]) == int or type(xyz) == float:
        sum = xyz[0]+len(xyz)
        return sum
    else:
        return "The first list item must be a number."

a=[1,2,3,4]
d=firstPlusLength(a)
print(d)

b=[4,3,2,1]
e=firstPlusLength(b)
print(e)

c=["banana","orange","lemon","apple"]
f=firstPlusLength(c)
print(f)


# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def valuesGreaterThanSecond(xyz):
        new_list=[]
        number_of_values = 0
        for i in xyz:
            if len(xyz)>1:                 #type(xyz[i])==int: or type(xyz[i]) == float:
                if i > xyz[1]:
                    number_of_values=number_of_values+1 #IS THERE A SHORTER WAY?
                    new_list.append(i)
            else:
                return False
        print("Number of values is",number_of_values)
        return new_list

a=[1,2,1,3,1,4,1,5,1,6,]
f=valuesGreaterThanSecond(a)
print(f)

b=[1,4,4,6,4,3,4,8,4,2,4,9]
g=valuesGreaterThanSecond(b)
print(g)

d=[2]
i=valuesGreaterThanSecond(d)
print(i)

#can't get this code to do what I want
c=["banana","orange","lemon","apple"] 
h=valuesGreaterThanSecond(c)
print(h)


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def thisLengthThatValue(xlength,yvalue):
    new_list=[]
    for i in range(xlength):
         new_list.append(yvalue)
    return new_list

a=thisLengthThatValue(3,3)
print(a)

b=thisLengthThatValue(5,5)
print(b)

c=thisLengthThatValue(7,7)
print(c)
