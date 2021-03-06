import os
import time
import module.loading as ld
import module.scene_manager as sm
import module.character_loader as cl
import module.os_manager as om
import data_manager as dm
from module.typing_text import textType as tt

cur_path = os.path.dirname(__file__)
user_info = dm.getUserInfo()

def SplashLoad():
    try:
        om.clear()
        print('   __                  _     _         __ _                   ')
        print('   \ \  ___  _ __ ___ | |__ | | ___   / _\ |_ ___  _ __ _   _ ')
        print('    \ \/ _ \|  _ ` _ \|  _ \| |/ _ \  \ \| __/ _ \|  __| | | |')
        print(' /\_/ / (_) | | | | | | |_) | | (_) | _\ \ || (_) | |  | |_| |')
        print(' \___/ \___/|_| |_| |_|_.__/|_|\___/  \__/\__\___/|_|   \__, |')
        print('                                                        |___/ ')
        print('\n                           Main Menu\n')
        print('                      1. Mulai Story Baru')
        print('                      2. Lanjutkan Story')
        print('                      3. Keluar\n')
        menu = input('                               ')
        if menu == '1' or menu == 'baru':
            sm.load('firstScene')
            sm.load('secondScene')
        elif menu == '2' or menu == 'lanjut':
            cs = dm.loadSavedProgress()
            if not cs == False:
                sm.load(cs)
            else:
                print('             Kamu tidak memiliki simpanan permainan')
                input('                 Tekan enter untuk melanjutkan')
                SplashLoad()
        elif menu == '3' or menu == 'keluar':
            exit(0)
        elif menu == 'char':
            print(cl.Mia())
        else:
            print('                          Menu salah...')
            input('                  Tekan enter untuk melanjutkan...')
            SplashLoad()
    except KeyboardInterrupt:
        print('\nForce Stopped by User...\n')
        exit(0)
    except EOFError:
        print('\nForce Stopped by User...\n')
        exit(0)

if __name__ == '__main__':
    SplashLoad()
