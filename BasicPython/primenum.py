# Input from the user
num = int(input("Enter a number to check if it's prime: "))


if num < 2:  
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, num): 
        if num % i == 0:
            is_prime = False
            break  

    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
