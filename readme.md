#示例
    cs161 reg = '(?<=a href=").*Slides\d*[^/]*.pdf(?=">)'
    cs166 reg = '(?<=<li><a href=").{1,20}/Slides\d*.pdf(?=">)'

#main中的url
    #url = 'http://web.stanford.edu/class/cs161/schedule.html' #获取下载地址的url 需要分析
    #url = 'https://web.stanford.edu/class/archive/cs/cs166/cs166.1146/'