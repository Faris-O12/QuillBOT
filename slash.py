try:
    import discord
    import variables
    import sys
    import os
    import datetime
    import math
    import random
    import string
    import webbrowser
    import wikipediaapi
    from discord.ext import commands
    from python_aternos import Client as aternosClient
    from discord import app_commands
except Exception as e:
    print("Error (Import): "+e)

themeColor = discord.Color.blurple()
errorColor = discord.Color.red()

client = commands.Bot(
    command_prefix=variables.PREFIX,
    description=variables.SHORT_DESCRIPTION,
    case_insensitive=True,
    intents=discord.Intents.all(),
    owner_id=variables.OWNERID,
)

os.chdir(r"G:\\QuillBOT")
client.remove_command('help')

"""Events"""
@client.event
async def on_ready():
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
    except Exception as e:
        print("Error: "+e)

@client.event
async def on_resumed():
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
    except Exception as e:
        print("Error: "+e)

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send(embed=discord.Embed(
            title="Description",
            description=variables.DESCRIPTION,
            color=themeColor
        ))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.app_commands.errors.CommandInvokeError):
        await ctx.send(embed=discord.Embed(
            title="__Error: __",
            description="There was an error on invoking this command",
            color=themeColor
        ), ephemeral=True)

"""Help book"""
@client.tree.command(name="help", description="List of every command")
@app_commands.describe(type="Type can be "+variables.HELP_COMMAND_TYPES)
async def help(ctx, *, type : str):
    if type.lower() == "info":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Help commands__",
            description=variables.INFO_COMMANDS,
            color=themeColor
        ), ephemeral=True) 
    elif type.lower() == "utility":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Utility__",
            description=variables.UTILITY_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "math":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Math__",
            description=variables.MATH_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "science":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Science__",
            description=variables.SCIENCE_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "time":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Time__",
            description=variables.TIME_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "misc":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Misc__",
            description=variables.MISC_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "random":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Random__",
            description=variables.RANDOM_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "questionmath":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Question math__",
            description=variables.QUESTIONMATH_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "admin":
        await ctx.response.send_message(embed=discord.Embed(
            title="__Administrator__",
            description=variables.ADMIN_COMMANDS,
            color=themeColor
        ), ephemeral=True)
    elif type.lower() == "total":
        await ctx.response.send_message(embed=discord.Embed(
            title="Total number of commands",
            description=str(variables.TOTAL_COMMANDS_SLASH),
            color=themeColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Types (Case Insensitive)__",
            description=variables.HELP_COMMAND_TYPES,
            color=themeColor
        ), ephemeral=True)

"""Help"""
# Get the prefix of the bot
@client.tree.command(name="prefix", description="Get the current prefix")
async def prefix(ctx):
    await ctx.response.send_message(f"The current prefix is: **{variables.PREFIX}**", ephemeral=True)

# Gets the link for an attachment
@client.tree.command(name="upload", description="Upload an image to recieve its url")
@app_commands.describe(attachment="Attach an image to discord")
async def upload(ctx, attachment: discord.Attachment):
    await ctx.response.send_message(f'Uploaded by **{ctx.user.name}** <{attachment.url}>')

# Get user's ID
@client.tree.command(name="myid", description="Get your unique user id")
async def myid(ctx):
    await ctx.response.send_message(ctx.user.id, ephemeral=True)

# Get other's ID
@client.tree.command(name="getid", description="Get the unique user id")
@app_commands.describe(member="Insert any user in the server to get their id")
async def getid(ctx, member : discord.User):
    await ctx.response.send_message(member.id, ephemeral=True)

# Get channel id
@client.tree.command(name="channelid", description="Get the unique channel id")
async def channelid(ctx):
    await ctx.response.send_message(ctx.channel.id, ephemeral=True)

# Get guild id
@client.tree.command(name="serverid", description="Get the unique server id")
async def serverid(ctx):
    await ctx.response.send_message(ctx.guild.id, ephemeral=True)

# Get the servers the bot is currently in
@client.tree.command(name="servers", description="Return the number of servers the bot is in")
async def servers(ctx):
    await ctx.response.send_message(embed=discord.Embed(
        description="**Number of server the bot is in: **"+str(len(client.guilds)),
        color=themeColor
    ), ephemeral=True)

