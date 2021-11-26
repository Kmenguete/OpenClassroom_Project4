## Table of contents
1. About the application
2. About the MVC Pattern
3. Required libraries, packages and modules 
4. The model
5. The View
6. The controller
7. The business logic
8. The database and the report 
9. About the utils 
## 1. About the application
***
The application is a chess tournament management system that aim to play
a chess tournament. The goal is not to play chess but to manage chess matches
in the real life. In other word, the application is not a chess game. The 
application is a system that let the user register the score of players when
a chess match is finished. In the application, we implement the swiss 
tournament system. The swiss tournament system is a system where each player
plays with a player that has the same level as him. Furthermore, two players
should never meet each other twice during a tournament. 

When the application start, we first ask the user to create a tournament by
entering the name of the tournament, the place of the tournament and an 
optional description for this tournament.

Once a tournament is created, we ask the user to enter the firstname and 
lastname of players. The default players number is set to 8. Thus, the user
should register 8 players. The default rank of players is determined by
the order in which the players were created. For the business logic of the
tournament, the default rank play an important role. 

Once players have been created, the application create the first round with
matches. When a chess match is finished, the user register the score of each 
player in the system. In a chess match, the winner get 1 point and the loser
get 0 point. If there is no winner, each player get 0.5 point. When the user
finished registering the score for each chess match the application sort players
by their score(if two players have the same score, then the rank is promoted) 
and create the next round and matches for the next round. For this next round,
the user repeat the process of the first round(registering the score of each
player in each match). After that players are sorted by their score, the third 
round and the third round's matches are created and the user repeat the process again.
The process is repeated until the last round. 

During the progress of the tournament the score of each player is accumulated.
If in a tournament there is 4 rounds and a player win every match, then, at 
the end of the tournament, the player get 4 points. At the end of the last round.
The application perform the final sort of players according their total score.
If two players haves the same total score then the rank of the last round is promoted.
The customer asked us to set the default rounds number to 4.
