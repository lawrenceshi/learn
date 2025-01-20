#大数定理
from random import randint
import numpy as np
import matplotlib.pyplot as plt
#本金

#times = [1,10,50,100,500,1000,5000,10000,50000,100000]
times = np.arange(2, 10000, 100)
#times=int(input('本金:'))
#times=100000

def flip_coin_raitio(N):

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0


    for i in range(N):
        randomint_num = randint(1, 6)
        if randomint_num == 1:
            one+=1
            #print('本金+1.8')
        elif randomint_num == 2:
            two+=1
        elif randomint_num == 3:
            three += 1
        elif randomint_num == 4:
            four += 1
        elif randomint_num == 5:
            five += 1
        elif randomint_num == 6:
            six += 1
    #print('本金-1')
    print('1:'+str(one))
    print('2:'+str(two))
    print('3:'+str(three))
    print('4:'+str(four))
    print('5:'+str(five))
    print('6:'+str(six))
    return [six*2+three*1, two*1.0+five*1.0+one*1.0+four*1.0]

#ydq=赢的钱,sdq=输的钱
ydq = []
sdq = []
zgl = []
for i in times:
    flip = flip_coin_raitio(i)
    ydq.append(flip[0])
    sdq.append(flip[1]) 
    lr = flip[0]-flip[1]
    print('利润:',lr)
    gl = lr/i
    zgl.append(gl)
    print("概率：",gl)

    print(ydq)
    print(sdq)

llkdq =[(1/6) * 2 + (1/6) * 1 + ((1/6) * (-1) *4)]*len(times)
print(llkdq)

plt.figure(figsize=(8, 5))
plt.plot(times, zgl, color='blue', marker = "o")
plt.plot(times, llkdq, color='red', linestyle='-') # 画一条标准0.5的线
plt.grid(True)
plt.show()

