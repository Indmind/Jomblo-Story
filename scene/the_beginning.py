import os
import time
import module.loading as ld
import module.command as cmd
import module.character_loader as cl
import data_manager as dm
from module.chat_system import chat_line as chatl
from module.setup import speaker as s
from module.text_type import textType as tt

def start():
    os.system('clear')
    time.sleep(.5)
    tt('Pada suatu hari', .2)
    time.sleep(.5)
    ld.createDots(5, .5)
    ld.deGa()
    tt('\n\n\nKamu sedang berjalan-jalan di taman kota...')
    ld.deGa()
    tt('\nMenikmati suasana kota di hari minggu yang cerah...')
    ld.deGa()
    tt('\nBerjalan menelusuri trotoar kota yang indah...')
    time.sleep(2)
    tt('\n\n\nGUBRAKK!!!!......', .01)
    ld.deGa()
    tt('\n\n\nKamu tidak sengaja menabrak seorang cewe\n')
    chatl('cewe', 'eh...')
    chatl('kamu', 'maaf maaf...')
    chatl('cewe', 'iya gpp, santai aja...')



