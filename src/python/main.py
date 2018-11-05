# global 변수
import importlib
import sys
import json
from module.globalsetting import GlobalSetting

def main():
    '''
    meta = {
        'module': 'module.globalsetting',
        'type': 'class',
        'clz': 'GlobalSetting',
        'fn': 'echoprint',
        'args': None
    }
    '''
    meta = json.loads(sys.argv[2])
    m = importlib.import_module(meta['module'])
    fn = None

    if meta['type'] == 'class':
        clz = getattr(m, meta['clz'])
        fn = getattr(clz, meta['fn'])
    else:
        fn = getattr(m, meta['fn'])
    fn(json.loads(meta['args'])) if meta['args'] != 'none' else fn()
        

if __name__ == '__main__':
    main()