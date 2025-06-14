#大数定理
from random import randint
from numpy import arange
import matplotlib.pyplot as plt

def raitio(N):

    one_three_five = 0
    two_four_six =0

    for i in range(N):
        randomint_num = randint(1,6)
        if randomint_num in [1,3,5]:
            one_three_five += 1
        elif randomint_num in [2,4,6]:
            two_four_six += 1

    one_three_five_raitio = float(one_three_five)/N
    two_four_six_raitio = float(two_four_six)/N

    return [one_three_five_raitio,two_four_six_raitio]

#x = [1 , 2, 3, 4, 8, 10, 20, 40, 80, 160, 1000, 5000,10000,100000000]
x = arange(6, 3000, 6)
Y_1_3_5 = []
Y_2_4_6 = []
for N in x:

    raitio_return = raitio(N)
    print("得出结果",raitio_return)
    
    Y_1_3_5.append(raitio_return[0])
    Y_2_4_6.append(raitio_return[1])


print(x)

Z = [0.5]*len(x)

print(Z)

plt.figure(figsize=(8, 5))
plt.plot(x, Y_1_3_5, color='blue', linewidth=2 , marker="o")
plt.plot(x, Y_2_4_6, color='yellow', linewidth=2 , marker="o")
plt.plot(x, Z, color='red', linestyle='-') # 画一条标准0.5的线
plt.grid(True)
plt.show()

