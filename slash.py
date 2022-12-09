"Personal discord bot by Faris#5260"

try:
    import variables
    import discord
    from discord import app_commands
    from discord.ext import commands
    import sys
    import os
    import datetime
    import math
    import random
    import string
    import webbrowser
    import wikipediaapi
    import asyncio
    from numpy import cbrt
    from stockfish import Stockfish
    from dotenv import load_dotenv
except ImportError as ImportImportError:
    print("Import Error: "+str(ImportImportError))

client = commands.Bot(
    command_prefix=variables.PREFIX,
    description=variables.SHORT_DESCRIPTION,
    case_insensitive=True,
    intents=discord.Intents.all(),
    owner_id=variables.OWNERID,
)

themeColor = discord.Color.from_rgb(31, 64, 194)
errorColor = discord.Color.red()

os.chdir(r"G:\\QuillBOT")
client.remove_command('help')

# Events
@client.event
async def on_ready():
    "Runs when the bot is ready"
    os.system("title Quill discord bot")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Launched ({variables.SHORT_DESCRIPTION})")
    print(f" - Launch time: {str(datetime.datetime.now()).split('.')[0]}")
    print(f" - User: {client.user}")
    print(f" - Latency: {client.latency * 1000}ms\n")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands\n")
        variables.TOTAL_COMMANDS_SLASH = int(len(synced) - variables.TOTAL_PRIVATE_COMMANDS_SLASH)
    except Exception as OnreadyGeneralError:
        print("Error: "+str(OnreadyGeneralError))

@client.event
async def on_resumed():
    "Runs when the bot resumes"
    os.system("title Quill discord bot")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Launched ({variables.SHORT_DESCRIPTION})")
    print(f" - Launch time: {str(datetime.datetime.now()).split('.')[0]}")
    print(f" - User: {client.user}")
    print(f" - Latency: {client.latency * 1000}ms\n")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands\n")
        variables.TOTAL_COMMANDS_SLASH = int(len(synced) - variables.TOTAL_PRIVATE_COMMANDS_SLASH)
    except Exception as OnresumeGeneralError:
        print("Error: "+str(OnresumeGeneralError))

@client.event
async def on_message(message):
    "Runs when a message is sent"
    if client.user.mentioned_in(message):
        await message.channel.send(embed=discord.Embed(
            title="Description",
            description=variables.DESCRIPTION,
            color=themeColor
        ))

@client.tree.command(name="help", description="List of every command")
@app_commands.describe(help_type="Type can be "+variables.HELP_COMMAND_TYPES)
async def help_command(ctx, *, help_type : str):
    "Help command"
    if help_type.lower() == "info":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Help commands__",
            description=variables.INFO_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "utility":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Utility__",
            description=variables.UTILITY_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "math":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Math__",
            description=variables.MATH_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "science":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Science__",
            description=variables.SCIENCE_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "time":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Time__",
            description=variables.TIME_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "misc":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Misc__",
            description=variables.MISC_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "random":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Random__",
            description=variables.RANDOM_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "questionmath":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Question math__",
            description=variables.QUESTIONMATH_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "admin":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Administrator__",
            description=variables.ADMIN_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "color" or help_type.lower() == "colour":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Color__",
            description=variables.COLOR_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "chess":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Chess__",
            description=variables.CHESS_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "code":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Code__",
            description=variables.CODE_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif help_type.lower() == "total":
        await ctx.response.send_message(embed=discord.Embed(
            title="Total number of commands",
            description=str(variables.TOTAL_COMMANDS_SLASH),
            color=themeColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title=f"__All Commands__",
            description=variables.ALL_COMMANDS,
            color=themeColor
        ), ephemeral=True)

"""Help"""
# Get the prefix of the bot
@client.tree.command(name="prefix", description="Get the current prefix")
async def prefix(ctx):
    "Return the current prefix"
    await ctx.response.send_message(
        f"The current prefix is: **{variables.PREFIX}**",
        ephemeral=True
    )

# Gets the link for an attachment
@client.tree.command(name="upload", description="Upload an image to recieve its url")
@app_commands.describe(attachment="Attach an image to discord")
async def upload(ctx, attachment: discord.Attachment):
    "Returns the link for an attachment"
    await ctx.response.send_message(f'Uploaded by **{ctx.user.name}** <{attachment.url}>')

# Get user's ID
@client.tree.command(name="myid", description="Get your unique user id")
async def myid(ctx):
    "Get the ID of the user running the command"
    await ctx.response.send_message(ctx.user.id, ephemeral=True)

# Get other's ID
@client.tree.command(name="getid", description="Get the unique user id")
@app_commands.describe(member="Insert any user in the server to get their id")
async def getid(ctx, member : discord.User):
    "Get the ID of any user"
    await ctx.response.send_message(member.id, ephemeral=True)

# Get channel id
@client.tree.command(name="channelid", description="Get the unique channel id")
async def channelid(ctx):
    "Get the ID of the channel the command is run on"
    await ctx.response.send_message(ctx.channel.id, ephemeral=True)

# Get guild id
@client.tree.command(name="serverid", description="Get the unique server id")
async def serverid(ctx):
    "Get the ID of the server the command is run on"
    await ctx.response.send_message(ctx.guild.id, ephemeral=True)

# Get the servers the bot is currently in
@client.tree.command(name="servers", description="Return the number of servers the bot is in")
async def servers(ctx):
    "Get the number of servers the bot is in"
    await ctx.response.send_message(embed=discord.Embed(
        description="**Number of server the bot is in: **"+str(len(client.guilds)),
        color=themeColor
    ), ephemeral=True)

# Get a user's Profile picture
@client.tree.command(name="pfp", description="Give an enlarged image of a user's profile picture")
@app_commands.describe(user="User you want to get the profile picture of")
async def pfp(ctx, user : discord.Member):
    "Get the Profile picture of any user"
    await ctx.response.send_message(user.avatar)

# Stop the bot
@client.tree.command(name="__stop", description="Owner command")
async def __stop(ctx):
    "Stop the bot"
    if ctx.user.id == client.owner_id:
        print("Stopped")
        await ctx.response.send_message("__Stopped__", ephemeral=True)
        await client.change_presence(status=discord.Status.dnd)
        await client.close()
    else:
        await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description="You do now have permissions to shut down the bot",
            colour=errorColor
        ), ephemeral=True)

# Restart the bot
@client.tree.command(name="__restart", description="Owner command")
async def __restart(ctx):
    "Restart the bot"
    if ctx.user.id == client.owner_id:
        print("Restarting...")
        await ctx.response.send_message("__Restarted__", ephemeral=True)
        await client.change_presence(status=discord.Status.dnd)
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description="You do now have permissions to shut down the bot",
            colour=errorColor
        ), ephemeral=True)

# Get the bot ping
@client.tree.command(name="latency", description="Returns the bot latency")
@app_commands.describe(estimation="Whether the number should be estimated or not (Default true)")
async def latency(ctx, estimation : str = "true"):
    "Returns the latency of the client"
    if estimation.lower() == "false":
        await ctx.response.send_message(f"Bot latency: **{client.latency*1000}ms**")
    elif estimation.lower() == "true":
        await ctx.response.send_message(f"Bot latency (estimated): **{int(client.latency*1000)}ms**")

"""Randoms"""
# Random int between a and b
@client.tree.command(name="randint", description="Choose a random number between the two numbers that were provided")
@app_commands.describe(number1="First number", number2="Second number")
async def randint(ctx, number1 : int, number2 : int):
    "Return a random number between two numbers"
    await ctx.response.send_message(f"Random number from {str(number1)} to {str(number2)}: **{random.randint(number1, number2)}**")

# Random option between a list
@client.tree.command(name="randoption", description="Input in your choices (Seperate with commas)")
@app_commands.describe(options="Your list of options")
async def randoption(ctx, *, options : str):
    "Return a random option froma list"
    await ctx.response.send_message(random.choice(options.split(",")))

"""Math"""
# Add 'A' and 'B'
@client.tree.command(name="add", description="Add the two provided numbers")
@app_commands.describe(number1="First number", number2="Second number")
async def add(ctx, number1: float, number2: float):
    "Add two numbers"
    if number1 > 1000000 or number2 > 1000000:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Any number cannot be higher than 1000000",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(f"**{number1} + {number2}**: __**{math.fsum([number1, number2])}**__")

# Multiply 'A' and 'B'
@client.tree.command(name="multiply", description="Multiply the two provided numbers")
@app_commands.describe(number1="First number", number2="Second number")
async def multiply(ctx, number1: float, number2: float):
    "Multiply two numbers"
    if number2 > 1000000 or number2 > 1000000:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Any number cannot be higher than 1000000",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(f"**{number1} × {number2}**: __**{number1 * number2}**__")

# Divide 'A' and 'B'
@client.tree.command(name="divide", description="Divide the two provided numbers")
@app_commands.describe(number1="First number", number2="Second number")
async def divide(ctx, number1: float, number2: float):
    "Divide two numbers"
    if number1 == 0 or number2 == 0:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Any number cannot contain zero",
            colour=errorColor
        ), ephemeral=True)
    elif number1 > 1000000 or number2 > 1000000:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Any number cannot be higher than 1000000",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(f"**{number1} ÷ {number2}**: __**{number1 / number2}**__")

# Subtract 'A' from 'B'
@client.tree.command(name="subtract", description="Subtract the two provided numbers")
@app_commands.describe(number1="First number", number2="Second number")
async def subtract(ctx, number1: float, number2: float):
    "Subtract two numbers"
    if number1 > 1000000 or number2 > 1000000:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Any number cannot be higher than 1000000",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(f"**{number1} - {number2}**: __**{number1 - number2}**__")

# Find the remainder between 'A' and 'B'
@client.tree.command(name="remainder", description="Find the remainder between the two numbers when divided")
@app_commands.describe(number1="First number", number2="Second number")
async def remainder(ctx, number1 : float, number2 : float):
    "Remainder of two numbers"
    if number1 == 0 or number2 == 0:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Any number cannot be zero",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(f"**{number1} ÷ {number2}** remainder: __**{number1 % number2}**__")

# Get the square root of a number
@client.tree.command(name="sqroot", description="Find the square root of any number")
@app_commands.describe(number="Number you want to find the square root of")
async def sqroot(ctx, number : float):
    "Find the square root of a number"
    if number == float(1):
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Square root of 1 is not possible",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(str(math.sqrt(number)))

# Get the square of a number
@client.tree.command(name="square", description="Square of the provided number")
@app_commands.describe(number="Number you want to find the square of")
async def square(ctx, number : float):
    "Find the square of a number"
    await ctx.response.send_message(str(number * number))

# Get the cube root of a number
@client.tree.command(name="curoot", description="Find the cube root of any number")
@app_commands.describe(number="Number you want to find the cube root of")
async def curoot(ctx, number : float):
    "Find the cube root of a number"
    if number == float(1):
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Cube root of 1 is not possible",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(cbrt(number))

