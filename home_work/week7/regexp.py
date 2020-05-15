import re

predl = "a on an the in into the"

f=open('html.txt')


html = ''
for i in re.findall(r'[a-z]+',re.sub(r'\s','',f.read().lower())):
    html += '<'+i+'.*?>'+'|'



s=''
for i in predl.split():
    s+='\s'+i+'\s'+'|'

str = "<a sdfsdfsdf>I have an article the <a"

res = re.sub(re.compile(html[:-1]),'',re.sub(re.compile(s[:-1]),' ',str))

print(res)
