#=============================IMPORTS===================================
import os
import time
#==========================GLOBAL VARIABLES============================
q='c'

p1_winstreak= 0
p2_winstreak= 0

#==============================ASSESTS==================================
logo = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠋⠈⣷⠶⠶⠶⠶⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣧⣤⣤⠤⣼⣷⣤⣄⣀⢿⠛⠛⠿⢿⣿⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⢀⡿⢸⡆⠀⠀⠀⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠀⠀⠀⣀⣀⣀⣀⣠⠞⠁⢸⡇⠀⠀⠀⡇⠈⠙⠻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⢻⡏⠉⠉⣧⠀⠀⢸⡇⠀⠀⢰⡇⠀⠀⡀⠘⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡾⢷⣄⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣟⣛⡻⠶⢤⣼⠿⣤⣄⣸⣇⠀⢠⡇⠀⢸⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⣠⢤⣄⠀⠀⠀⠀⠀⠀
⠀⣰⠶⢶⣏⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠘⠋⠉⠉⠛⢶⣤⡀⠀⠉⠉⠙⠓⠾⠁⠀⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⢀⡼⠋⠀⠉⣷⠀⠀⠀⠀⠀
⢸⡏⠀⠀⠈⠳⣄⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠦⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠟⠁⠀⢠⡾⠃⠀⠀⠀⠀⠀
⠈⢻⣦⡀⠀⠀⠈⠳⣦⡀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀
⣴⠏⠈⠻⣦⡀⠀⠀⠈⠻⣦⡀⠀⠀⠙⢿⣿⡟⠛⠛⠛⠷⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠻⣄⠀⠀⠈⠻⣦⡀⠀⠀⠈⠻⠆⠀⠀⠀⠙⠳⣄⡀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⢀⣾⡏⠀⠀⢀⣀⣠⠤⠴⠖⠚⣆
⠀⢩⡷⣤⡀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠆⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⢠⡿⠉⠉⠙⠻⢿⣿⠛⠋⠁⠀⠀⠀⢰⣿⡿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀⢸
⠀⣿⡄⠈⠛⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⣴⠋⠀⠀⠀⠀⢰⡄⠈⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡤⠤⠖⠚⠉
⠀⠈⠻⢦⣄⠀⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⡾⠁⠀⠀⠀⠀⠀⢸⠿⢦⡄⠀⠀⣇⣀⣠⣤⢤⣴⠖⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢷⣄⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⣇⠀⠀⠀⠀⠀⠀⡼⠀⠸⡇⠀⢸⠃⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⢻⡄⠀⠀⠀⠀⣼⠁⢀⡟⠛⠦⠾⠤⠤⠤⢤⡴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⢳⣄⢀⣼⠏⠀⠀⠀⠀⠀⠀⠸⠷⠤⢤⣄⣀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠙⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⡵⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣶⣦⣤⠶⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⢀⣤⣤⣤⣤⣤⣤⣶⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⢷⣶⣤⣤⣤⣤⣴⣶⣾⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

lets_play = """

███████████████████████████████████████████████████████
█▄─▄███▄─▄▄─█─▄─▄─█░█─▄▄▄▄█████▄─▄▄─█▄─▄████▀▄─██▄─█─▄█
██─██▀██─▄█▀███─███▄█▄▄▄▄─██████─▄▄▄██─██▀██─▀─███▄─▄██
▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▀▀▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀
                                                                  
 """

p1_icon ="""
                      ███████████
                      █▄─▄▄─█▀ ██
                      ██─▄▄▄██ ██
                      ▀▄▄▄▀▀▀▄▄▄▀"""

p2_icon ="""
                      ████████████
                      █▄─▄▄─█▀▄▄▀█
                      ██─▄▄▄██▀▄██
                      ▀▄▄▄▀▀▀▄▄▄▄▀"""

p1win_incon= """
      ███████████████████████████████████████████
      █▄─▄▄─█▀ ████▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█ █
      ██─▄▄▄██ █████─█─█─█─███─███─█▄▀─██▄▄▄▄─█▄█
      ▀▄▄▄▀▀▀▄▄▄▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▀"""
