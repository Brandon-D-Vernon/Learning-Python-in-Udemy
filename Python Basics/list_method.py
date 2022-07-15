#list method
# A list(li) method is own by a action

basket = [1,2,3,4,5]

# Adding
basket.append(100)
new_list = (basket)
print(basket)
print(new_list)

# Insert
new_list = (basket.insert(5, 100)) #insert by adding 100
print(basket)
print(new_list)

# Extend
new_list = basket.extend([100]) #extend by adding 100
print(basket)
print(new_list)

# Removing
basket.pop() #remove the last number 
basket.pop(0) #remove the first index
# new_list = basket.pop(4)
new_list = basket.remove(4) #give it the value you want to remove
new_list = basket.clear() # remove everything
print(basket)



#*****************************************

# List Method
# https://www.w3schools.com/python/python_ref_list.asp

# Method      Description
# append()	  Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	  Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	  Adds an element at the specified position
# pop()	      Removes the element at the specified position
# remove()	  Removes the first item with the specified value
# reverse()	  Reverses the order of the list
# sort()	    Sorts the list