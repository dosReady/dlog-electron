# pip install python-docx
# pip install docx-mailmerge
import os
import sys
from docx import Document
from mailmerge import MailMerge
__dirname__ = os.path.dirname(os.path.realpath(__file__))
__parentdir__ = os.path.abspath(os.path.join(__dirname__, '..'))
appdir = f'{__dirname__}\\resources\\app.asar'
templatedir = f'{appdir}\\dist\\electron\\template'

def wordcreate():
    # 문서를 선언 
    document = Document() 
    # Write title 
    document.add_heading('Document Title', 0) 
    # Write content 
    p = document.add_paragraph('This is first paragraph') 

    # 다음과 같이 p(문단) 뒤에 특정 글자만 추가해줄 수 있다. 
    p.add_run('by').bold = True 
    p.add_run('python-docx') 
    p.add_run('-sckim.').italic = True 
    # Write list format paragraph 
    document.add_paragraph( 
        'some text for list', 
        style='ListBullet' # 점 모양 리스트 
        # style='ListNumber' # 숫자 리스트 
    ) 

    records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
    )

    # Also can add tables 
    table = document.add_table(rows=1, cols=3) 
    hdr_cells = table.rows[0].cells 
    hdr_cells[0].text = 'Qty' 
    hdr_cells[1].text = 'Id' 
    hdr_cells[2].text = 'Desc' 

    for qty, id, desc in records: 
        row_cells = table.add_row().cells 
        row_cells[0].text = str(qty) 
        row_cells[1].text = str(id) 
        row_cells[2].text = desc 
    
    # Page Breaking 
    # Automatically page break 
    document.add_page_break() 
    # Saving 
    document.save('D:\\DEVDIR\\temp\\name.docx')
    
def mailmerge():
    templatefile = None
    outputfile = None
    tempdir = os.path.abspath(os.path.join(__parentdir__, '..')) + '\\temp'

    if(sys.argv[0].find('.exe') == -1):
        templatefile = f'{templatedir}\\word\\name.docx'
        outputfile = f'{tempdir}\\word\\name_output.docx'
    else:
        templatefile = f'{__parentdir__}\\template\\word\\name.docx'
        outputfile = f'{tempdir}\\word\\name_output.docx'

    document = MailMerge(templatefile)
    document.merge(제목='아침')
    document.write(outputfile)

def test():
    print(__dirname__)
    print(__parentdir__)
    print(os.path.realpath(__file__))

def info():
    infodict = {
        '__dirname__': __dirname__,
        '__parentdir__': __parentdir__,
        'realpath': os.path.realpath(__file__)
    }
    print(infodict)

if __name__ == '__main__':
    mailmerge()