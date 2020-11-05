def calculate(a, b, operator):
    """This will perform the specified
       arithmetic operation on the given
       operands"""

    result = 'Unexpected Operator'

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b

    return result
