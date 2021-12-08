## Table of contents
1. About the application
2. About the MVC Pattern
3. Required libraries, packages and modules 
4. The model
5. The View
6. The controller
7. The business logic
8. The database  
9. About the utils 
10. About the flake8 
11. Execution issue troubleshooting
### 1. About the application
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
the end of the tournament, the player get 4 points. At the end of the last round,
the application perform the final sort of players according their total score.
If two players haves the same total score then the rank of the last round is promoted.
The customer asked us to set the default rounds number to 4. When the last round 
is finished, the rank of each player is updated according the final sort of 
players by their total score. If at the end of the tournament the 8th player
get the higher total score then he become the 1st player and win the tournament.
If at the 3rd round, the 8th player get a higher total score than the 2nd player,
the 8th player become better ranked than the 2nd player. And if at the end of the
tournament the 8th player and the 2nd player get the same total score, the 8th
player will remain better ranked than the 2nd player because the 8th player got 
a higher total score than the 2nd player at the previous round.

When the tournament is finished. The application suggest a report to the user.
If the user want a report, the application will propose some information
to display from a tournament selected by the user. When the user choose which 
information to display from which tournament, the application will display
the information requested by the user and then stop running. Finally, if the
user doesn't want a report, the application will stop running. 
***
### 2. About the MVC Pattern
***
The MVC pattern is a software architecture model that was required for this
project. MVC stand for Model-View-Controller. An application that implement
the MVC pattern is more maintainable and bugs are easier to detect and fix.
On the next chapters of this README file, I will explain in more details 
each Part of the pattern(the model, the view and the controller). 
![alt text](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftechterms.com%2Fimg%2Flg%2Fmvc_1321.png&f=1&nofb=1)
***
### 3. Required libraries, packages and modules 
*** 
For this project, data generated by the application has to be stored in a
database. The database required by the customer is TinyDB. During the 
development of the application, we found that other Database Management 
System may be more suitable for this project.
***
### 4. The model
***
As introduced earlier, the MVC pattern play a very important role in the 
maintainability of the code and the possibility to detect and fix bugs 
faster. The model is the part of the application that let to instantiate
the different objects of the program such as a tournament, players, rounds
or matches. 
***
### 5. The View 
***
The view is the part of the application that is responsible to interact with
the user. The view display information to the user and collect data communicated
by the user. Next, the view notify to the controller, the data collected 
from the user and the controller updates information to the model that will
store this information to the database.
***
### 6. The controller
*** 
The controller is responsible to ensure that the application run properly.
This is the controller that implement every algorithm(from methods) 
responsible for the progress of the tournament(such as create the next round,
cumulate scores of players, generate matches....etc.).
***
### 7. The business logic
***
The business logic is the part of the application that deal with specific
end user's requirement. The business logic can be seen as the 
business/domain knowledge. In other words, the industry for which we are
developing an application(healthcare, finance, sport, energy....etc.). 

The match service is responsible to implement the swiss tournament system
for generating matches(each player plays with a player that have the 
same level as him/her). 

The player service is responsible to register score of players and 
accumulate them. The player service is also responsible to sort 
players by their score/rank and update rank at the end of the tournament.

The tournament service is responsible to create rounds and to make sure
that two players never meet twice in the tournament. This is also at the
tournament service level that the tournament is saved in the database 
when it is finished.

The report service is responsible to generate a report when the user 
request it.
***
### 8. The database 
*** 
The database consist of 4 tables. There is the tournament table, the round
table, the match table and the player table. As the name indicate it, the 
tournament table stores tournaments, the round table stores rounds, the match
table stores matches and the player's table stores players. Each table is
attached together. To store a match, you should first store two players,
to store a round, you should store matches, to store a tournament, you should
store rounds and players. Each object depend on each other and should always
be stored together. And each object, to be stored, need to be serialized first.
Each object need to be deserialized, if we want to load them back while
generating a report. The serialization is the process of converting an object
into a dictionary. Conversely, the deserialization is the process of 
converting a dictionary into an object. Consequently, the tournament serializer
serialize and deserialize tournaments objects, round serializer serialize and
deserialize rounds and so on. By the same way, to serialize a match, you should
first serialize two players, to serialize a round, you should first serialize
matches and so on. 
***
### 9. About the utils 
***
The utils package store constant variables and functions that does not deal
with business logic but that are necessary for a proper running of the 
application.
***
### 10. About the flake8
***
In order to make sure that the application respect the PEP8 convention. I 
installed flake8-html library in order to generate reports that certify 
that the application respect python conventions. In order to reformat
each python files of the application, I installed the black library. First, 
I used black to reformat each python file and then, I asked flake8-html
to generate a report that certify that each python file respect the PEP8
convention. 

I voluntarily decided to organize reports by directory. Because I consider
this way cleaner. For each directory, I blacked every file, I generate 
reports(using flake8-html) with them. Each directory of the application
has a flake8-html report directory. And each flake8-html report directory
are in the flake8_report directory. 
***
### 11. Execution issue troubleshooting 
***
In order to run the application, you will have to run it on the terminal.
The syntax for running the application is the following: 
python3 chess_tournament.py. While trying to run the application, you
may meet some trouble. This trouble is "fatal: No such file or directory:
../database/db.json". db.json is the database of the application. If you 
face this issue, go to the config file in the utils directory. Change the
DATABASE_NAME = "../database/db.json" to "./database/db.json". If it does
not fix the issue try ===> "db.json". 

Another issue you may face, you can get a ModuleNotFoundError while running
the application. To fix this issue, export the absolute path to the project.
Type the following command on the terminal: export PYTHONPATH="${PYTHONPATH}:
/path/to/the/directory". The directory is the entire project(the application itself).