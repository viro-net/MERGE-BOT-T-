import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "1923471")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "fcdc178451cd234e63faefd38895c991")
    TELEGRAM_API = os.environ["TELEGRAM_API"]
    OWNER = os.environ.get("OWNER", "880087645")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "jasuran2p0")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://video:video@cluster0.gp0rn.mongodb.net/?retryWrites=true&w=majorit")
    LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
