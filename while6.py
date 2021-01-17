'''6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt. '''

from random import randint
gyujto = 0
i = 0
while i < 20:
    value = randint(1, 12)
    if value % 3==0:
        print(value)
        gyujto = gyujto+1
    i = i+1
print(f'3-al osztható szám {gyujto} db volt.')