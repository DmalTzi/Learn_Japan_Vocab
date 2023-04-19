import random
from data import Hiragana, CompareHandK


Punctuation_Select = []
Shuffled_Punctuation = []
Run_Program = True

def shuffle_latter(Punctuation_selected):
    """"Shuffle punctuation from your select"""
    getlatter = Hiragana[Punctuation_selected]
    random.shuffle(getlatter)  
    return getlatter  


def check_vocab(latter):
    for i in latter:
        user = input(f"{i} Input Your guess : ").lower()
        try:
            if CompareHandK[user] == i:
                print("You right")
            else:
                print("You wrong")
        except Exception as e:
            print("Not have in this program's vacab")
            print(e)


def shuffle_answer(Punctuation_Select):
    for Punctuation_char in Punctuation_Select:
        for Shuffled_latter in shuffle_latter(Punctuation_char):
            Shuffled_Punctuation.append(Shuffled_latter)

    return Shuffled_Punctuation

while Run_Program:
    while True:
        select = input("Input : ").lower()
        if select == "0":
            break
        if select in Punctuation_Select:
            continue
        else:
            Punctuation_Select.append(select)

    Shuffled_answer = shuffle_answer(Punctuation_Select)
    
    random.shuffle(Shuffled_answer)

    check_vocab(Shuffled_answer)

    if input("Want to play again? Type 'y' or 'n' : ").lower() == 'n':
        print("End this program")
        Run_Program = False


print(Shuffled_Punctuation)
print(Punctuation_Select)