# Get the cube of a number
@client.tree.command(name="cube", description="Cube the provided number")
@app_commands.describe(number="Number you want to find the cube of")
async def cube(ctx, number : float):
    "Find the cube of a number"
    await ctx.response.send_message(str(number ** 3))

# Get the pythagorean triplet for 'A' and 'B'
@client.tree.command(name="hypotenuse", description="Use the pythagorean thereom to find the hypotenuse of a right triangle")
@app_commands.describe(leg1="First leg", leg2="Second leg")
async def hypotenuse(ctx, leg1 : float, leg2 : float):
    "Find the hypotenuse of a triangle"
    await ctx.response.send_message(f"{str(leg1)}² + {str(leg2)}² = x²\n{float(leg1) ** 2} + {float(leg2) ** 2} = x²\n{(float(leg1) ** 2) + (float(leg2) ** 2)} = x²\n__{math.sqrt((float(leg1) ** 2) + (float(leg2) ** 2))}__ = x")

# Evaluate an equation
@client.tree.command(name="evaluate", description="Evaluate the answer to your question")
@app_commands.describe(question="Multiplication is * and division is /")
async def evalute(ctx, *, question : str):
    "Evaluate an equation"
    try:
        question = question.replace(",","")
        answer = eval(question)
        await ctx.response.send_message(f"{question} = **__{answer}__**")
    except ZeroDivisionError:
        await ctx.response.send_message("Cannot divide with 0")
    except Exception as EvaluateGeneralError:
        await ctx.response.send_message("__Error__: "+EvaluateGeneralError)

# Exponenet a number with another number
@client.tree.command(name="exponent", description="Multiply the base by the amount of exponent")
@app_commands.describe(base="Base of the number", exponent="Exponent of the base")
async def exponent(ctx, base : int, exponent : int):
    "Get the exponent of base with the exponent"
    if exponent == 0 and base != 0:
        await ctx.response.send_message("1")
    elif exponent == 0 and base == 0:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="You cannot have a number with its base and exponent as 0",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(str(base ** exponent))

# Get the root of a number with the specified root
@client.tree.command(name="root", description="Root the number to the number")
@app_commands.describe(number="Number you want to find the root of", root="Power of the root")
async def root(ctx, number : int, root : int):
    "Root the number"
    if root < 2:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="The root number must be atleast over 1",
            colour=errorColor
        ), ephemeral=True)
    elif number == 1:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Number cannot be 1",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(str(number ** (1 / root)))

# Get the value of any constant
@client.tree.command(name="pi", description="Give you back the number pi")
async def constant(ctx, name : str):
    "Return the number of any constant"
    if name.lower() == "pi":
        await ctx.response.send_message(math.pi)
    elif name.lower() == "e":
        await ctx.response.send_message(math.e)
    elif name.lower() == "tau":
        await ctx.response.send_message(math.tau)
    else:
        await ctx.response.send_message(embed=discord.Embed(
                title="**__Error__ ❌**",
                description="Mathematical constants: pi, e, tau",
                colour=errorColor
            ), ephemeral=True)

# Get the percentage between numerator and denominator
@client.tree.command(name="percentage", description="Find the percentage of any fraction")
@app_commands.describe(numerator="Numerator of the fraction", denominator="Denominator of the fraction")
async def percentage(ctx, numerator : int, denominator : int):
    "Find the percentage of a fraction"
    await ctx.response.send_message(f"Percentage of {str(numerator)} / {str(denominator)} : **{str((numerator / denominator) * 100)}%**")

# Get the average value from a list
@client.tree.command(name="average", description="Find the average value of the numbers")
@app_commands.describe(numbers="Seperate the numbers with commas")
async def average(ctx, numbers : str):
    "Find the average of the list of numbers"
    numbers = numbers.replace(" ", "")
    numbers = numbers.split(",")
    numlist = list(map(int, numbers))
    await ctx.response.send_message(sum(numlist) / len(numlist))

# Get the increase percentange of any number
@client.tree.command(name="increase", description="Find the increase percentage of any number")
@app_commands.describe(number="The initial value", increase="The increase percentage")
async def increase(ctx, number : int, increase : int):
    "Find increase percentage given the number and the increase"
    await ctx.response.send_message(number + (number * increase / 100))

# Get the descrease percentage of any number
@client.tree.command(name="decrease", description="Find the decrease percentage of any number")
@app_commands.describe(number="The initial value", decrease="The decrease percentage")
async def decrease(ctx, number : int, decrease : int):
    "Find the decrease percentage given the number and the decrease"
    await ctx.response.send_message(number - (number * decrease / 100))

# Find the amount of diagonals a polygon has
@client.tree.command(name="diagonals", description="Find the amount of diagonals a polygon has")
@app_commands.describe(sides="The amount of sides the polygon has")
async def diagonals(ctx, sides : int):
    "Find the number of diagonals in a polygon"
    if sides == 2 or sides == 1 or sides <= 0:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description=f"There cannot be a polygon with {str(sides)} sides",
            colour=errorColor
        ), ephemeral=True)
    else:
        try:
            await ctx.response.send_message(str((sides * (sides - 3)) / 2))
        except Exception as DiagonalsGeneralError:
            await ctx.response.send_message(embed=discord.Embed(
                title="**__Error__ ❌**",
                description=DiagonalsGeneralError,
                colour=errorColor
            ), ephemeral=True)

@client.tree.command(name="factorial", description="Find the factorial of any number")
async def factorial(ctx, number : int):
    "Find the factorial of any number"
    try:
        await ctx.response.send_message(f"Factorial of **{number}** is **{math.factorial(number)}**")
    except ValuError:
        await ctx.response.send_message(embed=discord.Embed(
                title="**__Error__ ❌**",
                description="Value has to be an integral and cannot be a negative number",
                colour=errorColor
            ), ephemeral=True)

"""Question math"""
# Ask an addition question
@client.tree.command(name="question_add", description="Ask you an addition question")
async def question_add(ctx):
    "Ask a random addition question"
    num1 = random.randrange(10, 1000)
    num2 = random.randrange(10, 1000)
    await ctx.response.send_message(f"{str(num1)} + {str(num2)} = ||{str(num1 + num2)}||")

# Ask a subtraction question
@client.tree.command(name="question_subtract", description="Ask you a subtract question")
async def question_subtract(ctx):
    "Ask a random subtraction question"
    num1 = random.randrange(10, 1000)
    num2 = random.randrange(10, 1000)
    await ctx.response.send_message(f"{str(num1)} - {str(num2)} = ||{str(num1 - num2)}||")

# Ask a multiplication question
@client.tree.command(name="question_multiply", description="Ask you a multiplication question")
async def question_multiply(ctx):
    "Ask a random multiplication question"
    num1 = random.randrange(10, 1000)
    num2 = random.randrange(10, 1000)
    await ctx.response.send_message(f"{str(num1)} x {str(num2)} = ||{str(num1 * num2)}||")

# Ask a division question
@client.tree.command(name="question_divide", description="Ask you a division question")
@commands.cooldown(1, 1, commands.BucketType.user)
async def question_divide(ctx):
    "Ask a random division question"
    num1 = random.randrange(10, 1000)
    num2 = random.randrange(10, 1000)
    await ctx.response.send_message(f"{str(num1)} / {str(num2)} = ||{str(num1 / num2)}||")

"""Time"""
# Get the current UTC time
@client.tree.command(name="utc", description="Give you the current UTC time")
async def utc(ctx):
    "Return the current UTC time"
    await ctx.response.send_message("**UTC Time now: **"+str(str(str(datetime.datetime.utcnow()).split(".")[0]).split(" ")[1]).replace(":", " "))

"""Misc"""
# Embed a message
@client.tree.command(name="embed", description="Embed a message")
@app_commands.describe(title="Title of the embed", text="Body of the embed")
async def embed(ctx, title : str, text : str):
    "Make an embed"
    text = text.replace(";", "\n")
    await ctx.response.send_message(embed=discord.Embed(description=":white_check_mark: Embed sent", colour=themeColor), ephemeral = True)
    await ctx.channel.send(embed=discord.Embed(
        title="By "+ctx.user.name+", "+"__"+title+"__",
        description=text,
        color=themeColor
    ))

# A fun 8Ball command
@client.tree.command(name="8ball", description="Ask the magical 8 Ball any question to see its reponse")
@app_commands.describe(question="Question that you will ask")
async def Fortune(ctx,*,question : str):
    "Ask 8Ball a question"
    try:
        responses =["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Yes.",
                    "No",
                    "Signs point to yes.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Very doubtful."]
        if question is None:
            await ctx.response.send_message("Ask the magic orb something, and understand your future")
        else:
            await ctx.response.send_message(f'Hmmm, My magic orb says ,*"{random.choice(responses)}"*')
    except Exception:
        await ctx.response.send_message('Oh no! My orb just broke! Meet me after I fix it.')

# Sends the inputted message backwards
@client.tree.command(name="backward", description="Returns the inputted text backwards")
@app_commands.describe(text="Text that will be returned backwards")
async def backward(ctx, *, text : str):
    "Return the inputted text backwards"
    await ctx.response.send_message(text[::-1])

# Plays rock paper scissors with you
@client.tree.command(name="rps", description="Play rock, papers, scissor against the bot")
@app_commands.describe(choice="Your choice (Rock, Paper, Scissor)")
async def rps(ctx, *, choice : str):
    "Play Rock, paper, scissors against the bot"
    BChoices = ["rock", "paper", "scissors"]
    choice = choice.lower()
    botChoice = random.choice(BChoices)
    if choice == "rock":
        if botChoice == "rock":
            await ctx.response.send_message("Bot chose rock! **Draw!**")
        elif botChoice == "paper":
            await ctx.response.send_message("Bot chose paper! **You lose**")
        elif botChoice == "scissors":
            await ctx.response.send_message("Bot chose scissors! **You win!**")
    elif choice == "scissor" or choice == "scissors":
        if botChoice == "rock":
            await ctx.response.send_message("Bot chose rock! **You lose**")
        elif botChoice == "paper":
            await ctx.response.send_message("Bot chose paper! **You win!**")
        elif botChoice == "scissors":
            await ctx.response.send_message("Bot chose scissors! **Draw!**")
    elif choice == "paper":
        if botChoice == "rock":
            await ctx.response.send_message("Bot chose rock! **You win!**")
        elif botChoice == "paper":
            await ctx.response.send_message("Bot chose paper! **Draw!**")
        elif botChoice == "scissors":
            await ctx.response.send_message("Bot chose scissors! **You lose**")

# Ceaser cipher by a given shift
@client.tree.command(name="cipher", description="Use the ceaser cipher to encrypt the text")
@app_commands.describe(shift="Shift of the text", text="Text that will be shifted")
async def cipher(ctx, shift : int, *, text : str):
    "Cipher a message with the ceaser cipher"
    text = text.lower()
    shift %= 26
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypted = text.translate(table)
    await ctx.response.send_message(encrypted)

