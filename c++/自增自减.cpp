#include <iostream>

using namespace std; //创建一个为std的命名空间

int main() // 主程序
{
    int a = 999;
    a++; //自增
    int z = a;
    a=999;
    a--;
    int y = a;

    cout << "a = " << a << endl;
    cout << "z = " << z << endl;
    cout << "y = " << y << endl;



    return 0;

}