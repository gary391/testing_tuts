def add(x,y):
    """Add two numbers together."""
    return x + y

def subtract(x,y):
    """Subtract two numbers together."""
    return x - y

def multiply(x,y):
    """Multiply two numbers together."""
    return x * y

def divide(x,y):
    """Divide Function"""
    if y == 0:
        raise ZeroDivisionError
    return x / y
