"""
How strings work in python
contain a-z 0-9
In single and double quotes
"""

a = 'This is a single quote string'
b = "This is a double quote string"

print(a)
print(b)

c = "This is a 'single quote' inside a double quotes string"
d = 'This is a "double quote" inside a single quote string'
e = "Another way to handle \"quotes\""  # \ before " is used to treat the " as part of the string
f = "If a string too long to be written in a single line of code \
it can shown as now"  # Here \ is used to ignore the new line and treats the two lines as one continuous string
print(c)
print(d)
print(e)
print(f)

"""
String methods
"""
# printing first character of a string
name = "Emmanuel"
print(name[0])
str_ind = len(name)
pos = 0
print("Name =", name)
while pos != str_ind:
    print("Index", pos, "=", name[pos], "\t", end="")
    pos += 1

# A variable can be assigned part of another variable
full_name = "Emmanuel Mithamo"
pos_1 = 0
str_ind_1 = len(full_name)
print("\n\n", str_ind_1)
first_name = ""
last_name = ""
while full_name[pos_1] != " ":
    first_name = full_name[0:pos_1+1]
    pos_1 += 1
print(first_name)
if full_name[pos_1] == " ":
    pos_1 += 1
print(pos_1)
count = 0
while pos_1 <= str_ind_1:
    last_name = full_name[pos_1 - count:pos_1]
    pos_1 += 1
    count += 1
print(last_name)
print(pos_1)
print(last_name[0])

"""
Methods include:
len()           This gives the length of a string
lower()         This changes a string to small letters
upper()         This changes a string to capital letters
str()           This changes other datatype to string.
"""
print("\n")
name = first_name + last_name
print(name)
print(name.lower())
print(name.upper())
print(name + str(22))   # Here + is used in concatenation( combining a \
# variable to another plus there is datatype change to string
print("Hello "+"world")

"""
replace() - method to replace string item e.g..
"""
g = "abc89abc02abc123abc36"
print(g.replace("abc", "ABC"))      # replaced all lower case with upper case
print(g.replace("abc", "ABC", 1))   # count of 1 replaces only one instance of abc to ABC
print(g.replace('abc', 'ABC', 2))   # count of 2 replaces only two instances of abc to ABC

"""
Substrings
"""
h = "Town"
sub_h = h[0]
print(sub_h)    # Therefore sub_h is a substring of h string variable
sub_g = g[0:5]  # Here string characters taken are of index 1-4 thus value after colon is excluded
print(sub_g)
sub_g_2 = g[0:5:1]  # Here 1 is the default step from one index to another thus no difference
sub_g_3 = g[0:5:2]  # Here 1 index is skipped since its 2 steps e.g 0,1,2. 0 to 2 = 2 steps
print(sub_g_2)
print(sub_g_3)

"""
Slicing and indexing
"""
i = "This is a string"
print(i[:])     # Without values it prints the whole string
print(i[1:])    # With a value before : it prints string from that index value eg 1
print(i[-1])    # -ve value counts index from the end/last letter eg g is last letter
print(i[-2])    # This is second last letter
print(i[:-1])   # Prints all string except last letter
print(i[:len(i)])   # This prints whole string if length is unknown since last index is less than length
print(i[::2])   # Prints string with a step of 2
print(i[::-1])  # This prints the reverse of the string
# Therefore the slicing is done on runtime and does not change variable value

"""
String formatting
"""
city = "Nairobi"
event = "show"
# Two ways to print / format
# 1st format
print("Welcome to", city, ",enjoy the", event)
# 2nd format
print("Welcome to %s,enjoy the %s"%(city,event))    # %s defines string variable
print("Welcome to %s"%(city))
age = 25
name_1 = "Emmanuel"
print("Your name is %s and your age is %i"%(name_1,age))
