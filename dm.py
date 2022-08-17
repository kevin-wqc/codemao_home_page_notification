import requests, time
from json import loads,dumps,load,dump
from plyer import notification


def dianmao():
    with open(r'D:\DATA\WQC\github\python\首页通知书\dianmao.json','r') as f:
        works = load(f)


    headers = {
        "Content-Type": "application/json",
        "User-Agent": 'Mozilla/5.0 (Windows NT 5.1rv: 21.0) Gecko/20100101 Firefox/21.0',
        'cookie':r'_ga=GA1.2.590925500.1594294726; gr_user_id=a0ff1182-99f5-43c4-9ef1-7a117dc9e398; SL_C_23361dd035530_KEY=be556a167e74fcde3a3444e29b25f8e99fb0c59f; __ca_uid_key__=e8c3ac44-c960-4fe2-b463-8ad70648ca5d; SL_C_23361dd035530_VID=T4zwNk3zqV; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%222889060%22%2C%22first_id%22%3A%2217efbb4c909138-02629b7f0d4629c-5b161c50-921600-17efbb4c90b4a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTdlZmJiNGM5MDkxMzgtMDI2MjliN2YwZDQ2MjljLTViMTYxYzUwLTkyMTYwMC0xN2VmYmI0YzkwYjRhIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjg4OTA2MCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%222889060%22%7D%2C%22%24device_id%22%3A%2217efbb4c909138-02629b7f0d4629c-5b161c50-921600-17efbb4c90b4a%22%7D; authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoyODg5MDYwLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiI2NWVkQ1R5ZyIsImV4cCI6MTY2Mjg2MDg5NCwiaWF0IjoxNjU4OTcyODk0LCJqdGkiOiJkNzRmZGE3ZC04ZTk0LTQxNTAtYTc0Ni1lMTUzNzQ2NzIwYzQifQ.usOoJ8d-CRm2wO_2TGdt_oKMJuyCGtRVrbJDN5vsGTc; acw_tc=2f61f27116589736983145269e1bd91a55c5f22c9257e0ea4e2a48bc3fbde0'

    }

    dianmao = requests.get(r'https://api.codemao.cn/creation-tools/v1/pc/home/recommend-work?type=1',headers = headers)
    dianmao = loads(dianmao.text)
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



    works_now = works.copy()
    for i in j:
        works_now.append(i)

    with open(r'D:\DATA\WQC\github\python\首页通知书\dianmao.json','w')as file:
        dump(works_now,file)


    
    for i in range(len(all_work)):

        d = all_work[i]
        

        if d[0] in works:
           
            continue

        reply = '恭喜作者“{}”的“{}”上首页的点猫精选了！目前已经获得{}个赞和{}个观看次数了！'.format(d[4],d[1],d[3],d[2])
        p=requests.post(r'https://api.codemao.cn/creation-tools/v1/works/{}/comment'.format(d[0]),
            headers=headers, 
            data=dumps({'content': reply}))
        print(p.text)
        print('成功评论')
        p_2 = requests.post(r'https://api.codemao.cn/nemo/v2/works/{}/like'.format(d[0]),
                headers=headers,
                data=dumps({}))
        
        print('成功点赞')
        print('已完成对'+d[1]+'作品的评论点赞，等待5.5秒')
        time.sleep(5.5)
        
        
        notification.notify(
            title = '编程猫-首页通知书',
            message = '已评论一个新的作品(点猫)'+d[1],
            app_icon = r'D:\DATA\WQC\github\python\首页通知书\瓜！.ico',
            timeout = 17
        )
        print()
        print('=========================================')
        print('')
    
