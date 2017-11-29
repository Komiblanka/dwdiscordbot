from persistance import *

class player:
    discordid = ""
    telegramid = ""
    lastCommandDate = ""

    def __init__(self, discordid, telegramid, lastCommandDate):
        self.discordid = discordid
        self.telegramid = telegramid
        self.lastCommandDate = lastCommandDate

    def savePlayer():
        print("Saving player")
        playerDao.savePlayer(self)

    def loadPlayer():
        playerDao.loadPlayer(self)
        print("Loading Player")
