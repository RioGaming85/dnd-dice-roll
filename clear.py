def clear():
  from os import name, system
  if os.name == 'posix':
    os.system('clear') # Linux clear
  else:
    os.system('cls') # Windows clear
