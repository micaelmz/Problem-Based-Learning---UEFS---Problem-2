# The Problem
This is a fictional problem. The main objective of this one, is to create a text-based table game, using the concepts of matrices in Python. 

#### Note: the language of this program is Portuguese (pt-BR)

<br>

<img src="https://raw.githubusercontent.com/micaelmz/micaelmz/main/images/pbl2_image1.png"  width="500" />

<br>

## Basic Rules

This game is played by two players. The main purpose is to guess the sum of the columns or rows in the table, or at least, be the closest possible to the sum. The player who guesses right, or the player closer to the sum, wins the round. 

For example, there's a 4x4 table. If you want to guess the sum of line 1, you have to type line 1 and your move. The next player should do the same with their move.

If someone hits the sum, all the numbers in the row or column will be revealed. If nobody hits it, the closest to the value wins the round.

If the value of the move by the player winner was above the sum, the highest value in that row or column will be revealed. If they did a move below the sum, the lower value will be revealed.

## Points

For each number revealed by the player, it will count as one point for oneself.

If both hit or have the same approach, both will receive points.  

## Difficulty Levels

Easy: table 3x3, numbers generated between 1 and 30.

Medium: table 4x4, numbers generated between 1 and 60.

Hard: table 5x5, numbers generated between 1 and 100.

## How the game ends

The game will finish when the table is completely revealed, or when the round limit, set by the players, is reached.

At the end of the game, it will show a screen with the stats of the match and the name of the winner.

<img src="https://raw.githubusercontent.com/micaelmz/micaelmz/main/images/pbl2_image2.png"  width="500" />


### Goals proposed and achieved
- [x] A board game made by random numbers
- [x] Difficulty levels
- [ ] A board for each player
