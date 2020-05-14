import math

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

# Import the file.
with open('C:\Work\DevOps Apprenticeship\Module 1\Workshop\Step 3.txt') as file:
    content = [line.rstrip() for line in file]

calculations = {}
lineNumber = 1
for line in content:

    # Parse the line.
    instructions = line.split(' ')
    
    # If a calculation is specified, perform it. Round the result down to the nearest integer.
    if len(instructions) == 5:
        operator = instructions[2]
        operand1 = int(instructions[3])
        operand2 = int(instructions[4])
        resultOfOperation = operate(operator, operand1, operand2)
        newLineNumber = math.floor(resultOfOperation)
    # If no calculation is specified, just store the number given in the line.
    elif len(instructions) == 2:
        newLineNumber = int(instructions[1])
    # Error handling.
    else:
        print("Encountered instructions with unknown structure. Exiting.")
        exit()
    
    calculations[lineNumber] = (line, newLineNumber)
    print(lineNumber, calculations[lineNumber])

    lineNumber += 1

"""
# Calculate the result of each line in the final, and sum all of these results.
total = 0
for line in content:
    
    instructions = line.split(' ')
    
    operator = instructions[1]
    operand1 = int(instructions[2])
    operand2 = int(instructions[3])
    
    total += operate(operator, operand1, operand2)

# Print the answer.
print(total)
"""