import random
i = 0
score = 0
while i<5:
    options = ["rock", "paper", "scissors"]
    computer= random.randint(0,2)
    comChoice = options[computer]
    player = raw_input("rock, paper, scissors,\n")
    if comChoice==player:
        print "tie"
    elif player == "rock" and comChoice=="paper" or player=="scissors" and comChoice=="rock" or player == "paper" and comChoice=="scissors":
        print "you lose"
        score = score - 1
    elif player == "rock" and comChoice=="scissors" or player=="scissors" and comChoice=="paper" or player == "paper" and comChoice=="rock":
        print "you win"
        score = score + 1
    i =i+1
print "i'm done actually. your score was ", score
    
            
            
        
    
            
    