"""Code"""
# Display your code in an embed
@client.tree.command(name="code", description="Display your code in an embed")
@app_commands.describe(filename="Name of the file", description="Description of the code", code="The code")
async def code(ctx, filename : str, description : str, code : str):
    "Display a code in an embed"
    code = code.replace(";", "\n")
    description = description.replace(";", "\n")
    fileextension = ""
    try:
        fileextension = filename.split(".")[1]
        await ctx.response.send_message(embed=discord.Embed(
            title=filename,
            description=f"**Description**: {description}```{fileextension.lower()}\n{code}\n```",
            color=themeColor
        ))
    except Exception as IndexError:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description="File name is not valid: Syntax for 'filename' `name.extension`",
            colour=errorColor
        ), ephemeral=True)
        
# Search a topic on wikipedia
@client.tree.command(name="wikisearch", description="Seacrh wikipedia for a topic")
@app_commands.describe(topic="The topic you want to search for")
async def wikisearch(ctx, topic : str):
    "Search wikipedia for any topic"
    if topic.startswith("https://en"):
        topic = topic.replace("https://en.wikipedia.org/wiki/","")
    topic = topic.replace(" ", "_")

    wiki = wikipediaapi.Wikipedia('en')
    wikitopic = wiki.page(topic)
    if wikitopic.exists():
        await ctx.response.send_message(embed=discord.Embed(
            title=str(topic.capitalize()).replace("_", " "),
            description=f"**Link:** {wikitopic.fullurl}\n\n{wikitopic.summary}",
            colour=themeColor
        ))
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description=f"Topic **'{topic}'** does not exist",
            colour=errorColor
        ), ephemeral=True)

# Flip a coin
@client.tree.command(name="coinflip", description="Flip a cion and have equal chance of getting heads or tails")
async def coinflip(ctx):
    "Flip a coin"
    await ctx.response.send_message("The coin landed on **"+random.choice(["Tails", "Heads"])+"**")

"""Color"""
@client.tree.command(name="rgb", description="Show you the color you made with RGB")
@app_commands.describe(red="Red value", green="Green value", blue="Blue value")
async def rgb(ctx, red : int, green : int, blue : int):
    "Return an RGB color given the values"
    if red > 255 or green > 255 or blue > 255:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description="Values cannot be higher than 255",
            colour=errorColor
        ), ephemeral=True)
    elif red < 0 or green < 0 or blue < 0:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description="Values cannot be lower than 0",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title=f"Color from RGB __{red} {green} {blue}__",
            color=discord.Color.from_rgb(red, green, blue)
        ))

@client.tree.command(name="randomcolor", description="Return a random color")
async def randomcolor(ctx):
    "Return a random color"
    await ctx.response.send_message(embed=discord.Embed(
        description="Random color",
        color=discord.Color.random()
    ))

"""Administrator"""
# Kick a user
@client.tree.command(name="kick", description="Kick any user from the server")
@app_commands.describe(member="Member that will be kicked", reason="Reason on why the member is being kicked")
async def kick(ctx, member : discord.Member, *, reason : str = None):
    "Remove a user from the server"
    if ctx.user.guild_permissions.kick_members or ctx.user.id == client.owner_id:
        try:
            await member.kick(reason=reason)
            await ctx.response.send_message(embed=discord.Embed(
                title=f"{member.name}#{member.discriminator} is kicked",
                description="Reason: "+str(reason),
                colour=themeColor
            ))
        except Exception as KickGeneralError:
            await ctx.response.send_message(embed=discord.Embed(
                title="**__Error__ ❌**",
                description=KickGeneralError,
                colour=errorColor
            ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description="You do not have permissions to kick someone",
            colour=errorColor
        ), ephemeral=True)

# Ban a user
@client.tree.command(name="ban", description="Ban any user from the server")
@app_commands.describe(member="Member that is to be banned", reason="Reason on why the member is being banned")
async def ban(ctx, member : discord.Member, *, reason : str = None):
    "Ban a user from the server"
    if ctx.user.guild_permissions.ban_members or ctx.user.id == client.owner_id:
        try:
            await member.ban(reason=reason)
            await ctx.response.send_message(embed=discord.Embed(
                title=f"{member.name}#{member.discriminator} is Banned",
                description="Reason: "+str(reason),
                colour=themeColor
            ))
        except Exception as BanGeneralError:
            await ctx.response.send_message(embed=discord.Embed(
                title="**__Error__ ❌**",
                description=BanGeneralError,
                colour=errorColor
            ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description=f"You do not have permissions to ban someone",
            colour=errorColor
        ), ephemeral=True)

