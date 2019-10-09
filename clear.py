def clear():
  import os
  try:
    os.system('clear') # Linux clear
  except:
    os.system('cls') # Windows clear
