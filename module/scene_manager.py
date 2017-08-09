import os
import time
import module.loading as ld
import module.command as cmd
import data_manager as dm
from module.setup import speaker as s
from module.typing_text import textType as tt

import scene.the_beginning as firstScene


def load(ans):
    try:
        exec(ans+'.start()')
    except NameError:
        print('Error: no lavel '+ans)
    

