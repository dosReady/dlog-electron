from docx import Document
from mailmerge import MailMerge

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
    document.save('E:\\temp\\name.docx')
def mailmerge():
    document = MailMerge('E:\\temp\\name.docx')
    document.merge(제목='테스트')
    document.write('E:\\temp\\name_output.docx')

if __name__ == '__main__':
    mailmerge()