'''Write a Python program to create a lambda function that adds 25 to
a given number passed in as an argument.
sample input: 10
sample output: 35'''


n=int(input('enter number to add with 25: '))
print((lambda x:x+25)(n))
