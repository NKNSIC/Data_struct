#include <iostream>
using namespace std;

// 函数maxIncrease：计算销售额增幅
// 参数：s-销售额数组，n-销售额数组长度，n>1
// 返回值：销售额最大增幅
int maxIncrease(int s[], int n);

int main()
{
    int n, a[30], i;     // 定义变量及数组，n-销售额个数，a-销售额数组
    cin >> n;      // 输入销售额数量，n>1
    // 输入n个销售额，分别存入a[0]到a[n-1]
    for(i = 0; i < n; i++)
        cin >> a[i];
    i = maxIncrease(a,n);
    cout << "最大销售增幅为：" << i << endl;
    return 0;
}

int maxIncrease(int s[], int n)
{
    int maxIncrease = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            maxIncrease = (s[j] - s[i]) > maxIncrease ? s[j] - s[i] : maxIncrease;
        }
    }
    return maxIncrease;
}