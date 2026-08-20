def addition(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def divide(a,b):
    if(a<=0):
        return "Nominator should be greater then 0"
    
    return a/b


print(f"ADDITION OF TWO NUMBER {addition(2,2)}")
print(f"SUBTRACTION OF TWO NUMBER {subtract(6,2)}")
print(f"MULTIPLICATION OF TWO NUMBER {multiplication(2,2)}")
print(f"DIVISION OF TWO NUMBER {divide(4,2)}")
print(f"DIVISION OF TWO NUMBER {divide(0,2)}")