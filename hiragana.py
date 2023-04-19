import random
from data import Hiragana
selects = []


while True:
    select = input("Input : ")
    if select == "0":
        break
    if select in selects:
        continue
    else:
        selects.append(select)
    

for i in selects:
    print(i)
    print(Hiragana[i])

print(selects)