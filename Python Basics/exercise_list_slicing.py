#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

#My Answer
new_list = ['a', 'b', 'c']
print(new_list[1])
# Answer: b
print(new_list[-2])
# Answer: b
print(new_list[1:3])
# Answer: b, c
new_list[0] = 'z'
# Answer: z, b, c
print(new_list)
# Answer: a, b, c {Correct Answer: z, b, c}

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
# Answer: 1,2,3 {Correct Answer: z, 2, 3}
print(bonus)
# Answer: 11 {Correct Answer: 1, 2, 3, 5}