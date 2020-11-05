import functools
from flask import request


def inverse(function):
    """This will inverse the operator
        in HTTP POST request"""
    @functools.wraps(function)
    def wrapper():

        op = request.get_json()['op']
        if op == '+':
            request.get_json()['op'] = '-'
        elif op == '-':
            request.get_json()['op'] = '+'
        elif op == '*':
            request.get_json()['op'] = '/'
        elif op == '/':
            request.get_json()['op'] = '*'

        return function()

    return wrapper
