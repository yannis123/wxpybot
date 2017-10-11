from wxpy import *
from bot.models import Friend


class Wxbot(object):
    """docstring for ClassName"""
    def _init__(self):
        self.bot=Bot(cache_path=True)

    def get_myfriends():
        return self.bot.friends()

