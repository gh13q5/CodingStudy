#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    
    sort(rocks.begin(), rocks.end());
    
    int min = 0, max = distance;
    while(min <= max){
        int mid = (max + min) / 2;
        int del_cnt = 0, prev = 0;
        for(int i = 0; i < rocks.size(); i++){
            if(rocks[i] - prev < mid)   del_cnt++;
            else    prev = rocks[i];
        }
        if(distance - prev < mid)   del_cnt++;
        
        if(del_cnt <= n){
            min = mid + 1;
            answer = mid;
        }
        else    max = mid - 1;
    }
    
    return answer;
}

/*
    입국심사 문제처럼 마지막에 del_cnt >= n일 때 answer 올려줬더니 안 됨;
    얘는 결국 최댓값을 찾아야 하는 문제라 작은 쪽에서부터 찾아줬어야 하는 듯
*/
