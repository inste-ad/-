# -*- coding:utf-8 -*-
import re
import requests
import os
import sys
from multiprocessing import Pool #多进程
import logging
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
path = os.path.join(os.getcwd()+os.sep+'CS166'+os.sep+'slides'+os.sep)
#TODO：  断点重连部分需要解决。现在下载还是不完整

def download_file(url,path,filename):
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    # NOTE the stream=True parameter
    try:
        r = requests.get(url, timeout = 10000, stream=True)
    except requests.exceptions.ConnectionError:
        print('【错误】当前文件无法下载')

    
    total_size = int(r.headers['Content-Length'])
    temp_size = 0
    print(path,filename)
    with open(path+filename, 'wb') as f:
        
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep- alive new chunks
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                
                #############花哨的下载进度部分###############
                done = int(50 * temp_size / total_size)
                # 调用标准输出刷新命令行，看到\r回车符了吧
                # 相当于把每一行重新刷新一遍
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()

    return filename


def find_url(html, keyword, reg):
    #找到下载url
    down_url= re.findall(reg, html, re.S)
    if down_url != []:
        print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
        return down_url
    else:
        print("没有找到关键词，下载失败")
        return []

def download_process(down_url,keyword):
    
    url = 'http://web.stanford.edu/class/cs161/'+ down_url
    
    filename =''.join(re.findall("Lecture\d{1,2}[^/]*\."+keyword,down_url,re.S))

    print('正在下载' + filename + '个文件，图片地址:' + path+filename)
 

    download_file(url,path,filename)



    


#cs 161 下载地址 http://web.stanford.edu/class/cs161/Lectures/Lecture1/Lecture1.pptx
#cs  166 下载地址 https://web.stanford.edu/class/archive/cs/cs166/cs166.1146/lectures/00/Slides00.pdf
if __name__ == '__main__':
    word = input("Input key word: ")
    #url = 'http://web.stanford.edu/class/cs161/schedule.html' #获取下载地址的url 需要分析
    #url = input("Input url:")
    url = 'https://web.stanford.edu/class/archive/cs/cs166/cs166.1146/'
    #reg = input("Input regex:")
    reg = '(?<=a href=").*Slides\d*.pdf(?=">)'
    '''
    cs161 reg = '(?<=a href=").*Slides\d*[^/]*.pdf(?=">)'
    cs166 reg = '(?<=a href=").*Slides\d*.pdf(?=">)'
    '''
    result = requests.get(url)
    
    down_url = find_url(result.text, word,reg) # 获取下载地址
    
    if down_url != []:
    #多进程
        p = Pool(5)
        print(down_url)
        for i in down_url:
            p.apply_async(download_process,args=(i,word,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
    else:
        print("NO download link found！")