"""Science"""
# The periodic table input is symbol
@client.tree.command(name="elementsymbol", description="Input the symbol of any element to recieve its name")
@app_commands.describe(element="Symbol of the element")
async def elementsymbol(ctx, *, element : str):
    "Return the atomic number and name given the symbol"
    elem = element
    if elem == "H":
        await ctx.response.send_message(embed=discord.Embed(
            title="1. Hydrogen",
            color=themeColor
        ))
    elif elem == "He":
        await ctx.response.send_message(embed=discord.Embed(
            title="2. Helium",
            color=themeColor
        ))
    elif elem == "Li":
        await ctx.response.send_message(embed=discord.Embed(
            title="3. Lithium",
            color=themeColor
        ))
    elif elem == "Be":
        await ctx.response.send_message(embed=discord.Embed(
            title="4. Berylium",
            color=themeColor
        ))
    elif elem == "B":
        await ctx.response.send_message(embed=discord.Embed(
            title="5. Boron",
            color=themeColor
        ))
    elif elem == "C":
        await ctx.response.send_message(embed=discord.Embed(
            title="6. Carbon",
            color=themeColor
        ))
    elif elem == "N":
        await ctx.response.send_message(embed=discord.Embed(
            title="7. Nitrogen",
            color=themeColor
        ))
    elif elem == "O":
        await ctx.response.send_message(embed=discord.Embed(
            title="8. Oxygen",
            color=themeColor
        ))
    elif elem == "F":
        await ctx.response.send_message(embed=discord.Embed(
            title="9. Flourine",
            color=themeColor
        ))
    elif elem == "Ne":
        await ctx.response.send_message(embed=discord.Embed(
            title="10. Neon",
            color=themeColor
        ))
    elif elem == "Na":
        await ctx.response.send_message(embed=discord.Embed(
            title="11. Sodium",
            color=themeColor
        ))
    elif elem == "Mg":
        await ctx.response.send_message(embed=discord.Embed(
            title="12. Magnesium",
            color=themeColor
        ))
    elif elem == "Al":
        await ctx.response.send_message(embed=discord.Embed(
            title="13. Aluminium",
            color=themeColor
        ))
    elif elem == "Si":
        await ctx.response.send_message(embed=discord.Embed(
            title="14. Silicon",
            color=themeColor
        ))
    elif elem == "P":
        await ctx.response.send_message(embed=discord.Embed(
            title="15. Phosphorous",
            color=themeColor
        ))
    elif elem == "S":
        await ctx.response.send_message(embed=discord.Embed(
            title="16. Sulphur",
            color=themeColor
        ))
    elif elem == "Cl":
        await ctx.response.send_message(embed=discord.Embed(
            title="17. Chlorine",
            color=themeColor
        ))
    elif elem == "Ar":
        await ctx.response.send_message(embed=discord.Embed(
            title="18. Argon",
            color=themeColor
        ))
    elif elem == "K":
        await ctx.response.send_message(embed=discord.Embed(
            title="19. Potassium",
            color=themeColor
        ))
    elif elem == "Ca":
        await ctx.response.send_message(embed=discord.Embed(
            title="20. Calcium",
            color=themeColor
        ))
    elif elem == "Sc":
        await ctx.response.send_message(embed=discord.Embed(
            title="21. Scandium",
            color=themeColor
        ))
    elif elem == "Ti":
        await ctx.response.send_message(embed=discord.Embed(
            title="22. Titanium",
            color=themeColor
        ))
    elif elem == "V":
        await ctx.response.send_message(embed=discord.Embed(
            title="23. Vanadium",
            color=themeColor
        ))
    elif elem == "Cr":
        await ctx.response.send_message(embed=discord.Embed(
            title="24. Chromium",
            color=themeColor
        ))
    elif elem == "Mn":
        await ctx.response.send_message(embed=discord.Embed(
            title="25. Manganese",
            color=themeColor
        ))
    elif elem == "Fe":
        await ctx.response.send_message(embed=discord.Embed(
            title="26. Iron",
            color=themeColor
        ))
    elif elem == "Co":
        await ctx.response.send_message(embed=discord.Embed(
            title="27. Cobalt",
            color=themeColor
        ))
    elif elem == "Ni":
        await ctx.response.send_message(embed=discord.Embed(
            title="28. Nickel",
            color=themeColor
        ))
    elif elem == "Cu":
        await ctx.response.send_message(embed=discord.Embed(
            title="29. Copper",
            color=themeColor
        ))
    elif elem == "Zn":
        await ctx.response.send_message(embed=discord.Embed(
            title="30. Zinc",
            color=themeColor
        ))
    elif elem == "Ga":
        await ctx.response.send_message(embed=discord.Embed(
            title="31. Galium",
            color=themeColor
        ))
    elif elem == "Ge":
        await ctx.response.send_message(embed=discord.Embed(
            title="32. Germanium",
            color=themeColor
        ))
    elif elem == "As":
        await ctx.response.send_message(embed=discord.Embed(
            title="33. Arsenic",
            color=themeColor
        ))
    elif elem == "Se":
        await ctx.response.send_message(embed=discord.Embed(
            title="34. Selenium",
            color=themeColor
        ))
    elif elem == "Br":
        await ctx.response.send_message(embed=discord.Embed(
            title="35. Bromine",
            color=themeColor
        ))
    elif elem == "Kr":
        await ctx.response.send_message(embed=discord.Embed(
            title="36. Krypton",
            color=themeColor
        ))
    elif elem == "Rb":
        await ctx.response.send_message(embed=discord.Embed(
            title="37. Rubidium",
            color=themeColor
        ))
    elif elem == "Sr":
        await ctx.response.send_message(embed=discord.Embed(
            title="38. Strontium",
            color=themeColor
        ))
    elif elem == "Y":
        await ctx.response.send_message(embed=discord.Embed(
            title="39. Yttrium",
            color=themeColor
        ))
    elif elem == "Zr":
        await ctx.response.send_message(embed=discord.Embed(
            title="40. Zirconium",
            color=themeColor
        ))
    elif elem == "Nb":
        await ctx.response.send_message(embed=discord.Embed(
            title="41. Niobium",
            color=themeColor
        ))
    elif elem == "Mo":
        await ctx.response.send_message(embed=discord.Embed(
            title="42. Molybdenum",
            color=themeColor
        ))
    elif elem == "Tc":
        await ctx.response.send_message(embed=discord.Embed(
            title="43. Technetium",
            color=themeColor
        ))
    elif elem == "Ru":
        await ctx.response.send_message(embed=discord.Embed(
            title="44. Ruthenium",
            color=themeColor
        ))
    elif elem == "Rh":
        await ctx.response.send_message(embed=discord.Embed(
            title="45. Rhodium",
            color=themeColor
        ))
    elif elem == "Pd":
        await ctx.response.send_message(embed=discord.Embed(
            title="46. Palladium",
            color=themeColor
        ))
    elif elem == "Ag":
        await ctx.response.send_message(embed=discord.Embed(
            title="47. Silver",
            color=themeColor
        ))
    elif elem == "Cd":
        await ctx.response.send_message(embed=discord.Embed(
            title="48. Cadmium",
            color=themeColor
        ))
    elif elem == "In":
        await ctx.response.send_message(embed=discord.Embed(
            title="49. Indium",
            color=themeColor
        ))
    elif elem == "Sn":
        await ctx.response.send_message(embed=discord.Embed(
            title="50. Tin",
            color=themeColor
        ))
    elif elem == "Sb":
        await ctx.response.send_message(embed=discord.Embed(
            title="51. Antimony",
            color=themeColor
        ))
    elif elem == "Te":
        await ctx.response.send_message(embed=discord.Embed(
            title="52. Tellurium",
            color=themeColor
        ))
    elif elem == "I":
        await ctx.response.send_message(embed=discord.Embed(
            title="53. Iodine",
            color=themeColor
        ))
    elif elem == "Xe":
        await ctx.response.send_message(embed=discord.Embed(
            title="54. Xenon",
            color=themeColor
        ))
    elif elem == "Cs":
        await ctx.response.send_message(embed=discord.Embed(
            title="55. Cesium",
            color=themeColor
        ))
    elif elem == "Ba":
        await ctx.response.send_message(embed=discord.Embed(
            title="56. Barium",
            color=themeColor
        ))
    elif elem == "La":
        await ctx.response.send_message(embed=discord.Embed(
            title="57. Lanthanum",
            color=themeColor
        ))
    elif elem == "Ce":
        await ctx.response.send_message(embed=discord.Embed(
            title="58. Cerium",
            color=themeColor
        ))
    elif elem == "Pr":
        await ctx.response.send_message(embed=discord.Embed(
            title="59. Praseodymium",
            color=themeColor
        ))
    elif elem == "Nd":
        await ctx.response.send_message(embed=discord.Embed(
            title="60. Neodymium",
            color=themeColor
        ))
    elif elem == "Pm":
        await ctx.response.send_message(embed=discord.Embed(
            title="61. Promethium",
            color=themeColor
        ))
    elif elem == "Sm":
        await ctx.response.send_message(embed=discord.Embed(
            title="62. Samarium",
            color=themeColor
        ))
    elif elem == "Eu":
        await ctx.response.send_message(embed=discord.Embed(
            title="63. Europium",
            color=themeColor
        ))
    elif elem == "Gd":
        await ctx.response.send_message(embed=discord.Embed(
            title="64. Gadolinium",
            color=themeColor
        ))
    elif elem == "Tb":
        await ctx.response.send_message(embed=discord.Embed(
            title="65. Terbium",
            color=themeColor
        ))
    elif elem == "Dy":
        await ctx.response.send_message(embed=discord.Embed(
            title="66. Dysprosium",
            color=themeColor
        ))
    elif elem == "Ho":
        await ctx.response.send_message(embed=discord.Embed(
            title="67. Holmium",
            color=themeColor
        ))
    elif elem == "Er":
        await ctx.response.send_message(embed=discord.Embed(
            title="68. Erbium",
            color=themeColor
        ))
    elif elem == "Tm":
        await ctx.response.send_message(embed=discord.Embed(
            title="69. Thulium",
            color=themeColor
        ))
    elif elem == "Yb":
        await ctx.response.send_message(embed=discord.Embed(
            title="70. Ytterbium",
            color=themeColor
        ))
    elif elem == "Lu":
        await ctx.response.send_message(embed=discord.Embed(
            title="71. Lutetium",
            color=themeColor
        ))
    elif elem == "Hf":
        await ctx.response.send_message(embed=discord.Embed(
            title="72. Hafnium",
            color=themeColor
        ))
    elif elem == "Ta":
        await ctx.response.send_message(embed=discord.Embed(
            title="73. Tantalum",
            color=themeColor
        ))
    elif elem == "W":
        await ctx.response.send_message(embed=discord.Embed(
            title="74. Tungsten",
            color=themeColor
        ))
    elif elem == "Re":
        await ctx.response.send_message(embed=discord.Embed(
            title="75. Rhenium",
            color=themeColor
        ))
    elif elem == "Os":
        await ctx.response.send_message(embed=discord.Embed(
            title="76. Osmium",
            color=themeColor
        ))
    elif elem == "Ir":
        await ctx.response.send_message(embed=discord.Embed(
            title="77. Irdium",
            color=themeColor
        ))
    elif elem == "Pt":
        await ctx.response.send_message(embed=discord.Embed(
            title="78. Platinum",
            color=themeColor
        ))
    elif elem == "Au":
        await ctx.response.send_message(embed=discord.Embed(
            title="79. Gold",
            color=themeColor
        ))
    elif elem == "Hg":
        await ctx.response.send_message(embed=discord.Embed(
            title="80. Mercury",
            color=themeColor
        ))
    elif elem == "Tl":
        await ctx.response.send_message(embed=discord.Embed(
            title="81. Thallium",
            color=themeColor
        ))
    elif elem == "Pb":
        await ctx.response.send_message(embed=discord.Embed(
            title="82. Lead",
            color=themeColor
        ))
    elif elem == "Bi":
        await ctx.response.send_message(embed=discord.Embed(
            title="83. Bismuth",
            color=themeColor
        ))
    elif elem == "Po":
        await ctx.response.send_message(embed=discord.Embed(
            title="84. Polonium",
            color=themeColor
        ))
    elif elem == "A":
        await ctx.response.send_message(embed=discord.Embed(
            title="85. Astatine",
            color=themeColor
        ))
    elif elem == "Rn":
        await ctx.response.send_message(embed=discord.Embed(
            title="86. Radon",
            color=themeColor
        ))
    elif elem == "Fr":
        await ctx.response.send_message(embed=discord.Embed(
            title="87. Francium",
            color=themeColor
        ))
    elif elem == "Ra":
        await ctx.response.send_message(embed=discord.Embed(
            title="88. Radium",
            color=themeColor
        ))
    elif elem == "Ac":
        await ctx.response.send_message(embed=discord.Embed(
            title="89. Actinium",
            color=themeColor
        ))
    elif elem == "Th":
        await ctx.response.send_message(embed=discord.Embed(
            title="90. Thorium",
            color=themeColor
        ))
    elif elem == "Pa":
        await ctx.response.send_message(embed=discord.Embed(
            title="91. Protactinium",
            color=themeColor
        ))
    elif elem == "U":
        await ctx.response.send_message(embed=discord.Embed(
            title="92. Uranium",
            color=themeColor
        ))
    elif elem == "Np":
        await ctx.response.send_message(embed=discord.Embed(
            title="93. Neptunium",
            color=themeColor
        ))
    elif elem == "Pu":
        await ctx.response.send_message(embed=discord.Embed(
            title="94. Plutonium",
            color=themeColor
        ))
    elif elem == "Am":
        await ctx.response.send_message(embed=discord.Embed(
            title="95. Americium",
            color=themeColor
        ))
    elif elem == "Cm":
        await ctx.response.send_message(embed=discord.Embed(
            title="96. Curium",
            color=themeColor
        ))
    elif elem == "Bk":
        await ctx.response.send_message(embed=discord.Embed(
            title="97. Berkelium",
            color=themeColor
        ))
    elif elem == "Cf":
        await ctx.response.send_message(embed=discord.Embed(
            title="98. Californium",
            color=themeColor
        ))
    elif elem == "Es":
        await ctx.response.send_message(embed=discord.Embed(
            title="99. Einsteinium",
            color=themeColor
        ))
    elif elem == "Fm":
        await ctx.response.send_message(embed=discord.Embed(
            title="100. Fermium",
            color=themeColor
        ))
    elif elem == "Md":
        await ctx.response.send_message(embed=discord.Embed(
            title="101. Mendelevium",
            color=themeColor
        ))
    elif elem == "No":
        await ctx.response.send_message(embed=discord.Embed(
            title="102. Nobelium",
            color=themeColor
        ))
    elif elem == "Lr":
        await ctx.response.send_message(embed=discord.Embed(
            title="103. Lawrencium",
            color=themeColor
        ))
    elif elem == "Rf":
        await ctx.response.send_message(embed=discord.Embed(
            title="104. Rutherfodium",
            color=themeColor
        ))
    elif elem == "Db":
        await ctx.response.send_message(embed=discord.Embed(
            title="105. Dubnium",
            color=themeColor
        ))
    elif elem == "Sg":
        await ctx.response.send_message(embed=discord.Embed(
            title="106. Seaborgium",
            color=themeColor
        ))
    elif elem == "Bh":
        await ctx.response.send_message(embed=discord.Embed(
            title="107. Bohrium",
            color=themeColor
        ))
    elif elem == "Hs":
        await ctx.response.send_message(embed=discord.Embed(
            title="108. Hassium",
            color=themeColor
        ))
    elif elem == "Mt":
        await ctx.response.send_message(embed=discord.Embed(
            title="109. Meitnerium",
            color=themeColor
        ))
    elif elem == "Ds":
        await ctx.response.send_message(embed=discord.Embed(
            title="110. Darmstadtium",
            color=themeColor
        ))
    elif elem == "Rg":
        await ctx.response.send_message(embed=discord.Embed(
            title="111. Roentgenium",
            color=themeColor
        ))
    elif elem == "Cn":
        await ctx.response.send_message(embed=discord.Embed(
            title="112. Copernicium",
            color=themeColor
        ))
    elif elem == "Nh":
        await ctx.response.send_message(embed=discord.Embed(
            title="113. Nihonium",
            color=themeColor
        ))
    elif elem == "Fl":
        await ctx.response.send_message(embed=discord.Embed(
            title="114. Flerovium",
            color=themeColor
        ))
    elif elem == "Mc":
        await ctx.response.send_message(embed=discord.Embed(
            title="115. Moscovium",
            color=themeColor
        ))
    elif elem == "Lv":
        await ctx.response.send_message(embed=discord.Embed(
            title="116. Livermorium",
            color=themeColor
        ))
    elif elem == "Ts":
        await ctx.response.send_message(embed=discord.Embed(
            title="117. Tennessine",
            color=themeColor
        ))
    elif elem == "Og":
        await ctx.response.send_message(embed=discord.Embed(
            title="118. Oganesson",
            color=themeColor
        ))
    elif elem is None:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="No element specified",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description=f"Element '{element}' does not exist",
            colour=errorColor
        ), ephemeral=True)

