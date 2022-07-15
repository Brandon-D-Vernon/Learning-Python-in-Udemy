# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

# My Answer
# The original equation was missing brackets. So I had to correct that in order to run the program properly.
# I got the right answer, but there was a better way

# basket = [
#   ["Banana"], 
#   ["Apples"], 
#   ["Oranges"], 
#   ["Blueberries"]
# ];
# print(basket[2])

#Correct answer
print(basket[1][1][0])