# Write a program to find smallest of given 3 number
n1 = int(input('Enter the 1st Number: '))
n2 = int(input('Enter the 2nd Number: '))
n3 = int(input('Enter the 3rd Number: '))
if n1 <= n2 and n1 <= n3:
    print('The {} is smallest'.format(n1))
elif n2 <= n3 and n2 <= n1:
    print('The {} is smallest'.format(n2))
else:
    print('The {} is smallest'.format(n3))
