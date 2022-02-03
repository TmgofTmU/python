import random

b= random.randint(1,10)
def guessnumber(i):
 print ("game rules :\n 1.geuss any number beteen 1 and 10\n 2. you have 3 chances")  
 while i<3:
   a=int(input("guess any number "))
   if a == b:
    print ("the number you guessed is right ")
    break
   else :
    print('the number you guessed is wrong')
   i=i+1

print(guessnumber(0))


# the code below is the first time i tried and then wrapped the code above in functon 
# i=0
# while i<3:
#    a=int(input("guess any number "))
#    if a == 9:
#     print ("the number you guessed is right ")
#     break
#    else :
#     print('the number you guessed is wrong')
    
#    i=i+1

