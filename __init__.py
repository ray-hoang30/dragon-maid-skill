from mycroft import MycroftSkill, intent_file_handler


class DragonMaid(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('maid.dragon.intent')
    def handle_maid_dragon(self, message):
        self.speak_dialog("playing it")


def create_skill():
    return DragonMaid()

