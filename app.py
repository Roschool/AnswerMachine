import random as rd
from random import choice as cs

questions = [
    "Wat is je naam?",
    "Hoe oud ben je?",
    "Wat is je geboorte plaats?"
    ]

answerBack =  {
    "Wat is je naam?": "Wat een mooie naam!",
    "Hoe oud ben je?": "Jeetje dat is oud!",
    "Wat is je geboorte plaats?": "Dat is een mooie plaats!"
}

def askingQuestions():
    randomQuestion = cs(questions)
    askQuestion = input(randomQuestion + " ")

    answerGivesBack = answerBack[randomQuestion]

    print(answerGivesBack)

askingQuestions()
