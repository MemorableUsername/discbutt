import discord
import random
import config
from butter import score_sentence
from butter import buttify

from discord.ext.commands import Bot

c = config.config()
bot = Bot(command_prefix=c['command_prefix'])


@bot.command()
async def butt(*args):
    if args:
        return await bot.say(buttify(' '.join(args), min_words=1))
    else:
        return await bot.say("can't butt the unbuttable!")


@bot.event
async def on_message(message):
    if message.author != bot.connection.user: # prevent the bot from triggering itself with random responses
        if message.clean_content[0] == c['command_prefix']:
            return await bot.process_commands(message)
        else:
            if random.random() < c['response_rate']:
                return await bot.send_message(message.channel, buttify(message.clean_content, min_words=1))

@bot.command()
async def debutt(*args):
    """.debutt <text> -- provides debug butting info for a line of text"""

    result = 'response rate set at `' + str(c['response_rate']) + '/1.0`'

    if args:
        message = ' '.join(args)
        sent, score = score_sentence(message)

        result += ';\n{0}: '.format(score.sentence())
        for i, word in enumerate(sent):
            if score.word(i) == 0:
                result += '-'.join(word) + '(0) '
            else:
                result += '-'.join(word) + '({0}: {1}) '.format(
                    score.word(i), score.syllable(i))

    return await bot.say(result)

bot.run(c['token'])