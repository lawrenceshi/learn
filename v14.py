#大数定理
from random import randint
import numpy as np
import matplotlib.pyplot as plt
#本金

bj=int(input('本金:'))
#bj=10000

def flip_coin_raitio(N):

    front = 0
    back = 0

    for i in range(N):
        randomint_num = randint(1, 2)
        if randomint_num == 1:
            front+=1
            #print('本金+1.8')
        elif randomint_num == 2:
            back+=1
            #print('本金-1')
    print('正面:'+str(front))
    print('反面:'+str(back))
    return [front*0.8,back*1.0]

#ydq=赢的钱,sdq=输的钱
ydq,sdq= flip_coin_raitio(bj)

print('利润:',ydq-sdq)

print(ydq)
print(sdq)
llpdq = 0.1* bj
print('理论亏',0.5*0.8+0.5*(-1))