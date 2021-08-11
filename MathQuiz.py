#score counter
score1 = 0

#opening text
print ("<<<<<Welcome to the Mighty Math Quiz>>>>>")

#Question 1
answer = input("Q1, What is 12 + 20?  \n" )

if answer == '32':

    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)
