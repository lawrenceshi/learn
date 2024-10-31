from random import randint
#随机2次

front = 0
back = 0

for i in range(2):
    #随机硬币正反面
    randomint_num = randint(1, 2)

    if randomint_num == 1:
        print("正面")
        front+=1
    elif randomint_num == 2:
        print("反面")
        back+=1

print("正面次数：", front)
print("反面次数：", back)
