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
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "AQAaiBkAuw3lf8-ZdKhp0I4LsYh__v-nmBcApt5jiO_R1heFGAf-iJyKikc1xcwC1-mK5aT-vqT3he-aaOYpU1sHt9b1pjTByVZwlCCZkOl5XbWhc1kUOs1Tqg1hQlX35hZkNcu0UfBLnGsfUFy1V19C6KeQkq9210DTzmq0Ol8eOGtTgXT-3Tqw2fAMUpSnSU-c869_hmHlHbecSkHCeBy1KtZNrLXt_D1I9KLV-qf-Puh2FEWNA3NfT-0sdnRI46gOl4BHOQNT8wcUV1VQzmZVHobA3FV2cnztOLHipb986bP-0czB5B5GXOZ99ShnQisn4zFGNUXpOs4cl4-nGO-wbCdkIQAAAABRsDH9AA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
