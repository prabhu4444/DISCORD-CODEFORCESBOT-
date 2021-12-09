# Discord Codeforces Bot
Discord Bot that enables users to fetch activity of fellow codeforces users as well as compete with each other.

#### Demonstration:

The commands the bot provides and their uses are as follows:

- .help
![image](https://user-images.githubusercontent.com/55255331/122050240-e8716700-ce00-11eb-89ca-74c0c2064065.png)
This command displays how to use the bot providing syntaxes for useful commands that the bot can act on.

- !stalk username
![image](https://user-images.githubusercontent.com/55255331/122050572-34241080-ce01-11eb-9757-09940727c9a0.png)
Displays latest solved/submitted 10 problems by the mentioned user that received an AC verdict.

- !lags username1 username2
![image](https://user-images.githubusercontent.com/55255331/122050787-75b4bb80-ce01-11eb-90c0-8ad0b34c3cf8.png)
Displays 10 problems user 2 has solved/submitted correctly that user user 1 hasn't.

- !hardest username
![image](https://user-images.githubusercontent.com/55255331/122050893-95e47a80-ce01-11eb-9151-b830c0a9114a.png)
Displays the 10 most difficult problems sbumitted by the mentioned user to receive an AC verdict.

- !challenge username1 username2 time 
The time can be given as 60 or 120 to initiate an hour long contest or a couple of hours. Provides a link on which both users must change their first names to a randomly generated string, once the names have been changed the contest initiates providing both users with the same 3 problems from Codeforces. It declares the winner after the contest duration has ended.
![image](https://user-images.githubusercontent.com/55255331/122064950-2d9c9580-ce0f-11eb-9049-18e4d440ded8.png)
It won't allow you to compete with yourself, nor to compete for any time interval other than 60 or 120 minutes. If the names aren't changed within 60 seconds, the contest won't start.