# Get a user's Profile picture
@client.tree.command(name="avatar", description="Give an enlarged image of a user's profile picture")
@app_commands.describe(user="User you want to get the avatar of")
async def avatar(ctx, user : discord.Member):
    await ctx.response.send_message(user.avatar)

# Stop the bot
@client.tree.command(name="stop", description="(Requires being bot's owner) Stop the bot")
async def stop(ctx):
    if ctx.user.id == client.owner_id:
        print("Stopped")
        await ctx.response.send_message("__Stopped__", ephemeral=True)
        await client.close()
    else:
        await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description="You do now have permissions to shut down the bot",
            colour=errorColor
        ), ephemeral=True)

# Restart the bot
@client.tree.command(name="restart", description="(Requires being bot's owner) Restart the bot")
async def restart(ctx):
    if ctx.user.id == client.owner_id:
        print("Restarting...")
        await ctx.response.send_message("__Restarted__", ephemeral=True)
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
    if estimation.lower() == "false":
        await ctx.response.send_message(f"Bot latency: **{client.latency*1000}ms**")
    elif estimation.lower() == "true":
        await ctx.response.send_message(f"Bot latency (estimated): **{int(client.latency*1000)}ms**")

"""Randoms"""
# Random int between 'a' and 'b'
@client.tree.command(name="randint", description="Choose a random number between the two numbers that were provided")
@app_commands.describe(number1="First number", number2="Second number")
async def randint(ctx, number1 : int, number2 : int):
    await ctx.response.send_message(f"Random number from {str(number1)} to {str(number2)}: **{random.randint(number1, number2)}**")

# Random option between a list
@client.tree.command(name="randoption", description="Input in your choices (Seperate with commas)")
@app_commands.describe(options="Your list of options")
async def randoption(ctx, *, options : str):
    await ctx.response.send_message(random.choice(options.split(",")))

"""Math"""    
# Add 'A' and 'B'
@client.tree.command(name="add", description="Add the two provided numbers")
@app_commands.describe(number1="First number", number2="Second number")
async def add(ctx, number1: float, number2: float):
    if number1 > 1000000 or number2 > 1000000:
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Any number cannot be higher than 1000000",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(f"**{number1} + {number2}**: __**{number1 + number2}**__")
    
# Multiply 'A' and 'B'
@client.tree.command(name="multiply", description="Multiply the two provided numbers")
@app_commands.describe(number1="First number", number2="Second number")
async def multiply(ctx, number1: float, number2: float):
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
    await ctx.response.send_message(str(number * number))

