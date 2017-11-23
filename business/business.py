class business:
    players = []
    def __init__(self):
        #Llamará a leer de la bdd y se rellenará el listado de jugadores
        self.players = []

    def dispatcher(self, message):
        understood = False
        commandParts = message.split(" ")
        if len(commandParts) < 1:
            return "Sorry, I didn't understand. Please check the help"

        if commandParts == "subscribe":
            understood = True
            return "subscribed"
        if understood == False:
            return "Sorry, I didn't understand. Please check the help"
