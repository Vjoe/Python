def fact():
    c = 1
    
    n = int(input("Enter the number to find factorial...!"))
    
    if (n == 0):
        print("The factorial is 1)")
        
    elif (n < 0):
        print("Enter a positive integer")
    else:
        for a in range(n):
            a = a + 1
            c = c*a
            
        print (a, "!= ", c)
    
fact()

