# This is a guess the release date of Disney Cartoon Movies

from random import shuffle

print ("Welcome to the Magical Guess the Release Date Game for Dinsey Movies!")
print ("A movie will be chosen at random and you must to try to guess")
print ("the correct year it was released.")
print ("Here is some good luck with Tinker Bell's Pixie Dust *****")

with open("guessthereleasedateqanda.txt") as a:
    lines = a.readlines()

shuffle(lines)
guesses = 0
wrong = []

name = raw_input("What is your name?")

numberQuestions = int(raw_input("How many questions out of 40, would you like to answer?"))


for line in lines[:numberQuestions]:
        questions, rightAnswer = line.strip().split('\t')
        answer = int(raw_input(questions + ''))
        if answer == int(rightAnswer):
            print ('Congratulations! You are right!')
            guesses += 1
        else:
            print ('Sorry, you are not so magical that is NOT the correct answer!: the answer is %s.' %rightAnswer)
            wrong.append(questions)

print('You got %d right! AWESOME!' % (guesses))
if(wrong):
    print("Sorry Tinker Bell's Pixie Dust did not help your luck and you got the following wrong:")
    for w in wrong:
        print (w)

print "Thanks for playing have a magical rest of your day!"
