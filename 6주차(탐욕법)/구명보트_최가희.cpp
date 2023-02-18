#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    sort(people.begin(), people.end());    // 내림차순 정렬
    
    int idx = 0;
    while(idx < people.size()){
        int weight = people.back();
        people.pop_back();
        
        if(weight + people[idx] <= limit)   idx++;
        answer++;
    }
    
    return answer;
}
