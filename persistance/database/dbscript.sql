PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE players(id integer primary key autoincrement,
discordid string,
telegramid string,
lastCommandDate string);
COMMIT;
