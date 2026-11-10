def binary(n):
    remainder = []

    while n > 0:
        r = n % 2
        n = n // 2
        
        remainder.append(str(r))

    remainder.reverse()
    
    result = "".join(remainder)  
    

    print(f"Output: {result}")

binary(8)