# The periodic table to get the symbol
@client.tree.command(name="elementnumber", description="Return the name of the element if given the atomic number")
@app_commands.describe(number="The atomic number")
async def elementnumber(ctx, *, number : str):
    "Return the name and symbol given the atomic number"
    elem = number
    if elem == "1":
        await ctx.response.send_message(embed=discord.Embed(
            title="Hydrogen H",
            color=themeColor
        ))
    elif elem == "2":
        await ctx.response.send_message(embed=discord.Embed(
            title="Helium He",
            color=themeColor
        ))
    elif elem == "3":
        await ctx.response.send_message(embed=discord.Embed(
            title="Lithium Li",
            color=themeColor
        ))
    elif elem == "4":
        await ctx.response.send_message(embed=discord.Embed(
            title="Berylium Be",
            color=themeColor
        ))
    elif elem == "5":
        await ctx.response.send_message(embed=discord.Embed(
            title="Boron B",
            color=themeColor
        ))
    elif elem == "6":
        await ctx.response.send_message(embed=discord.Embed(
            title="Carbon C",
            color=themeColor
        ))
    elif elem == "7":
        await ctx.response.send_message(embed=discord.Embed(
            title="Nitrogen N",
            color=themeColor
        ))
    elif elem == "8":
        await ctx.response.send_message(embed=discord.Embed(
            title="Oxygen O",
            color=themeColor
        ))
    elif elem == "9":
        await ctx.response.send_message(embed=discord.Embed(
            title="Flourine F",
            color=themeColor
        ))
    elif elem == "10":
        await ctx.response.send_message(embed=discord.Embed(
            title="Neon Ne",
            color=themeColor
        ))
    elif elem == "11":
        await ctx.response.send_message(embed=discord.Embed(
            title="Sodium Na",
            color=themeColor
        ))
    elif elem == "12":
        await ctx.response.send_message(embed=discord.Embed(
            title="Magnesium Mg",
            color=themeColor
        ))
    elif elem == "13":
        await ctx.response.send_message(embed=discord.Embed(
            title="Aluminium Al",
            color=themeColor
        ))
    elif elem == "14":
        await ctx.response.send_message(embed=discord.Embed(
            title="Silicon Si",
            color=themeColor
        ))
    elif elem == "15":
        await ctx.response.send_message(embed=discord.Embed(
            title="Phosphorous P",
            color=themeColor
        ))
    elif elem == "16":
        await ctx.response.send_message(embed=discord.Embed(
            title="Sulphur S",
            color=themeColor
        ))
    elif elem == "17":
        await ctx.response.send_message(embed=discord.Embed(
            title="Chlorine Cl",
            color=themeColor
        ))
    elif elem == "18":
        await ctx.response.send_message(embed=discord.Embed(
            title="Argon Ar",
            color=themeColor
        ))
    elif elem == "19":
        await ctx.response.send_message(embed=discord.Embed(
            title="Potassium K",
            color=themeColor
        ))
    elif elem == "20":
        await ctx.response.send_message(embed=discord.Embed(
            title="Calcium Ca",
            color=themeColor
        ))
    elif elem == "21":
        await ctx.response.send_message(embed=discord.Embed(
            title="Scandium Sc",
            color=themeColor
        ))
    elif elem == "22":
        await ctx.response.send_message(embed=discord.Embed(
            title="Titanium Ti",
            color=themeColor
        ))
    elif elem == "23":
        await ctx.response.send_message(embed=discord.Embed(
            title="Vanadium V",
            color=themeColor
        ))
    elif elem == "24":
        await ctx.response.send_message(embed=discord.Embed(
            title="Chromium Cr",
            color=themeColor
        ))
    elif elem == "25":
        await ctx.response.send_message(embed=discord.Embed(
            title="Manganese Mn",
            color=themeColor
        ))
    elif elem == "26":
        await ctx.response.send_message(embed=discord.Embed(
            title="Iron Fe",
            color=themeColor
        ))
    elif elem == "27":
        await ctx.response.send_message(embed=discord.Embed(
            title="Cobalt Co",
            color=themeColor
        ))
    elif elem == "28":
        await ctx.response.send_message(embed=discord.Embed(
            title="Nickel Ni",
            color=themeColor
        ))
    elif elem == "29":
        await ctx.response.send_message(embed=discord.Embed(
            title="Copper Cu",
            color=themeColor
        ))
    elif elem == "30":
        await ctx.response.send_message(embed=discord.Embed(
            title="Zinc Zn",
            color=themeColor
        ))
    elif elem == "31":
        await ctx.response.send_message(embed=discord.Embed(
            title="Galium Ga",
            color=themeColor
        ))
    elif elem == "32":
        await ctx.response.send_message(embed=discord.Embed(
            title="Germanium Ge",
            color=themeColor
        ))
    elif elem == "33":
        await ctx.response.send_message(embed=discord.Embed(
            title="Arsenic As",
            color=themeColor
        ))
    elif elem == "34":
        await ctx.response.send_message(embed=discord.Embed(
            title="Selenium Se",
            color=themeColor
        ))
    elif elem == "35":
        await ctx.response.send_message(embed=discord.Embed(
            title="Bromine Br",
            color=themeColor
        ))
    elif elem == "36":
        await ctx.response.send_message(embed=discord.Embed(
            title="Krypton Kr",
            color=themeColor
        ))
    elif elem == "37":
        await ctx.response.send_message(embed=discord.Embed(
            title="Rubidium Rb",
            color=themeColor
        ))
    elif elem == "38":
        await ctx.response.send_message(embed=discord.Embed(
            title="Strontium Sr",
            color=themeColor
        ))
    elif elem == "39":
        await ctx.response.send_message(embed=discord.Embed(
            title="Yttrium Y",
            color=themeColor
        ))
    elif elem == "40":
        await ctx.response.send_message(embed=discord.Embed(
            title="Zirconium Zr",
            color=themeColor
        ))
    elif elem == "41":
        await ctx.response.send_message(embed=discord.Embed(
            title="Niobium Nb",
            color=themeColor
        ))
    elif elem == "42":
        await ctx.response.send_message(embed=discord.Embed(
            title="Molybdenum Mo",
            color=themeColor
        ))
    elif elem == "43":
        await ctx.response.send_message(embed=discord.Embed(
            title="Technetium Tc",
            color=themeColor
        ))
    elif elem == "44":
        await ctx.response.send_message(embed=discord.Embed(
            title="Ruthenium Ru",
            color=themeColor
        ))
    elif elem == "45":
        await ctx.response.send_message(embed=discord.Embed(
            title="Rhodium Rh",
            color=themeColor
        ))
    elif elem == "46":
        await ctx.response.send_message(embed=discord.Embed(
            title="Palladium Pd",
            color=themeColor
        ))
    elif elem == "47":
        await ctx.response.send_message(embed=discord.Embed(
            title="Silver Ag",
            color=themeColor
        ))
    elif elem == "48":
        await ctx.response.send_message(embed=discord.Embed(
            title="Cadmium Cd",
            color=themeColor
        ))
    elif elem == "49":
        await ctx.response.send_message(embed=discord.Embed(
            title="Indium In",
            color=themeColor
        ))
    elif elem == "50":
        await ctx.response.send_message(embed=discord.Embed(
            title="Tin Sn",
            color=themeColor
        ))
    elif elem == "51":
        await ctx.response.send_message(embed=discord.Embed(
            title="Antimony Sb",
            color=themeColor
        ))
    elif elem == "52":
        await ctx.response.send_message(embed=discord.Embed(
            title="Tellurium Te",
            color=themeColor
        ))
    elif elem == "53":
        await ctx.response.send_message(embed=discord.Embed(
            title="Iodine I",
            color=themeColor
        ))
    elif elem == "54":
        await ctx.response.send_message(embed=discord.Embed(
            title="Xenon Xe",
            color=themeColor
        ))
    elif elem == "55":
        await ctx.response.send_message(embed=discord.Embed(
            title="Cesium Cs",
            color=themeColor
        ))
    elif elem == "56":
        await ctx.response.send_message(embed=discord.Embed(
            title="Barium Ba",
            color=themeColor
        ))
    elif elem == "57":
        await ctx.response.send_message(embed=discord.Embed(
            title="Lanthanum La",
            color=themeColor
        ))
    elif elem == "58":
        await ctx.response.send_message(embed=discord.Embed(
            title="Cerium Ce",
            color=themeColor
        ))
    elif elem == "59":
        await ctx.response.send_message(embed=discord.Embed(
            title="Praseodymium Pr",
            color=themeColor
        ))
    elif elem == "60":
        await ctx.response.send_message(embed=discord.Embed(
            title="Neodymium Nd",
            color=themeColor
        ))
    elif elem == "61":
        await ctx.response.send_message(embed=discord.Embed(
            title="Promethium Pm",
            color=themeColor
        ))
    elif elem == "62":
        await ctx.response.send_message(embed=discord.Embed(
            title="Samarium Sm",
            color=themeColor
        ))
    elif elem == "63":
        await ctx.response.send_message(embed=discord.Embed(
            title="Europium Eu",
            color=themeColor
        ))
    elif elem == "64":
        await ctx.response.send_message(embed=discord.Embed(
            title="Gadolinium Gd",
            color=themeColor
        ))
    elif elem == "65":
        await ctx.response.send_message(embed=discord.Embed(
            title="Terbium Tb",
            color=themeColor
        ))
    elif elem == "66":
        await ctx.response.send_message(embed=discord.Embed(
            title="Dysprosium Dy",
            color=themeColor
        ))
    elif elem == "67":
        await ctx.response.send_message(embed=discord.Embed(
            title="Holmium Ho",
            color=themeColor
        ))
    elif elem == "68":
        await ctx.response.send_message(embed=discord.Embed(
            title="Erbium Er",
            color=themeColor
        ))
    elif elem == "69":
        await ctx.response.send_message(embed=discord.Embed(
            title="Thulium Tm",
            color=themeColor
        ))
    elif elem == "70":
        await ctx.response.send_message(embed=discord.Embed(
            title="Ytterbium Yb",
            color=themeColor
        ))
    elif elem == "71":
        await ctx.response.send_message(embed=discord.Embed(
            title="Lutetium Lu",
            color=themeColor
        ))
    elif elem == "72":
        await ctx.response.send_message(embed=discord.Embed(
            title="Hafnium Hf",
            color=themeColor
        ))
    elif elem == "73":
        await ctx.response.send_message(embed=discord.Embed(
            title="Tantalum Ta",
            color=themeColor
        ))
    elif elem == "74":
        await ctx.response.send_message(embed=discord.Embed(
            title="Tungsten W",
            color=themeColor
        ))
    elif elem == "75":
        await ctx.response.send_message(embed=discord.Embed(
            title="Rhenium Re",
            color=themeColor
        ))
    elif elem == "76":
        await ctx.response.send_message(embed=discord.Embed(
            title="Osmium Os",
            color=themeColor
        ))
    elif elem == "77":
        await ctx.response.send_message(embed=discord.Embed(
            title="Irdium Ir",
            color=themeColor
        ))
    elif elem == "78":
        await ctx.response.send_message(embed=discord.Embed(
            title="Platinum Pt",
            color=themeColor
        ))
    elif elem == "79":
        await ctx.response.send_message(embed=discord.Embed(
            title="Gold Au",
            color=themeColor
        ))
    elif elem == "80":
        await ctx.response.send_message(embed=discord.Embed(
            title="Mercury Hg",
            color=themeColor
        ))
    elif elem == "81":
        await ctx.response.send_message(embed=discord.Embed(
            title="Thallium Tl",
            color=themeColor
        ))
    elif elem == "82":
        await ctx.response.send_message(embed=discord.Embed(
            title="Lead Pb",
            color=themeColor
        ))
    elif elem == "83":
        await ctx.response.send_message(embed=discord.Embed(
            title="Bismuth Bi",
            color=themeColor
        ))
    elif elem == "84":
        await ctx.response.send_message(embed=discord.Embed(
            title="Polonium Po",
            color=themeColor
        ))
    elif elem == "85":
        await ctx.response.send_message(embed=discord.Embed(
            title="Astatine A",
            color=themeColor
        ))
    elif elem == "86":
        await ctx.response.send_message(embed=discord.Embed(
            title="Radon Rn",
            color=themeColor
        ))
    elif elem == "87":
        await ctx.response.send_message(embed=discord.Embed(
            title="Francium Fr",
            color=themeColor
        ))
    elif elem == "88":
        await ctx.response.send_message(embed=discord.Embed(
            title="Radium Ra",
            color=themeColor
        ))
    elif elem == "89":
        await ctx.response.send_message(embed=discord.Embed(
            title="Actinium Ac",
            color=themeColor
        ))
    elif elem == "90":
        await ctx.response.send_message(embed=discord.Embed(
            title="Thorium Th",
            color=themeColor
        ))
    elif elem == "91":
        await ctx.response.send_message(embed=discord.Embed(
            title="Protactinium Pa",
            color=themeColor
        ))
    elif elem == "92":
        await ctx.response.send_message(embed=discord.Embed(
            title="Uranium U",
            color=themeColor
        ))
    elif elem == "93":
        await ctx.response.send_message(embed=discord.Embed(
            title="Neptunium Np",
            color=themeColor
        ))
    elif elem == "94":
        await ctx.response.send_message(embed=discord.Embed(
            title="Plutonium Pu",
            color=themeColor
        ))
    elif elem == "95":
        await ctx.response.send_message(embed=discord.Embed(
            title="Americium Am",
            color=themeColor
        ))
    elif elem == "96":
        await ctx.response.send_message(embed=discord.Embed(
            title="Curium Cm",
            color=themeColor
        ))
    elif elem == "97":
        await ctx.response.send_message(embed=discord.Embed(
            title="Berkelium Bk",
            color=themeColor
        ))
    elif elem == "98":
        await ctx.response.send_message(embed=discord.Embed(
            title="Californium Cf",
            color=themeColor
        ))
    elif elem == "99":
        await ctx.response.send_message(embed=discord.Embed(
            title="Einsteinium Es",
            color=themeColor
        ))
    elif elem == "100":
        await ctx.response.send_message(embed=discord.Embed(
            title="Fermium Fm",
            color=themeColor
        ))
    elif elem == "101":
        await ctx.response.send_message(embed=discord.Embed(
            title="Mendelevium Md",
            color=themeColor
        ))
    elif elem == "102":
        await ctx.response.send_message(embed=discord.Embed(
            title="Nobelium No",
            color=themeColor
        ))
    elif elem == "103":
        await ctx.response.send_message(embed=discord.Embed(
            title="Lawrencium Lr",
            color=themeColor
        ))
    elif elem == "104":
        await ctx.response.send_message(embed=discord.Embed(
            title="Rutherfodium Rf",
            color=themeColor
        ))
    elif elem == "105":
        await ctx.response.send_message(embed=discord.Embed(
            title="Dubnium Db",
            color=themeColor
        ))
    elif elem == "106":
        await ctx.response.send_message(embed=discord.Embed(
            title="Seaborgium Sg",
            color=themeColor
        ))
    elif elem == "107":
        await ctx.response.send_message(embed=discord.Embed(
            title="Bohrium Bh",
            color=themeColor
        ))
    elif elem == "108":
        await ctx.response.send_message(embed=discord.Embed(
            title="Hassium Hs",
            color=themeColor
        ))
    elif elem == "109":
        await ctx.response.send_message(embed=discord.Embed(
            title="Meitnerium Mt",
            color=themeColor
        ))
    elif elem == "110":
        await ctx.response.send_message(embed=discord.Embed(
            title="Darmstadtium Ds",
            color=themeColor
        ))
    elif elem == "111":
        await ctx.response.send_message(embed=discord.Embed(
            title="Roentgenium Rg",
            color=themeColor
        ))
    elif elem == "112":
        await ctx.response.send_message(embed=discord.Embed(
            title="Copernicium Cn",
            color=themeColor
        ))
    elif elem == "113":
        await ctx.response.send_message(embed=discord.Embed(
            title="Nihonium Nh",
            color=themeColor
        ))
    elif elem == "114":
        await ctx.response.send_message(embed=discord.Embed(
            title="Flerovium Fl",
            color=themeColor
        ))
    elif elem == "115":
        await ctx.response.send_message(embed=discord.Embed(
            title="Moscovium Mc",
            color=themeColor
        ))
    elif elem == "116":
        await ctx.response.send_message(embed=discord.Embed(
            title="Livermorium Lv",
            color=themeColor
        ))
    elif elem == "117":
        await ctx.response.send_message(embed=discord.Embed(
            title="Tennessine Ts",
            color=themeColor
        ))
    elif elem == "118":
        await ctx.response.send_message(embed=discord.Embed(
            title="Oganesson Og",
            color=themeColor
        ))
    elif elem is None:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="No element specified",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description=f"Element with number '{number}' does not exist",
            colour=errorColor
        ), ephemeral=True)

