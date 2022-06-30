# -*- coding: utf-8 -*- 

##!pip install googletrans==4.0.0-rc1
##!pip install deep-translator
##!python -m pip install requests beautifulsoup4

import requests,re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#from googletrans import Translator
#translator = Translator()

from deep_translator import GoogleTranslator
#translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig

uAgent = {'User-Agent': "Mozilla/5.0 (Linux; Android 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",'Referer': 'https://www.google.com/'}
se = requests.Session()
res = se.get(url,headers=uAgent)
sch = urlparse(res.url).scheme
base = urlparse(res.url).netloc
import os
urldirname = os.path.dirname(res.url)

import pathlib
basepath = pathlib.Path(res.url)

#import os
#result = os.popen("curl -s " + url).read()
#sch = urlparse(url).scheme
#base = urlparse(url).netloc
#soup = BeautifulSoup(result, "html.parser")
soup = BeautifulSoup(res.text, "html.parser")
res.close()
del se

ptag_list_0 = soup.find_all('p')
h6tag_list_0 = soup.find_all('h6')
title_list_0 = soup.find_all('title')
print(title_list_0[0].text)
title = re.sub(r'\s','_',title_list_0[0].text)

nullch = '𓄃'
#nullch = '𓂃'
code_tag = soup.find_all('code')
code_counter = 0
code_contents = []
if len(code_tag) > 0:
    for index,tag in enumerate(code_tag):
        print(index,tag)
        if re.match(r'\<code(\S|\s).*?\>',str(tag)):
            code_contents.append(str(tag))
            strip_tag = re.sub(r'\<code(\S|\s)*?>',f"{nullch}{code_counter}{nullch}",str(tag))
            strip_tag = re.sub(r'\<\/code\>',f"{nullch}{nullch}{code_counter}{nullch}{nullch}",strip_tag)
            code_tag[index].string = strip_tag
            print(index,strip_tag)
            code_counter += 1

link = soup.find_all('link')
if len(link) > 0:
    for index,v in enumerate(link):
        if not v.has_attr('rel'):
            continue
#        print(index,v['rel'])
        if v['rel'] == ["stylesheet"]:
            #css location
            #print(type(v))
            if not v.has_attr('href'):
           #if ('href') in v:
                continue
#            print(v['href'])
            if (bool(re.match(r'^http',v['href']))==False):
                print(v['href'])
                if (bool(re.match(r'^\/',v['href']))==True):
#                    link[index]['href'] = sch + "://" + base + v['href']
                    link[index]['href'] = urldirname + v['href']
                else:
                    if re.match(r'^\.',v['href']):
                        temp_work = pathlib.Path(str(basepath) + '/'+ v['href']).resolve()
                        link[index]['href'] = re.sub(rf"^\S+?(?={base})",sch + "://",str(temp_work))
                    else:
#                        link[index]['href'] = sch + "://" + base + '/' +v['href']
                        link[index]['href'] = urldirname + '/' +v['href']
                print(link[index]['href'])

image = soup.find_all('img')
if len(image) > 0:
    for index,im in enumerate(image):
#        print(index,im)
        #if im['alt'] == "Bellingcat" or im['alt'] == "GIJNlogo":
        if not im.has_attr('src'):
            continue
        if (bool(re.match(r'^http',im['src']))==False):
            print(im['src'])
        #    image[index]['src'] = 'https://www.bellingcat.com' + im['src']
            if (bool(re.match(r'^\/',im['src']))==True):
#                image[index]['src'] = sch + '://' + base + im['src']
                image[index]['src'] = urldirname + '/' + im['src']
            else:
                if re.match(r'^\.',im['src']):
                    temp_work = pathlib.Path(str(basepath) + '/'+ im['src']).resolve()
                    image[index]['src'] = re.sub(rf"^\S+?(?={base})",sch + "://",str(temp_work))
                else:
#                    image[index]['src'] = sch + '://' + base + '/' + im['src']
                    image[index]['src'] = urldirname + '/' + im['src']
            print(index,image[index]['src'])


