import random
str1="This is a Guessing Game!"
print(str1)
number=random.randint(1,9)
chances=5

while(chances>0):
    guess=int(input("Enter Your Number :"))
    if(guess>number):
        print("Please Enter A Number Less Than Your Previous Guess!")
        chances=chances-1
    elif(guess<number):
        print("Please Enter A Number More Than Your Previous Guess!")
        chances=chances-1    
    else:
        print("Bravo!! You Win!")
if(chances==0):
    print("Uh Oh, You Ran Out Of Chances")
    