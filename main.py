import time
from dm import dianmao
from xz import xinzuo
from bcmHelper import *
#cookie = r'_ga=GA1.2.590925500.1594294726; gr_user_id=a0ff1182-99f5-43c4-9ef1-7a117dc9e398; SL_C_23361dd035530_KEY=be556a167e74fcde3a3444e29b25f8e99fb0c59f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%222889060%22%2C%22first_id%22%3A%2217efbb4c909138-02629b7f0d4629c-5b161c50-921600-17efbb4c90b4a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTdlZmJiNGM5MDkxMzgtMDI2MjliN2YwZDQ2MjljLTViMTYxYzUwLTkyMTYwMC0xN2VmYmI0YzkwYjRhIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjg4OTA2MCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%222889060%22%7D%2C%22%24device_id%22%3A%2217efbb4c909138-02629b7f0d4629c-5b161c50-921600-17efbb4c90b4a%22%7D; SL_C_23361dd035530_VID=o7LaihX_M5; __ca_uid_key__=93980332-1f7c-4da9-8b23-81c2e105f4e4; authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoyODg5MDYwLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiI2NWVkQ1R5ZyIsImV4cCI6MTY2NDc2MzQyNSwiaWF0IjoxNjYwODc1NDI1LCJqdGkiOiJhYjI0MGZjNS04Njg0LTQyNTMtYTk1My1jZjIyZTM4MzNhYmQifQ.HWcjNva07ezKBiexdGEhDZjcg2ZkhzeT8w61eGPOZUk; acw_tc=2f624a0616608768892002146e5020b9bfa49a5023bf3efcd6f27f36fffa3f'

usr = user('185015688225','Wqc20080408')

while True:
    print('开始检查首页点猫\n')
    dianmao(usr)
    

    print('开始检查首页新作\n')
    xinzuo(usr)
    
    print('等待3min')

    time.sleep(180)
    
