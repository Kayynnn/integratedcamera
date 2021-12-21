
x = 2
y = 0
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print( "division by zero!")
    else:
        print ("result is", result)
    finally:
        print ("executing finally clause")

divide(x,y)