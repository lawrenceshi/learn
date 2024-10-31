from random import randint
#随机2次
for i in range(2):
    #随机硬币正反面
    randomint_num = randint(1, 2)

    if randomint_num == 1:
        print("正面")
    elif randomint_num == 2:
        print("反面")
