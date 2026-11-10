def calculator(x, operator, y):
    if not x < 0 or x > 0:
        return "x must be an integer"
    if not y < 0 or y > 0:
        return "y must be an integer"
    if y == 0 and operator is '/' :
        return "cannot divide by zero"
    if operator == '%' :
        return "Invalid operator"
    result = input('value of x:  ')
    operator = ('operator: ' )
    y = input('value of y: ')

    result = x operator y

    return result