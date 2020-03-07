# -*- coding:utf-8 -*-
import re
import requests
import os
import sys
from multiprocessing import Pool #多进程
import logging
import io

#TODO:  断点重连部分需要解决。现在下载还是不完整
#TODO:  使用beautiful soup或者lxml 来优雅地处理html数据。 
#NOTE: 使用前需要修改的是 reg， url 和downprocess里的url

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

def download_process(down_url,keyword,path):
    #cs161 url = 'http://web.stanford.edu/class/cs161/'
    #cs 166 https://web.stanford.edu/class/archive/cs/cs166/cs166.1146/lectures/00/Slides00.pdf
    url = r'https://15445.courses.cs.cmu.edu/fall2019'
    url = url+down_url
    print(url)
    filename =  down_url.split('/')[-1]
    print (filename)
    print('正在下载' + filename + '个文件，图片地址:' + path+filename)
    download_file(url,path,filename)



#cs 161 下载地址 http://web.stanford.edu/class/cs161/Lectures/Lecture1/Lecture1.pptx
#cs  166 下载地址 https://web.stanford.edu/class/archive/cs/cs166/cs166.1146/lectures/00/Slides00.pdf
if __name__ == '__main__':
    # keyword = input("Input file type: ")
    # url = input("Input url:")#http://www-inst.eecs.berkeley.edu/~cs61a/fa11/61a-python/content/www/index.html
    # reg = input("Input regex:")
    
    keyword="pdf"
    url= r'https://15445.courses.cs.cmu.edu/fall2019/schedule.html'
    reg = '(?<=href="\.).{1,30}\.pdf(?=")'  

    result = requests.get(url)
    down_url = find_url(result.text.encode('ISO-8859-1').decode('utf-8'), keyword,reg) 
    #  查看resul.encode 来查看编码方式。填入相应的编码解码方式。
    #获取下载地址ca
    path_name = input('储存文件夹名字')
    path = os.path.join(os.getcwd()+os.sep+path_name+os.sep+keyword+os.sep)
    if down_url != []:
        #单进程
        # for i in down_url:
        #     download_process(i,keyword,path)
        #多进程
        p = Pool(5)
        print(down_url)
        for i in down_url:
            p.apply_async(download_process,args=(i,keyword,path))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
    else:
        print("NO download link found！")






