import random
def get_choices():
  while True:
    player_choice = input("enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    if player_choice in options:
      return choices
    else:
      print("pls choose from the three options given")
   


def check_win(player, computer):
    print(f"you choose {player}, computer choose {computer}")
    if player == computer:
     return "IT'S A TIE!"
    elif  player == "rock":
      if computer == "scissors":
        return "rock smashes scissors! YOU WIN"
      else:
        return "paper cover's rock! YOU LOOSE"
    elif  player == "paper":
      if computer == "rock":
        return "paper's cover rock! YOU WIN"
      else:
        return "scissors cut's paper! YOU LOOSE"
    elif  player == "scissors":
      if computer == "paper":
        return "scissors cut's paper! YOU WIN"
    else:
      return "paper cover's rock! YOU LOOSE"
    

choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)
