# pip install python-docx
# pip install docx-mailmerge
import os
import sys
import json
from docx import Document
from mailmerge import MailMerge

# global 변수
__mode__ = sys.argv[1]
__prod_dir__ = os.path.dirname(os.path.realpath(__file__)) 
__dev_dir__ = os.path.abspath(os.path.join(__prod_dir__, '..'))
__this_dir__ = __prod_dir__ if __mode__ == 'production' else __dev_dir__
__conf_file__ = f'{__this_dir__}\\conf\\options.json'
    
def mailmerge():
    f = open(__conf_file__,'r')
    data = json.loads(f.read())
    data['argv'] = []
    
    print(json.dumps(data))
    document = MailMerge(data['tempdir']+'\\name.docx')
    document.merge(제목='낼출근..')
    document.write(data['exportdir'] + '\\output123.docx')

if __name__ == '__main__':
    mailmerge()