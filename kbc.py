print(""" 
*********************************************************************************************************************************************************************
                                                                     ----------------
--------------------------------------------------------------------| WELCOME TO KBC |-------------------------------------------------------------------------------
                                                                     ----------------
*********************************************************************************************************************************************************************
    """)
print("                                                                !!! SO LETS GET STARTED !!!")    
print()
KBC = {
    1:{
        "question":"Question.1  IF you have one, you want to share it. But once you share it, you do not have it. What is it?",
        "option1" : "[A] A massage            [B] A secret",
        "option2" : "[C] A gift               [D] A person",
        "answer"  : "B"
    },
    2:{
        "question":"Question.2  If it takes eight men ten hours to build a wall, how long would it take four men?",
        "option1" : "[A] five hours           [B] ten hours",
        "option2" : "[C] zero hours           [D] three hours",
        "answer"  : "C"
    },
    3:{
        "question":"Question.3  If you had only one match and entered a dark room containing an oil lamp, some kindling wood, and a newspaper, which would you light first?",
        "option1" : "[A] oil lamp             [B] newspaper",
        "option2" : "[C] wood                 [D] match",
        "answer"  : "D"
    },
    4:{
        "question":"Question.4  If you spell “sit in the tub” s-o-a-k, and you spell “a funny story” j-o-k-e, how do you spell “the white of an egg”?",
        "option1" : "[A] E-G-G  W-H-I-T-E               [B] W-H-I-T-E  E-G-G",
        "option2" : "[C] E-G-G  E-G-G                   [D] W-H-I-T-E  W-H-I-T-E",
        "answer"  : "A"
    },
    5:{
        "question":"Question.5  How much dirt is there in a hole that is 3 feet deep, 6 feet long, and 4 feet wide?",
        "option1" : "[A] 3 feet               [B] None",
        "option2" : "[C] 6 feet               [D] 4 feet",
        "answer"  : "B"
    },
    6:{
        "question":"Question.6  I start out tall, but the longer I stand, the shorter I grow. What am I?",
        "option1" : "[A] A match              [B] A fire",
        "option2" : "[C] A coal               [D] A candle",
        "answer"  : "D"
    },
    7:{
        "question":"Question.7  Everyone in the world needs it, but they usually give it without taking it. What is it?",
        "option1" : "[A] A money              [B] An information ",
        "option2" : "[C] An advice            [D] A secret",
        "answer"  : "C"
    },
    8:{
        "question":"Question.8  What two words, when combined, hold the most letters?",
        "option1" : "[A] Police Station           [B] Post Office ",
        "option2" : "[C] Pop Corn                 [D] Paper Pen",
        "answer"  : "B"
    },
    9:{
        "question":"Question.9  What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats?",
        "option1" : "[A] River                  [B] Silicon ",
        "option2" : "[C] Jungle                 [D] Paper",
        "answer"  : "A"
    },
    10:{
        "question":"Question.10  A truck driver is going down a one way street the wrong way, and passes at least ten cops. Why is he not caught?",  
        "option1" : "[A] Because he has laicence                            [B] Because he is driving safely ",
        "option2" : "[C] Because he doesn't know about cops                 [D] Because he is walking",
        "answer"  : "D"
    },
}
def kbcgame():
    score = 0
    for a in KBC:
        print("""-------------------------------------------------------------------------------------------------------------------------------------------------------""")
        print(KBC[a]["question"])
        print("""-------------------------------------------------------------------------------------------------------------------------------------------------------""")
        print(KBC[a]["option1"])
        print()
        print(KBC[a]["option2"])
        print()
        ans = input("                                                                Enter your answer: ")
        print()
        print()
        if ans == KBC[a]["answer"]:
            print("                                                 *****************************************************")
            print("                                                 .....CONGRATULATIONS.....THIS IS A RIGHT ANSWER.....")
            print("                                                 *****************************************************")
            print()
            score += 50
            print()
        else:
            print("                                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("                                                    .....BAD LUCK.....THIS IS A WRONG ANSWER.....")
            print("                                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print()
            score -= 50
            print()
    print("                                                           -----------------------------------")
    print(f"                                                            YOUR TOTAL SCORE IS : {score} ")
    print("                                                           -----------------------------------")
    print()
    if score == 0:
        print("                                                     X X X SORRY YOU DIDN'T WIN ANY PRICE MONEY X X X")
    elif score < 0:
        print("                                                     X X X BAD LUCK YOU DIDN'T WIN...YOU HAVE TO PAY 5000 X X X")
    elif score in range(1,51):
        print("                                                   ...CONGRATULATIONS YOU WON 500 RUPEES...")
    elif score in range(50,101):
        print("                                                   ...CONGRATULATIONS YOU WON 1000 RUPEES...")
    elif score in range(100,201):
        print("                                                   ...CONGRATULATIONS YOU WON 2000 RUPEES...")
    elif score in range(200,301):
        print("                                                   ...CONGRATULATIONS YOU WON 3000 RUPEES...")
    elif score in range(300,401):
        print("                                                   ...CONGRATULATIONS YOU WON 4000 RUPEES...")
    elif score in range(400,501):
        print("                                                   ...CONGRATULATIONS YOU WON 5000 RUPEES...")
    print()
kbcgame()