p2win_incon= """
      ████████████████████████████████████████████
      █▄─▄▄─█▀▄▄▀███▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█ █
      ██─▄▄▄██▀▄█████─█─█─█─███─███─█▄▀─██▄▄▄▄─█▄█
      ▀▄▄▄▀▀▀▄▄▄▄▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▀"""

tie_icon="""
                 █████████████████████
                 █─▄─▄─█▄─▄█▄─▄▄─███ █
                 ███─████─███─▄█▀███▄█
                 ▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▄▀
"""
#==========================================================
os.system('cls')
print(logo)
print(lets_play)                #Display initial screen
time.sleep(1)

while q != 'q':                #quit or continue while loop
    p1=''
    p2=''
    p1_valid=0 
    p2_valid=0
    os.system('cls')
    
    while p1_valid != 1:                               #validate input, by cheking that the input is either "r","p" or "s"
        if p1 =='r' or p1 =='p' or p1 =='s':
            p1_valid = 1
        else:
            print(logo)
            print("\n",p1_icon)    
            p1 = input("\n            [ r:rock, p:paper, s:scissors ]\n\n                           ")
            os.system('cls')

    while p2_valid != 1:
        if p2 =='r' or p2 =='p' or p2 =='s':
            p2_valid = 1
        else:
            print(logo)
            print("\n",p2_icon)
            p2 = input("\n            [ r:rock, p:paper, s:scissors ]\n\n                           ")
            os.system('cls')



    if p1 == p2 and p1 != '':
     print(logo)   
     print ("\n",tie_icon)
    elif p1 == 'r':
        if p2 == 'p':
            p2_winstreak += 1 
            print(logo)
            print("                         ▓▓▓▓▓")    #Small animation 
            time.sleep(0.1)
            print("                          ▓▓▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print(p2win_incon)
            print("\n         [ P1 Streak |",p1_winstreak,"]   [ P2 Streak |",p2_winstreak,"]")
            print("\n                [ P1 |",p1,"]   [ P2 |",p2,"]")
            
        else:
            p1_winstreak += 1
            print(logo)
            print("                         ▓▓▓▓▓")
            time.sleep(0.1)
            print("                          ▓▓▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            print(p1win_incon)
            print("\n         [ P1 Streak |",p1_winstreak,"]   [ P2 Streak |",p2_winstreak,"]")
            print("\n                [ P1 |",p1,"]   [ P2 |",p2,"]")
            
    elif p1 == 'p':
        if p2 == 'r':
            p1_winstreak += 1
            print(logo)
            print("                         ▓▓▓▓▓")
            time.sleep(0.1)
            print("                          ▓▓▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            print(p1win_incon)
            print("\n         [ P1 Streak |",p1_winstreak,"]   [ P2 Streak |",p2_winstreak,"]")
            print("\n                [ P1 |",p1,"]   [ P2 |",p2,"]")
            
        else:
            p2_winstreak += 1
            print(logo)
            print("                         ▓▓▓▓▓")
            time.sleep(0.1)
            print("                          ▓▓▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            print(p2win_incon)
            print("\n         [ P1 Streak |",p1_winstreak,"]   [ P2 Streak |",p2_winstreak,"]")
            print("\n                [ P1 |",p1,"]   [ P2 |",p2,"]")
            
    elif p1 == 's':
        if p2 == 'p':
            p1_winstreak += 1
            print(logo)
            print("                         ▓▓▓▓▓")
            time.sleep(0.1)
            print("                          ▓▓▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            print(p1win_incon)
            print("\n         [ P1 Streak |",p1_winstreak,"]   [ P2 Streak |",p2_winstreak,"]")
            print("\n                [ P1 |",p1,"]   [ P2 |",p2,"]")
            
        else:
            p2_winstreak += 1
            print(logo)
            print("                         ▓▓▓▓▓")
            time.sleep(0.1)
            print("                          ▓▓▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            time.sleep(0.1)
            print("                           ▓")
            print(p2win_incon)
            print("\n         [ P1 Streak |",p1_winstreak,"]   [ P2 Streak |",p2_winstreak,"]")
            print("\n                [ P1 |",p1,"]   [ P2 |",p2,"]")
    print("\n                 ]===================[")
    q=input ("\n                 c: continue | q: quit\n\n                             ")

