'''
Name:        Zachary Doubikin
Date:        10/17/21
Program:     Guessing game
Description: 3-5 Performance assessment
'''
#############################################################################
#Importing libraries---------------------------------------------------------
#############################################################################
import random
import csv
#############################################################################
#Global Variables------------------------------------------------------------
#############################################################################
random.seed()   #Prepare random number generator

userList = []   #List for the users' names
guessList = []  #List for the attempts of thier guesses
#############################################################################
#Functions-------------------------------------------------------------------
#############################################################################
'''
=============================================================================
Function:greetUser
Parameters:None
Return:user
Description:Greets the user and saving the users' name
=============================================================================
'''
def greetUser(): #greeting the user
    print("Please enter your first name")
    user = input()
    userList.append(user)#Records the users' name
    print("Hello " + user + "!")
    return user
'''
=============================================================================
Function:randint
Parameters:None
Return:rnum
Description:Sets the random number generator for the guessing game
=============================================================================
'''
def randint():
    rnum = random.randint(1,10) #Random number generator
    return rnum
'''
=============================================================================
Function:gameRound
Parameters:None
Return:counter
Description:Main decision make for the game is using for loop to record the
amount of guesse the user takes.
=============================================================================
'''
def gameRound():
    counter = 0 #counter for the guesses
    rnum2 = randint()
    print("Please guess a number between 1 and 10... ")
    answer = int(input())
#Decision maker to see if the user guessed correctly using a while statement
    while rnum2 != answer:
        if rnum2 < answer:
            print("You guessed too high..")
        elif rnum2 > answer:
            print("You guessed too low..")
        else:
            print("Correct")
        counter = counter + 1 #Records the amount of guesses
        print("Please guess a number between 1 and 10... ")
        answer = int(input())
    guessList.append(counter)#adds final guess count to the csv file
    return counter
'''
=============================================================================
Function:reader
Parameters:None
Return:None
Description:opens csv file and reads it out row for row
Also used to read out the previous users and their scores
=============================================================================
'''
def reader():
    scoreFile=open('scoreskept.csv','a', newline = '')#creates file if none existed
    scoreFile.close()
    scoreFile=open('scoreskept.csv','r')
    reader=csv.reader(scoreFile)
    print('[Users , Score]')
    for row in reader:#Prints out row for row
        if any(row):#If there was no rows it will skip
            print(row)
    scoreFile.close()
            
'''
=============================================================================
Function:writer
Parameters:None
Return:None
Description:Writes out the list given and sets it to specific rows
Records and saves the scores of the current users
=============================================================================
'''
def writer():
    scoreKeeper = open('scoreskept.csv', 'a', newline = '')
    with scoreKeeper:
        csvWriter = csv.writer(scoreKeeper)
        for i in range(len(userList)):
            csvWriter.writerow((userList[i],guessList[i]))
        scoreKeeper.close()
'''
=============================================================================
Function:end
Parameters:None
Return:None
Description:End of program and gives a list of the recent users and
their amount of guesses
=============================================================================
'''
def end():
    players = str(userList)[1:-1]
    guesses = str(guessList)[1:-1]
    print("The name of the players are " +players)
    print("The amount of guesses are " +guesses)
'''
=============================================================================
Function:takeSecond
Parameters:None
Return:elem[1]
Description: Allow to use the second element in a list 
=============================================================================
'''
def takeSecond(elem):
    return elem[1]
'''
=============================================================================
Function:sorter
Parameters:None
Return:None
Description: Sorts list to list the highest score individual
=============================================================================
'''
def sorter():
    curScore = list(zip(userList,guessList))#used to combined separate lists
    keptscore = open('scoreskept.csv', newline = '')
    reader = csv.reader(keptscore)
    scoreList = list(reader)
    curScore.sort(key=takeSecond)#sorting by the second element(numbers in
                                 #the scorelist
    scoreList.sort(key=takeSecond)
    print('The highest score from this game is ' + str(curScore[0])[1:-1])
    print('The previous highest score is ' + str(scoreList[0])[1:-1])
'''
=============================================================================
Function:main
Parameters:None
Return:None
Description:puts everything together main brain of the program
=============================================================================
'''
def main():
    keepGoing = "Y"
    reader()
    while keepGoing=="Y" or keepGoing=="Yes":
        user = greetUser()
        counter = gameRound()
        print("Congratulations, " + user + " You guessed the number in " + str(counter) + " tries!")
        keepGoing = input("Should I start another game? (Y/Yes to continue)")
    writer()
    end()
    sorter()
#############################################################################
#Main Section of the Program starts here-------------------------------------
#############################################################################
main()
