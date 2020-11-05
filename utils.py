def calculate(a, b, operator):
    """This will perform the specified
       arithmetic operation on the given
       operands"""

    if type(a) not in [int, float]:
        raise TypeError('The operand type must be either integer or float.')

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
