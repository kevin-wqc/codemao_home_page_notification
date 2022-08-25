import requests, time
from json import loads,dumps,load,dump
from plyer import notification

def xinzuo(cookie):
    with open('xinzuo.json','r') as f:
        works = load(f)
        
    print(type(works))


    headers = {
        "Content-Type": "application/json",
        "User-Agent": 'Mozilla/5.0 (Windows NT 5.1rv: 21.0) Gecko/20100101 Firefox/21.0',
        'cookie':cookie

    }

    dianmao = requests.get(r'https://api.codemao.cn/creation-tools/v1/pc/home/recommend-work?type=2',headers = headers)
    dianmao = loads(dianmao.text)
    print('开始获取，获取首页新作内容如下：\n')


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

    with open(r'xinzuo.json','w')as file:
        dump(works_now,file)



    
    for i in range(len(all_work)):
        
        d = all_work[i]
        

        if d[0] in works:
            
            continue

        reply = '恭喜作者“{}”的“{}”上首页的新作喵喵看了！目前已经获得{}个赞和{}个观看次数了！'.format(d[4],d[1],d[3],d[2])
        p=requests.post(r'https://api.codemao.cn/creation-tools/v1/works/{}/comment'.format(d[0]),
            headers=headers, 
            data=dumps({'content': reply}))
        print(p.text)
        print('成功评论')
        p_2 = requests.post(r'https://api.codemao.cn/nemo/v2/works/{}/like'.format(d[0]),
                headers=headers,
                data=dumps({}))
        print(p_2.text)
        print('成功点赞')
        print('已完成对'+d[1]+'作品的评论点赞，等待5.5秒')
        time.sleep(5.5)
        notification.notify(
            title = '编程猫-首页通知书',
            message = '已评论一个新的作品(新作)'+d[1],
            app_icon = '瓜！.ico',
            timeout = 17
        )
        print()
        print('=========================================')
        print()
    
    
