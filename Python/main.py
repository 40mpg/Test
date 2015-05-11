try:
    import theMeat
    Anh = "Anh"
    newUser = False
    userChoice = 0
    
    userName = input("Please input your username: ")
    
    userScore = theMeat.getUserPoint(userName)
    
    if userScore == "-1":
        newUser = True
        
    else:
        pass
        
    if newUser:
        userScore = 0
    
    while userChoice != "-1":
        userScore = theMeat.askUser()
        
        userChoice = input("Input -1 to quit the game, or any other key to continue:")
    
    theMeat.updateUserPoints(newUser,userName,userScore)

except IOError:
    print ("There was an unknown error")
    
    


