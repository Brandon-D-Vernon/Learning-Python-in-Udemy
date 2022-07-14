#excercise: type conversion

name = 'Brandon Vernon'
age = 40
relationship_status = 'single'

relationship_status = 'it\'s complicated'

print(relationship_status)

# having fun
print(f"{name} age {age} is in {relationship_status}")

#*****************************************

birth_year = input('What year was you born')
# print(type(birth_year))
age = 2022 - int(birth_year)

print(f'your age is: {age}')