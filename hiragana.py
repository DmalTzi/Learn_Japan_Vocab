import random
from data_vocab import Hiragana, CompareHandK, CompareHandK_Reverse
from os import system


def shuffle_answer(Punctuation_Select):
    """combine punctuation and chose punctuation by your select"""
    global max_point

    for Punctuation_char in Punctuation_Select:
        getlatter = Hiragana[Punctuation_char]
        random.shuffle(getlatter) 

        for Shuffled_latter in getlatter:
            Shuffled_Punctuation.append(Shuffled_latter)

    max_point += len(Shuffled_Punctuation)

    return Shuffled_Punctuation


def check_vocab(latter):
    global point
    system('clear') # support bash command line (linux/macos/unix)
    system('cls') # support command prompt (windows)
    
    for i in latter:
        print("===============")
        print(f"Goal : {max_point}")
        user = input(f"{i} Input Your guess : ").lower()
        try:
            if CompareHandK[user] == i:
                point += 1
                print(f"Your right, here you point : {point}")
            else:
                failed.append(f"{CompareHandK_Reverse[i]} : {i}")
                print(f"Your wrong, The asnwer is : '{CompareHandK_Reverse[i]}'")
                print(f"Your point : {point}")
        except Exception as e:
            print("Not have in this program's vacab")
            print(e)


Run_Program = True

while Run_Program:
    point = 0
    max_point = 0
    Punctuation_Select = []
    Shuffled_Punctuation = []
    failed = []

    while True:
        select = input("Choise punctuation you want, and type '0' to next : ").lower()
        if select == "0":
            break
        if select in Punctuation_Select:
            continue
        else:
            Punctuation_Select.append(select)

    Shuffled_answer = shuffle_answer(Punctuation_Select)
    
    random.shuffle(Shuffled_answer)

    check_vocab(Shuffled_answer)
    
    print("======= your mistake =========")
    [print(i) for i in failed]
    print("================")
    if input("Want to play again? Type 'y' or 'n' : ").lower() == 'n':
        print("See you naxt time.")
        Run_Program = False