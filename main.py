from roll import rollDice as roll
from clear import clear
from re import split as regSplit
from re import search

def main():
  while True:
    ans = input('\n > ').upper()
    if ans == '':
      pass
    else:
      if search(r'ROLL (\d*)D(\d*) [+] \d',ans) != None or search(r'RL (\d*)D(\d*) [+] \d',ans): # bit of extra string manipulation for modifiers
        ans = regSplit(r'\s',ans)
        ans[1] = ans[1] + ans[2] + ans[3]
        roll(ans[1])
      elif search(r'ROLL (\d*)D(\d*)',ans) != None or search(r'RL (\d*)D(\d*)',ans) != None: # check the input
        roll(regSplit(r'\s',ans)[1]) # using the roll function
      elif ans in ['CLEAR','CLS']:
        clear()
        print('''
CLEAR or CLS: Clear the Output Log
QUIT or Q: Quit Application
ROLL or RL: Roll Dice''')
      elif ans in ['Q','QUIT']:
        print('Goodbye.')
        break
      else:
        print('Invalid Input')

print('\033[1m'+'\nWelcome to Dice Roll!'+'\033[0m') # the '\033[1m' is to display the line in bold
print('''
CLEAR or CLS: Clear the Output Log
QUIT or Q: Quit Application
ROLL or RL: Roll Dice''')
main()
