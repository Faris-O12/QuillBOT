"""
# Variables:
 1. PREFIX
 2. OWNERID
 3. REPO_LINK
 4. TOTAL_PRIVATE_COMMANDS_SLASH
 5. TOTAL_COMMANDS_SLASH
 6. HELP_COMMAND_TYPES
 7. INFO_COMMANDS
 8. UTILITY_COMMANDS
 9. MATH_COMMANDS
 10. QUESTIONMATH_COMMANDS
 11. RANDOM_COMMANDS
 12. TIME_COMMANDS
 13. MISC_COMMANDS
 14. MCSERVER_COMMANDS
 15. SCIENCE_COMMANDS
 16. ADMIN_COMMANDS
 17. CHESS_COMMANDS
 18. COLOR_COMMANDS
 19. CODE_COMMANDS
 20. DATA_COMMANDS
 21. ALL_COMMANDS
 22. SHORT_DESCRIPTION
 23. DESCRIPTION
 24. STOCKFISH_PATH
"""

PREFIX='/'
OWNERID=804233465293570068

COLOR_R=31
COLOR_G=64
COLOR_B=194

REPO_LINK="https://github.com/Faris-O12/QuillBOT"

TOTAL_PRIVATE_COMMANDS_SLASH=7
TOTAL_COMMANDS_SLASH=0
HELP_COMMAND_TYPES="""
- Info
- Utility
- Math
- Science
- QuestionMath
- Random
- Time
- Misc
- Color
- Chess
- Admin
- Code
- Data
- Total
- All
"""
INFO_COMMANDS="""
**1. prefix** : Displays the current prefix
**2. latency** estimation(Default: True) : Get the ping latency of the client. Estimation must be either 'True' or 'False'
"""
UTILITY_COMMANDS="""
**1. upload** file : Upload a file to chat
**2. myid** : Gives you your discord user id
**3. getid** user : Gets the user id of another user
**4. channelid** : Returns the current channel id
**5. serverid** : Returns the id of the current server
**6. pfp** user : Get a bigger picture of a user's profile picture
**7. servers** : Gives you how many servers the bot is in
"""
MATH_COMMANDS="""
**1. add** number1 number2 : Addition
**2. subtract** number1 number2 : Subtraction
**3. multiply** number1 number2 : Multiplication
**4. divide** number1 number2 : Division
**5. remainder** number1 number2 : Perform division and tell you the remainder
**6. sqroot** number : Square root of number
**7. square** number : Square of number
**8. curoot** number : Cube root of number
**9. cube** number : Cube of number
**10. hypotenuse** (or 'hyp') leg1 leg2 : Hypotenuse of a right triangle
**11. evaluate** (or 'eval') equation : Evaluate an equation
**12. constant** name : Gives you the number of any constant, it can be: pi, e, tau
**13. exponent** base exponent : Finds the exponent for base
**14. root** number rootnumber : Finds the root of number, the power of the root is the 'rootnumber'
**15. percentage** numerator denominator : Gets the percentage of the numerator with the deneominator
**16. average** numbers : Find the arithimetic mean of the numbers, seperate the numbers with commas
**17. increase** value increase% : Find how much the value increased with the increase percentage
**18. decrease** value decrease% : Find how much the value decreases with the decrease percentage
**19. diagonals** sides : Find the amount of diagonals a poligon can have, given its sides
**20. factorial** number : Find the factorial of any number
**21. lcm** numbers : Find the least common multiply of the numbers
"""
QUESTIONMATH_COMMANDS="""
**1. question_add** time(Default : 10) : Gives you a random addition question
**2. question_subtract** time(Default : 10) : Gives you a random subtraction question
**3. question_multiply** time(Default : 10) : Gives you a random multiplication question
**4. question_divide** time(Default : 10) : Gives you a random division question
"""
RANDOM_COMMANDS="""
**1. randint** number1 number2 : Gives a random number between number1 and number2
**2. randoption** options : Input in text seperated by commas, the bot will choose one of the options randomly
"""
TIME_COMMANDS="""
**1. utc** (or 'utc') : Current UTC time
"""
MISC_COMMANDS="""
**1. embed** "title" "text" : Sends a embed with your title and text
**2. 8ball** (or 'Fortune') question : Ask 8ball a question
**4. backward** message : Gives back message in backwards
**5. cipher** shift text : Ceaser cipher text with the shift
**6. rps** choice(rock, paper, scissor) : Play rock paper scissors with the bot
**7. wikisearch** link (or title) : Sends an embed about the summary of the topic
**8. coinflip** : Have a half chance of getting heads or tails
"""
MCSERVER_COMMANDS="""
**1. server_start** server : Insert the name of the server for the bot to start the minecraft server
**2. server_playerlist** server : Get the amount of players in a server
**3. server_status** server : Tell the status of the server (eg. online, offline, loading etc.)
"""
SCIENCE_COMMANDS="""
**1. elementsymbol** symbol : Returns the name of the element if given its symbol
**2. elementname** name : Returns the symbol of the element if given its name
**3. elementnumber** number : Returns the name of the element given its atomic number
**4. periodic_table** : Gives you the periodic table
**5. cell_organelles** name : A small paragraph about the specified organelle
"""
ADMIN_COMMANDS="""
**1. kick** user : Kicks the user from the current server
**2. ban** user : Bans the user from the current server
"""
CHESS_COMMANDS="""
**1. bestmove** fen : Find the best move of a position with its FEN
"""
COLOR_COMMANDS="""
**1. rgb** r g b : Numbers can only be between 0 - 255
**2. randomcolor** : Return a random color
"""
CODE_COMMANDS="""
**1. code** filename description code : Display your code in an embed
"""
DATA_COMMANDS="""
**__Note:__** Amount of Y data should be equal to the X data
**1. line_graph** name vertical_name horizontal_name vertical_objects horizontal_objects : Create a line graph with your inputted data
**2. bar_graph** name vertical_name horizontal_name vertical_objects horizontal_objects : Create a bar graph with your inputter data
**3. pie_chart** name values labels : Create a pie chart with the inputter values and the corrosponding labels
"""
ALL_COMMANDS=f"""
**● Info**
```{INFO_COMMANDS.replace("**", "")}```
**● Utility**
```{UTILITY_COMMANDS.replace("**", "")}```
**● Math**
```{MATH_COMMANDS.replace("**", "")}```
**● QuestionMath**
```{QUESTIONMATH_COMMANDS.replace("**", "")}```
**● Random**
```{RANDOM_COMMANDS.replace("**", "")}```
**● Time**
```{TIME_COMMANDS.replace("**", "")}```
**● Misc**
```{MISC_COMMANDS.replace("**", "")}```
**● Science**
```{SCIENCE_COMMANDS.replace("**", "")}```
**● Admin**
```{ADMIN_COMMANDS.replace("**", "")}```
**● Chess**
```{CHESS_COMMANDS.replace("**", "")}```
**● Color**
```{COLOR_COMMANDS.replace("**", "")}```
**● Code**
```{CODE_COMMANDS.replace("**", "")}```
"""

SHORT_DESCRIPTION="Personal discord bot made by Faris#5260"
DESCRIPTION=f"""
Personal discord bot made by **Faris#5260**
Current Prefix:  **{PREFIX}**
Help command types: **{HELP_COMMAND_TYPES}**

**Bot statuses:**
● Online: If the bot is online, it means that the bot is functioning correctly
● Do not disturb: The bot is on, but commands wouldn't work at the time
● Idle: The bot is being programmed, commands might not work if the bot is restarting at the moment you run the command
● Offline: The bot is not online or being programmed

Use **/help** to get a list of every command
```
Usage: /help <type>
```
"""

STOCKFISH_PATH="G:\\QuillBOT\\stockfish_engine\\stockfish_15_x64_popcnt.exe"
