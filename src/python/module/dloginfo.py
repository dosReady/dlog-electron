import os
import sys
import json

__dirname__ = os.path.dirname(os.path.realpath(__file__))
__parentdir__ = os.path.abspath(os.path.join(__dirname__, '..'))

def info():
    infodict = {
        '__dirname__': __dirname__,
        '__parentdir__': __parentdir__,
        'realpath': os.path.realpath(__file__),
        'argv': sys.argv,
        '__name__': __name__
    }
    print(json.dumps(infodict))
    
if __name__ == '__main__':
    info()