import time
counter = 0
def trans(list0,translator,counter):
#def trans(list0,lang):
    link_list = []
    link_words_list = []

    for index,lines in enumerate(list0):
        counter2 = counter
        print()
        print(index, lines)
#        xxxx = lines.text.strip()
        #xxxx1 = re.finditer(r'\b((\=|\.|\d|\w|[ -;:,"“’\'&\?\!\.])*(?!([^<]*>)))',str(lines))

        #(?<=\<p\>)(.+)(?=\<\/p)
        #(\w|,|\.|\&|\=|;|([ —-]))+(?!([^<]*>))

        soup2 = BeautifulSoup(str(lines), "html.parser")
        a_link = soup2.find_all('a')
        newtag = []
        if len(a_link) > 0:
            for i,v in enumerate(a_link):
                #link_words = re.findall(r'\b(\w+?(?!([^<]*>)))\b',str(v))
                if v.has_attr('href'):
                    pass
                else:
                    continue

                link_href = v.get('href')
                if (bool(re.search(r'^http',link_href))==False):
                    if (bool(re.match(r'^\/',link_href))==True):
                        temp_work = pathlib.Path(str(basepath) + link_href).resolve()
                        link_href = re.sub(rf"^\S+?(?={base})",sch + "://",str(temp_work))
                        #link_href = sch + '://' + base + link_href
                    else:
                        temp_work = pathlib.Path(str(basepath) + '\/'+ link_href).resolve()
                        link_href = re.sub(rf"^\S+?(?={base})",sch + "://",str(temp_work))
                        #link_href = sch + '://' + base + '/' + link_href
                link_words = v.text
                print()
                print("words",link_words)
                print("a link:",link_href)
                link_list.append(link_href)
                link_words_list.append(link_words)

                if len(link_words) > 0:
                    tag = soup.new_tag('a',href= link_href)
                    if link_words != '':
                        tag.string = link_words
                    elif link_words == False:
                        tag.string = str(link_href)
                    else:
                        tag.string = str(link_href)
                    newtag.append(tag)

        print(newtag)
        xxxx0 = re.sub(r'\<p\>|\<\/p\>','',str(lines))
        xxxx1 = re.finditer(r'((\.|\d|\w|&|\=|[ \/\(\)\-;:,├%#+…|"“’‘”\'&\?\!\.])*(?!([^<]*>)))',xxxx0)
        xxxx2 = ""
        for word in xxxx1:
            t = word[1]
            xxxx2 += t + '𓂀'
        print()
        print(xxxx2)

#        mark_words = []
#        mark_words2 = []
#
#        link_addr = re.findall(r'(?<=href\=\").+?(?=\")',str(lines))
#        if len(link_addr) > 0:
#            atag = re.findall(r'(?<=\<a).+?(?=\<\/a)',str(lines))
#            print(atag)
#            for a_text in atag:
#                mark_words += re.findall(r'\b(\w+?(?!([^<]*>)))\b',a_text)
#            for v in mark_words:
#                strvv = ' '.join(v)
#                mark_words2.append(strvv.strip())
#        print("words",mark_words2)
#        print('link:',link_addr)

        #xxxx3 = re.sub(r"\s{3,}",' ',xxxx2.strip())
        xxxx3 = re.sub(r"𓂀",'',xxxx2.strip())

        print()
        print(xxxx3)

#        if(re.match(r'\w|\“',xxxx) != None ):
        if(re.match(r'\w|\“',xxxx3) != None ):
            print()
#            print(xxxx3)
            #pattern match
#            texts = re.sub(r'\.\s+','. ',xxxx)
#            texts = re.sub(r'\s{2}',' \'',texts)
            texts = xxxx3
            texts = re.sub(r'\s{2,}',' \'',texts)
            texts = re.sub(r'\.\s+','. ',texts)
            texts = re.sub(r'\?\s+','? ',texts)
            texts = re.sub(r'\!\s+','! ',texts)
            texts = re.sub(r'\,\s+',', ',texts)
            print()
