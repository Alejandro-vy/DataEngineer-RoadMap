def sumar (a, b):
    return a + b


print(sumar(5, 5))



def warm_or_cold (temperature):
    
    if temperature > 7:
        
        return ("Warm")
    else:
        
        return ("Cold")
        

print(warm_or_cold(10))  



def foo(temperature):
    
    if temperature > 25:
       return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"




print(foo(15))
print(foo(16))
print(foo(25))
print(foo(26))
print(foo(5))    