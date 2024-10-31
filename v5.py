from random import randint



x = [1, 2, 3, 4, 8, 10, 20, 40, 80, 160, 1000, 5000]
Y = []
Z = []
for i in x:
    print("设定抛"+str(i)+"次硬币")
    front = 0
    back = 0
    for e in range(i):
        #随机硬币正反面
        randomint_num = randint(0, 1)

        if randomint_num == 0:
            print("正面")
            front+=1
        elif randomint_num == 1:
            print("反面")
            back+=1
        print("目前抛了"+str(e+1)+"次硬币")
        print("正面次数：", front)
        print("反面次数：", back)
    front_Raitio = front*1.0/i
    back_Raitio = 1-front_Raitio
    print("正面比例：",front_Raitio)
    print("反面比例：",back_Raitio)
    Y.append(front_Raitio)
    Z.append(back_Raitio)
print(Y)
print(Z)