#            print(index, xxxx)
            print(index, texts)
            if len(newtag) > 0:
                for link_v in newtag:
                    print('newtag text:',link_v.text)
                    print('newtag val:',link_v)
                    counter += 1
                    try:
                        texts = re.sub(rf"{link_v.text}",f"‌𓃡{link_v.text}𓃡✦✧{counter}✧✸‌",texts)
#                       texts = re.sub(rf"{link_v.text}",'<span class="e;notranslate"e;>' + f"𓃵☽𓃡☽✸✦✦{link_v.text}𓃡✦✦✧{counter}✧✸"+'</span>',texts)
                        print('texts :',texts)
                    except:
                        print('error')
                        texts = link_v.text

            try:
                print()
                print('translated:')
#                translator = GoogleTranslator(source='auto', target=lang)
                translated = translator.translate(text=texts)
                print(index, translated)
#                translated = translator.translate(str(texts), dest=lang)
#                print(index, translated.text)
                print('______________________________')
#                list0[index].string = translated.text
                list0[index].string = translated
                if len(newtag) > 0:
                    for link in newtag:
                        counter2 += 1
                        div = soup.new_tag('div')
                        div.string = '✦link✧✸' + str(counter2) + ':'
                        div.append(link)
                        list0[index].append(div)

            except:
#                time.sleep(5)
                print('translated: fail')

    return link_list,link_words_list,soup

translator = GoogleTranslator(source='auto', target=lang)
links1,word1,soup = trans(h6tag_list_0,translator,counter)
links2,word2,soup = trans(ptag_list_0,translator,counter)
del translator
#trans(ptag_list_0,lang)
#trans(h6tag_list_0,lang)

links3 = []
if links1 != None and links2 != None:
    links3 = links1 + links2
elif links1 != None:
    links3 = links1
else:
    pass

word3 = []
if word1 != None and word2 != None:
    word3 = word1 + word2
elif word1 != None:
    word3 = word1
else:
    pass

metatag = soup.new_tag('meta')
metatag.attrs['charset'] = "utf-8"
soup.head.append(metatag)

#import os
#filename = os.path.basename(url)
filename = title[0:6] + '.html'
filename = re.sub(r'\/','_',filename)

