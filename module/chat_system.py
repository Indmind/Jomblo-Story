import os
import time
import module.loading as ld
import module.command as cmd
import data_manager as dm
from module.setup import speaker as s
from module.typing_text import textType as tt

def chat_line(name, chat):
    time.sleep(.2)
    s(name)
    ld.deGa()
    tt(chat)
    ld.deGa()
