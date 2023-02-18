#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.begin(), citations.end(), greater<int>());
    
    for(int i = 0; i < citations.size(); i++){
        if(i >= citations[i]){
            answer = i;
            break;
        }
        if(i == citations.size() - 1)   answer = i + 1; // 마지막까지 돌았는데도 h값을 뽑지 못 했을 때
    }
    
    return answer;
}
