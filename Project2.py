#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.mylastmove = my_move
        self.enemylastmove = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class RockPlayer(Player):
    def move(self):
        return 'rock'


class HumanPlayer(Player):
    def move(self):
        while True:
            Humanmove = input("Your move: ").lower()
            if Humanmove == "rock":
                return "rock"
            elif Humanmove == "scissors":
                return "scissors"
            elif Humanmove == "paper":
                return "paper"
            else:
                print("Please enter a valid move!")


class CyclePlayer(Player):
    def __init__(self):
        self.mylastmove = 'scissors'
        self.score = 0

    def move(self):
        if self.mylastmove == 'rock':
            return "paper"
        elif self.mylastmove == 'paper':
            return "scissors"
        elif self.mylastmove == 'scissors':
            return "rock"
        else:
            return "rock"


class ReflectPlayer(Player):
    def __init__(self):
        self.enemylastmove = random.choice(moves)
        self.score = 0

    def move(self):
        if self.enemylastmove == 'rock':
            return "rock"
        elif self.enemylastmove == 'paper':
            return 'paper'
        elif self.enemylastmove == 'scissors':
            return 'scissors'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.p1.score += 1
            score1 = self.p1.score
            score2 = self.p2.score
            print("Player 1 beats Player2\n")
            print(f"\nYour score: {score1} player2 score: {score2}")
        elif beats(move2, move1):
            self.p2.score += 1
            score1 = self.p1.score
            score2 = self.p2.score
            print("player 2 beats player1\n")
            print(f"\nYour score: {score1} player2 score: {score2}")
        else:
            print("It's a DRAW\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

        # Showing the winner
        if self.p1.score > self.p2.score:
            print("You are the WINNER!")
        elif self.p2.score > self.p1.score:
            print("Player2 is the WINNER!")
        else:
            print("No one won!")


if __name__ == '__main__':
    while True:
        playerinput = input(
        """\nWelcome to Rock Paper Scissors game
Plaese enter the type of player you want to play against
(rocky, random, cycle or reflect): """).lower()
        if playerinput == "random":
            game = Game(HumanPlayer(), RandomPlayer())
            break
        elif playerinput == "cycle":
            game = Game(HumanPlayer(), CyclePlayer())
            break
        elif playerinput == "reflect":
            game = Game(HumanPlayer(), ReflectPlayer())
            break
        elif playerinput == "rocky":
            game = Game(HumanPlayer(), RockPlayer())
            break
        else:
            print("\nPlease enter a valid player type")


game.play_game()
