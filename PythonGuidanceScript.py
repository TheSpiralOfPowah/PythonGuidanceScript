# hello everyone.
# I'm spirabot.
# Today we'll learn the basics of python.

# First, type "import time"
import time
# This is a module. You can use modules for greater flexibility in python.
# For instance, look at the code below.
time.sleep(5.0)
# That is a module command. When you import a module, you are reccomended to put it at the top of your script rather than somewhere else.
# Now for the base commands.
print("Hello, world!")
# They are like module commands, but you do not need to import a random module to use them.
# Now for for loops.

for i in 10:
    print("This is a for loop!")
# That is a for loop. They are good for repeating things.
if 1 == 1:
    print("1 is 1!")
# This is an if statement. It fires if something is true. Like if a variable is a specific number. (Also works with greater and less than)
# The thing below is a variable
health = 100
# You can add, subtract, or set variables to different values.
health = health-10
health = health+10
health = 0
# Very useful for if statements.
if health == 0:
    print("Game over!")
# This detects if the health is 0, and then prints "Game over!"
# Now for "else" statements.
if health > 0:
    print("I'm alive!")
else:
    print("I am dead!")
# Else statements can let you provide a response even if a boolean is invalid.
# Now to take user input
print(input("Put a thing"))
# That is an input statement. It gets the input of the user.
# You can use it for a simple chat game.
print(input("You: "))
print("\n David: Hello, Can you tell me your name?")
name = input("You: ")
print("David: Well, {name}, I think you're pretty cool.")
# It allows the user to control.
# Now for lists.

hello_list = [1, 2, 3]

# Lists can allow you to access multiple things.
print(hello_list[3])

# You can add and remove things from lists.
hello_list.append(4)
hello_list.remove(4)

# Tuples are like lists' edgy mean cousins. They can't add or remove.
hello_tuple.append(4) # Does nothing

hello_tuple = tuple(1, 2, 3)

# You can access objects in tuples just like lists though.
print(hello_tuple[1])

# That's basically everything you need to know about python to get started with self-learning.