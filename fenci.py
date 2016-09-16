# encoding=utf-8
import jieba
import re

list = []

def flushtxt():
    
    with open('ok.txt', 'w') as f:
        f.write('')
    with open('rec2.txt', 'w') as f:
        f.write('')
    with open('test.txt', 'w') as f:
        f.write('')
        
def removename():
    with open('rec.txt', 'r') as f:
        for i in f.readlines():
            i = i.strip('\n')       
            strinfo = re.compile("(\[.*\]).*")
            result = strinfo.findall(i)   
            print i
            print result
            for t in result:
                i = i.replace(t,"",1)
                i = i.strip(":")
                i = i.decode("utf-8",'ignore')
                print i
                with open('test.txt', 'a+') as d:
                    print>>d,i.encode("utf-8")

        

def fenci():
    with open('ok.txt', 'w') as f:
        f.write('')
    with open('test.txt', 'r') as f:
        for i in f.readlines():
            seg_list = jieba.cut(i, cut_all=False)
            a = ("/ ".join(seg_list))    #unicode
            utf8string = a.encode("utf-8")   #str

            with open('ok.txt', 'a+') as f:
                print >> f,utf8string.strip("\n")
  

fenci()
