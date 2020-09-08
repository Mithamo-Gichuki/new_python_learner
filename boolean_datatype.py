"""
boolean datatype that has only two values
True which is 1
False which is 0
"""
a = True
b = False
print(a)
print(b)
print("\n\n")
print("The bool value of zero is ", bool(0))  # as shown in execution the value displayed is false
print("The bool value of one is ", bool(1))  # as shown in execution the value is true
print("\n\n")

"""
Therefore this can be used to test the value in a string variable
e.g if a string variable is empty or not
"""
c = ""
d = "Name"
print(bool(c), ",thus empty string")  # This shows false since the string is empty
print(bool(d), ",thus string not empty")  # This shows the string is not empty
print("\n\n")

"""
This then can be used to detect the value of user input
"""

name = input("Enter your name: ")
bool_name = bool(name)
if bool_name == False:
    print("You have not entered anything")
else:
    print("Your name is ", name)
