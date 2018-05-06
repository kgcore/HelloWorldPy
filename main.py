# import the modules
import sys
import random

ans = True

while ans:
    question = input("Ask the magic 10 ball a question:(press enter to quit)")
    
    answers = random.randint(1, 10)
    
    if question == "":
        sys.exit()
        
    elif answers == 1:
        print("It is certain")

    elif answers == 2:
        print("Outlook good")

    elif answers == 3:
        print("You may rely on it")

    elif answers == 4:
        print("Ask again later")
        
    elif answers == 5:
        print("Concentrate and ask again")
        
    elif answers == 6:
        print("Reply hazy, try again")
        
    elif answers == 7:
        print("My reply is no")
    
    elif answers == 8:
        print("No way dude not going to happen")
    
    elif answers == 9:
        print("No way dude not going to happen")
    
    elif answers == 10:
        print("You betcha")
    
