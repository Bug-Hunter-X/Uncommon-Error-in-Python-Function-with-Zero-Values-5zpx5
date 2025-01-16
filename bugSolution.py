def improved_function(a, b):
    if b == 0:
        return float('inf') if a>0 else float('-inf') if a<0 else 0
    elif a == 0:
        return 0
    else:
        return a / b

result = improved_function(5, 0)
print(result) # Output: inf
result2 = improved_function(0, 10)
print(result2) # Output: 0
result3 = improved_function(10,0)
print(result3) # Output: inf
result4 = improved_function(-10,0)
print(result4) # Output: -inf
#In this improved version, the function now consistently handles cases with zero in the denominator, preventing ZeroDivisionErrors.  
#It returns positive or negative infinity as appropriate, or 0 when the numerator is also 0.