# The periodic table to get the symbol
@client.tree.command(name="elementname", description="Input the name of any element to recieve its symbol")
@app_commands.describe(element="Name of the element (First letter must be capital)")
async def elementname(ctx, *, element : str):
    "Return the atomic number and symbol given the name"
    elem = element
    if elem == "Hydrogen":
        await ctx.response.send_message(embed=discord.Embed(
            title="1. H",
            color=themeColor
        ))
    elif elem == "Helium":
        await ctx.response.send_message(embed=discord.Embed(
            title="2. He",
            color=themeColor
        ))
    elif elem == "Lithium":
        await ctx.response.send_message(embed=discord.Embed(
            title="3. Li",
            color=themeColor
        ))
    elif elem == "Berylium":
        await ctx.response.send_message(embed=discord.Embed(
            title="4. Be",
            color=themeColor
        ))
    elif elem == "Boron":
        await ctx.response.send_message(embed=discord.Embed(
            title="5. B",
            color=themeColor
        ))
    elif elem == "Carbon":
        await ctx.response.send_message(embed=discord.Embed(
            title="6. C",
            color=themeColor
        ))
    elif elem == "Nitrogen":
        await ctx.response.send_message(embed=discord.Embed(
            title="7. N",
            color=themeColor
        ))
    elif elem == "Oxygen":
        await ctx.response.send_message(embed=discord.Embed(
            title="8. O",
            color=themeColor
        ))
    elif elem == "Flourine":
        await ctx.response.send_message(embed=discord.Embed(
            title="9. F",
            color=themeColor
        ))
    elif elem == "Neon":
        await ctx.response.send_message(embed=discord.Embed(
            title="10. Ne",
            color=themeColor
        ))
    elif elem == "Sodium":
        await ctx.response.send_message(embed=discord.Embed(
            title="11. Na",
            color=themeColor
        ))
    elif elem == "Magnesium":
        await ctx.response.send_message(embed=discord.Embed(
            title="12. Mg",
            color=themeColor
        ))
    elif elem == "Aluminium":
        await ctx.response.send_message(embed=discord.Embed(
            title="13. Al",
            color=themeColor
        ))
    elif elem == "Silicon":
        await ctx.response.send_message(embed=discord.Embed(
            title="14. Si",
            color=themeColor
        ))
    elif elem == "Phosphorous":
        await ctx.response.send_message(embed=discord.Embed(
            title="15. P",
            color=themeColor
        ))
    elif elem == "Sulphur":
        await ctx.response.send_message(embed=discord.Embed(
            title="16. S",
            color=themeColor
        ))
    elif elem == "Chlorine":
        await ctx.response.send_message(embed=discord.Embed(
            title="17. Cl",
            color=themeColor
        ))
    elif elem == "Argon":
        await ctx.response.send_message(embed=discord.Embed(
            title="18. Ar",
            color=themeColor
        ))
    elif elem == "Potassium":
        await ctx.response.send_message(embed=discord.Embed(
            title="19. K",
            color=themeColor
        ))
    elif elem == "Calcium":
        await ctx.response.send_message(embed=discord.Embed(
            title="20. Ca",
            color=themeColor
        ))
    elif elem == "Scandium":
        await ctx.response.send_message(embed=discord.Embed(
            title="21. Sc",
            color=themeColor
        ))
    elif elem == "Titanium":
        await ctx.response.send_message(embed=discord.Embed(
            title="22. Ti",
            color=themeColor
        ))
    elif elem == "Vanadium":
        await ctx.response.send_message(embed=discord.Embed(
            title="23. V",
            color=themeColor
        ))
    elif elem == "Chromium":
        await ctx.response.send_message(embed=discord.Embed(
            title="24. Cr",
            color=themeColor
        ))
    elif elem == "Manganese":
        await ctx.response.send_message(embed=discord.Embed(
            title="25. Mn",
            color=themeColor
        ))
    elif elem == "Iron":
        await ctx.response.send_message(embed=discord.Embed(
            title="26. Fe",
            color=themeColor
        ))
    elif elem == "Cobalt":
        await ctx.response.send_message(embed=discord.Embed(
            title="27. Co",
            color=themeColor
        ))
    elif elem == "Nickel":
        await ctx.response.send_message(embed=discord.Embed(
            title="28. Ni",
            color=themeColor
        ))
    elif elem == "Copper":
        await ctx.response.send_message(embed=discord.Embed(
            title="29. Cu",
            color=themeColor
        ))
    elif elem == "Zinc":
        await ctx.response.send_message(embed=discord.Embed(
            title="30. Zn",
            color=themeColor
        ))
    elif elem == "Galium":
        await ctx.response.send_message(embed=discord.Embed(
            title="31. Ga",
            color=themeColor
        ))
    elif elem == "Germanium":
        await ctx.response.send_message(embed=discord.Embed(
            title="32. Ge",
            color=themeColor
        ))
    elif elem == "Arsenic":
        await ctx.response.send_message(embed=discord.Embed(
            title="33. As",
            color=themeColor
        ))
    elif elem == "Selenium":
        await ctx.response.send_message(embed=discord.Embed(
            title="34. Se",
            color=themeColor
        ))
    elif elem == "Bromine":
        await ctx.response.send_message(embed=discord.Embed(
            title="35. Br",
            color=themeColor
        ))
    elif elem == "Krypton":
        await ctx.response.send_message(embed=discord.Embed(
            title="36. Kr",
            color=themeColor
        ))
    elif elem == "Rubidium":
        await ctx.response.send_message(embed=discord.Embed(
            title="37. Rb",
            color=themeColor
        ))
    elif elem == "Strontium":
        await ctx.response.send_message(embed=discord.Embed(
            title="38. Sr",
            color=themeColor
        ))
    elif elem == "Yttrium":
        await ctx.response.send_message(embed=discord.Embed(
            title="39. Y",
            color=themeColor
        ))
    elif elem == "Zirconium":
        await ctx.response.send_message(embed=discord.Embed(
            title="40. Zr",
            color=themeColor
        ))
    elif elem == "Niobium":
        await ctx.response.send_message(embed=discord.Embed(
            title="41. Nb",
            color=themeColor
        ))
    elif elem == "Molybdenum":
        await ctx.response.send_message(embed=discord.Embed(
            title="42. Mo",
            color=themeColor
        ))
    elif elem == "Technetium":
        await ctx.response.send_message(embed=discord.Embed(
            title="43. Tc",
            color=themeColor
        ))
    elif elem == "Ruthenium":
        await ctx.response.send_message(embed=discord.Embed(
            title="44. Ru",
            color=themeColor
        ))
    elif elem == "Rhodium":
        await ctx.response.send_message(embed=discord.Embed(
            title="45. Rh",
            color=themeColor
        ))
    elif elem == "Palladium":
        await ctx.response.send_message(embed=discord.Embed(
            title="46. Pd",
            color=themeColor
        ))
    elif elem == "Silver":
        await ctx.response.send_message(embed=discord.Embed(
            title="47. Ag",
            color=themeColor
        ))
    elif elem == "Cadmium":
        await ctx.response.send_message(embed=discord.Embed(
            title="48. Cd",
            color=themeColor
        ))
    elif elem == "Indium":
        await ctx.response.send_message(embed=discord.Embed(
            title="49. In",
            color=themeColor
        ))
    elif elem == "Tin":
        await ctx.response.send_message(embed=discord.Embed(
            title="50. Sn",
            color=themeColor
        ))
    elif elem == "Antimony":
        await ctx.response.send_message(embed=discord.Embed(
            title="51. Sb",
            color=themeColor
        ))
    elif elem == "Tellurium":
        await ctx.response.send_message(embed=discord.Embed(
            title="52. Te",
            color=themeColor
        ))
    elif elem == "Iodine":
        await ctx.response.send_message(embed=discord.Embed(
            title="53. I",
            color=themeColor
        ))
    elif elem == "Xenon":
        await ctx.response.send_message(embed=discord.Embed(
            title="54. Xe",
            color=themeColor
        ))
    elif elem == "Cesium":
        await ctx.response.send_message(embed=discord.Embed(
            title="55. Cs",
            color=themeColor
        ))
    elif elem == "Barium":
        await ctx.response.send_message(embed=discord.Embed(
            title="56. Ba",
            color=themeColor
        ))
    elif elem == "Lanthanum":
        await ctx.response.send_message(embed=discord.Embed(
            title="57. La",
            color=themeColor
        ))
    elif elem == "Cerium":
        await ctx.response.send_message(embed=discord.Embed(
            title="58. Ce",
            color=themeColor
        ))
    elif elem == "Praseodymium":
        await ctx.response.send_message(embed=discord.Embed(
            title="59. Pr",
            color=themeColor
        ))
    elif elem == "Neodymium":
        await ctx.response.send_message(embed=discord.Embed(
            title="60. Nd",
            color=themeColor
        ))
    elif elem == "Promethium":
        await ctx.response.send_message(embed=discord.Embed(
            title="61. Pm",
            color=themeColor
        ))
    elif elem == "Samarium":
        await ctx.response.send_message(embed=discord.Embed(
            title="62. Sm",
            color=themeColor
        ))
    elif elem == "Europium":
        await ctx.response.send_message(embed=discord.Embed(
            title="63. Eu",
            color=themeColor
        ))
    elif elem == "Gadolinium":
        await ctx.response.send_message(embed=discord.Embed(
            title="64. Gd",
            color=themeColor
        ))
    elif elem == "Terbium":
        await ctx.response.send_message(embed=discord.Embed(
            title="65. Tb",
            color=themeColor
        ))
    elif elem == "Dysprosium":
        await ctx.response.send_message(embed=discord.Embed(
            title="66. Dy",
            color=themeColor
        ))
    elif elem == "Holmium":
        await ctx.response.send_message(embed=discord.Embed(
            title="67. Ho",
            color=themeColor
        ))
    elif elem == "Erbium":
        await ctx.response.send_message(embed=discord.Embed(
            title="68. Er",
            color=themeColor
        ))
    elif elem == "Thulium":
        await ctx.response.send_message(embed=discord.Embed(
            title="69. Tm",
            color=themeColor
        ))
    elif elem == "Ytterbium":
        await ctx.response.send_message(embed=discord.Embed(
            title="70. Yb",
            color=themeColor
        ))
    elif elem == "Lutetium":
        await ctx.response.send_message(embed=discord.Embed(
            title="71. Lu",
            color=themeColor
        ))
    elif elem == "Hafnium":
        await ctx.response.send_message(embed=discord.Embed(
            title="72. Hf",
            color=themeColor
        ))
    elif elem == "Tantalum":
        await ctx.response.send_message(embed=discord.Embed(
            title="73. Ta",
            color=themeColor
        ))
    elif elem == "Tungsten":
        await ctx.response.send_message(embed=discord.Embed(
            title="74. W",
            color=themeColor
        ))
    elif elem == "Rhenium":
        await ctx.response.send_message(embed=discord.Embed(
            title="75. Re",
            color=themeColor
        ))
    elif elem == "Osmium":
        await ctx.response.send_message(embed=discord.Embed(
            title="76. Os",
            color=themeColor
        ))
    elif elem == "Irdium":
        await ctx.response.send_message(embed=discord.Embed(
            title="77. Ir",
            color=themeColor
        ))
    elif elem == "Platinum":
        await ctx.response.send_message(embed=discord.Embed(
            title="78. Pt",
            color=themeColor
        ))
    elif elem == "Gold":
        await ctx.response.send_message(embed=discord.Embed(
            title="79. Au",
            color=themeColor
        ))
    elif elem == "Mercury":
        await ctx.response.send_message(embed=discord.Embed(
            title="80. Hg",
            color=themeColor
        ))
    elif elem == "Thallium":
        await ctx.response.send_message(embed=discord.Embed(
            title="81. Tl",
            color=themeColor
        ))
    elif elem == "Lead":
        await ctx.response.send_message(embed=discord.Embed(
            title="82. Pb",
            color=themeColor
        ))
    elif elem == "Bismuth":
        await ctx.response.send_message(embed=discord.Embed(
            title="83. Bi",
            color=themeColor
        ))
    elif elem == "Polonium":
        await ctx.response.send_message(embed=discord.Embed(
            title="84. Po",
            color=themeColor
        ))
    elif elem == "Astatine":
        await ctx.response.send_message(embed=discord.Embed(
            title="85. A",
            color=themeColor
        ))
    elif elem == "Radon":
        await ctx.response.send_message(embed=discord.Embed(
            title="86. Rn",
            color=themeColor
        ))
    elif elem == "Francium":
        await ctx.response.send_message(embed=discord.Embed(
            title="87. Fr",
            color=themeColor
        ))
    elif elem == "Radium":
        await ctx.response.send_message(embed=discord.Embed(
            title="88. Ra",
            color=themeColor
        ))
    elif elem == "Actinium":
        await ctx.response.send_message(embed=discord.Embed(
            title="89. Ac",
            color=themeColor
        ))
    elif elem == "Thorium":
        await ctx.response.send_message(embed=discord.Embed(
            title="90. Th",
            color=themeColor
        ))
    elif elem == "Protactinium":
        await ctx.response.send_message(embed=discord.Embed(
            title="91. Pa",
            color=themeColor
        ))
    elif elem == "Uranium":
        await ctx.response.send_message(embed=discord.Embed(
            title="92. U",
            color=themeColor
        ))
    elif elem == "Neptunium":
        await ctx.response.send_message(embed=discord.Embed(
            title="93. Np",
            color=themeColor
        ))
    elif elem == "Plutonium":
        await ctx.response.send_message(embed=discord.Embed(
            title="94. Pu",
            color=themeColor
        ))
    elif elem == "Americium":
        await ctx.response.send_message(embed=discord.Embed(
            title="95. Am",
            color=themeColor
        ))
    elif elem == "Curium":
        await ctx.response.send_message(embed=discord.Embed(
            title="96. Cm",
            color=themeColor
        ))
    elif elem == "Berkelium":
        await ctx.response.send_message(embed=discord.Embed(
            title="97. Bk",
            color=themeColor
        ))
    elif elem == "Californium":
        await ctx.response.send_message(embed=discord.Embed(
            title="98. Cf",
            color=themeColor
        ))
    elif elem == "Einsteinium":
        await ctx.response.send_message(embed=discord.Embed(
            title="99. Es",
            color=themeColor
        ))
    elif elem == "Fermium":
        await ctx.response.send_message(embed=discord.Embed(
            title="100. Fm",
            color=themeColor
        ))
    elif elem == "Mendelevium":
        await ctx.response.send_message(embed=discord.Embed(
            title="101. Md",
            color=themeColor
        ))
    elif elem == "Nobelium":
        await ctx.response.send_message(embed=discord.Embed(
            title="102. No",
            color=themeColor
        ))
    elif elem == "Lawrencium":
        await ctx.response.send_message(embed=discord.Embed(
            title="103. Lr",
            color=themeColor
        ))
    elif elem == "Rutherfodium":
        await ctx.response.send_message(embed=discord.Embed(
            title="104. Rf",
            color=themeColor
        ))
    elif elem == "Dubnium":
        await ctx.response.send_message(embed=discord.Embed(
            title="105. Db",
            color=themeColor
        ))
    elif elem == "Seaborgium":
        await ctx.response.send_message(embed=discord.Embed(
            title="106. Sg",
            color=themeColor
        ))
    elif elem == "Bohrium":
        await ctx.response.send_message(embed=discord.Embed(
            title="107. Bh",
            color=themeColor
        ))
    elif elem == "Hassium":
        await ctx.response.send_message(embed=discord.Embed(
            title="108. Hs",
            color=themeColor
        ))
    elif elem == "Meitnerium":
        await ctx.response.send_message(embed=discord.Embed(
            title="109. Mt",
            color=themeColor
        ))
    elif elem == "Darmstadtium":
        await ctx.response.send_message(embed=discord.Embed(
            title="110. Ds",
            color=themeColor
        ))
    elif elem == "Roentgenium":
        await ctx.response.send_message(embed=discord.Embed(
            title="111. Rg",
            color=themeColor
        ))
    elif elem == "Copernicium":
        await ctx.response.send_message(embed=discord.Embed(
            title="112. Cn",
            color=themeColor
        ))
    elif elem == "Nihonium":
        await ctx.response.send_message(embed=discord.Embed(
            title="113. Nh",
            color=themeColor
        ))
    elif elem == "Flerovium":
        await ctx.response.send_message(embed=discord.Embed(
            title="114. Fl",
            color=themeColor
        ))
    elif elem == "Moscovium":
        await ctx.response.send_message(embed=discord.Embed(
            title="115. Mc",
            color=themeColor
        ))
    elif elem == "Livermorium":
        await ctx.response.send_message(embed=discord.Embed(
            title="116. Lv",
            color=themeColor
        ))
    elif elem == "Tennessine":
        await ctx.response.send_message(embed=discord.Embed(
            title="117. Ts",
            color=themeColor
        ))
    elif elem == "Oganesson":
        await ctx.response.send_message(embed=discord.Embed(
            title="118. Og",
            color=themeColor
        ))
    elif elem is None:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="No element specified",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description=f"Element '{element}' does not exist",
            colour=errorColor
        ), ephemeral=True)

