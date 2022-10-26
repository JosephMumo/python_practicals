import random
while True:
    option = input("please enter your option to play between rock, paper and scissors: ")
    option = option.lower()
    answer = random.choice(["rock", "paper", "scissors"])
    if option == "rock" and answer == "paper":
        print(f"Your choice was {option} and the computers choice was {answer}. You lost!!!")
        continue
    elif option == "rock" and answer == "scissors":
        print(f"Your choice was {option} and the computers choice was {answer}. you won!!!")
        continue
    elif option == "paper" and answer == "rock":
        print(f"Your choice was {option} and the computers choice was {answer}. you won!!!")
        continue
    elif option == "paper" and answer == "scissors":
        print(f"Your choice was {option} and the computers choice was {answer}. you lost!!!")
        continue
    elif option == "scissors" and answer == "rock":
        print(f"Your choice was {option} and the computers choice was {answer}. you lost!!!")
        continue
    elif option == answer:
        print(f"Your choice was {option} and the computers choice was {answer}. Fair please try again!!")
        continue
    elif option == "scissors" and answer == "paper":
        print(f"Your choice was {option} and the computers choice was {answer}. you won!!!")
        continue
    elif option == "exit":
        break
        
