import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6435409185:AAG9JSM6BXy8spEdkZ5O-_W52xel3HGE5IM")
    TELEGRAM_API = 1923471
    OWNER = os.environ.get("OWNER", "880087645")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "jasuran2p0")
    PASSWORD = os.environ.get("PASSWORD", "asuran")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://leecher:leecher@cluster0.606mkpi.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002119311182")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "AQAaiBkATgE1YOnPwVM0OTdcrdq_ElOY4XKjAvPTZEyUWM6kRa-6jWHvvxA3PwTb0H78m2-WJ_ip3-54xnmkxZSFZQBZcJGKlU9at0KVw46na33BD1ZOSZbTF0JhSh4OLAV4LzokF5S0IQgWopVOC7OgJPlG8oEB3AHb9ytCIb56DxxTdUvp1c1kAseR8CDEAYneOXIAHmldvdlXqBJqr4SpGfoH2rI6D_mBu_SUhHyYFY4-j1T41vAQEadzYFW6sWnOQeNFg8yPiZqJxjb0JJv8DCLgaif4kKm3oEA_Wlbi47i-iDxc5lUmFohidp48IBj0l7b4-H1ieXbHYIK15iu9j8wafAAAAABRsDH9AA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
