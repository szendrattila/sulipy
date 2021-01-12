"""5. Feladat
Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó."""
szam = 1
folytatja = True
while folytatja:
  print("mondj egy páros számot")
  valasz = int(input())
  if valasz == szam + 2:
    folytatja = False

  