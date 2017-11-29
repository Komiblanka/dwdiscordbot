from persistance import *
from business.player import player

class dispatcher:
    def __init__(self):
        #Llamará a leer de la bdd y se rellenará el listado de jugadores
        self.players = []

    def dispatcher(self, discordMessage):
        understood = False
        message = discordMessage.content
        commandParts = message.split(" ")

        if len(commandParts) < 1:
            return "Sorry, I didn't understand. Please check the help"

        if commandParts[1] == "subscribe":
            returnMessage = self.subscribePlayer(discordMessage)
            understood = True
            return returnMessage

        if commandParts[1] == "printPlayerData":
            returnMessage = self.printPlayerData(discordMessage)
            understood = True
            return returnMessage

        if understood == False:
            return "Sorry, I didn't understand. Please check the help"

    def subscribePlayer(self, message):
        playerToSubscribe = player(message.author,"", message.timestamp) 
        messageToReturn = playerDao.savePlayer(playerToSubscribe)
        return messageToReturn 

    # Method used for debugging players from database
    def printPlayerData(self, message):
        loadedPlayer = playerDao.loadPlayer(message.author)
        return loadedPlayer.lastCommandDate.day

