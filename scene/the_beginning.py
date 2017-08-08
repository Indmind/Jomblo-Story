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
    st('Pada suatu hari', .2)
    time.sleep(.5)
    ld.createDots(5, .5)
    nl(2)
    st('Kamu sedang berjalan-jalan di taman kota...')
    st('Menikmati suasana kota di hari minggu yang cerah...')
    st('Berjalan menelusuri trotoar kota yang indah...')
    time.sleep(2)
    nl(2)
    st('GUBRAKK!!!!......', .01)
    time.sleep(1.5)
    nl(2)
    st('Kamu tidak sengaja menabrak seorang cewe')
    nl(1)
    chatl('cewe', 'eh...')
    chatl('kamu', 'maaf maaf...')
    chatl('cewe', 'iya gpp, santai aja...')
    nl(2)
    st('5 menit kemudian', .15)
    ld.createDots(5, .3)
    nl(2)
    st('dia kecelakaan....')
    st('tamat....')
    nl(1)

