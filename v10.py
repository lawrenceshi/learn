#大数定理
from random import randint
from numpy import arange
import matplotlib.pyplot as plt

def raitio(N):

    one = 0
    two =0
    three = 0
    four = 0
    five = 0
    six = 0
    for i in range(N):
        randomint_num = randint(1,6)
        if randomint_num == 1:
            one += 1
        elif randomint_num == 2:
            two += 1
        elif randomint_num == 3:
            three += 1
        elif randomint_num == 4:
            four += 1
        elif randomint_num == 5 :
            five += 1
        elif randomint_num == 6:
            six += 1

    one_raitio = float(one)/N
    two_raitio = float(two)/N
    three_raitio = float(three)/N
    four_raitio = float(four)/N
    five_raitio = float(five)/N
    six_raitio = float(six)/N

    return [one_raitio, two_raitio, three_raitio, four_raitio, five_raitio, six_raitio]

#x = [1 , 2, 3, 4, 8, 10, 20, 40, 80, 160, 1000, 5000,10000,100000000]
x = arange(6, 3000, 6)
Y_1 = []
Y_2 = []
Y_3 = []
Y_4 = []
Y_5 = []
Y_6 = []

for N in x:

    raitio_return = raitio(N)
    print("得出结果",raitio_return)
    
    Y_1.append(raitio_return[0])
    Y_2.append(raitio_return[1])
    Y_3.append(raitio_return[2])
    Y_4.append(raitio_return[3])
    Y_5.append(raitio_return[4])
    Y_6.append(raitio_return[5])

print(x)

Z = [0.167]*len(x)

print(Z)

plt.figure(figsize=(8, 5))
plt.plot(x, Y_1, color='blue', linewidth=2 , marker="o")
plt.plot(x, Y_2, color='yellow', linewidth=2 , marker="o")
plt.plot(x, Y_3, color='black', linewidth=2 , marker="o")
plt.plot(x, Y_4, color='brown', linewidth=2 , marker="o")
plt.plot(x, Y_5, color='purple', linewidth=2 , marker="o")
plt.plot(x, Y_6, color='green', linewidth=2 , marker="o")
plt.plot(x, Z, color='red', linestyle='-') # 画一条标准0.5的线
plt.grid(True)
plt.show()

