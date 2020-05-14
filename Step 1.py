# Define how to operate on given inputs.
def operate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == 'x':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    else:
        return 'Invalid operator or operands.'

continueFlag = True
while continueFlag == True:

    # Enter the operator.
    operator = ''
    while operator not in ('+', '-', 'x', '/'):
        operator = input('Please enter one of the following operators: "+", "-", "x" or "/"\n')

    # Enter the first operand.
    operand1 = 0.5
    while operand1 != round(operand1, 0):
        argument1 = input('Please enter the first integer to operate on:\n')
        operand1 = float(argument1)
    operand1 = int(operand1)

    # Enter the second operand.
    operand2 = 0.5
    while operand2 != round(operand2, 0):
        argument2 = input('Please enter the second integer to operate on:\n')
        operand2 = float(argument2)
    operand2 = int(operand2)

    # Perform the operation on the given inputs.
    print(f"{operand1} {operator} {operand2} = {operate(operator, operand1, operand2)}")

    # Ask whether to perform another calculation.
    continueArgument = ''
    while continueArgument.lower() not in ('y', 'n'):
        continueArgument = input('Please enter "y" if you wish to perform another calculation, or "n" if you wish to exit:\n')
    if continueArgument.lower() == 'n':
        continueFlag = False
