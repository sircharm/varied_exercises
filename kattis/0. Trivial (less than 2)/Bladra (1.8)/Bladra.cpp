//Accepted (100) - 0.05s

#include <iostream>

int main()
{
    int a, b, numberof_problems, numberof_cases;
    std::cin >> numberof_problems >> numberof_cases;
    int problems[numberof_problems] = {0};
    
    for (int i; i < numberof_cases; i++)
    {
        std::cin >> a >> b;
        problems[b-1]++;
    }
    
    int lowest = problems[0];
    for (int i = 1; i < numberof_problems; i++)
    {
        if (problems[i] < lowest)
        {
            lowest = problems[i];
        }
    }
    
    std::cout << lowest;
}
