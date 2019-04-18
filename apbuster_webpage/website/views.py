from django.shortcuts import render
from django.http import HttpResponse
import json
from PttAuto import *
# Create your views here.
def home(request):
    with open('website/static/website/json/posts.json', 'r') as f:
        posts = json.load(f)
    with open('website/static/website/txt/posttext.txt.0.txt') as f:
        text = f.read()
    #text = text.split(']')[1]
    return render(request, 'website/index.html', {'posts': posts, 'text': text})

#def test(request):
#    return render(request, 'website/success.html')


def test(request):
    host = 'ptt.cc'
    user = 'chadyoung'   #'snailchuang'
    password = '08070973'   #'jeff0118'
    ptt = Ptt(host, user, password)
    #+======================= load 10 best sentences =============================#
#    caption = '[this is a content test]This is a title test'
    with open('website/static/website/txt/posttext.txt.0.txt',encoding = 'utf-8-sig') as f:
        caption = f.readline()
    print(caption)
    title = caption.split(']')[1]
#    title = 'test1'
    content = '冬天到了,已經一陣子沒關心空氣品質,{},有沒有卦?'.format(caption.split(']')[0][1:])
    #content = 'lets test the content{},testing now'.format(caption.split(']')[0])
#    content = 'test2'
#    caption='test3'
    time.sleep(1)
    if ptt.is_connect():
        if ptt.login():
            ptt.post('Test', content, caption)
    ptt.logout()
#    return render(request, 'website/index.html')
    return render(request, 'website/success.html')
