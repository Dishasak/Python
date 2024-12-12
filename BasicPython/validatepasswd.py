passwd = input("Enter your password: ")

if len(passwd) < 8:
    print("Password should be at least 8 characters long")
elif len(passwd) > 12:
    print("Password should be no more than 12 characters long")
else:
    
    uc = 0  
    lc = 0  
    dg = 0 
    sp = 0  

    special_characters = "@#$"

   
    for char in passwd:
        if char.isupper():
            uc += 1
        elif char.islower():
            lc += 1
        elif char.isdigit():
            dg += 1
        elif char in special_characters:
            sp += 1

   
    if uc < 1:
        print("Password should include at least one uppercase letter")
    if lc < 2:
        print("Password should include at least two lowercase letters")
    if dg < 1:
        print("Password should include at least one digit")
    if sp < 1:
        print("Password should include at least one special character")

    if uc >= 1 and lc >= 2 and dg >= 1 and sp >= 1:
        print("Password is valid!")
    else:
        print("Invalid password!!!")
