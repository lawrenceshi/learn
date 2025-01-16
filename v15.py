#大数定理
from random import randint
import numpy as np
import matplotlib.pyplot as plt
#本金

bj=int(input('本金:'))
#bj=10000

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
ydq,sdq= flip_coin_raitio(bj)

lr = ydq-sdq
print('利润:',lr)

print("概率：",lr/bj)

print(ydq)
print(sdq)
#llkdq=理论亏的钱
llkdq = 0.167 * 2 + 0.167 * 1 + (0.167 * (-1) *4)
print('理论亏', llkdq)