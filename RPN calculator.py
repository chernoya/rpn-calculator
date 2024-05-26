
#Reverse Polish Notation (RPN) Calculator 


# convert string expression into individual characters in an array && preferably remove letters
def expressionInput():
    global expression, array 
    expression = input("Enter RPN expression: ")
    array = list(expression.split())
    print(array)

# main function that'll calculate the final value using the stack
def evaluateExpression(array):
    global stack
    stack = []
    for char in array:
        if char in ['/', '*', '+', '-',]:
            if len(stack) < 2:
                print("Insufficient values in stack")

            item1 = stack.pop()
            item2 = stack.pop()
            
            if char == '/':
                stack.append(item2 / item1)
            elif char == '*':
                stack.append(item2 * item1)
            elif char == '+':
                stack.append(item2 + item1)
            elif char == '-':
                stack.append(item2 - item1)
            print(stack)
        else:
            stack.append(int(char))

expressionInput()
evaluateExpression(array)