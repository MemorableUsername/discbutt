import inspect
import json
import os

if not os.path.exists('config'):
    open('config', 'w').write(inspect.cleandoc(
        r'''
        {
          "command_prefix": ".",
          "response_rate": 0.1,
          "token": "PUT YOUR BOT'S USER TOKEN HERE"
        }''') + '\n')


def config():
    try:
        return json.load(open('config'))
    except ValueError as e:
        print(' ERROR: malformed config!', e)
