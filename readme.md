#示例
    cs161 reg = '(?<=a href=").*Slides\d*[^/]*.pdf(?=">)'
    cs166 reg = '(?<=<li><a href=").{1,20}/Slides\d*.pdf(?=">)'
    cs61A reg = '(?<=a href=")slides/.{1,25}\.(pdf|py)(?=">)'
    cmu network reg = '(?<=a href=")slides/.{1,25}\.pdf(?=">)'
    cs61B reg = '(?<=a href=")materials/.{1,20}\.pdf(?=")'

#main中的url
    #url = 'http://web.stanford.edu/class/cs161/schedule.html' #获取下载地址的url 需要分析
    #url = 'https://web.stanford.edu/class/archive/cs/cs166/cs166.1146/'
    #url = 'http://www-inst.eecs.berkeley.edu/~cs61a/fa11/61a-python/content/www/index.html' cs61A
    #url = 'https://computer-networks.github.io/sp19/lectures.html' 
    #url = 'https://inst.eecs.berkeley.edu/~cs61b/fa19/' cs61A

#CS234 reinforcement learning
    url= r'http://web.stanford.edu/class/cs234/slides/'
    reg = '(?<=a href=").{1,20}\.pdf(?=")'  

# cmu 15-445 數據庫
    url = https://15445.courses.cs.cmu.edu/fall2019/schedule.html
    reg ='(?<=href="\.).{1,30}\.pdf(?=")'
    down_url = https://15445.courses.cs.cmu.edu/fall2019  +  /slides/23-distributedoltp.pdf

# cmu 15-410 操作系統
    url = 'https://www.cs.cmu.edu/~410/lecture.html'
    reg = '(?<=a href=").{1,20}\.pdf(?=")'
    down_url = https://www.cs.cmu.edu/~410/ + lectures/L04_Process.pdf

# cmu 15-213 计算机系统 csapp
    url ='http://www.cs.cmu.edu/afs/cs/academic/class/15213-f19/www/schedule.html'
    reg = '(?<=a href=").{1,51}\.pdf(?=")'
    http://www.cs.cmu.edu/afs/cs/academic/class/15213-f19/www/ + recitations/recitation03-datalab.pdf