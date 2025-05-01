//Accepted - 0.00s

#include <iostream>

int main()
{
    int input, cases;
    std::cin >> cases;
    
    int count = 0;
    for (int i = 0; i < cases; i++)
    {
        std::cin >> input;
        count += input;
    }
    
    std::cout << count;
}