# Get the cube root of a number
@client.tree.command(name="curoot", description="Find the cube root of any number")
@app_commands.describe(number="Number you want to find the cube root of")
async def curoot(ctx, number : float):
    if number == float(1):
        await ctx.response.send_message(embed=discord.Embed(
            title="__Error__ ❌",
            description="Cube root of 1 is not possible",
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(str(number ** (1 / 3)))

# Get the cube of a number
@client.tree.command(name="cube", description="Cube the provided number")
@app_commands.describe(number="Number you want to find the cube of")
async def cube(ctx, number : float):
    await ctx.response.send_message(str(number ** 3))

# Get the pythagorean triplet for 'A' and 'B'
@client.tree.command(name="hypotenuse", description="Use the pythagorean thereom to find the hypotenuse of a right triangle")
@app_commands.describe(leg1="First leg", leg2="Second leg")
async def hypotenuse(ctx, leg1:float, leg2:float):
    await ctx.response.send_message(f"{str(leg1)}² + {str(leg2)}² = x²\n{float(leg1) ** 2} + {float(leg2) ** 2} = x²\n{(float(leg1) ** 2) + (float(leg2) ** 2)} = x²\n__{math.sqrt((float(leg1) ** 2) + (float(leg2) ** 2))}__ = x")

# Evaluate an equation
@client.tree.command(name="evaluate", description="Evaluate the answer to your question")
@app_commands.describe(question="Multiplication is * and division is /")
async def evalute(ctx, *, question : str):
    try:
        answer = eval(question)
        await ctx.response.send_message(f"{question} = **__{answer}__**")
    except ZeroDivisionError:
        await ctx.response.send_message("Cannot divide with 0")
    except Exception as e:
        await ctx.response.send_message("__Error__: "+e)

# Exponenet a number with another number
@client.tree.command(name="exponent", description="Multiply the base by the amount of exponent")
@app_commands.describe(base="Base of the number", exponent="Exponent of the base")
async def exponent(ctx, base : int, exponent : int):
    if exponent == 1:
        await ctx.response.send_message("1")
    else:
        await ctx.response.send_message(str(base ** exponent))

# Get the root of a number with the specified root
@client.tree.command(name="root", description="Root the number to the number")
@app_commands.describe(number="Number you want to find the root of", root="Power of the root")
async def root(ctx, number : int, root : int):
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

# Get PI
@client.tree.command(name="pi", description="Give you back the number pi")
async def pi(ctx):
    await ctx.response.send_message(math.pi)

# Get the percentage between numerator and denominator
@client.tree.command(name="percentage", description="Find the percentage of any fraction")
@app_commands.describe(numerator="Numerator of the fraction", denominator="Denominator of the fraction")
async def percentage(ctx, numerator : int, denominator : int):
    await ctx.response.send_message(f"Percentage of {str(numerator)} / {str(denominator)} : **{str((numerator / denominator) * 100)}%**")

# Get the average value from a list
@client.tree.command(name="average", description="Find the average value of the numbers")
@app_commands.describe(numbers="Seperate the numbers with commas")
async def average(ctx, numbers : str):
    numbers = numbers.replace(" ", "")
    numbers = numbers.split(",")
    numlist = list(map(int, numbers))
    await ctx.response.send_message(sum(numlist) / len(numlist))

# Get the increase percentange of any number
@client.tree.command(name="increase", description="Find the increase percentage of any number")
@app_commands.describe(number="The initial value", increase="The increase percentage")
async def increase(ctx, number : int, increase : int):
    await ctx.response.send_message(number + (number * increase / 100))

# Get the descrease percentage of any number
@client.tree.command(name="decrease", description="Find the decrease percentage of any number")
@app_commands.describe(number="The initial value", decrease="The decrease percentage")
async def decrease(ctx, number : int, decrease : int):
    await ctx.response.send_message(number - (number * decrease / 100))

# Find the amount of diagonals a polygon has
@client.tree.command(name="diagonals", description="Find the amount of diagonals a polygon has")
@app_commands.describe(sides="The amount of sides the polygon has")
async def diagonals(ctx, sides : int):
    if sides == 2 or sides == 1 or sides <= 0:
        await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description=f"There cannot be a polygon with {str(sides)} sides",
            colour=errorColor
        ), ephemeral=True)
    else:
        try:
            await ctx.response.send_message(str((sides * (sides - 3)) / 2))
        except Exception as e:
            await ctx.response.send_message(embed=discord.Embed(
            title="**__Error__ ❌**",
            description=e,
            colour=errorColor
        ), ephemeral=True)

"""Question math"""
# Ask an addition question
@client.tree.command(name="question_add", description="Ask you an addition question")
async def question_add(ctx):
    num1 = random.randrange(10, 10000)
    num2 = random.randrange(10, 10000)

    await ctx.response.send_message(f"{str(num1)} + {str(num2)} = ||{str(num1 + num2)}||")

# Ask a subtraction question
@client.tree.command(name="question_subtract", description="Ask you a subtract question")
async def question_subtract(ctx):
    num1 = random.randrange(10, 10000)
    num2 = random.randrange(10, 10000)

    await ctx.response.send_message(f"{str(num1)} - {str(num2)} = ||{str(num1 - num2)}||")

# Ask a multiplication question
@client.tree.command(name="question_multiply", description="Ask you a multiplication question")
async def question_multiply(ctx):
    num1 = random.randrange(10, 10000)
    num2 = random.randrange(10, 10000)

    await ctx.response.send_message(f"{str(num1)} x {str(num2)} = ||{str(num1 * num2)}||")

# Ask a division question
@client.tree.command(name="question_divide", description="Ask you a division question")
@commands.cooldown(1, 1, commands.BucketType.user)
async def question_divide(ctx):
    num1 = random.randrange(10, 10000)
    num2 = random.randrange(10, 10000)

    await ctx.response.send_message(f"{str(num1)} / {str(num2)} = ||{str(num1 / num2)}||")

"""Time"""
# Get the current UTC time
@client.tree.command(name="utc", description="Give you the current UTC time")
async def utc(ctx):
    await ctx.response.send_message("**UTC Time now: **"+str(str(str(datetime.datetime.utcnow()).split(".")[0]).split(" ")[1]).replace(":", " "))

