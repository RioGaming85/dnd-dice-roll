from roll import rollDice as roll
from clear import clear

def main():
  while True:
    ans = input('''
CLEAR or CLS: Clear the Output Log
QUIT or Q: Quit Application
ROLL or RL: Roll Dice
 > ''').upper()
    if ans in ['ROLL','RL']: # check the input
      roll(input('\nInput dice and amount:\n > ').upper()) # using the roll function
    elif ans in ['CLEAR','CLS']:
      clear()
    elif ans in ['Q','QUIT']:
      print('Goodbye.')
      break
    else:
      print('Invalid Input')

print('\033[1m'+'\nWelcome to Dice Roll!'+'\033[0m') # the '\033[1m' is to display the line in bold
main()
