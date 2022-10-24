# This is a smart calculator
def smart_calculator():
    print('Welcome to smart calculator interface')
    decision = eval(input('To go ahead press 1 or any other number to quit'))
    if decision == 1:
        number_1 = eval(input('Enter the first number'))
        number_2 = eval(input('Enter the second number'))
    else:
        print('Thanks for using smart calculator')
smart_calculator()