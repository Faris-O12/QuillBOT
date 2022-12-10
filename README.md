# **Quill.py**

*Made using discord.py*

#### Requirements to run:
- A `.env` file
- `TOKEN` variable holding your bot's token in the `.env` file
- `QUILL_PATH` variable holding the path of the folder in the `.env` file
- A `.stockfish_engine` folder with stockfish's engine

#### Libraries:
- discord       : **pip install discord**
- wikipediaapi  : **pip install wikipedia-api**
- stockfish     : **pip install stockfish**
- dotenv        : **pip install python-dotenv**
- numpy         : **pip install numpy**

## <u>Listeners</u>

- On ready (on_ready)
    - Runs when the bot starts running.
    - Clears the terminal and displays information.
- On resume (on_resume)
    - Runs when the bot resumes.
    - Does the same function as the On ready.
- On message (on_message)
    - Runs when a user messages in a server (or DM) the bot is in.
    - Checks whether the bot was pinged to give a short description about it.

## <u>Help command</u>

A command to give you the list of every command in the bot.

Syntax: `/help help_type`

You can run `/help` along with a type, the type can be of the following:

- `Info:` Commands to get information of the bot
- `Utility:` Commands that give you information of the user or a server the bot is in
- `Math:` Commands that performs a mathematical caculation
- `Science:` Commands that relate to biology, physics and chemistry
- `Time:` Commands that involve countdowns or UTC
- `Misc:` Commands that does not have a specified type
- `Random:` Commands that performs a random choice
- `QuestionMath:` Category of commands that gives you a math question
- `Admin:` Admin commands can only be run with permissions
- `Color:` Commands which returns color as an output
- `Chess:` Commands that involve stockfish analysing a chess position
- `Code:` Commands that involve programming or coding
- `Total:` Gives the total amount of commands

Depending on which type is chosen, the output would give you command of the specified catgory. If the input is not in these categories, it would return an embed with every command.