"""Misc"""
# Embed a message
@client.tree.command(name="embed", description="Embed a message")
@app_commands.describe(title="Title of the embed", text="Body of the embed")
async def embed(ctx, title : str, text : str):
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
        if question == None:
            await ctx.response.send_message("Ask the magic orb something, and understand your future")
        else:
            await ctx.response.send_message(f'Hmmm, My magic orb says ,*"{random.choice(responses)}"*')
    except Exception:
        await ctx.response.send_message('Oh no! My orb just broke! Meet me after I fix it.')

# Sends the inputted message backwards
@client.tree.command(name="backward", description="Returns the inputted text backwards")
@app_commands.describe(text="Text that will be returned backwards")
async def backward(ctx, *, text : str):
    await ctx.response.send_message(text[::-1])

# Plays rock paper scissors with you
@client.tree.command(name="rps", description="Play rock, papers, scissor against the bot")
@app_commands.describe(choice="Your choice (Rock, Paper, Scissor)")
async def rps(ctx, *, choice : str):
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
    text = text.lower()
    shift %= 26
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypted = text.translate(table)
    await ctx.response.send_message(encrypted)

# Gives you your password but hashed out
@client.tree.command(name="hash", description="Use the MD5 encoding on your text")
@app_commands.describe(text="Text that will be encoded")
async def hash(ctx, *, text : str):
    await ctx.response.send_message(aternosClient.md5encode(text))

# Display your code in an embed
@client.tree.command(name="code", description="Display your code in an embed")
async def code(ctx, filename : str, description : str, code : str):
    code = code.replace(";", "\n")
    description = description.replace(";", "\n")
    fileextension = filename.split(".")[1]
    filenamepart = filename.split(".")[0]

    await ctx.response.send_message(embed=discord.Embed(
        title=filename,
        description=f"**Description**: {description}```{fileextension.lower()}\n{code}\n```",
        color=themeColor
    ))

# Search a topic on wikipedia
@client.tree.command(name="wikisearch", description="Seacrh wikipedia for a topic")
@app_commands.describe(topic="The topic you want to search for")
async def wikisearch(ctx, topic : str):
    if topic.startswith("https://"):
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

"""Administrator"""
# Kick a user
@client.tree.command(name="kick", description="Kick any user from the server")
@app_commands.describe(member="Member that will be kicked", reason="Reason on why the member is being kicked")
async def kick(ctx, member : discord.Member, *, reason : str = None):
    if ctx.user.guild_permissions.kick_members or ctx.user.id == client.owner_id:
        try:
            await member.kick(reason=reason)
            await ctx.response.send_message(embed=discord.Embed(
                title=f"{member.name}#{member.discriminator} is kicked",
                description="Reason: "+str(reason),
                colour=themeColor
            ))
        except Exception as e:
            await ctx.response.send_message(embed=discord.Embed(
                title=f"**__Error__ ❌**",
                description=e,
                colour=errorColor
            ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title=f"**__Error__ ❌**",
            description=f"You do not have permissions to kick someone",
            colour=errorColor
        ), ephemeral=True)

# Ban a user
@client.tree.command(name="ban", description="Ban any user from the server")
@app_commands.describe(member="Member that is to be banned", reason="Reason on why the member is being banned")
async def ban(ctx, member : discord.Member, *, reason : str = None):
    if ctx.user.guild_permissions.ban_members or ctx.user.id == client.owner_id:
        try:
            await member.ban(reason=reason)
            await ctx.response.send_message(embed=discord.Embed(
                title=f"{member.name}#{member.discriminator} is Banned",
                description="Reason: "+str(reason),
                colour=themeColor
            ))
        except Exception as e:
            await ctx.response.send_message(embed=discord.Embed(
                title=f"**__Error__ ❌**",
                description=e,
                colour=errorColor
            ), ephemeral=True)
    else:
        await ctx.response.send_message(embed=discord.Embed(
            title=f"**__Error__ ❌**",
            description=f"You do not have permissions to ban someone",
            colour=errorColor
        ), ephemeral=True)

