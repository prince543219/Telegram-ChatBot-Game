# Telegram-ChatBot-Game
A rock-paper-scissors game based on Telegram's ChatBot.

- Content: 
  There are five games in one round. User and Bot will receive five cards in each game.
  Then users and Bot need to play five games with their five cards.
- Mehthod: Use Telegram's API to implement this project.

- Flow: start > choose (play > justice)
  - start: Shuffle the cards and deal cards to Bot and user.
  - choose: Appear the five buttons that user can choose one of it to play the cards.
  - play: The strategy that how bot beat user.
  - justice: Show the result of each game.
  
- How to get your token?
  1. open your Telegram, add "BotFather"
  2. type "/start", it will show you all the functions and commands
  3. type "/newbot", it will ask you to name your bot
  4. enter your bot's name
  5. enter your bot's username,  with the rule that its name ended with "bot"
  6. BotFather will show an unique token to you (Don't tell anyone the string)