# Get the periodic table
@client.tree.command(name="periodic_table", description="Returns the periodic table")
async def periodic_table(ctx):
    "Return an image of the periodic table"
    with open('assets/periodic_table.png', 'rb') as file:
        await ctx.response.send_message("**__Periodic table__**\n● Yellow: Alkali metals\n● Pink: Non metals\n● Dark orange: Alkali earth metals\n● Light blue: Halogens\n● Blue: Transition Metals\n● Purple: Noble gases\n● Black: Other metals\n● Red: Lanthanides\n● Grey: Metalloids\n● Green: Actinides", file=discord.File(file))

# Get the types of cell organelles
@client.tree.command(name="cell_organelles", description="Organelles are things that make up a cell")
@app_commands.describe(organelle="Types: Cell wall, Cell membrane, Nucleas, Cytoplasm, Mitochondria, Endoplasmic reticulum, Ribosomes, Golgi appratus, Chloroplasts, Vacoules, Lysomes")
async def cell_organelles(ctx, *, organelle : str):
    "Return information of a cell organelle"
    organelle = organelle.lower()
    if organelle == "cell wall":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Cell wall__",
            description="```A cell wall is defined as a rigid, external layer that is specifically designed to provide structural support and rigidity. It also keeps the interior components of the cell intact and safe from the external environment. It is present only within plant cells.```",
            color=themeColor
        ))
    elif organelle == "cell membrane":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Cell membrane__",
            description="```The cell membrane, also called the plasma membrane, is found in all cells and separates the interior of the cell from the outside environment. The cell membrane consists of a lipid bilayer that is semipermeable. The cell membrane regulates the transport of materials entering and exiting the cell.```",
            color=themeColor
        ))
    elif organelle == "nucleas":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Nucleas__",
            description="```A nucleus, as related to genomics, is the membrane-enclosed organelle within a cell that contains the chromosomes. An array of holes, or pores, in the nuclear membrane allows for the selective passage of certain molecules (such as proteins and nucleic acids) into and out of the nucleus.```",
            color=themeColor
        ))
    elif organelle == "cytoplasm":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Cytoplasm__",
            description="```Cytoplasm is the gelatinous liquid that fills the inside of a cell. It is composed of water, salts, and various organic molecules. Some intracellular organelles, such the nucleus and mitochondria, are enclosed by membranes that separate them from the cytoplasm.```",
            color=themeColor
        ))
    elif organelle == "mitochondria":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Mitochondria__",
            description="```Mitochondria are membrane-bound cell organelles (mitochondrion, singular) that generate most of the chemical energy needed to power the cell's biochemical reactions. Chemical energy produced by the mitochondria is stored in a small molecule called adenosine triphosphate (ATP).```",
            color=themeColor
        ))
    elif organelle == "endoplasmic reticulum":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Endplasmic reticulam__",
            description="```The endoplasmic reticulum (ER) is a continuous membrane system that forms a series of flattened sacs within the cytoplasm of eukaryotic cells. All eukaryotic cells contain an ER. In animal cells, the ER usually constitutes more than half of the membranous content of the cell.```",
            color=themeColor
        ))
    elif organelle == "ribosomes":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Ribosomes__",
            description="```A ribosome is an intercellular structure made of both RNA and protein, and it is the site of protein synthesis in the cell. The ribosome reads the messenger RNA (mRNA) sequence and translates that genetic code into a specified string of amino acids, which grow into long chains that fold to form proteins.```",
            color=themeColor
        ))
    elif organelle == "golgi apparatus":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Golgi apparatus__",
            description="```A Golgi body, also known as a Golgi apparatus, is a cell organelle that helps process and package proteins and lipid molecules, especially proteins destined to be exported from the cell. Named after its discoverer, Camillo Golgi, the Golgi body appears as a series of stacked membranes.```",
            color=themeColor
        ))
    elif organelle == "chloroplasts":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Chloroplasts__",
            description="```A chloroplast is an organelle within the cells of plants and certain algae that is the site of photosynthesis, which is the process by which energy from the Sun is converted into chemical energy for growth.```",
            color=themeColor
        ))
    elif organelle == "vacoules":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Vacoules__",
            description="```A vacuole is a membrane-bound cell organelle. In animal cells, vacuoles are generally small and help sequester waste products. In plant cells, vacuoles help maintain water balance. Sometimes a single vacuole can take up most of the interior space of the plant cell```",
            color=themeColor
        ))
    elif organelle == "lysomes":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Lysomes__",
            description="```A lysosome is a membrane-bound cell organelle that contains digestive enzymes. Lysosomes are involved with various cell processes. They break down excess or worn-out cell parts. They may be used to destroy invading viruses and bacteria.```",
            color=themeColor
        ))
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error: ❌",
            description=f"```Cell organelle '{organelle.capitalize()}' does not exist\nTypes: Cell wall, Cell membrane, Nucleas, Cytoplasm, Mitochondria, Endoplasmic reticulum, Ribosomes, Golgi appratus, Chloroplasts, Vacoules, Lysomes```",
            color=errorColor
        ), ephemeral=True)

