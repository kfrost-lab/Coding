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

#Question 2
answer = input("Q2, What is 78 + 10?  \n" )

if answer == '88':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")
    

print ("your total score is...")
print (score1 )

#Question 3
answer = input("Q3, What is 83 - 52?  \n" )

if answer == '31':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)

#Question 4
answer = input("Q4, What is 23 - 11?  \n" )

if answer == '12':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)

#Question 5
answer = input("Q5, What is 12 × 5?  \n" )

if answer == '60':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)

#Question 6
answer = input("Q6, What is 9 × 6?  \n" )

if answer == '54':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)

#Question 7
answer = input("Q7, What is 60 ÷ 6?  \n" )

if answer == '10':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)

#Question 8
answer = input("Q8, What is 45 ÷ 9?  \n" )

if answer == '5':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)


#Question 9
answer = input("Q9, What is 524 + 165?  \n" )

if answer == '689':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)

#Question 10
answer = input("Q10, What is 614 + 138?  \n" )

if answer == '752':
    print("Nice that was Correct! ")
    score1 = score1 +1

else:
    print("oh no that was incorrect")

print ("your total score is...")
print (score1)

if (score1) > 7:
    print ("Great job you passed the test")

else:
    print ("Sorry, you failed the test")


print ("Thanks for playing, See you next time")
