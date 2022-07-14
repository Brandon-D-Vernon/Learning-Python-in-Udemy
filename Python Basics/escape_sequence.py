#escape sequence

# weather = 'It's sunny' - error because of single quote in it's
# weather = "It's sunny" - to change that you add double quote
# weather = "It's "kind of" sunny" - won't work because you cant have double quotes inside a double quote, unless.

#Escape Sequence
weather1 = "It\'s \"kind of\" sunny" # You can fix the double qoutes within a double quotes by adding back slash \
# Back slash \ lets the computer knows, whatever comes after a back slah \ is a string (str) 

print(weather1)

#*****************************************

# Back slash with T - /t means add tab.
weather2 = "\t It\'s \"kind of\" sunny"

print(weather2)

#*****************************************

# Back slash with N - /n means new line.
weather3 = "\t It\'s \"kind of\" sunny \n hope you have a good!"

print(weather3)