with open(filename, "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))

# ‌𓃵𓃡☽✸✦✦ 𓃡✦✦✧ ✧✸

file = open(filename, "r", encoding='utf-8')
line_list = file.readlines()
newtext = ""
re_pattern = re.compile(r"(𓃡\S+?𓃡✦✧\S+?✧✸)")
re_pattern2 = re.compile(r"(✦✧\S+?✧✸)")
for linebyline in line_list:
    temp_1 = []
    temp_2 = []
    #a_link_num = re.findall(r'𓃡\S+?𓃡✦✧(\d+?)✧✸',linebyline)
    a_link_num = re.findall(r'𓃡.*?𓃡✦✧(\S+?)✧✸',linebyline)
    if len(a_link_num) > 0:
        temp_0 = []
        line2 = linebyline
        for i,v in enumerate(a_link_num):
            if not v in temp_0:
                temp_2.append(v)
                temp_0.append(v)
                print('a_link_num:',i,v)
                num = int(v)

                #extract_words = re.finditer(r"𓃡(\S+?)𓃡✦✧\d+?✧✸",linebyline)
                extract_words = re.finditer(r"𓃡(\S+?)𓃡✦✧\S+?✧✸",linebyline)

                if extract_words != None:
                    if num < len(links3):
                        for iew,w in enumerate(extract_words):
                            ws = str(w.group()) #link_words ...translated word
                            if not ws in temp_1:
                                temp_1.append(ws)
                                print(ws)
                                matc = re.findall(re_pattern,line2)
                                if len(matc) > 0:
                                    for ms in matc:
                                        if (ms.find(ws)) != -1:

                                            link_number = re.match(r'𓃡\S+?𓃡✦✧(?P<number>\S+?)✧✸',ws)
                                            #print('link_number:',link_number.groups()[0])
                                            # linl_number.groups()[0] == link_number.group('number')
                                            print('link_number:',link_number.group('number'))
                                            number = int(link_number.groups()[0])
                                            embed_link = str(links3[number - 1])
                                            word = str(word3[number-1])
                                            print('non skipped')
                                            striped_ws = re.sub(r'𓂀|✸|✦|𓃡|','',ws)
                                            print(striped_ws)
                                            if (bool(re.search(rf"{ws}",line2))==True):
                                                print(line2)
                                                line2 = line2.replace(ws,f"<a href={embed_link}>{striped_ws}</a>",1)
                                                print(line2)
                                            #line2 = re.sub(r'𓂀|✸|✦|𓃡|','',line2)
                                            break

                                else:
                                    print('skipped!!!')

        newtext += line2
    else:
        newtext += linebyline


    #a_link_num2 = re.findall(r'✦✧(\d+?)✧✸',line2)
    a_link_num2 = re.findall(r'✦✧(\S+?)✧✸',newtext)
    if len(a_link_num2) > 0:
        temp_0 = []
        for i,v in enumerate(a_link_num2):
            print('a_link_num2:',i,v)
            if not v in temp_2:
                print(temp_2)
                if not v in temp_0:
                    temp_0.append(v)
                    print('a_link_num2:',i,v)
                    num = int(v)
                    extract_words2 = v
                    if extract_words2 != None:
                        if num < len(links3):
                            if not extract_words2 in temp_1:
                                temp_1.append(extract_words2)
                                print(extract_words2)
                                matc = re.findall(re_pattern2,newtext)
                                if len(matc) > 0:
                                    for ms in matc:
                                        if (ms.find(extract_words2)) != -1:

                                            link_number = num
                                            print('link_number:',num)
                                            embed_link = str(links3[num - 1])
                                            word = str(word3[num - 1])
                                            print('non skipped')
                                            newtext= newtext.replace('✦✧'+ extract_words2 + '✧✸',f"<a href={embed_link}>✦✧{extract_words2}✧✸</a>")
                                            newtext = re.sub(r'𓂀|✸|✦|𓃡|','',newtext)

                                else:
                                    print('skipped!!!')
    
    codetag = re.findall(rf"{nullch}\d+?{nullch}.+?{nullch}{nullch}\d+?{nullch}{nullch}",newtext)
    if len(codetag) > 0:
        print('code found!')
        for cv in codetag:
            counter_num = re.match(rf"{nullch}(\d+?){nullch}",str(cv))
            print(counter_num)
            match1 = counter_num.group(0)
            i = re.sub(rf"{nullch}",'',match1)
            print("i:",i)
            contents = code_contents[int(i)]
            print('code:',contents)
            if len(re.findall(rf"{match1}",cv)) != 2:
                #text = re.sub(rf"{match1}",contents,str(cv))
                #newtext = re.sub(rf"{nullch}\d+?{nullch}",text,newtext,1)
                continue
            print(cv)
            text = re.sub(rf"^{nullch}\d+?{nullch}.+?{nullch}{nullch}\d+?{nullch}{nullch}",contents,str(cv))
            #text = re.sub(r'^𓄃\d+?𓄃','<code>',str(cv))
            #text = re.sub(r'𓄃𓄃\d+?𓄃𓄃','</code>',str(text))
            newtext = re.sub(rf"{nullch}\d+?{nullch}.+?{nullch}{nullch}\d+?{nullch}{nullch}",text,newtext,1)
            #newtext = re.sub(r'𓄃\d+?𓄃.+?𓄃𓄃\d+?𓄃𓄃',str(text),newtext,1)
    newtext = re.sub(rf'({nullch}{nullch}\d+?{nullch}{nullch})','',newtext)
    newtext = re.sub(rf'({nullch}\d+?{nullch})','',newtext)
    newtext = re.sub(rf'({nullch}\d+)','',newtext)
    newtext = re.sub(rf'({nullch})','',newtext)
re.purge()
file.close()

with open('generated.html', "w+", encoding='utf-8') as file:
    file.write(newtext)
# 𓃵𓃡☽✸✦✦ 𓃡✦✦✧ ✧✸