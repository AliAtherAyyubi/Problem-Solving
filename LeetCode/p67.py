

def addBinary( a, b):
    # Convert binary strings to integers
    a = int(a, 2)
    b = int(b, 2)
    print(a,b)
    # Add the integers
    result = a + b

    # Convert the result back to binary and remove the '0b' prefix
    return bin(result)[2:]

    
        

print(addBinary("11", "1"))  # Output: "100"