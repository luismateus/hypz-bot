import discord
import config
####--------------------- COMMAND HANDLER --------------------------####

class CommandHandler:

    def __init__(self,client):
        self.client = client
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)
    
    def command_handler(self, message):
        for command in self.commands:
            if message.content.startswith(command["trigger"]):
                args = message.content.split(' ')
                if args[0] ==  command["trigger"]:
                    args.pop(0)
                    if command['args_num'] == 0:
                        return self.client.send_message(message.channel,str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >=  command["args_num"]:
                            return self.client.send_message(message.channel,str(command['function'](message, self.client, args)))
                            break
                        else:
                            return self.client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
                            break
                else:
                    break


####--------------------- INITIALIZE CLIENT AND COMMAND HANDLER --------------------------####
client = discord.Client()
token = config.token
ch = CommandHandler(client)

####--------------------- LISTENERS --------------------------####
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)
        print('Discord.py Version: {}'.format(discord.__version__))
    except Exception as e:
        print(e)    

@client.event
async def on_message(message):
    
    # if the message is from the bot itself ignore it
    if message.author == client.user:
        pass
    else:
        
        # try to evaluate with the command handler
        try:
            await ch.command_handler(message)
            
        # message doesn't contain a command trigger
        except TypeError as e:
            pass
        
        # generic python error
        except Exception as e:
            print(e)



####--------------------- BOT COMMANDS --------------------------####

# Argument One: {}'.format(message.author, args[0])

def hello_function(message, client, args):
    try:
        a = str(message.author).split('#')
        return 'Fuck you {}, call me when you have something usefull to say, you dumb shit!'.format(a[0])
    except Exception as e:
        return e
ch.add_command({
    'trigger': '!hello',
    'function': hello_function,
    'args_num': 0,
    'args_name': ['string'],
    'description': 'Will respond hello to the caller'
})


def commands_command(message, client, args):
    try:
        coms = '**Commands List**\n'
        for command in ch.commands:
            coms += '**{}** : {}\n'.format(command['trigger'], command['description'])
        return coms
    except Exception as e:
        print(e)
ch.add_command({
    'trigger': '!commands',
    'function': commands_command,
    'args_num': 0,
    'args_name': [],
    'description': 'Prints a list of all the commands!'
})


####--------------------- RUN --------------------------####
# start bot
client.run(token)