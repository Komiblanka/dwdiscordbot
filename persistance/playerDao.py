from business import *
from business.player import player
import sqlite3
from datetime import datetime

class playerDao:
    def savePlayer(playerToSave):
        # Connecting to the database file
        sqlite_file = "discordbot/persistance/database/discordbot.db"

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        
        print("Saving player to database")
        
        cmd = "insert into players (discordid, telegramid, lastCommandDate) values (?, ?, ?);"
        c.execute(cmd, (str(playerToSave.discordid), playerToSave.telegramid, playerToSave.lastCommandDate))

        conn.commit()
        return "Subscribed!"

    def loadPlayer(playerToLoad):
        # Connecting to the database file
        sqlite_file = "discordbot/persistance/database/discordbot.db"

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        print("Loading player from database")

        cmd = "select * from players where discordid = ?;"
        c.execute(cmd, (str(playerToLoad),))

        data = c.fetchall()
        if len(data) == 1:
            loadedPlayer = data[0]
        # 2017-11-29 22:03:15.370000
            datetimeObject = datetime.strptime(loadedPlayer[3], "%Y-%m-%d %H:%M:%S.%f")
            returnPlayer = player(loadedPlayer[1], loadedPlayer[2], datetimeObject) 

            return returnPlayer 

        else:
            return None
