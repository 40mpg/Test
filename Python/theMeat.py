import random
import os




def getUserPoint(userName):
    content =[]
    
    try:
        x = open('userScores.txt', 'r')
    
        for i in x:
            content = i.split(',')
            if content[0] == userName:
                x.close()
                return content[0]+","+ content[1]
            else:
                x.close()
                return "-1"
        
        
        
        
    
    except IOError:
        print ('File not Found')
        x = open('userScores.txt', 'w') 
        x.close()
        return '-1'

def updateUserPoints(newUser, userName, score):
    if newUser == True:
        input = open('userScores.txt', 'a')
        input.write(userName +','+ score)
        input.close()
                
    else:
        in1 = open('userScores.tmp', 'w')
        in2 = open('userScores.txt', 'r')
        for i in in2:
            content = i.split(',')
            if content[0] == userName:
                content[1] == score
                i = content[0] + ',' + content[1] + '\n'
            
            in1.write(i)
        
        in1.close()
        in2.close()
        
    os.remove('userScores.txt')
    #os.rename('userScores.tmp', 'userScores.txt')
        

        
def genQuestion():
    operandList = []
    operatorList = []
    operatorDict = {1:"+",2:"-",3:"*",4:"**"}
    questionString =''

    for x in range(5):
        operandList.append(random.randint(1,9))

    for x in range(4):
        if x > 0 and operatorList[x -1] != "**":
            operatorList.append(operatorDict[random.randint(1,4)])
        else:
            operatorList.append(operatorDict[random.randint(1,3)])
    
    for a in range(4):
        if a == 3:
            questionString += (str(operandList[a]) + operatorList[a] + str(operandList[a+1]))
        else:
            questionString += (str(operandList[a]) + operatorList[a])
            
            
    
   
    return questionString


    
    


def askUser():
    string = genQuestion()
    string1 = string.replace("**", "^")
    state = True
    
    print ("What is the answer to: " + string1)
    userAnswer = (input("Please input answer in integer\n"))
    
    while state:
        try:
            if int(userAnswer) == eval(string):
                print ("Great...you win a cookie\n")
                state = False
                return 1
            else:
                print ("Nah homey, you got it wrong, go back to school\n")
                state = False
                return 0
        
        except IOError:
            print("Please only input a fucking number and nothing else\n")
            userAnswer = (input("Please input answer in integer: \n"))
            
    
    
        
            
    




