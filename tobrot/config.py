from tobrot.sample_config import Config

class Config(Config):
    TG_BOT_TOKEN= "1578450031:AAEi-BgP28oOS5P4LxhLSu0TlXJ8CcoZSaA"
    APP_ID = "2699106"
    OWNER_ID = "1218670347"
    API_HASH = "dbc0763f2ec0505c88130f3ab7b64484"
    AUTH_CHANNEL = [-1001153183002]
    INDEX_LINK = "https://torrentleech.torrentleech-gdrive.workers.dev"
    GLEECH_COMMAND = "gleech@Torrentsgspfirbot"
    YTDL_COMMAND = 'ytdl@Torrentsgspfirbot'
    TELEGRAM_LEECH_COMMAND_G = "tleech@Torrentsgspfirbot"
    CLONE_COMMAND_G = "gclone@Torrentsgspfirbot"
    PYTDL_COMMAND_G = "pytdl@Torrentsgspfirbot"
    STATUS_COMMAND = "status "
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    LEECH_COMMAND = "leech@Torrentsgspfirbot"
    #fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    # Do not delete [DRIVE] #do not delete [DRIVE] but replace remaining part with yours data..if more data use common sense
    RCLONE_CONFIG = """
[DRIVE]
type = drive
scope = drive
token = {"ac—fill—yours—data—jNc3MpTRy2PuGD_Lvsodct---fill--yours---0-18T12:11:26.58411451Z"}
team_drive = 0ABS@gautamk9PVA"""
