# -*- coding: utf-8 -*-
import string
import random
from chuck import ChuckNorris

jokes = ChuckNorris();
def fiveLines():
    print "\n"*4

def cleanScreen():
    print "\n"*24

def deleteLowercase(p):
    return string.upper(p)

def isRightLetter(c):
    if c  in "abcdefghijqlmnñopqrstuvwxyz":
        if c not in "aeiou":
            return True
        else:
            return False
    else:
        return False

def countWords(p):
    l = p.split(" ")
    return len(l) < 4

def isACorrectPanel(p):
    l = p.split(" ")
    if len(l) < 4:
        for lletra in p:
            if lletra not in "abcdefghijqlmnopqrstuvwxyz ":
                return False
        return True
    else:
        return False

def secretPanel(p):
    r = ""
    for lletra in p:
        if lletra != " ":
            r = r + "_"
        else:
            r = r + lletra
    return r

def containsLetter(p,c):
    return (c in p)

def updateSecretWord(w,sw,c):
    r = ""
    i = 0
    while i < len(w):
        lletra = w[i]
        if lletra == c:
            r = r + c
        else:
            r = r + sw[i]
        i = i + 1
    return r


def generateNumber():
    return random.randint(0,5)

def updatePoints(sw,c):
    contador = 0
    for lletra in sw:
        if lletra == c:
            contador = contador + 1
    return contador


def correctPanel(w,sol):
    if w == sol:
        return True
    else:
        return False

# def randomSentence(goodorbad):
#     random_number = random.randrange(0,3)
#     if goodorbad == True:
#         sentence = ["Wrong word, your imagination is not high isn't it?","Wrong word, YOU WANT TO PLAY TRICKS ON ME!?","Wrong word, try again!"]
#     else goodorbad == False:
#         sentence = [""]
#
#     random_sentence = sentence[random_number]
#     print random_sentence

def Game():
    print ""
#   _______             _______                       __             __      __               
#  |       \           |       \                     |  \           |  \    |  \              
#  | $$$$$$$\ __    __ | $$$$$$$\  ______   __    __ | $$  ______  _| $$_  _| $$_     ______  
#  | $$__/ $$|  \  |  \| $$__| $$ /      \ |  \  |  \| $$ /      \|   $$ \|   $$ \   /      \ 
#  | $$    $$| $$  | $$| $$    $$|  $$$$$$\| $$  | $$| $$|  $$$$$$\\$$$$$$ \$$$$$$  |  $$$$$$\
#  | $$$$$$$ | $$  | $$| $$$$$$$\| $$  | $$| $$  | $$| $$| $$    $$ | $$ __ | $$ __ | $$    $$
#  | $$      | $$__/ $$| $$  | $$| $$__/ $$| $$__/ $$| $$| $$$$$$$$ | $$|  \| $$|  \| $$$$$$$$
#  | $$       \$$    $$| $$  | $$ \$$    $$ \$$    $$| $$ \$$     \  \$$  $$ \$$  $$ \$$     \
#   \$$       _\$$$$$$$ \$$   \$$  \$$$$$$   \$$$$$$  \$$  \$$$$$$$   \$$$$   \$$$$   \$$$$$$$
#            |  \__| $$                                                                       
#             \$$    $$                                                                       
#              \$$$$$$                                                                        
""

print "Welcome to the PyRoulette"
guessed = False
data = jokes.random()
print data.joke
print "Which player do you want to be?"
print "1) Word Writter, 2) Word guesser"
player_id = input("Write 1 or 2 = ")
print "Entering the matrix...."
playerA = True
playerB = False
player_name1 = raw_input("Player 1 tell me your name ")
player_name2 = raw_input("Player 2 tell me your name ")
players = [player_name1, player_name2]
print players[1] + " " + "You'll be the word guesser"
print players[0] + " " + "You'll be the word Writter"
once = 0
if(player_id == 2):
    player_id = 1
while(player_id == 1 and playerA == True):
    if(once == 0):
        print players[1] +" "+ "please wait until" + " " +  players[0]+ " " +"writes a word"
    elif(once > 1):
        print players[0] +" "+ "please wait until" + " " +  players[1]+ " " +"writes a word"

    print "Don't look cheater!"
    print "A good word it's always lowercase containing only letters"
    paraula = raw_input("Insert a word: ")
    while not isACorrectPanel(paraula):
        data = jokes.random(categories=['nerdy'])
        print data.joke
        print "Bad Word, choose another one please"
        paraula = raw_input(players[0] + " "  + "Insert a word: ")
    if(isACorrectPanel(paraula) == True):
        print "That's a good word! your imagination is very high!"
        print "Chuck Norris would be proud of you"
        cleanScreen()
        print players[1] + " " + "Try to guess this word if you can"
        data = jokes.random(categories=['nerdy'])
        print data.joke
        paraula_secreta = secretPanel(paraula)
        print paraula_secreta
        player_id = 2
        playerA  = False
    while (player_id == 2 and guessed == False and playerA == False):
        choosed_letter = raw_input("Guess a letter:")
        if(len(choosed_letter) == 1 and containsLetter(paraula,choosed_letter) == True):
            paraula_secreta = updateSecretWord(paraula,paraula_secreta,choosed_letter)
            print paraula_secreta
            points = updatePoints(paraula_secreta,choosed_letter)
            print points
        elif(len(choosed_letter) > 1):
            print "Must write one letter at first"
        elif(containsLetter(paraula,choosed_letter) == False):
            print "The letter is not in there! Try again looser"+ " " + players[1] + " " + "here's a quick joke for you:" + " " + data.joke
        if(correctPanel(paraula_secreta,paraula)== True):
            guessed == True
            print "Good Job " + players[1] + "!"
            print "You scored: " + str(points) + " " + "Points"
            print players[1]+ " "+ "Now it's your turn to write a word"
            player_id = 1
            playerA = True
            once = True
            once = once + 1
Game()

