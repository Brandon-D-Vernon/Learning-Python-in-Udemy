#list slicing
# creating a new copy of a list

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]

# Unlike strings(str), list(li) is mutable
amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[0:3]
new_cart = amazon_cart[:]
new_cart[0] = 'gum'


print(new_cart)
print(amazon_cart)