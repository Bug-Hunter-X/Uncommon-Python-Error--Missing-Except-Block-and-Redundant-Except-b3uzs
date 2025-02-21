def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
except TypeError:
    return "Invalid input type"
    #return "Invalid input type" # this line is the source of error

#Corrected Version
def function_with_uncommon_error_corrected(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError):
        return "Invalid input or division by zero"