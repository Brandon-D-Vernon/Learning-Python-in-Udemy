#dictionary (dict)
# Dictionary unordered key value pair

dictionary = {
  # 'a' : 1, #key(string['a']) to grab the value (1)
  # 'b' : 2
  'a' : [1,2,3],
  'b' : 'hello',
  'c' : True
}

my_list = [
  {
  'a' : [1,2,3],
  'b' : 'hello',
  'c' : True
  },
  {
  'a' : [4,5,6],
  'b' : 'hello',
  'c' : True  
  }
]

print(my_list[0]['a'][2])
print(dictionary['a'][1])