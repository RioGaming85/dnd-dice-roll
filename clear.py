def clear():
  import os
  if os.name == 'posix':
    os.system('clear') # Linux clear
  else:
    os.system('cls') # Windows clear
