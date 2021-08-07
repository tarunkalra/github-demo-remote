def add(x,y):
    pass
def subtract(x,y):
    pass          #On bug456
def multiply(x,y):
    return x*y              #On bug branch
def divide(x,y):
    if y==0:                        #On master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
def square(x):
    return x*x