# This is a guess the release date of Disney Movies

from random import shuffle

# Introdcution & Welcoming code 

name = raw_input("Hello, What is your name?")

print ("Welcome" +name+  ", to the Magical Guess the Release Date Game for Disney Movies!")
print ("A movie will be chosen at random and you must to try to guess")
print ("the correct year it was released.")
print ("Here is some good luck with Tinker Bell's Pixie Dust *****")

print ("*** *** " * 2)
print (" ***   **" * 1)
print ("*   ***   " * 2)
print ("***  ***  " * 1)
print ("****   **" * 1)
print ("***   *** " * 2)
print ("  *****" * 2)
print ("*  ***  " * 2)
print ("***  ***  " * 1)
print ("**  **   **" * 1)

print("**  "*6)
print("  **"*6)

# Code for amount of questions 
with open("guessthereleasedateqanda.txt") as a:
    lines = a.readlines()

shuffle(lines)
guesses = 0
wrong = []
num_wrong = 0

numberQuestions = int(raw_input(name + ", How many questions out of 40, would you like to answer?"))

#Code for answers

for line in lines[:numberQuestions]:
        questions, rightAnswer = line.strip().split('\t')
        answer = int(raw_input(questions + ''))
        if answer == int(rightAnswer):
            print ('Congratulations! You are right!')
            guesses += 1
        else:
            print (name + ', Sorry! you are not so magical at the moment. That is NOT the correct answer!: the answer is %s.' %rightAnswer)
            wrong.append(questions)
            num_wrong +=1
            
right=numberQuestions - num_wrong
grade= 100 / numberQuestions * right
grade= str(grade)+"%" 
            
# Code for ending & summary of questions answered 

print('You got %s right! AWESOME!' % (grade))
if (guesses)==1:
        print("Nice Try, but better luck next time")
        
if(wrong):
    print("Sorry Tinker Bell's Pixie Dust did not help your luck and you got the following wrong:")
    for w in wrong:
        print (w)

print "Thanks for playing have a magical rest of your day!"
