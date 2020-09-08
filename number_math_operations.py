"""
this is a multi line comment
as below
"""
a = 20
b = 238.34
c = a + b  # sum
d = a * b  # multiplication
e = b / a  # division
print('c=', c)
print('d=', d)
print('e=', e)

"""
double asterisk is used to calculate the power/exponent of a number
"""
exp = 12 ** 10
print('12 ** 10=', exp)

"""
Modulus / remainder operation
"""
f, g = 100, 3
remainder = f % g  # % is used to calculate the modulus / remainder
print('100 % 3 =', remainder)

"""
arithmetic order of precedence
"""
# * and / have higher precedence than + and -
# () has higher precedence than * and /
h = 1 + 2 - 3 * 4 / 5
print("1 + 2 - 3 * 4 / 5 =", h)
# therefore the order is as follows
print("\n\n The explanation of order of precedence steps are as shown below")
h_explanation = 4 / 5
print("Division")
print(h_explanation)
h_explanation *= 3
print("Multiplication")
print(h_explanation)
h_explanation_n = 1 + 2
print("Addition")
print(h_explanation_n)
h_explanation = h_explanation_n - h_explanation
print("Subtraction")
print(h_explanation)
