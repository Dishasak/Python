number= int(input("enter the number"))
rev =0
i =0
while i< number:
    rem = number% 10
    rev = rev*10+rem
    number =number//10
print(rev)