"""Science"""
# The periodic table input is symbol
@client.tree.command(name="element", description="Input the symbol of any element to recieve its name")
@app_commands.describe(element="Symbol of the element")
async def element(ctx, *, element : str):
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
    elif elem == "Mo":
        await ctx.response.send_message(embed=discord.Embed(
            title="41. Molybdenum",
            color=themeColor
        ))
    elif elem == "Tc":
        await ctx.response.send_message(embed=discord.Embed(
            title="42. Technetium",
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
    elif elem == None:
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
@client.tree.command(name="elementsymbol", description="Input the name of any element to recieve its symbol")
@app_commands.describe(element="Name of the element (First letter must be capital)")
async def elementsymbol(ctx, *, element : str):
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
    elif elem == "Molybdenum":
        await ctx.response.send_message(embed=discord.Embed(
            title="41. Mo",
            color=themeColor
        ))
    elif elem == "Technetium":
        await ctx.response.send_message(embed=discord.Embed(
            title="42. Tc",
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
    elif elem == None:
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
    with open('assets/periodic_table.png', 'rb') as f:
        await ctx.response.send_message("**__Periodic table__**\n● Yellow: Alkali metals\n● Pink: Non metals\n● Dark orange: Alkali earth metals\n● Light blue: Halogens\n● Blue: Transition Metals\n● Purple: Noble gases\n● Black: Other metals\n● Red: Lanthanides\n● Grey: Metalloids\n● Green: Actinides", file=discord.File(f))

# Get the types of cell organelles
@client.tree.command(name="cell_organelles", description="Organelles are things that make up a cell")
@app_commands.describe(organelle="Types: Cell wall, Cell membrane, Nucleas, Cytoplasm, Mitochondria, Endoplasmic reticulum, Ribosomes, Golgi appratus, Chloroplasts, Vacoules, Lysomes")
async def cell_organelles(ctx, *, organelle : str):
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

"""Personal commands"""
# Set bot status
@client.tree.command(name="botstatus", description="(Requires being bot's owner) Change the bot status")
@app_commands.describe(status="Status the bot will change to (Online, DND, Idle, Offline)")
async def botstatus(ctx, status : str):
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
        elif status == "offline" or status == "invisible":
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
@client.tree.command(name="openlink", description="(Requires being bot's owner) Open a link in your browser")
@app_commands.describe(link="Link to open")
async def openlink(ctx, *, link : str):
    if ctx.user.id == client.owner_id:
        if link.startswith("https://"):
            await ctx.response.send_message("Opening "+link, ephemeral=True)
            webbrowser.open_new_tab(link)
        elif link.lower() == "ddportal":
            await ctx.response.send_message("Opening discord developer portal", ephemeral=True)
            webbrowser.open_new_tab(variables.DEVELOPER_PORTAL)
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
@client.tree.command(name="echo", description="(Requires being bot's owner) Make the bot say something")
@app_commands.describe(channelid="ID of the channel you want to send the text to", text="What the bot will respond with")
async def echo(ctx, channelid : str, *, text : str):
    if ctx.user.id == client.owner_id:
        try:
            text = text.replace(";", "\n")
            channel = client.get_channel(int(channelid))
            await channel.send(text)
            await ctx.response.send_message(embed=discord.Embed(description=":white_check_mark: Message sent!", colour=themeColor), ephemeral=True)
        except Exception as e:
            await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description=e,
            colour=errorColor
        ), ephemeral=True)
    else:
        await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description="You do now have permissions to run this command",
            colour = errorColor
        ), ephemeral=True)

# Run a python script
@client.tree.command(name="runpy", description="(Requires being bot's owner) Run a python script")
@app_commands.describe(script="The python script that is to be executed")
async def runpy(ctx, *, script : str):
    if ctx.user.id == client.owner_id:
        try:
            script = script.replace(";", "\n")
            exec(script)
            await ctx.response.send_message(embed = discord.Embed(
                title="__Execute python script__",
                description=f"```py\n{script}\n```",
                colour = themeColor
            ), ephemeral=True)
        except Exception as e:
            await ctx.response.send_message(embed = discord.Embed(
                title="__Error__ ❌",
                description=e,
                colour = errorColor
            ), ephemeral=True)
    else:
        await ctx.response.send_message(embed = discord.Embed(
            title="__Error__ ❌",
            description="You do now have permissions to run this command",
            colour = errorColor
        ), ephemeral=True)

if __name__ == "__main__":
    try:
        client.run(variables.TOKEN)
    except Exception as e:
        print("Error:",str(e))