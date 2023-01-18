#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> gwalho;
    
    for(int i = 0; i < s.length(); i++){
        if((s[i] == ')') && (!gwalho.empty())){
            if(gwalho.top() == '(')
                gwalho.pop();
            else
                break;
        }
        else
            gwalho.push(s[i]);
    }
    
    if(!gwalho.empty())
        answer = false;
    return answer;
}
