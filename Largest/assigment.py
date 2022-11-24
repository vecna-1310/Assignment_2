#Program to find smallest and largest number in the list
list = [1,67,89,69,3,5]
print(list)
print("The largest number in the list is:",max(list))
print("The minimum list in the list is:",min(list))


#Deleting alternate numbers from the list

list = [1,67,89,69,3]
list.pop(1)
list.pop(3)
print(list)

#Deleting odd elements and printing even elements
list = [1,67,89,68,3]
print("The number of elements in list" + str(list))
res = []
for val in list:
    if not (val% 2!=0):
        res.append(val)
print("List after removal of odd values:" + str(res))