"""Chess"""
@client.tree.command(name="bestmove", description="Find the best move in any position given its FEN")
@app_commands.describe(fen="The FEN of the position", depth="Depth of stockfish (Maximum 15)")
async def bestmove(ctx, fen : str, depth : int = 15):
    "Return the best move in any chess position given the FEN"
    if depth > 15:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="The depth cannot be higher than 15",
            colour=errorColor
        ), ephemeral=True)
    else:
        stockfish = Stockfish(path=variables.STOCKFISH_PATH, depth=depth)
        if stockfish.is_fen_valid(fen):
            stockfish.set_fen_position(fen)
            await ctx.response.send_message("Location - Move: **"+stockfish.get_best_move()+"**")
        else:
            await ctx.response.send_message(embed=discord.Embed(
                title="__Error__ ❌",
                description="FEN is Invalid",
                colour=errorColor
            ), ephemeral=True)

"""Owner commands"""
# Set bot status
@client.tree.command(name="__status", description="Owner command")
@app_commands.describe(status="Status of the bot")
async def __status(ctx, status : str):
    "Change the status of the bot"
    if ctx.user.id == client.owner_id:
        status = status.lower()
        if status == "online":
            await client.change_presence(status=discord.Status.online)
            await ctx.response.send_message("Changed bot status to **Online**", ephemeral=True)
        elif status == "dnd":
            await client.change_presence(status=discord.Status.dnd)
            await ctx.response.send_message("Changed bot status to **Do not disturb**", ephemeral=True)
        elif status == "idle":
            await client.change_presence(status=discord.Status.idle)
            await ctx.response.send_message("Changed bot status to **Idle**", ephemeral=True)
        elif status in ["offline", "invisible"]:
            await client.change_presence(status=discord.Status.offline)
            await ctx.response.send_message("Changed bot status to **Offline**", ephemeral=True)
        else:
            await ctx.response.send_message(embed=discord.Embed(
                title="__Error__ ❌",
                description="Status does not exist",
                colour=errorColor
            ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="You do not have permission to run this command",
            colour=errorColor
        ), ephemeral=True)

# Personal command to open a link
@client.tree.command(name="__open", description="Owner command")
@app_commands.describe(link="Link to open")
async def __open(ctx, *, link : str):
    "Open any link"
    if ctx.user.id == client.owner_id:
        if link.startswith("https://"):
            await ctx.response.send_message("Opening "+link, ephemeral=True)
            webbrowser.open_new_tab(link)
        elif link.lower() == "ddp":
            await ctx.response.send_message("Opening discord developer portal", ephemeral=True)
            webbrowser.open_new_tab(variables.DDPORTAL_LINK)
        elif link.lower() == "repo":
            await ctx.response.send_message("Opening github repo", ephemeral=True)
            webbrowser.open_new_tab(variables.REPO_LINK)
        else:
            await ctx.response.send_message("Opening https://"+link, ephemeral=True)
            webbrowser.open_new_tab("https://"+link)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="You do not have permission to run this command",
            colour=errorColor
        ), ephemeral=True)

# Message a text into any channel
@client.tree.command(name="__echo", description="Owner command")
@app_commands.describe(channelid="ID of the channel you want to send the text to", text="What the bot will respond with")
async def __echo(ctx, channelid : str, *, text : str):
    "Echo a message in any channel"
    if ctx.user.id == client.owner_id:
        try:
            text = text.replace(";", "\n")
            channel = client.get_channel(int(channelid))
            await channel.send(text)
            await ctx.response.send_message(embed=discord.Embed(description=":white_check_mark: Message sent!", colour=themeColor), ephemeral=True)
        except Exception as __EchoGeneralError:
            await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description=__EchoGeneralError,
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description="You do now have permissions to run this command",
            colour = errorColor
        ), ephemeral=True)

# Make the bot type for a specific time
@client.tree.command(name="__type", description="Owner command")
@app_commands.describe(time="Time")
async def __type(ctx, time : int):
    "Make the bot type in any channel for any period of time"
    if ctx.user.id == client.owner_id:
        await ctx.response.send_message("Started typing for **"+str(time)+"** seconds", ephemeral=True)
        async with ctx.channel.typing():
            await asyncio.sleep(time)
    else:
        await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description="You do now have permissions to run this command",
            colour = errorColor
        ), ephemeral=True)

# Send a text to speech message
@client.tree.command(name="__tts", description="Owner command")
@app_commands.describe(message="Message")
async def __tts(ctx, message : str, ephemeral : bool = True):
    "Send a text to speech message"
    await ctx.response.send_message(message, tts=True, ephemeral=ephemeral)

if __name__ == "__main__":
    try:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
    except Exception as RunGeneralError:
        print("Error:",str(RunGeneralError))
