#set a random list
import random
listOfElements = []
for i in range(0,20):
    n = random.randint(0,99)
    listOfElements.append(n)

player = 1
print('''
-This game is played by 2 persons.
-During a turn a player may remove either one or two adjacent tokens.
-The player who removes the last token wins.
________________________________________________________________________
''')

print("The list:  ",listOfElements)

while True:
    # get a valid number
    print("Player ",player," turn")
    while True:
        answer = str(input("Do you want to select one number or two numbers? \n")).upper()
        if answer == "TWO" or answer == "2":
            DeletedNum1 = int(input("Please choose the index of the first number from [1:20] \n"))
            DeletedNum2 = int(input("Please choose the index of the second number from [1:20] \n"))
        
            if listOfElements[DeletedNum1-1] != "-" and listOfElements[DeletedNum2-1] != "-":
                if DeletedNum1 == DeletedNum2 -1 :
                    
                    if DeletedNum1 in range ((len(listOfElements))+1):
                        listOfElements[DeletedNum1-1] = "-"
                    if DeletedNum2 in range ((len(listOfElements))+1):
                        listOfElements[DeletedNum2-1] = "-"
                    #show the state of the list
                    print("The state of the list: ", listOfElements)

                    #check the winner if result of the count matches woth result from len()

                    result = listOfElements.count(listOfElements[0]) == len(listOfElements)
                    if result:
                        print("Player ",player," wins!")
                        quit()

                    #switch the players
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                    if DeletedNum1 != ((len(listOfElements)+1)):
                        break
                    else:
                        print("Wrong number, please try again")
                else:
                    print("Please enter two adjacent numbers")
            else:
                print("Please enter a number that wasn't already choosen")
        if answer == "ONE" or answer == "1":
                DeletedNum1 = int(input("Please choose the index of the number from [1:20] \n"))
                if listOfElements[DeletedNum1-1] != "-":

                    if DeletedNum1 in range((len(listOfElements))+1):
                        listOfElements[DeletedNum1-1] = "-"
                        #show the state of the list
                        print("The state of the list: \n", listOfElements)

                        #check the winner if the result of the count matches with the result from len()
                        result = listOfElements.count(listOfElements[0]) == len(listOfElements)
                        if result:
                            print("Player ",player," wins!")
                            quit()

                        #switch the players
                        if player == 1:
                            player = 2
                        else:
                            player = 1
                        if DeletedNum1 != ((len(listOfElements))+1):
                            break
                        else:
                            print("Wrong number, please try again")
                    else:
                        print("Please enter an index from [1:20] \n")
                else:
                    print("Please enter a number that wasn't already choosen")
        else:
            print("Please enter either 'one or 1' or 'two or 2' only")