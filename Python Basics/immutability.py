#immutability

# string can be access quite easily. 
# The ideal Start, Stop, and Stepover is called Slicing (or Strength Slicing)
# selfish[start:stop:stepover]

# Example
# selfish = '01234567' - 01234567 index order
# selfish[0] = '8' - You can't reassign a part of a string once created. The only way to change it, is to created something new.


#*****************************************


# Example1
selfish1 = '01234567' 
           #01234567

selfish1 = selfish1 + '8'

print(selfish1)

