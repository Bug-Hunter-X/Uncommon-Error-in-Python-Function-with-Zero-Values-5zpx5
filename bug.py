def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(5, 0)
print(result) # This will raise ZeroDivisionError
result2 = function_with_uncommon_error(0, 10)
print(result2) # This will return 10, which is fine
result3 = function_with_uncommon_error(10,0)
print(result3) #this will raise ZeroDivisionError

#Uncommon error: The function appears to handle zero values in a way that causes unexpected behavior based on parameter order. 
#In some cases it returns the other parameter, but in others it will raise a ZeroDivisionError. 
#This is subtle and can be difficult to find.