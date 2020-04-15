import multiprocessing as mp
import os.path
from ckiptagger import WS, POS
import re

text = []
file_list = []
seg=[]
def list_file(path):
    global text
    files = os.listdir(path)
    for file in files:
        file_list.append(file)
    # print(file_list)
#讀取文件內容
def read_content(path, file):
    f = open(path + '/' + file, 'r', encoding='utf-8')
    txt = f.readlines()[0].split("'content':")[1]
    return txt
#刪掉標點符號
def remove_punctuation(line):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    line = rule.sub('', line)
    return line

#移除小寫英文字元、數字等等(大寫的可能會是機場捷運站名，故先保留)
def word_filter(word):
    pattern = '[^a-z0-9\+\-\*\/]+'
    #     print(re.findall(pattern, word))
    return re.findall(pattern, word)

def seg_result(content):
    ws = WS('E:/DMtest/data')
    pos = POS('E:/DMtest/data')
    ws_result = ws([content])
    for j in range(len(ws_result)):
        for jj in range(len(ws_result[j])):
            try:
                if len(word_filter(ws_result[j][jj])[0]) >= 1:
                    seg.append(word_filter(ws_result[j][jj])[0])
                else:
                    pass
            except IndexError as e:
                pass
        seg_result = '\n'.join(seg)
        # print(seg)
        with open('E:/DMtest/result/' + '_' + file, 'w', encoding='utf-8') as w:
            w.write(seg_result)

if __name__=='__main__':
    paths = os.listdir('E:/DMtest/mobile01/')
    for path in paths:
        files = os.listdir('E:/DMtest/mobile01/' + path)
        print('open:', path)
        for file in files:
            content = remove_punctuation(read_content('E:/DMtest/mobile01/' + path, file))
            print('執行斷詞中: ', file)
            seg_result(content)
            print(file, '完成')

