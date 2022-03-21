#include <iostream>

using std::cout; using std::cin; using std::endl;

int meb(int n)
{
    if (n == 1)
        return 1;


    int* dividers = new int[n];


    int div = 2, count = 0;
    
    //каноническе разложение числа на простые множитили 
    while (n > 1)
    {
        while (n % div == 0)
        {   
            dividers[count] = div;
            count ++;
            n = n / div;
        }
        div++;
    }

    //поиск повторяющихся чисел в разложение, поиск квадратов для функции мебиуса
    for(int i = 0; i < count; i++)
    {   
        int number = dividers[i];
        for(int j = i+1; j < count; j ++ )
        {
            if (number == dividers[j])
                return 0;
        }
        
    }

    
    return (count % 2 == 0)? 1 : -1;
}

int main()
{
    int n;
    cout <<  "Enter number n: ";
    // cin >> n;
    for (int i = 1; i < 100; i ++)
    {
        cout << "[" << i << "] ";
        cout << meb(i) << endl;
    }
    
    return 0;
}
