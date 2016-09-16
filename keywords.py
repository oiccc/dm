# encoding=utf-8
import sys
sys.path.append('../')

import os
import jieba

jieba.load_userdict("userdict.txt")
import jieba.analyse
from optparse import OptionParser



USAGE = "usage:    python extract_tags_with_weight.py [file name] -k [top k] -w [with weight=1 or 0]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

if opt.withWeight is None:
    withWeight = False
else:
    if int(opt.withWeight) is 1:
        withWeight = True
    else:
        withWeight = False

content = open(file_name, 'rb').read()



tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)


if withWeight is True:
    for tag in tags:
        a = os.popen('grep -o '+tag[0].encode("utf-8")+' test.txt|wc -l')     #加入统计词数功能
#        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
        c = int(a.read())
        print("tag: %s\t\t weight: %f\t\t count: %d" % (tag[0],tag[1],c))

        
    
else:
    print(",".join(tags))
