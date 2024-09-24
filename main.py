player1 = input("Enter player 1 value: (r, p, s):").lower()
player2 = input("Enter player 2 value: (r, p, s):").lower()
winner = ""

if player1 == player2:
    print("Draw")
    winner = "both player 1 and 2"
elif player1 == "r" and player2 == "s":
    winner = "Player 1"
elif player1 == "p" and player2 == "r":
    winner = "Player 1"
elif player1 == "s" and player2 == "p":
    winner = "Player 1"
elif player2 == "r" and player1 == "s":
    winner = "Player 2"
elif player2 == "p" and player1 == "r":
    winner = "Player 2"
elif player2 == "s" and player1 == "p":
    winner = "Player 2"

print("The winner is ", winner)
