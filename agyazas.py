"""
Készíts egy programot, amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a képernyőre egy pocak szerű alakzatot az alábbiak szerint!
  Adj meg egy páros számot! 8
  
  O 
  O O 
  O O O 
  O O O O 
  O O O O 
  O O O 
  O O 
  O 
  """
n = int(input('Adj meg egy páros számot!'))
sor = 0
while sor <n:
    oszlop = 0
    while oszlop < sor+1:
        print('0 ', end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1

sor = 0
while sor <n:
    oszlop = 0
    while oszlop < n-sor:
        print('0 ', end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1