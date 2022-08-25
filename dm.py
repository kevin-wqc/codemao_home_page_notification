import requests, time
from json import loads,dumps,load,dump
from plyer import notification
from bcmHelper import *

def dianmao(usr):
    with open('dianmao.json','r') as f:
        works = load(f)



    dianmao = get_homepage_work(1)

    print('开始获取，获取首页点猫内容如下：\n')

    for i in dianmao:
        print(i['name'])
    print()
    print('=========================================')
    print()
    all_work = []
    j = []
    for work in dianmao:
        id = work['id']
        name = work['name']
        view = work['view_times']
        like = work['praise_times']
        user = work['user']['nickname']
        l = [id,name,view,like,user]
        all_work.append(l)
        if id not in works:
            j.append(id)
            print('新的首页作品：{}, {}'.format(id,name))



    works_now = works.copy()
    for i in j:
        works_now.append(i)

    with open('dianmao.json','w')as file:
        dump(works_now,file)


    
    for i in range(len(all_work)):

        d = all_work[i]
        

        if d[0] in works:
           
            continue

        reply = '恭喜作者@{}的《{}》上首页的点猫精选了！'.format(d[4],d[1])
        usr.reply_work(d[0],content = reply)

        print('成功评论')
        usr.like_work(d[0])
        
        print('成功点赞')
        print('已完成对'+d[1]+'作品的评论点赞，等待5.5秒')
        time.sleep(5.5)
        
        
        notification.notify(
            title = '编程猫-首页通知书',
            message = '已评论一个新的作品(点猫)'+d[1],
            app_icon = '瓜！.ico',
            timeout = 17
        )
        print()
        print('=========================================')
        print('')
    
