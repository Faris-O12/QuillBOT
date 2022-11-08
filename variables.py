PREFIX='/'
OWNERID=804233465293570068
TOKEN="MTAyMjgwNTM5NDQwNzU1NTExNQ.GG32ym.vpEm27Lk0CUuJB2gHbycKlyjNU8KClDNrQhFk4"
DEVELOPER_PORTAL="https://discord.com/developers/applications/1022805394407555115/"

TOTAL_PRIVATE_COMMANDS_SLASH:int=4
TOTAL_COMMANDS_SLASH:int=0
HELP_COMMAND_TYPES="Info, Utility, Math, Science, QuestionMath, Random, Time, Misc, Admin, Total"
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
**6. avatar** user : Get a bigger picture of a user's profile picture
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
**12. pi** : Gives you the number PI
**13. exponent** base exponent : Finds the exponent for base
**14. root** number rootnumber : Finds the root of number, the power of the root is the 'rootnumber'
**15. percentage** numerator denominator : Gets the percentage of the numerator with the deneominator
**16. average** numbers : Find the arithimetic mean of the numbers, seperate the numbers with commas
**17. increase** value increase% : Find how much the value increased with the increase percentage
**18. decrease** value decrease% : Find how much the value decreases with the decrease percentage
**19. diagonals** sides : Find the amount of diagonals a poligon can have, given its sides
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
**1. countdown** time type(s: seconds, m: minutes, h: hours) : Countdown form a specific time
**2. utc** (or 'utc') : Current UTC time
"""
MISC_COMMANDS="""
**1. embed** "title" "text" : Sends a embed with your title and text
**2. 8ball** (or 'Fortune') question : Ask 8ball a question
**4. backward** message : Gives back message in backwards
**5. cipher** shift text : Ceaser cipher text with the shift
**6. rps** choice(rock, paper, scissor) : Play rock paper scissors with the bot
**7. hash** password : Insert your password (secretly) and get the hashed version of it
**8. code** filename description code : Display your code in an embed
**9. wikisearch** link (or title) : Sends an embed about the summary of the topic
"""
MCSERVER_COMMANDS="""
**1. server_start** server : Insert the name of the server for the bot to start the minecraft server
**2. server_playerlist** server : Get the amount of players in a server
**3. server_status** server : Tell the status of the server (eg. online, offline, loading etc.)
"""
SCIENCE_COMMANDS="""
**1. element** symbol : Returns the name of the element if given its symbol
**2. elementsymbol** name : Returns the symbol of the element if given its name
**3. periodic_table** : Gives you the periodic table
**4. cell_organelles** name : A small paragraph about the specified organelle
"""
ADMIN_COMMANDS="""
**1. kick** user : Kicks the user from the current server
**2. ban** user : Bans the user from the current server
"""

SHORT_DESCRIPTION="Personal discord bot made by Faris#5260"
DESCRIPTION=f"""
Personal discord bot made by **Faris#5260**
Current Prefix:  **{PREFIX}**
Help command types: **{HELP_COMMAND_TYPES}**

Use **/help** to get a list of every command
```
Usage: /help <type>
```
"""