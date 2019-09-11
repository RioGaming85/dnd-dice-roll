def rollDice(diceInp):
  from random import randint
  from re import findall
  if (diceInp.find('+') != -1): # if there is a modifier
    try:
      diceNum = findall(r'/([D+])/g', str(diceInp)
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
    print(str diceRollArray)+' + '+str(diceNum[2]))
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
    print diceRollArray)
  print('Total: '+ str(diceTotal))
#########################################################################################
def main():
  while True:
    ans = input('''
CLEAR or CLS: Clear the Output Log
QUIT or Q: Quit Application
ROLL or RL: Roll Dice
 > ''').upper()
    if ans in ['ROLL','RL']:
      rollDice(input('\nInput dice and amount:\n > ').upper())
    elif ans in ['CLEAR','CLS']:
      import os
      clear = lambda: os.system('clear')
      clear()
    elif ans in ['Q','QUIT']:
      print('Goodbye.')
      break
    else:
      print('Invalid Input')
#########################################################################################
print('''
Welcome to Dice Roll!
''')
main()
