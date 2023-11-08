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
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "AQBpWydV1UKceBoLI2tvQUx0C3XtW25fJP9YasbsBnZrNSIRgviUB9WmAZiZ65-KS9GELLBygNdJ3lkhVvADlXSiTibGPjUkpKKnXg7xrxIOKXRFzHyBav9bjC-Vv_J-0Ze_NSPlU8hHiGXM3VctFNCYyM6pZOYpe8FmQo-tsFVvbot4mVHNMU2wNWvJa7F-0qQ5eol8S0N8NkXFqBdbyRTEruJyYUQU8A5uJXDqvoglJbsmHEp3wmTX_oG83DOeCLTajf74nc-J4o7qCKqLWMUiRZrAE1h-sf0lJJXQVRSjZF3RmqpguKflZz0THRs23sQEc6heoqsaTivN7kNuE7WSUbAx_QA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
