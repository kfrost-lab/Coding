import random

print ("Welcome to your maths quiz")
score=0

for i in range(1,11):
    symbols = ['+' , '-' , 'x']
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    question = random.choice(symbols)
    math = eval(str(num1) + question + str(num2))
    print ("The Question is" ,num1,question,num2)
    
    q= int(input("what is your answer:"))
    if q==math:
        print ("correct")
        score = score + 1
        print ("your total score is")
        print (score)

    else:
        print ("incorrect, the answer was" ,math)


