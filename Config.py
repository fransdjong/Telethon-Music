import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6020826394:AAGjQMZYOUmoeu9CHkeACoiJc2xUZQG-hpI)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOLgBuz_L3hJ8eJ8vFH9hdd0cnQFtaDCAh_tAiph_vGfbZ1UUJ4B1o2Dd7lotHi7z55-vfv004OF3LeqXFGecTBeBTTmhtgzigqjdENsw9LsWqE2D4J3YC4E7hB1kcbudi6E1czHavNhbB9P6PamQL7cWgz_rtd7uZ8gXI-lTVgWZCcTz9B9hIxHBiBXD6WvgGAcYYTaCXUKjgLhiMLUJb3xGjWMlCVm4xJVDPEBuImr-S_wFJkpfZBWqvVBfwC1paDS4NFUcwCzVjxLogduANS6smiIY_OisuBneMR5_8NhEhutttUAFzoqQA4z9cYS1aReAzgK5EhEryrPEswtgulO_c18=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
