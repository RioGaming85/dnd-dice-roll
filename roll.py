def rollDice(diceInp):
  from random import randint
  if (diceInp.find('+') != -1): # if there is a modifier
    try:
      diceNum = diceInp.split('D')
      splitHolder=(diceNum[1].split('+'))
      diceNum.remove(diceNum[1])
      diceNum.append(splitHolder[0])
      diceNum.append(splitHolder[1])
    except:
      print('Incorrect Syntax.\nThe correct syntax is xDy(+z)')
      return None
    diceRollArray = []
    diceTotal = 0
    for x in range(int(diceNum[0])):
      roll = randint(1,int(diceNum[1]))
      diceRollArray.append(str(roll))
      diceTotal += roll
    print('Roll ('+str(diceNum[0])+'d'+str(diceNum[1])+'+'+str(diceNum[2])+'):')
    print(str(diceRollArray)+' + '+str(diceNum[2]))
#######################################################################################
  else: # if there is no modifier
    try:
      diceNum = diceNum.split('D')  
    except:
      print('Incorrect Syntax.\nThe correct syntax is xDy(+z)')
      return None
    diceRollArray = []
    diceTotal = 0
    for x in range(int(diceNum[0])):
      roll = randint(1,int(diceNum[1]))
      diceRollArray.append(str(roll))
      diceTotal += roll
    print('Roll ('+str(diceNum[0])+'d'+str(diceNum[1])+'):')
    print(diceRollArray)
  print('Total: '+ str(diceTotal))
