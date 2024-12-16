# Manually adding the goal number
# n1 =5
# for i in range(1, 100):
#     cn=int(input("enter the number!!! Goodluck"))
#     if n1 ==cn:
#         print("Well guessed")
#         break
#     else:
#         print("Better luck next time")

#Random selecting the number
import random
target_num  = random.randint(1, 10)
guess_num =  0
while target_num != guess_num:
   guess_num = int(input('Guess a number between 1 and 10 till you get it right'))
print('Well guessed!') 
