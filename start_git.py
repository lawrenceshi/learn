import requests
import time
import os

print("该程序提交/拉取前请务必执行，否则将会导致提交/拉取失败！")
print("乐乐通用gitea启动程序！by Lawrence(lawrenceshi)")
print("we used fastapi to start gitea!")

get_git = requests.get("https://git.lawrenceshi.space")
print(get_git.status_code)
print(get_git.text)
if get_git.status_code == 200:
    print("gitea已经启动！无须重复启动")
    input("按任意键退出")
    os._exit(0)


get = requests.get("https://apiy.lawrenceshi.space/control/gitea")
print(get.status_code)
if get.status_code == 200:
    print(get.text)
    print("让我们等待20秒，以便gitea启动！")
    for z in range(1,21):
        for i in range(20 , 0 , -1):
            print("等待"+str(i)+"秒","第"+str(z)+"-20次")
            time.sleep(1)
        get_git = requests.get("https://git.lawrenceshi.space")
        print(get_git.status_code)
        print(get_git.text)
        if get_git.status_code == 200:
            print("gitea启动成功！")
            print("你现在可以使用git来自由的提交和拉去代码了")
            print("P.S:gitea将在10分钟后自动关闭，请尽快完成提交")
            break
        else:
            print("让我们再等待20秒，以便gitea启动！")
    if get_git.status_code != 200:
        print("gitea启动失败！此问题不是您的网络问题，请联系管理员处理")

else:
    print("gitea启动失败！请检查网络连接！如果依然有问题，请联系管理员")

input("按任意键退出")