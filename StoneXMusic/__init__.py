from StoneXMusic.core.bot import Stoney
from StoneXMusic.core.dir import dirr
from StoneXMusic.core.git import git
from StoneXMusic.core.userbot import Userbot
from StoneXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Stoney()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
