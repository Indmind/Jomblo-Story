import os
import time
import module.loading as ld
import module.command as cmd
import module.character_loader as cl
import module.os_manager as om
import data_manager as dm
from module.story_env import chat_line as chatl
from module.story_env import story_telling as st
from module.story_env import new_line as nl
from module.setup import speaker as s
from module.typing_text import textType as tt

def start():
    om.clear()
    time.sleep(.5)
    st("Pada keesokan harinya....", .2)
    nl(2)
    st("Kamu melayat di rumahnya dan kamu berkenalan dengan adiknya dan kamu mulai suka padanya dan itu membuatnya cemburu hehe")
    