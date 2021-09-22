from mycroft import MycroftSkill, intent_file_handler
import pafy
import vlc


class DragonMaid(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('maid.dragon.intent')
    def handle_maid_dragon(self, message):
        self.speak_dialog('maid.dragon')
        url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
		video = pafy.new(url)
		best = video.getbest()
		playurl = best.url
		Instance = vlc.Instance()
		player = Instance.media_player_new()
		Media = Instance.media_new(playurl)
		Media.get_mrl()
		player.set_media(Media)
		player.play()


def create_skill():
    return DragonMaid()

