import random

options = (1, 2, 3) # 1.Rock - 2.Paper - 3.Scissors
pcwin = 0
plwin = 0
round = 1
print("\n=================================== \n======= Welcome to RPS GAME =======\n===================================\n")

# Cycle of rounds
while(pcwin<2 and plwin<2):
    print(f"------------- ROUND {round} -------------")
    player = int(input("Chose: 1.Rock - 2.Paper - 3.Scissors => "))
    # Check player option cycle
    while(player<1 or player>3):
        print("\n======= YOU DON'T CHOSE AN CORRECT OPTION ======")
        player = int(input("Chose: 1.Rock - 2.Paper - 3.Scissors => "))
        
    # PC Random number of options
    pc = random.choice(options)
    
    # assign name of Player and PC option for label
    if(player==1):
        plynm = "Rock"
    elif(player==2):
        plynm = "Paper"
    else:
        plynm = "Scissors"
    if(pc==1):
        pcnm = "Rock"
    elif(pc==2):
        pcnm = "Paper"
    else:
        pcnm = "Scissors"

    # Round RESULTS
    print(f"\n\tPlayer:   VS   PC: \n\t{plynm}      {pcnm}")
    if(pc == player):
        print("\tTIE :O\n")
    elif(player == 1):
        if(pc == 2):
            print("\tPC WIN :(\n")
            pcwin +=1
        elif(pc == 3):
            print("\tYOUUU WIIIINNNNNN!!! :D\n")
            plwin +=1
    elif(player == 2):
        if(pc == 1):
            print("YOUUU WIIIINNNNNN!!! :D\n")
            plwin +=1
        elif(pc == 3):
            print("\tPC WIN :(\n")
            pcwin +=1
    elif(player == 3):
        if(pc == 2):
            print("\tYOUUU WIIIINNNNNN!!! :D\n")
            plwin +=1
        elif(pc == 1):
            print("\tPC WIN :(\n")
            pcwin +=1
    else:
        print("\nHow do you get here? :v\n")

    # Partial total wins
    print(f"    ==== Player {plwin} VS PC {pcwin} ====")
    #Reset Player and PC options for the next round
    player = 0
    pc = 0
    round +=1

print(f"\n\n\t======= FINALLY =======\n\tPlayer {plwin} VS PC {pcwin}")
if(pcwin > plwin):
    print("\t:( \tPC WIN\t :(\n")
else:
    print("\t:D \tPLAYER WINNNNNNNNNNNNNN!!!!!!!!\t :D")