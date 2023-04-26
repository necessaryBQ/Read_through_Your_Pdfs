import fitz
import pandas as pd
import os
import re

text_lst =[]

bbox_lst1=[]
bbox_lst2=[]
bbox_lst3=[]
bbox_lst4=[]
pageNum_lst=[]
filePath_lst=[]

global pgCount
pgCount=0

def read_each_page(pageObj,pageNum,pdfName):
    Page_each=pageObj.get_text("dict")["blocks"]
    global pgCount
    pgCount=pgCount+1
    for block_i in  Page_each:
        try:
            for lines_i in block_i['lines']:
                for spans_i in lines_i['spans']:
                    text_lst.append(spans_i['text'])
                    bbox_lst1.append(spans_i['bbox'][0])
                    bbox_lst2.append(spans_i['bbox'][1])
                    bbox_lst3.append(spans_i['bbox'][2])
                    bbox_lst4.append(spans_i['bbox'][3])
                    pageNum_lst.append(pageNum+1)
                    filePath_lst.append(pdfName)
        except:
            print(pdfName,pageNum)
            pass
			
def read_allPdf(filepath):
    doc = fitz.open(filepath)

    filename=re.findall(r'.*\\(.*)$',file_path)[0]

    print(filename)
    for i in range(0,len(doc)):
        page = doc[i]

        read_each_page(page,i,filename)

rootdir = r'C:\Users\emmjiang\xxxx' #Alt_Text
list_pdfs=[]
for file in os.listdir(rootdir):
    pdf_file = os.path.join(rootdir, file)
    print(pdf_file)
    list_pdfs.append(pdf_file)


for file_path in list_pdfs:
    
    if file_path[-4:-1]=='.pd':
        
        filename=re.findall(r'.*\\(.*)$',file_path)
        print(filename)
        read_allPdf(file_path)

result_dict = {'text':text_lst,'bbox1':bbox_lst1,
               'bbox2':bbox_lst2,'bbox3':bbox_lst3,'bbox4':bbox_lst4,'PageNum':pageNum_lst,'filePath':filePath_lst}


a = pd.DataFrame(result_dict)
a.to_csv("textnewAll_122pdfs_11_09.csv", index=False)


## for analysis purpose:
len(bbox_lst4)
len(filePath_lst)
pgCount
