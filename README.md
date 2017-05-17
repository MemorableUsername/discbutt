# discbutt
Another Buttbot for Discord

A Python3 Buttbot. We can't let Buttbot die with IRC now, can we? I'm not ready for that. The world isn't ready for
that.

Installation
============

I recommend making a virtualenv and activating it. Remember to make sure it's a Python3 virtualenv.

```
git clone https://github.com/MemorableUsername/discbutt
pip install -r requirements.txt
```

Running
=======
```
python bot.py
```

The initial run will crash, but generate a file `config` in the cwd. Add your bot's user token to this. You *did* set
up a discord bot user, didn't you?

Once you've added the token, run the command again and the bot will launch.

How to add the bot to your server
=================================
On a computer where you have logged into discord, open this link:
https://discordapp.com/oauth2/authorize?client_id=[*YOUR BOT'S CLIENT ID HERE*]&scope=bot&permissions=0

If you have Manage Server permissions you'll be able to add your bot.