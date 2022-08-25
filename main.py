import time
from dm import dianmao
from xz import xinzuo
from bcmHelper import *


usr = user(账号，密码)

while True:
    print('开始检查首页点猫\n')
    dianmao(usr)
    

    print('开始检查首页新作\n')
    xinzuo(usr)
    
    print('等待3min')

    time.sleep(180)
    
