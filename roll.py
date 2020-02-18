def rollDice(diceInp):
  from re import split as regSplit # re.split() has the same effect as the base python .split() but takes a regex
  from random import randint
  if (diceInp.find('+') != -1): # Check if there is a positive modifier
    try:
            diceNum = regSplit(r'[D+]',diceInp)

    except:
      print('Incorrect Syntax.\nThe correct syntax is xDy(modifier)')
      return None
    diceRollArray = []
    diceTotal = diceNum[2] # Adding the modifier to the total
    diceTotal = int(diceTotal)
    for x in range(int(diceNum[0])): # The range will be equal to the number of dice
      roll = randint(1,int(diceNum[1])) # Actually rolling the dice, with the second argument being the number of faces on the die
      diceRollArray.append(str(roll))
      diceTotal += roll
    print('Roll ('+str(diceNum[0])+'d'+str(diceNum[1])+'+'+str(diceNum[2])+'):') # Sending all this back to the user
    print(str(diceRollArray)+' + '+str(diceNum[2]))
#######################################################################################
  elif (diceInp.find('-') != -1): # Check if there is a negative modifier
    try:
      diceNum = regSplit(r'[D+]',diceInp)
    except:
      print('Incorrect Syntax.\nThe correct syntax is xDy(modifier)')
      return None
    diceRollArray = []
    diceTotal = int(0 - (int(diceNum[2]))) # Subtracting the modifier from zero
    for x in range(int(diceNum[0])): # Everything else here is the same as for positive
      roll = randint(1,int(diceNum[1]))
      diceRollArray.append(str(roll))
      diceTotal += roll
    print('Roll ('+str(diceNum[0])+'d'+str(diceNum[1])+'-'+str(diceNum[2])+'):')
    print(str(diceRollArray)+' - '+str(diceNum[2]))
  
  else: # if there is no modifier
    try:
      diceNum = regSplit(r'[D]',diceInp)  
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
  print('Total: '+ str(diceTotal)) # Outputting the actual rolled total
