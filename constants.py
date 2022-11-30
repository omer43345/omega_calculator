def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power(num1, num2):
    return pow(num1, num2)


def mod(num1, num2):
    return num1 % num2


def minimum(num1, num2):
    if num1 < num2:
        return num1
    return num2


def maximum(num1, num2):
    if num1 > num2:
        return num1
    return num2


def neg(num):
    return -num


def avg(num1, num2):
    return (num1 + num2) / 2


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


priority_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6}
operators_dict = {'+': plus, '-': minus, '*': multiply, '/': divide, '^': power, '%': mod, '$': maximum, '&': minimum,
                  '@': avg, '~': neg, '!': factorial}
side_of_operands = {'+': 'both', '-': 'both', '*': 'both', '/': 'both', '^': 'both', '%': 'both', '$': 'both',
                    '&': 'both', '@': 'both', '~': 'right', '!': 'left'}
