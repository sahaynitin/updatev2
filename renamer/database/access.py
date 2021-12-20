# (c) @AbirHasan2005

from configs import Config
from renamer.database.db import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
