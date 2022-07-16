#dictionary method 2

user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}


#.keys - show the keys variable in the dictionary
print('hello' in user.keys())

# .items grabs all the Items.
print(user.items())

# .clear - cleans the dictionary to make it empty
print(user.clear())

# .copy allows to copy a user
user2 = user.copy()
print(user.clear()) #clear the first user
print(user2) #first user info was save with a .copy

# .pop off the value
print(user.pop('age'))
print(user)

# .popitem randomly pop off the keys
print(user.popitem())
print(user)

#  .update a key item
print(user.update({'age': 55}))
print(user)