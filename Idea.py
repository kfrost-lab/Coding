import random

print ("Welcome to your maths quiz")
score=0

for question_num in range(1, 11):
    ops = ['+', '-', '*']
    rand=random.randint(1,10)
    rand2=random.randint(1,10)
    operation = random.choice(ops)
    maths = eval(str(rand) + operation + str(rand2))
    print('\nQuestion number: {}'.format(question_num))
    print ("The question is",rand,operation,rand2)

    d=int(input ("What is your answer:"))
    if d==maths:
        print ("Correct")
        score=score+1
        print ("Your total score is")
        print (score)

    else:
        print ("Incorrect. The actual answer is",maths)
