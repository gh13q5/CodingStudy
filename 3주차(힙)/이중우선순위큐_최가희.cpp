#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    priority_queue<int, vector<int>, greater<int>> greater_pq;  // 오름차순 (최솟값)
    priority_queue<int, vector<int>, less<int>> less_pq;    // 내림차순 (최댓값)
    
    int size = 0;   // 현재 queue 사이즈 -> 삭제할 때마다 감소
    for(int i = 0; i < operations.size(); i++){
        switch(operations[i].front()){
            case 'I':{
                int input = stoi(operations[i].substr(2));
                greater_pq.push(input);
                less_pq.push(input);
                size++;
                break;
            }
            case 'D':{
                if(size == 0)  continue;    // 큐가 비어있을 때 들어온 삭제 연산 무시
                if(operations[i].at(2) == '1')
                    less_pq.pop();
                else
                    greater_pq.pop();
                size--;
                if(size == 0)
                    while(!greater_pq.empty()){
                        greater_pq.pop();
                        less_pq.pop();  // pop하고 큐의 size가 0이 됐을 때 모든 큐를 다 비워줌
                    }
                break;
            }
        }
    }
    
    
    if(size == 0){
        answer.push_back(0);
        answer.push_back(0);
    }
    else{
        answer.push_back(less_pq.top());
        answer.push_back(greater_pq.top());
    }
    
    return answer;
}
