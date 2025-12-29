# Using a while loop to keep code executing as long as a Boolean expression remains tru
"""
# Variables
x=input("Enter a number to count to: ")
x=int(x)
y=1

while y<=x:
    print(y)
    y=y+1
"""

#  use a Boolean check and break to stop the loop when the check evaluates as false
"""
# Variables
x=input("Enter a number to count to: ")
x=int(x)
y=1

while True:
    print(y)
    y=y+1
    if y>x:
        break
"""

# embed the program in a while loop that checks if the user enters a quit command, such as q or quit

while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
