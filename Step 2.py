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
with open('C:\Work\DevOps Apprenticeship\Module 1\Workshop\Step 2.txt') as file:
    content = [line.rstrip() for line in file]

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