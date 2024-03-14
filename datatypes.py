# Creation of array
array1 = [1, 2, 3, "thimphu", 2.3]
print (array1)

#retrieving
element1 = array1[0]
element2 = array1[4]
print(element2)
lastElement = array1[-1]
print(lastElement)

print(array1)
# modyfying elements
array1[0] = 10
print(array1)

# getting number of elemnts in an array
no_of_elements = len(array1)
print(no_of_elements)

#slicing
elements = array1[0:3]
print(elements)

#concatenate lists
arr1 = [1,10]
arr2 = ['thimphu', 'wangdue']
print(arr1 + arr2)

number_to_check = 1
result = number_to_check in arr1
print(result)

#add element
arrvariable = [1,3,2]
arrvariable.append(4) #[1,3,2,4]
#insert at a specific index
arrvariable.insert(1,10) #[1,10,3,2]
arrvariable.sort
print(arrvariable)

stackvar = []
# adding to stack
stackvar.append(4)
stackvar.append(2)
stackvar.append(9)
stackvar.append(1)

print('Ater appending', stackvar)
stackvar.pop()
print('after poping', stackvar)