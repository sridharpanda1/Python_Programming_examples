# Write a program to check whether the given Number is in between 1 and 100
n1 = int(input('Enter the number: '))
if n1 >= 1 and n1 <= 100:
    print('The number {} is in between 1 to 100'.format(n1))
else:
    print('The number {} is not in between 1 to 100'.format(n1))
