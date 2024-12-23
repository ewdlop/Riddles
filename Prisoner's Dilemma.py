import random

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.score = 0

    def choose_action(self):
        if self.strategy == "cooperate":
            return "C"
        elif self.strategy == "betray":
            return "B"
        elif self.strategy == "random":
            return random.choice(["C", "B"])

def play_round(player1, player2):
    action1 = player1.choose_action()
    action2 = player2.choose_action()

    if action1 == "C" and action2 == "C":
        player1.score += 3
        player2.score += 3
    elif action1 == "C" and action2 == "B":
        player1.score += 0
        player2.score += 5
    elif action1 == "B" and action2 == "C":
        player1.score += 5
        player2.score += 0
    elif action1 == "B" and action2 == "B":
        player1.score += 1
        player2.score += 1

    return action1, action2

def main():
    # Define players with different strategies
    player1 = Player(strategy="cooperate")
    player2 = Player(strategy="random")

    rounds = 10
    for _ in range(rounds):
        action1, action2 = play_round(player1, player2)
        print(f"Player 1 chose {action1}, Player 2 chose {action2}")
        print(f"Scores: Player 1: {player1.score}, Player 2: {player2.score}\n")

    print("Final Scores:")
    print(f"Player 1: {player1.score}")
    print(f"Player 2: {player2.score}")

if __name__ == "__main__":
    main()
