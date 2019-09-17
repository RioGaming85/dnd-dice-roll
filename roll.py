def rollDice(diceInp):
  from random import randint
  from re import split as regSplit
  if (diceInp.find('+') != -1): # if there is a modifier
    try:
      diceNum=[]
      diceNum = (regSplit(r'/([D+])/g', str(diceInp)))
      print(regSplit(r'/([D+])/g', str(diceInp)))
      print(diceNum)
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
