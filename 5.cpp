#include <iostream>
#include <cmath>

using namespace std;

int nod(int a, int b)
{
    if (a % b == 0)
        return b;
    if (b % a == 0)
        return a;

    while (1)
    {
        if (a % b == 0)
            return b;
        if (b % a == 0)
            return a;
        
        if (a > b)
            a = a%b;
        else
            b = b%a;
    }
    
}

int el(int n)
{   
    int count = 0;
    for (int i = 1; i < n; i ++)
    {
        if (nod(n, i) == 1) //Проверка на взаимо простоту чисел
            count ++;       // Подсчет таких чисел
    }

    return count;

}

int el_(int n)
{
    int div = 2;
    int answ = 1;
    while (n > 1)
    {
        int c = 0;
        while (n % div == 0)
        {   
            c++;
            n = n / div;
        }
        if (c != 0)
            answ *= pow(div, c) - pow(div, c-1);
        div++;
    }
    return answ;
}

int main()
{
    int n;
    cout << "ENter n: ";
    cin >> n;

    cout << el(n) << endl;
    cout << el_(n) << endl;
    
    return 0;

}