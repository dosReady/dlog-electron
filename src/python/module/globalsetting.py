import sys
import os

class GlobalSetting(object):
    __mode__ = None if len(sys.argv) < 2 else sys.argv[1]
    __prod_dir__ = os.path.dirname(os.path.realpath(__file__)) 
    __dev_dir__ = os.path.abspath(os.path.join(__prod_dir__, '../../'))
    __this_dir__ = __prod_dir__ if __mode__ == 'production' else __dev_dir__
    __conf_file__ = f'{__this_dir__}\\conf\\options.json'

    @staticmethod
    def echoprint():
        print('echo')