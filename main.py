from roll import rollDice as roll
from clear import clear

def main():
  while True:
    ans = input('''
CLEAR or CLS: Clear the Output Log
QUIT or Q: Quit Application
ROLL or RL: Roll Dice
 > ''').upper()
    if ans in ['ROLL','RL']:
      roll(input('\nInput dice and amount:\n > ').upper())
    elif ans in ['CLEAR','CLS']:
      clear()
    elif ans in ['Q','QUIT']:
      print('Goodbye.')
      break
    else:
      print('Invalid Input')

print('\033[1m'+'\nWelcome to Dice Roll!'+'\033[0m')
main()
