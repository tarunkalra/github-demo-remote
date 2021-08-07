# Add implementation
def add(x,y):
    return x+y
# Subtract implementation
def subtract(x,y):
    return x-y          #On master branch
# Multiply implementation    
def multiply(x,y):
    return x*y              #On bug branch
#Divide implementation
def divide(x,y):
    if y==0:                        #On master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
# Square implementation
def square(x):
    return x*x