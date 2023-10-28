# Write a program to find biggest of give 3 numbers from the Command Prompt
n1 = int(input('Enter First Number: '))
n2 = int(input('Enter Second Number: '))
n3 = int(input('Enter Third Number: '))
if n1>n2 and n1>n3:
    print('Biggest number is {}'.format(n1))
elif n2>n3 and n2>n1:
    print('Biggest number is {}'.format(n2))
else:
    print('Biggest number is {}'.format(n3))